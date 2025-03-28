import os

#p = "/home/hep/jtafoyav/production_2023/CMSSW_13_2_0/src/Configuration/GenProduction/data"
#files = os.listdir(p)

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '2023_GENSIM_postBPix-ext/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'gensim_postBPix_cfg.py'
config.JobType.maxMemoryMB = 2500
# config.JobType.numCores = 8

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/tafoyava/samples/GENSIM/'
config.Data.publication = True
config.Data.outputDatasetTag = 'GENSIM_2023_postBPix-ext'

config.Site.storageSite = 'T2_US_UCSD'
"""

datasets = {
    #"scenarioA_mpi_10_mA_1p00_ctau_0p1": "/scenarioA_mpi_10_mA_1p00_ctau_0p1/tafoyava-scenarioA_mpi_10_mA_1p00_ctau_0p1_2023-622dffdc6a3cfe7c99a725908eb67d1a/USER",
}

for name, dataset in datasets.items():
    # name = f.split(".")[0]
    # print(cmnd.format(name=name))
    # print(name)
    if os.path.exists(f"2023_GENSIM_postBPix-ext/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2023_GENSIM_postBPix-ext/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("crab submit 2023_GENSIM_postBPix-ext/crab_submit_%s.py &" % name)

