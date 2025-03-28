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
config.Data.outputDatasetTag = 'nanotron_2023'

config.Site.storageSite = 'T2_US_UCSD'
"""

datasets = {
    # "scenarioA_mpi_4_mA_1p33_ctau_10": "/scenarioA_mpi_4_mA_1p33_ctau_10/tafoyava-MINIAODSIM_2022-0bd1d498d73b5aba673807038d08dab2/USER",
    # "scenarioA_mpi_4_mA_1p33_ctau_100": "/scenarioA_mpi_4_mA_1p33_ctau_100/tafoyava-MINIAODSIM_2022-0bd1d498d73b5aba673807038d08dab2/USER",
    # "scenarioA_mpi_4_mA_1p33_ctau_0p1": "/scenarioA_mpi_4_mA_1p33_ctau_0p1/tafoyava-MINIAODSIM_2022-0bd1d498d73b5aba673807038d08dab2/USER",
    # "scenarioA_mpi_4_mA_1p33_ctau_1p0": "/scenarioA_mpi_4_mA_1p33_ctau_1p0/tafoyava-MINIAODSIM_2022-0bd1d498d73b5aba673807038d08dab2/USER",
}

for name, dataset in datasets.items():
    if os.path.exists(f"2023/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2023/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("crab submit 2023/crab_submit_%s.py" % name)

