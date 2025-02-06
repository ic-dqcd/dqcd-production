# This script reads the sample configuration files (python/*_cfg.py and data/*.slha) used for production of 2022 and combines them into a single file
# The output file also contains additional configuration flags requiered to use the pythia version used by central production
# This file also generates the request.csv library file, which summarises all the desired samples

import os

py_file_dir = "./separate_files/python/"
slha_file_dir = "./separate_files/slha/"
output_file_dir = "./combined_files/"

request_file_path = output_file_dir + "request.csv"

def convert_file(cfg_filename):
    # dataset name must follow naming convention (https://cms-pdmv.gitbook.io/project/mccontact/rules-for-run3-2024-dataset-names)
    # PROCESS_[BINNING]_[FILTER]_[PARAMETERS]_TUNE_BEAME_ME-PS
    #scenarioA_mpi2_mA_0p67_ctau_100 -> GluGluHToDarkShowers_Par-ctau-100-mA-0p67-mPi2_TuneCP5_13p6TeV_powheg-pythia8
    new_cfg_filename = "GluGluHToDarkShowers" # base process name
    new_cfg_filename += "-" + (cfg_filename.split("_")[0]).replace("scenario","Scenario") # scenario, capital "S"
    new_cfg_filename += "_Par" # parameters
    new_cfg_filename += "-ctau-" + cfg_filename.split("ctau_")[1] #+ "mm" # par. ctau
    new_cfg_filename += "-mA-" + (cfg_filename.split("mA_")[1]).split("_")[0] #+ "GeV" # par. mA
    new_cfg_filename += "-mpi-" + (cfg_filename.split("mpi_")[1]).split("_")[0] #+ "GeV" # par. mPi

    print(" Initial filename: " + cfg_filename)
    print(" New filename: " + new_cfg_filename)
    
    py_file_path = py_file_dir + cfg_filename + "_cfi.py"
    slha_file_path = slha_file_dir + cfg_filename + ".slha"
    output_file_path = output_file_dir + new_cfg_filename + "_cfi.py"

    # Read the .py file
    with open(py_file_path, "r") as py_file:
        py_lines = py_file.readlines()

    # Read the .slha file
    with open(slha_file_path, "r") as slha_file:
        slha_content = slha_file.read()

    # Convert SLHA content into a cms.vstring-compatible format
    #formatted_slha_content = [f'    "{line.strip()}",\n' for line in slha_content.splitlines()]
    formatted_slha_content = []
    for line in slha_content.splitlines():
        line = line.strip()
        if line and not (line.startswith("!") or line.startswith("#") or line.startswith("Beams") or line.startswith("Init") or line.startswith("Next") or line.startswith("Main")):
            formatted_slha_content.append(12 * " " + f'"{line.strip()}",\n')

    # Replace params in the .py file
    updated_py_lines = []
    skip_block = False
    stop_writing = False  # Flag to stop writing after encountering MuMuFilter
    for i, line in enumerate(py_lines):
        # Stop writing after encountering the MuMuFilter i.e. don't write the bottom of the original .py file into the merged one
        if stop_writing:
            continue

        # Skip the block related to importing and reading the .slha file
        if "import os" in line or 'f = os.environ["CMSSW_BASE"]' in line or 'with open(f) as f:' in line:
            skip_block = True
            continue
        if skip_block and "params = " in line:
            skip_block = False
            continue

        # Insert the new import on the 4th line
        if i == 3:
            updated_py_lines.append("from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *\n")

        # Modify "parameterSets" to separate the last parenthesis and add 'pythia8CP5Settings' on a new line
        elif "parameterSets = cms.vstring(" in line:
            # Extract the core of the parameterSets
            base_part = line.split("cms.vstring(")[-1].strip(")\n")
            # Append the modified version
            updated_py_lines.append("        parameterSets = cms.vstring(\n")
            updated_py_lines.append("            'pythia8CommonSettings',\n")
            for item in base_part.split(", "):
                updated_py_lines.append(f"            {item},\n")
            updated_py_lines.append("            'pythia8CP5Settings',\n")
            updated_py_lines.append("        ),\n")
            continue

        # Add configuration instructions around  "pythia8PSweightsSettingsBlock"
        if "pythia8PSweightsSettingsBlock" in line:
            updated_py_lines.append("        pythia8CommonSettingsBlock,\n")
            updated_py_lines.append("        pythia8PSweightsSettingsBlock,\n")
            updated_py_lines.append("        pythia8CP5SettingsBlock,\n")
            continue;

        # Replace the "params" variable with the SLHA content
        if "processParameters = cms.vstring(params)" in line:
            updated_py_lines.append("        processParameters = cms.vstring(\n")
            updated_py_lines.extend(formatted_slha_content)
            #updated_py_lines.append("    \"\",\n")
            #updated_py_lines.append("    \"! Tau limits to override pythia8CommonSettings configuration\",\n")
            updated_py_lines.append("            \"ParticleDecays:limitTau0 = off           ! Tau limits to override pythia8CommonSettings configuration\",\n")
            updated_py_lines.append("            \"POWHEG:nFinal = 1           ! needed since it uses ggH gridpacks\",\n")
            updated_py_lines.append("        ),\n")
        # replace Pythia8GeneratorFilter with Pythia8ConcurrentGeneratorFilter
        elif "Pythia8GeneratorFilter" in line:
            updated_py_lines.append(line.replace("Pythia8GeneratorFilter", "Pythia8ConcurrentGeneratorFilter"))
        # stop writing after encountering the MuMuFilter (it's assuming there's nothing important afterwards)
        elif 'MuMuFilter = cms.EDFilter("MCParticlePairFilter",' in line:
            stop_writing = True
            continue
        else:
            updated_py_lines.append(line)

    # Save the updated file
    with open(output_file_path, "w") as output_file:
        output_file.writelines(updated_py_lines)
    print(f"Combined file saved to: {output_file_path}")


    # Pass configuration information to the request.csv file
    with open(request_file_path, "a") as request_file:
        #request_file.write("dqcd_"+cfg_filename+"_cfi_2024test_TuneCP5_13p6TeV_powheg-pythia8,genFragments/dqcd/"+cfg_filename+"_cfi.py,1000000,powheg,/cvmfs/cms.cern.ch/phys_generator/gridpacks/RunIII/13p6TeV/slc7_amd64_gcc10/powheg/V2/gg_H_quark-mass-effects_mwindow1d0_slc7_amd64_gcc10_CMSSW_12_4_8.tgz,70.62865,100.00,1.0,1.0\n")
        request_file.write(new_cfg_filename + "_TuneCP5_13p6TeV_powheg-pythia8,genFragments/Hadronizer/13p6TeV/DQCD_Run3/" + new_cfg_filename + "_cfi.py,1000000,powheg,/cvmfs/cms.cern.ch/phys_generator/gridpacks/RunIII/13p6TeV/slc7_amd64_gcc10/powheg/V2/gg_H_quark-mass-effects_mwindow1d0_slc7_amd64_gcc10_CMSSW_12_4_8.tgz,70.62865,100.00,1.0,1.0\n")


# Overwrite the request.csv file (if it already exists) with the header of the file
with open(request_file_path, "w") as request_file:
        request_file.write("dataset,fragment,events,generator,gridpack,time per event,size per event,match efficiency,filter efficiency\n")



# Extract the name of all scenario*.slha (whithout the extension). The path to these files is indicated in slha_file_dir
# Once the base filename is extracted, it will merge the slha configuration into the corresponding cfg.py file
# The corresponding configuration will also be appended to request.csv

directory = os.fsencode(slha_file_dir)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.startswith("scenario") and filename.endswith(".slha"): 
        cfg_filename = filename.split(".")[0]
        #print( cfg_filename )
        convert_file(cfg_filename)
        continue
    else:
        continue

#cfg_filename = "scenarioA_mpi_10_mA_1p00_ctau_0p1"
#convert_file(cfg_filename)
