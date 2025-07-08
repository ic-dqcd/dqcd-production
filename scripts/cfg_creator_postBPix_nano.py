import os

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '2023_NANOAOD_postBPix-ext/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'produceNANO.py'
# config.JobType.maxMemoryMB = '2500'
config.JobType.pyCfgParams = ['year=2023', 'isData=False']

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/tafoyava/samples/nanotron/'
config.Data.publication = True
config.Data.outputDatasetTag = 'nanotron_2023_postBPix-ext'

config.Site.storageSite = 'T2_US_UCSD'

config.Site.blacklist = ['T2_US_MIT']
config.Site.whitelist = ['T2_US_UCSD','T2_US_Wisconsin','T2_US_Florida']
config.section_("Debug")
config.Debug.extraJDL = ['My.CMS_ALLOW_OVERFLOW=False']
"""

datasets = {
    "scenarioA_mpi_4_mA_1p33_ctau_10": "/scenarioA_mpi_4_mA_1p33_ctau_10/tafoyava-MINIAODSIM_2022-REPLACETHISSIGNATURE/USER",
}

for name, dataset in datasets.items():
    if os.path.exists(f"2023_NANOAOD_postBPix-ext/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2023_NANOAOD_postBPix-ext/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("crab submit 2023_NANOAOD_postBPix-ext/crab_submit_%s.py" % name)
