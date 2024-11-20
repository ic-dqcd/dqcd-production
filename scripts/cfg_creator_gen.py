import os


cmnd = """
    cmsDriver.py Configuration/GenProduction/python/{name}_cfi.py --python_filename {aux_path}/gen_{name}_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --fileout file:gen_{name}.root --conditions 106X_upgrade2018_realistic_v4 --beamspot Realistic25ns13TeVEarly2018Collision --step GEN --geometry DB:Extended --era Run2_2018 --no_exec --mc -n -1
"""

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '{aux_path}/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '{aux_path}/gen_{name}_cfg.py'

config.Data.outputPrimaryDataset = '{name}'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 2500
NJOBS = 400
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/user/jleonhol/samples/'
config.Data.publication = True
config.Data.outputDatasetTag = '{name}'

config.Site.storageSite = 'T2_UK_London_IC'
"""

def submit(name, aux_path="."):
    if os.path.exists(f"{aux_path}/{name}/crab_{name}"):
        return
    os.system(f"mkdir -p {aux_path}")
    print("Launching", name)
    os.system(cmnd.format(name=name, aux_path=aux_path))
    with open(f"{aux_path}/crab_submit_{name}.py", "w+") as f:
        f.write(crab.format(name=name, aux_path=aux_path))
    os.system(f"crab submit {aux_path}/crab_submit_{name}.py")


if __name__ == "__main__":
    p = "Configuration/GenProduction/data/"
    files = os.listdir(p)
    files = [
      # # # "scenarioA_mpi_10_mA_1p00_ctau_0p1.slha",
      # # # "scenarioA_mpi_10_mA_1p00_ctau_10.slha",
      # # # "scenarioA_mpi_10_mA_1p00_ctau_100.slha",
      # # # "scenarioA_mpi_10_mA_1p00_ctau_1p0.slha",
      # # # "scenarioA_mpi_10_mA_3p33_ctau_0p1.slha",
      # # # "scenarioA_mpi_10_mA_3p33_ctau_10.slha",
      # # # "scenarioA_mpi_10_mA_3p33_ctau_100.slha",
      # # # "scenarioA_mpi_10_mA_3p33_ctau_1p0.slha",
      # # # "scenarioA_mpi_1_mA_0p33_ctau_0p1.slha",
      # # # "scenarioA_mpi_1_mA_0p33_ctau_10.slha",
      # # # "scenarioA_mpi_1_mA_0p33_ctau_100.slha",
      # # # "scenarioA_mpi_1_mA_0p33_ctau_1p0.slha",
      # # # "scenarioA_mpi_2_mA_0p67_ctau_0p1.slha",
      # # # "scenarioA_mpi_2_mA_0p67_ctau_10.slha",
      # # # "scenarioA_mpi_2_mA_0p67_ctau_100.slha",
      # # # "scenarioA_mpi_2_mA_0p67_ctau_1p0.slha",
      # # # "scenarioA_mpi_4_mA_0p40_ctau_0p1.slha",
      # # # "scenarioA_mpi_4_mA_0p40_ctau_10.slha",
      # # # "scenarioA_mpi_4_mA_0p40_ctau_100.slha",
      # # # "scenarioA_mpi_4_mA_0p40_ctau_1p0.slha",
      # # # "scenarioA_mpi_4_mA_1p33_ctau_0p1.slha",
      # # # "scenarioA_mpi_4_mA_1p33_ctau_10.slha",
      # # # "scenarioA_mpi_4_mA_1p33_ctau_100.slha",
      # # # "scenarioA_mpi_4_mA_1p33_ctau_1p0.slha",
      # # # "scenarioB1_mpi_1_mA_0p33_ctau_0p1.slha",
      # # # "scenarioB1_mpi_1_mA_0p33_ctau_10.slha",
      # # # "scenarioB1_mpi_1_mA_0p33_ctau_100.slha",
      # # # "scenarioB1_mpi_1_mA_0p33_ctau_1p0.slha",
      # # # "scenarioB1_mpi_2_mA_0p40_ctau_0p1.slha",
      # # # "scenarioB1_mpi_2_mA_0p40_ctau_10.slha",
      # # # "scenarioB1_mpi_2_mA_0p40_ctau_100.slha",
      # # # "scenarioB1_mpi_2_mA_0p40_ctau_1p0.slha",
      # # # "scenarioB1_mpi_2_mA_0p67_ctau_0p1.slha",
      # # # "scenarioB1_mpi_2_mA_0p67_ctau_10.slha",
      # # # "scenarioB1_mpi_2_mA_0p67_ctau_100.slha",
      # # # "scenarioB1_mpi_2_mA_0p67_ctau_1p0.slha",
      # # # "scenarioB1_mpi_4_mA_0p80_ctau_0p1.slha",
      # # # "scenarioB1_mpi_4_mA_0p80_ctau_10.slha",
      # # # "scenarioB1_mpi_4_mA_0p80_ctau_100.slha",
      # # # "scenarioB1_mpi_4_mA_0p80_ctau_1p0.slha",
      # # # "scenarioB1_mpi_4_mA_1p33_ctau_0p1.slha",
      # # # "scenarioB1_mpi_4_mA_1p33_ctau_10.slha",
      # # # "scenarioB1_mpi_4_mA_1p33_ctau_100.slha",
      # # # "scenarioB1_mpi_4_mA_1p33_ctau_1p0.slha",
      # # # "scenarioB2_mpi_1_mA_0p60_ctau_0p1.slha",
      # # # "scenarioB2_mpi_1_mA_0p60_ctau_10.slha",
      # # # "scenarioB2_mpi_1_mA_0p60_ctau_100.slha",
      # # # "scenarioB2_mpi_1_mA_0p60_ctau_1p0.slha",
      # # # "scenarioB2_mpi_2_mA_1p10_ctau_0p1.slha",
      # # # "scenarioB2_mpi_2_mA_1p10_ctau_10.slha",
      # # # "scenarioB2_mpi_2_mA_1p10_ctau_100.slha",
      # # # "scenarioB2_mpi_2_mA_1p10_ctau_1p0.slha",
      # # # "scenarioB2_mpi_4_mA_2p10_ctau_0p1.slha",
      # # # "scenarioB2_mpi_4_mA_2p10_ctau_10.slha",
      # # # "scenarioB2_mpi_4_mA_2p10_ctau_100.slha",
      # # # "scenarioB2_mpi_4_mA_2p10_ctau_1p0.slha",
      # # # "scenarioC_mpi_10_mA_8p00_ctau_0p1.slha",
      # # # "scenarioC_mpi_10_mA_8p00_ctau_10.slha",
      # # # "scenarioC_mpi_10_mA_8p00_ctau_100.slha",
      # # # "scenarioC_mpi_10_mA_8p00_ctau_1p0.slha",
      # # # "scenarioC_mpi_2_mA_1p60_ctau_0p1.slha",
      # # # "scenarioC_mpi_2_mA_1p60_ctau_10.slha",
      # # # "scenarioC_mpi_2_mA_1p60_ctau_100.slha",
      # # # "scenarioC_mpi_2_mA_1p60_ctau_1p0.slha",
      # # # "scenarioC_mpi_4_mA_3p20_ctau_0p1.slha",
      # # # "scenarioC_mpi_4_mA_3p20_ctau_10.slha",
      # # # "scenarioC_mpi_4_mA_3p20_ctau_100.slha",
      # # # "scenarioC_mpi_4_mA_3p20_ctau_1p0.slha",
      # # # "testZPrime_ctau10.slha",
      "hiddenValleyGridPack_vector_m_10_ctau_100_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_10_ctau_10_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_10_ctau_1_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_10_ctau_500_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_10_ctau_50_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_15_ctau_100_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_15_ctau_10_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_15_ctau_1_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_15_ctau_500_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_15_ctau_50_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_20_ctau_100_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_20_ctau_10_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_20_ctau_1_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_20_ctau_500_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_20_ctau_50_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_2_ctau_1_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_2_ctau_500_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_2_ctau_50_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_5_ctau_100_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_5_ctau_10_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_5_ctau_1_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_5_ctau_500_xiO_1_xiL_1.slha",
      "hiddenValleyGridPack_vector_m_5_ctau_50_xiO_1_xiL_1.slha"
    ]

    names = [f.split(".")[0] for f in files]
    for name in names:
        submit(name)
