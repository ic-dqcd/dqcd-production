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
  "scenarioA_mpi_1_mA_0p25_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p25-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p25_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p25-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p25_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p25-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p33_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p33-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p40_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p40-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p40_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p40-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p45_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p45-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p50_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p50-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_0p50_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p50-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p67_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p67-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p80_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p80-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p90_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-0p90-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_1p00_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-1p00-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_1p00_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-1p00-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_1p33_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-1p33-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_1p67_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-1p67-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_1p90_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-1p90-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_2p00_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-2p00-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_2p40_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-2p40-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_3p33_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-3p33-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_4p90_ctau_0p1": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-0p1-mA-4p90-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p25_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p25-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p25_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p25-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p25_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p25-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p33_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p33-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p40_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p40-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p40_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p40-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p45_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p45-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p50_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p50-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_0p50_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p50-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p67_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p67-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p80_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p80-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p90_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-0p90-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_1p00_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-1p00-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_1p00_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-1p00-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_1p33_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-1p33-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_1p67_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-1p67-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_1p90_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-1p90-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_2p00_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-2p00-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_2p40_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-2p40-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_3p33_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-3p33-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_4p90_ctau_10": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-10-mA-4p90-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p25_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p25-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p25_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p25-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p25_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p25-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p33_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p33-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p40_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p40-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p40_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p40-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p45_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p45-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p50_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p50-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_0p50_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p50-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p67_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p67-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p80_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p80-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p90_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-0p90-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_1p00_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-1p00-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_1p00_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-1p00-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_1p33_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-1p33-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_1p67_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-1p67-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_1p90_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-1p90-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_2p00_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-2p00-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_2p40_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-2p40-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_3p33_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-3p33-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_4p90_ctau_100": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-100-mA-4p90-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p25_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p25-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p25_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p25-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p25_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p25-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p33_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p33-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p40_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p40-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p40_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p40-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_1_mA_0p45_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p45-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p50_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p50-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_0p50_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p50-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p67_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p67-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_0p80_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p80-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_2_mA_0p90_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-0p90-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_1p00_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-1p00-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_1p00_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-1p00-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_1p33_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-1p33-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_1p67_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-1p67-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_4_mA_1p90_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-1p90-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_2p00_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-2p00-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_5_mA_2p40_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-2p40-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_3p33_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-3p33-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioA_mpi_10_mA_4p90_ctau_1p0": "/GluGluHToDarkShowers-ScenarioA_Par-ctau-1p0-mA-4p90-mpi-10_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_1_mA_0p33_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-0p33-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p33_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-0p33-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_1_mA_0p40_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-0p40-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p40_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-0p40-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p67_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-0p67-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_0p67_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-0p67-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_0p80_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-0p80-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_0p83_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-0p83-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p90_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-0p90-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_1p00_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-1p00-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_1p33_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-1p33-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_1p67_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-1p67-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_1p90_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-1p90-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_2p40_ctau_0p1": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-0p1-mA-2p40-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_1_mA_0p33_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-0p33-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p33_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-0p33-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_1_mA_0p40_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-0p40-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p40_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-0p40-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p67_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-0p67-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_0p67_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-0p67-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_0p80_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-0p80-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_0p83_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-0p83-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p90_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-0p90-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_1p00_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-1p00-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_1p33_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-1p33-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_1p67_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-1p67-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_1p90_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-1p90-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_2p40_ctau_10": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-10-mA-2p40-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_1_mA_0p33_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-0p33-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p33_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-0p33-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_1_mA_0p40_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-0p40-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p40_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-0p40-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p67_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-0p67-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_0p67_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-0p67-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_0p80_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-0p80-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_0p83_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-0p83-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p90_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-0p90-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_1p00_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-1p00-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_1p33_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-1p33-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_1p67_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-1p67-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_1p90_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-1p90-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_2p40_ctau_100": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-100-mA-2p40-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_1_mA_0p33_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-0p33-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p33_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-0p33-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_1_mA_0p40_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-0p40-mpi-1_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p40_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-0p40-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p67_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-0p67-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_0p67_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-0p67-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_0p80_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-0p80-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_0p83_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-0p83-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_2_mA_0p90_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-0p90-mpi-2_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_1p00_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-1p00-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_1p33_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-1p33-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_1p67_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-1p67-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_4_mA_1p90_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-1p90-mpi-4_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
  "scenarioB1_mpi_5_mA_2p40_ctau_1p0": "/GluGluHToDarkShowers-ScenarioB1_Par-ctau-1p0-mA-2p40-mpi-5_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24MiniAODv6-150X_mcRun3_2024_realistic_v2-v2/MINIAODSIM",
}

for name, dataset in datasets.items():
    if os.path.exists(f"2024_NANOAOD/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2024_NANOAOD/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("CRAB_USE_MYPROXY=0 crab submit 2024_NANOAOD/crab_submit_%s.py" % name)
