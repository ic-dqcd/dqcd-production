import os

p = "/vols/cms/jtafoyav/production/CMSSW_13_2_0/src/Configuration/GenProduction/data"
files = os.listdir(p)

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'miniaod_postEE_cfg.py'
config.JobType.maxMemoryMB = 2500
# config.JobType.numCores = 8

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/tafoyava/samples/MINIAODSIM/'
config.Data.publication = True
config.Data.outputDatasetTag = 'MINIAODSIM_2022'

config.Site.storageSite = 'T2_US_UCSD'
"""

datasets = {
    "scenarioA_mpi_4_mA_1p33_ctau_10": "/scenarioA_mpi_4_mA_1p33_ctau_10/tafoyava-AODSIM_2022-6c55dbd4f99ed6c824b000a7a99348b1/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_100": "/scenarioA_mpi_4_mA_1p33_ctau_100/tafoyava-AODSIM_2022-6c55dbd4f99ed6c824b000a7a99348b1/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_0p1": "/scenarioA_mpi_4_mA_1p33_ctau_0p1/tafoyava-AODSIM_2022-6c55dbd4f99ed6c824b000a7a99348b1/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_1p0": "/scenarioA_mpi_4_mA_1p33_ctau_1p0/tafoyava-AODSIM_2022-6c55dbd4f99ed6c824b000a7a99348b1/USER",
}

for name, dataset in datasets.items():
    # name = f.split(".")[0]
    # print(cmnd.format(name=name))
    # print(name)
    if os.path.exists(f"{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("crab submit crab_submit_%s.py" % name)

