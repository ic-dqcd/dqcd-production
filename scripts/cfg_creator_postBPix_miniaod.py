import os

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '2023_MINIAOD_postBPix-ext/{name}'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'miniaod_postBPix_cfg.py'
config.JobType.maxMemoryMB = 2500
# config.JobType.numCores = 8

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/tafoyava/samples/MINIAODSIM/'
config.Data.publication = True
config.Data.outputDatasetTag = 'MINIAODSIM_2023_postBPix-ext'

config.Site.storageSite = 'T2_US_UCSD'

config.Site.blacklist = ['T2_US_MIT']
config.Site.whitelist = ['T2_US_UCSD','T2_US_Wisconsin','T2_US_Florida']
config.section_("Debug")
config.Debug.extraJDL = ['My.CMS_ALLOW_OVERFLOW=False']
"""

datasets = {
    "scenarioA_mpi_10_mA_1p00_ctau_0p1": "/scenarioA_mpi_10_mA_1p00_ctau_0p1/tafoyava-AODSIM_2023_postBPix-ext-REMPLACETHISSIGNATURE/USER",
}

for name, dataset in datasets.items():
    if os.path.exists(f"2023_MINIAOD_postBPix-ext/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2023_MINIAOD_postBPix-ext/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("crab submit 2023_MINIAOD_postBPix-ext/crab_submit_%s.py" % name)
