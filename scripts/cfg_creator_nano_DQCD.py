import os

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '2024_NANOAOD/{name}'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nanotron/NANOProducer/test/produceNANO.py'
# config.JobType.maxMemoryMB = '2500'
config.JobType.pyCfgParams = ['year=2024', 'isData=False']

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 100000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'global'
config.Data.publishDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/tafoyava/samples/nanotron/'
config.Data.publication = True
config.Data.outputDatasetTag = 'nanotron-v15_2024-RunIII2024Summer24-150X_mcRun3_2024_realistic-v2'

config.Site.storageSite = 'T2_US_UCSD'

config.Site.blacklist = ['T2_US_MIT','T1_RU_JINR']
# N.B. whitelisting and CMS_ALLOW_OVERFLOW=False also limit to which servers we have access to. If a server storing one of the samples is not explicitly mentioned, the processing will ignore it and run only over those explicitly accessible
#config.Site.whitelist = ['T2_US_UCSD','T2_US_Wisconsin','T2_US_Florida', 'T2_BE_IIHE', 'T2_IT_Rome', 'T2_US_Nebraska', 'T1_UK_RAL',]
#config.section_("Debug")
#config.Debug.extraJDL = ['My.CMS_ALLOW_OVERFLOW=False']
"""

datasets = {
  "QCD_Pt-1000_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-120To170_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-120to170_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-15To20_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-15to20_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-170To300_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-170to300_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-20To30_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-20to30_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-300To470_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-300to470_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-30To50_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-30to50_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-470To600_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-470to600_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-50To80_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-50to80_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-600To800_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-600to800_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-800To1000_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-800to1000_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "QCD_Pt-80To120_MuEnriched_TuneCP5_13p6TeV_pythia8": "/QCD_Bin-PT-80to120_Fil-MuEnriched_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
}

for name, dataset in datasets.items():
    if os.path.exists(f"2024_NANOAOD/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2024_NANOAOD/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("CRAB_USE_MYPROXY=0 crab submit 2024_NANOAOD/crab_submit_%s.py" % name)
