import os

p = "/home/hep/jleonhol/samplegeneration/gen/nicepythia/CMSSW_13_2_0/src/Configuration/GenProduction/data/"
files = os.listdir(p)

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '2023/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'aod_cfg.py'
config.JobType.maxMemoryMB = 2500
# config.JobType.numCores = 8

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/jleonhol/samples/AODSIM/'
config.Data.publication = True
config.Data.outputDatasetTag = 'AODSIM_2023'

config.Site.storageSite = 'T2_UK_London_IC'
"""

datasets = {
    # "scenarioA_mpi_4_mA_1p33_ctau_10": "/scenarioA_mpi_4_mA_1p33_ctau_10/jleonhol-scenarioA_mpi_4_mA_1p33_ctau_10_2022-ecf4a583228f65e16019e00d96f41f77/USER",
    # "scenarioA_mpi_4_mA_1p33_ctau_0p1": "/scenarioA_mpi_4_mA_1p33_ctau_0p1/jleonhol-scenarioA_mpi_4_mA_1p33_ctau_0p1_2022-0df1009824dae361041086fdd8b62230/USER",
    # "scenarioA_mpi_4_mA_1p33_ctau_100": "/scenarioA_mpi_4_mA_1p33_ctau_100/jleonhol-scenarioA_mpi_4_mA_1p33_ctau_100_2022-083453e5d820d4dc4b07e180627c561e/USER",
    # "scenarioA_mpi_4_mA_1p33_ctau_1p0": "/scenarioA_mpi_4_mA_1p33_ctau_1p0/jleonhol-scenarioA_mpi_4_mA_1p33_ctau_1p0_2022-53a0d741c19eae261a06f270970f54e0/USER",
}

for name, dataset in datasets.items():
    # name = f.split(".")[0]
    # print(cmnd.format(name=name))
    # print(name)
    if os.path.exists(f"2023/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2023/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("crab submit 2023/crab_submit_%s.py" % name)

