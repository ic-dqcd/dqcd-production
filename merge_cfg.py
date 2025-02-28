# This script reads the sample configuration files (python/*_cfg.py and data/*.slha) used for production of 2022 and combines them into a single file
# The output file also contains additional configuration flags requiered to use the pythia version used by central production
# This file also generates the request.csv library file, which summarises all the desired samples

import os, re

py_file_dir = "./python/"
slha_file_dir = "./data/"
output_file_dir = "./combined/"

request_file_path=output_file_dir+"request.csv"

def convert_file(cfg_filename):
    py_file_path = py_file_dir+cfg_filename+"_cfi.py"
    slha_file_path = slha_file_dir+cfg_filename+".slha"
    output_file_path = output_file_dir+cfg_filename+"_cfi.py"

    # Read the .py file
    with open(py_file_path, "r") as py_file:
        py_lines = py_file.readlines()

    # Read the .slha file
    with open(slha_file_path, "r") as slha_file:
        slha_content = slha_file.read()

    # Convert SLHA content into a cms.vstring-compatible format

    formatted_slha_content = []
    for line in slha_content.splitlines():
        line = line.strip()
        if line and not (line.startswith("!") or line.startswith("#") or line.startswith("Beams") or line.startswith("Init") or line.startswith("Next") or line.startswith("Main")):
            formatted_slha_content.append(12 * " " + f'"{line.strip()}",\n')

    # formatted_slha_content = [f'    "{line.strip()}",\n' for line in slha_content.splitlines() if '""' not in line and '"!' not in line and '"#' not in line]

    # Replace params in the .py file
    updated_py_lines = []
    skip_block = False
    for i, line in enumerate(py_lines):
        # Skip the block related to importing and reading the .slha file
        if "import os" in line or 'f = os.environ["CMSSW_BASE"]' in line or 'with open(f) as f:' in line:
            skip_block = True
            continue
        if skip_block and "params = " in line:
            skip_block = False
            continue

        # Insert the new import on the 4th line
        if i == 3:
            updated_py_lines.append("from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *\n")

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
            updated_py_lines.append("        ),\n")
        elif "Pythia8GeneratorFilter" in line:
            updated_py_lines.append(line.replace("Pythia8GeneratorFilter", "Pythia8ConcurrentGeneratorFilter"))
        else:
            updated_py_lines.append(line)

    updated_py_lines.append("generator.PythiaParameters.pythia8CommonSettings.extend(['ParticleDecays:limitTau0 = off'])")



    updated_py_lines.append("""
MuMuFilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(1, 1),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleID1 = cms.untracked.vint32(13,-13),
)
ProductionFilterSequence = cms.Sequence(generator*MuMuFilter)
""")

    # Save the updated file
    with open(output_file_path, "w") as output_file:
        output_file.writelines(updated_py_lines)
    print(f"Combined file saved to: {output_file_path}")


    # Pass configuration information to the request.csv file
    #pattern = r"hiddenValleyGridPack_vector_m_(.*)_ctau_(.*)_xiO_1_xiL_1"
    #match = re.fullmatch(pattern, cfg_filename)
    #dataset_name = f"GluGluHToDarkShowers_VP_mA-{match.group(1)}_ctau-{match.group(2)}_TuneCP5_13TeV_pythia8"
    #with open(request_file_path, "a") as request_file:
    #    request_file.write(dataset_name + ",genFragments/dqcd/"+cfg_filename+"_cfi.py,500000,pythia\n")



# Overwrite the request.csv file (if it already exists) with the header of the file
with open(request_file_path, "w") as request_file:
        request_file.write("dataset,fragment,events,generator\n")



# Extract the name of all scenario*.slha (whithout the extension). The path to these files is indicated in slha_file_dir
# Once the base filename is extracted, it will merge the slha configuration into the corresponding cfg.py file
# The corresponding configuration will also be appended to request.csv

directory = os.fsencode(slha_file_dir)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    cfg_filename = filename.split(".")[0]
    convert_file(cfg_filename)

#cfg_filename = "scenarioA_mpi_10_mA_1p00_ctau_0p1"
#convert_file(cfg_filename)
