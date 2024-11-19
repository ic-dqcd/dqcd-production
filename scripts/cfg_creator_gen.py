import os

p = "Configuration/GenProduction/data/"
files = os.listdir(p)

cmnd = """
    cmsDriver.py Configuration/GenProduction/python/{name}_cfi.py --python_filename 2023/gen_{name}_cfg.py --eventcontent RAWSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN --fileout file:gen_{name}.root --conditions 130X_mcRun3_2023_realistic_v15  --beamspot Realistic25ns13p6TeVEarly2023Collision --step GEN --geometry DB:Extended --era Run3 --no_exec --mc -n -1
"""

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '2023/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '2023/gen_{name}_cfg.py'

config.Data.outputPrimaryDataset = '{name}'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/user/jleonhol/samples/GEN'
config.Data.publication = True
config.Data.outputDatasetTag = '{name}_2023'

config.Site.storageSite = 'T2_UK_London_IC'
"""


files = [
  # "scenarioA_mpi_10_mA_1p00_ctau_0p1.slha",
  # "scenarioA_mpi_10_mA_1p00_ctau_10.slha",
  # "scenarioA_mpi_10_mA_1p00_ctau_100.slha",
  # "scenarioA_mpi_10_mA_1p00_ctau_1p0.slha",
  # "scenarioA_mpi_10_mA_3p33_ctau_0p1.slha",
  # "scenarioA_mpi_10_mA_3p33_ctau_10.slha",
  # "scenarioA_mpi_10_mA_3p33_ctau_100.slha",
  # "scenarioA_mpi_10_mA_3p33_ctau_1p0.slha",
  # "scenarioA_mpi_1_mA_0p33_ctau_0p1.slha",
  # "scenarioA_mpi_1_mA_0p33_ctau_10.slha",
  # "scenarioA_mpi_1_mA_0p33_ctau_100.slha",
  # "scenarioA_mpi_1_mA_0p33_ctau_1p0.slha",
  # "scenarioA_mpi_2_mA_0p67_ctau_0p1.slha",
  # "scenarioA_mpi_2_mA_0p67_ctau_10.slha",
  # "scenarioA_mpi_2_mA_0p67_ctau_100.slha",
  # "scenarioA_mpi_2_mA_0p67_ctau_1p0.slha",
  # "scenarioA_mpi_4_mA_0p40_ctau_0p1.slha",
  # "scenarioA_mpi_4_mA_0p40_ctau_10.slha",
  # "scenarioA_mpi_4_mA_0p40_ctau_100.slha",
  # "scenarioA_mpi_4_mA_0p40_ctau_1p0.slha",
  # "scenarioA_mpi_4_mA_1p33_ctau_0p1.slha",
  # "scenarioA_mpi_4_mA_1p33_ctau_10.slha",
  # "scenarioA_mpi_4_mA_1p33_ctau_100.slha",
  # "scenarioA_mpi_4_mA_1p33_ctau_1p0.slha",
  # "scenarioB1_mpi_1_mA_0p33_ctau_0p1.slha",
  # "scenarioB1_mpi_1_mA_0p33_ctau_10.slha",
  # "scenarioB1_mpi_1_mA_0p33_ctau_100.slha",
  # "scenarioB1_mpi_1_mA_0p33_ctau_1p0.slha",
  # "scenarioB1_mpi_2_mA_0p40_ctau_0p1.slha",
  # "scenarioB1_mpi_2_mA_0p40_ctau_10.slha",
  # "scenarioB1_mpi_2_mA_0p40_ctau_100.slha",
  # "scenarioB1_mpi_2_mA_0p40_ctau_1p0.slha",
  # "scenarioB1_mpi_2_mA_0p67_ctau_0p1.slha",
  # "scenarioB1_mpi_2_mA_0p67_ctau_10.slha",
  # "scenarioB1_mpi_2_mA_0p67_ctau_100.slha",
  # "scenarioB1_mpi_2_mA_0p67_ctau_1p0.slha",
  # "scenarioB1_mpi_4_mA_0p80_ctau_0p1.slha",
  # "scenarioB1_mpi_4_mA_0p80_ctau_10.slha",
  # "scenarioB1_mpi_4_mA_0p80_ctau_100.slha",
  # "scenarioB1_mpi_4_mA_0p80_ctau_1p0.slha",
  # "scenarioB1_mpi_4_mA_1p33_ctau_0p1.slha",
  # "scenarioB1_mpi_4_mA_1p33_ctau_10.slha",
  # "scenarioB1_mpi_4_mA_1p33_ctau_100.slha",
  # "scenarioB1_mpi_4_mA_1p33_ctau_1p0.slha",
  # "scenarioB2_mpi_1_mA_0p60_ctau_0p1.slha",
  # "scenarioB2_mpi_1_mA_0p60_ctau_10.slha",
  # "scenarioB2_mpi_1_mA_0p60_ctau_100.slha",
  # "scenarioB2_mpi_1_mA_0p60_ctau_1p0.slha",
  # "scenarioB2_mpi_2_mA_1p10_ctau_0p1.slha",
  # "scenarioB2_mpi_2_mA_1p10_ctau_10.slha",
  # "scenarioB2_mpi_2_mA_1p10_ctau_100.slha",
  # "scenarioB2_mpi_2_mA_1p10_ctau_1p0.slha",
  # "scenarioB2_mpi_4_mA_2p10_ctau_0p1.slha",
  # "scenarioB2_mpi_4_mA_2p10_ctau_10.slha",
  # "scenarioB2_mpi_4_mA_2p10_ctau_100.slha",
  # "scenarioB2_mpi_4_mA_2p10_ctau_1p0.slha",
  # "scenarioC_mpi_10_mA_8p00_ctau_0p1.slha",
  # "scenarioC_mpi_10_mA_8p00_ctau_10.slha",
  # "scenarioC_mpi_10_mA_8p00_ctau_100.slha",
  # "scenarioC_mpi_10_mA_8p00_ctau_1p0.slha",
  # "scenarioC_mpi_2_mA_1p60_ctau_0p1.slha",
  # "scenarioC_mpi_2_mA_1p60_ctau_10.slha",
  # "scenarioC_mpi_2_mA_1p60_ctau_100.slha",
  # "scenarioC_mpi_2_mA_1p60_ctau_1p0.slha",
  # "scenarioC_mpi_4_mA_3p20_ctau_0p1.slha",
  # "scenarioC_mpi_4_mA_3p20_ctau_10.slha",
  # "scenarioC_mpi_4_mA_3p20_ctau_100.slha",
  # "scenarioC_mpi_4_mA_3p20_ctau_1p0.slha",
]


for f in files:
    name = f.split(".")[0]
    if os.path.exists(f"2023/{name}/crab_{name}"):
        continue
    print("Launching", name)
    # continue
    # print(cmnd.format(name=name))
    # print(name)
    os.system(cmnd.format(name=name))
    with open("2023/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name))
    os.system("crab submit 2023/crab_submit_%s.py" % name)

