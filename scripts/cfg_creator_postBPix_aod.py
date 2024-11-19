import os

p = "/vols/cms/jtafoyav/production/CMSSW_13_2_0/src/Configuration/GenProduction/data"
files = os.listdir(p)

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '2023/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'aod_postBPix_cfg.py'
config.JobType.maxMemoryMB = 2500
# config.JobType.numCores = 8

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 100
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/tafoyava/samples/AODSIM/'
config.Data.publication = True
config.Data.outputDatasetTag = 'AODSIM_2023'

config.Site.storageSite = 'T2_US_UCSD'
"""

datasets = {
    # "scenarioA_mpi_4_mA_1p33_ctau_10": "/scenarioA_mpi_4_mA_1p33_ctau_10/tafoyava-scenarioA_mpi_4_mA_1p33_ctau_10_2022-7f5f2da1509daceb668e678ad7f6c826/USER",
    # "scenarioA_mpi_4_mA_1p33_ctau_100": "/scenarioA_mpi_4_mA_1p33_ctau_100/tafoyava-scenarioA_mpi_4_mA_1p33_ctau_100_2022-0d52a2f512a8dff64215063478ed58d4/USER",
    # "scenarioA_mpi_4_mA_1p33_ctau_0p1": "/scenarioA_mpi_4_mA_1p33_ctau_0p1/tafoyava-scenarioA_mpi_4_mA_1p33_ctau_0p1_2022-a9026f8b948d21e523e910a9f4d11f1c/USER",
    # "scenarioA_mpi_4_mA_1p33_ctau_1p0": "/scenarioA_mpi_4_mA_1p33_ctau_1p0/tafoyava-scenarioA_mpi_4_mA_1p33_ctau_1p0_2022-9250a3d6ebbbc29553c17fb39e5f0303/USER",
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

