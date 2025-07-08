import os

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '2023_AOD_postBPix-ext/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'aod_postBPix_cfg.py'
config.JobType.maxMemoryMB = 2500
# config.JobType.numCores = 8

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/tafoyava/samples/AODSIM/'
config.Data.publication = True
config.Data.outputDatasetTag = 'AODSIM_2023_postBPix-ext'

config.Site.storageSite = 'T2_US_UCSD'

config.Site.blacklist = ['T2_US_MIT']
config.Site.whitelist = ['T2_US_UCSD','T2_US_Wisconsin','T2_US_Florida']
config.section_("Debug")
config.Debug.extraJDL = ['My.CMS_ALLOW_OVERFLOW=False']
"""

datasets = {
     "scenarioA_mpi_10_mA_1p00_ctau_0p1": "/scenarioA_mpi_10_mA_1p00_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_1p00_ctau_10": "/scenarioA_mpi_10_mA_1p00_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_1p00_ctau_100": "/scenarioA_mpi_10_mA_1p00_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_1p00_ctau_1p0": "/scenarioA_mpi_10_mA_1p00_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_2p00_ctau_0p1": "/scenarioA_mpi_10_mA_2p00_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_2p00_ctau_10": "/scenarioA_mpi_10_mA_2p00_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_2p00_ctau_100": "/scenarioA_mpi_10_mA_2p00_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_2p00_ctau_1p0": "/scenarioA_mpi_10_mA_2p00_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_3p33_ctau_0p1": "/scenarioA_mpi_10_mA_3p33_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_3p33_ctau_10": "/scenarioA_mpi_10_mA_3p33_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_3p33_ctau_100": "/scenarioA_mpi_10_mA_3p33_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_3p33_ctau_1p0": "/scenarioA_mpi_10_mA_3p33_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_4p90_ctau_0p1": "/scenarioA_mpi_10_mA_4p90_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_4p90_ctau_10": "/scenarioA_mpi_10_mA_4p90_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_4p90_ctau_100": "/scenarioA_mpi_10_mA_4p90_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_10_mA_4p90_ctau_1p0": "/scenarioA_mpi_10_mA_4p90_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p25_ctau_0p1": "/scenarioA_mpi_1_mA_0p25_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p25_ctau_10": "/scenarioA_mpi_1_mA_0p25_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p25_ctau_100": "/scenarioA_mpi_1_mA_0p25_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p25_ctau_1p0": "/scenarioA_mpi_1_mA_0p25_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p33_ctau_0p1": "/scenarioA_mpi_1_mA_0p33_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p33_ctau_10": "/scenarioA_mpi_1_mA_0p33_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p33_ctau_100": "/scenarioA_mpi_1_mA_0p33_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p33_ctau_1p0": "/scenarioA_mpi_1_mA_0p33_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p45_ctau_0p1": "/scenarioA_mpi_1_mA_0p45_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p45_ctau_10": "/scenarioA_mpi_1_mA_0p45_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p45_ctau_100": "/scenarioA_mpi_1_mA_0p45_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_1_mA_0p45_ctau_1p0": "/scenarioA_mpi_1_mA_0p45_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p25_ctau_0p1": "/scenarioA_mpi_2_mA_0p25_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p25_ctau_10": "/scenarioA_mpi_2_mA_0p25_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p25_ctau_100": "/scenarioA_mpi_2_mA_0p25_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p25_ctau_1p0": "/scenarioA_mpi_2_mA_0p25_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p40_ctau_0p1": "/scenarioA_mpi_2_mA_0p40_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p40_ctau_10": "/scenarioA_mpi_2_mA_0p40_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p40_ctau_100": "/scenarioA_mpi_2_mA_0p40_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p40_ctau_1p0": "/scenarioA_mpi_2_mA_0p40_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p50_ctau_0p1": "/scenarioA_mpi_2_mA_0p50_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p50_ctau_10": "/scenarioA_mpi_2_mA_0p50_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p50_ctau_100": "/scenarioA_mpi_2_mA_0p50_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p50_ctau_1p0": "/scenarioA_mpi_2_mA_0p50_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p67_ctau_0p1": "/scenarioA_mpi_2_mA_0p67_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p67_ctau_10": "/scenarioA_mpi_2_mA_0p67_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p67_ctau_100": "/scenarioA_mpi_2_mA_0p67_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p67_ctau_1p0": "/scenarioA_mpi_2_mA_0p67_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p90_ctau_0p1": "/scenarioA_mpi_2_mA_0p90_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p90_ctau_10": "/scenarioA_mpi_2_mA_0p90_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p90_ctau_100": "/scenarioA_mpi_2_mA_0p90_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_2_mA_0p90_ctau_1p0": "/scenarioA_mpi_2_mA_0p90_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p25_ctau_0p1": "/scenarioA_mpi_4_mA_0p25_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p25_ctau_10": "/scenarioA_mpi_4_mA_0p25_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p25_ctau_100": "/scenarioA_mpi_4_mA_0p25_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p25_ctau_1p0": "/scenarioA_mpi_4_mA_0p25_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p40_ctau_0p1": "/scenarioA_mpi_4_mA_0p40_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p40_ctau_10": "/scenarioA_mpi_4_mA_0p40_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p40_ctau_100": "/scenarioA_mpi_4_mA_0p40_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p40_ctau_1p0": "/scenarioA_mpi_4_mA_0p40_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p80_ctau_0p1": "/scenarioA_mpi_4_mA_0p80_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p80_ctau_10": "/scenarioA_mpi_4_mA_0p80_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p80_ctau_100": "/scenarioA_mpi_4_mA_0p80_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_0p80_ctau_1p0": "/scenarioA_mpi_4_mA_0p80_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_1p33_ctau_0p1": "/scenarioA_mpi_4_mA_1p33_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_1p33_ctau_10": "/scenarioA_mpi_4_mA_1p33_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_1p33_ctau_100": "/scenarioA_mpi_4_mA_1p33_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_1p33_ctau_1p0": "/scenarioA_mpi_4_mA_1p33_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_1p90_ctau_0p1": "/scenarioA_mpi_4_mA_1p90_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_1p90_ctau_10": "/scenarioA_mpi_4_mA_1p90_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_1p90_ctau_100": "/scenarioA_mpi_4_mA_1p90_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_4_mA_1p90_ctau_1p0": "/scenarioA_mpi_4_mA_1p90_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_0p50_ctau_0p1": "/scenarioA_mpi_5_mA_0p50_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_0p50_ctau_10": "/scenarioA_mpi_5_mA_0p50_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_0p50_ctau_100": "/scenarioA_mpi_5_mA_0p50_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_0p50_ctau_1p0": "/scenarioA_mpi_5_mA_0p50_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_1p00_ctau_0p1": "/scenarioA_mpi_5_mA_1p00_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_1p00_ctau_10": "/scenarioA_mpi_5_mA_1p00_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_1p00_ctau_100": "/scenarioA_mpi_5_mA_1p00_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_1p00_ctau_1p0": "/scenarioA_mpi_5_mA_1p00_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_1p67_ctau_0p1": "/scenarioA_mpi_5_mA_1p67_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_1p67_ctau_10": "/scenarioA_mpi_5_mA_1p67_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_1p67_ctau_100": "/scenarioA_mpi_5_mA_1p67_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_1p67_ctau_1p0": "/scenarioA_mpi_5_mA_1p67_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_2p40_ctau_0p1": "/scenarioA_mpi_5_mA_2p40_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_2p40_ctau_10": "/scenarioA_mpi_5_mA_2p40_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_2p40_ctau_100": "/scenarioA_mpi_5_mA_2p40_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioA_mpi_5_mA_2p40_ctau_1p0": "/scenarioA_mpi_5_mA_2p40_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_1_mA_0p33_ctau_0p1": "/scenarioB1_mpi_1_mA_0p33_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_1_mA_0p33_ctau_10": "/scenarioB1_mpi_1_mA_0p33_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_1_mA_0p33_ctau_100": "/scenarioB1_mpi_1_mA_0p33_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_1_mA_0p33_ctau_1p0": "/scenarioB1_mpi_1_mA_0p33_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_1_mA_0p40_ctau_0p1": "/scenarioB1_mpi_1_mA_0p40_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_1_mA_0p40_ctau_10": "/scenarioB1_mpi_1_mA_0p40_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_1_mA_0p40_ctau_100": "/scenarioB1_mpi_1_mA_0p40_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_1_mA_0p40_ctau_1p0": "/scenarioB1_mpi_1_mA_0p40_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p33_ctau_0p1": "/scenarioB1_mpi_2_mA_0p33_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p33_ctau_10": "/scenarioB1_mpi_2_mA_0p33_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p33_ctau_100": "/scenarioB1_mpi_2_mA_0p33_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p33_ctau_1p0": "/scenarioB1_mpi_2_mA_0p33_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p40_ctau_0p1": "/scenarioB1_mpi_2_mA_0p40_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p40_ctau_10": "/scenarioB1_mpi_2_mA_0p40_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p40_ctau_100": "/scenarioB1_mpi_2_mA_0p40_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p40_ctau_1p0": "/scenarioB1_mpi_2_mA_0p40_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p67_ctau_0p1": "/scenarioB1_mpi_2_mA_0p67_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p67_ctau_10": "/scenarioB1_mpi_2_mA_0p67_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p67_ctau_100": "/scenarioB1_mpi_2_mA_0p67_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p67_ctau_1p0": "/scenarioB1_mpi_2_mA_0p67_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p90_ctau_0p1": "/scenarioB1_mpi_2_mA_0p90_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p90_ctau_10": "/scenarioB1_mpi_2_mA_0p90_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p90_ctau_100": "/scenarioB1_mpi_2_mA_0p90_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_2_mA_0p90_ctau_1p0": "/scenarioB1_mpi_2_mA_0p90_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_0p67_ctau_0p1": "/scenarioB1_mpi_4_mA_0p67_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_0p67_ctau_10": "/scenarioB1_mpi_4_mA_0p67_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_0p67_ctau_100": "/scenarioB1_mpi_4_mA_0p67_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_0p67_ctau_1p0": "/scenarioB1_mpi_4_mA_0p67_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_0p80_ctau_0p1": "/scenarioB1_mpi_4_mA_0p80_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_0p80_ctau_10": "/scenarioB1_mpi_4_mA_0p80_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_0p80_ctau_100": "/scenarioB1_mpi_4_mA_0p80_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_0p80_ctau_1p0": "/scenarioB1_mpi_4_mA_0p80_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_1p33_ctau_0p1": "/scenarioB1_mpi_4_mA_1p33_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_1p33_ctau_10": "/scenarioB1_mpi_4_mA_1p33_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_1p33_ctau_100": "/scenarioB1_mpi_4_mA_1p33_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_1p33_ctau_1p0": "/scenarioB1_mpi_4_mA_1p33_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_1p90_ctau_0p1": "/scenarioB1_mpi_4_mA_1p90_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_1p90_ctau_10": "/scenarioB1_mpi_4_mA_1p90_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_1p90_ctau_100": "/scenarioB1_mpi_4_mA_1p90_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_4_mA_1p90_ctau_1p0": "/scenarioB1_mpi_4_mA_1p90_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_0p83_ctau_0p1": "/scenarioB1_mpi_5_mA_0p83_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_0p83_ctau_10": "/scenarioB1_mpi_5_mA_0p83_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_0p83_ctau_100": "/scenarioB1_mpi_5_mA_0p83_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_0p83_ctau_1p0": "/scenarioB1_mpi_5_mA_0p83_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_1p00_ctau_0p1": "/scenarioB1_mpi_5_mA_1p00_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_1p00_ctau_10": "/scenarioB1_mpi_5_mA_1p00_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_1p00_ctau_100": "/scenarioB1_mpi_5_mA_1p00_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_1p00_ctau_1p0": "/scenarioB1_mpi_5_mA_1p00_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_1p67_ctau_0p1": "/scenarioB1_mpi_5_mA_1p67_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_1p67_ctau_10": "/scenarioB1_mpi_5_mA_1p67_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_1p67_ctau_100": "/scenarioB1_mpi_5_mA_1p67_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_1p67_ctau_1p0": "/scenarioB1_mpi_5_mA_1p67_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_2p40_ctau_0p1": "/scenarioB1_mpi_5_mA_2p40_ctau_0p1/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_2p40_ctau_10": "/scenarioB1_mpi_5_mA_2p40_ctau_10/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_2p40_ctau_100": "/scenarioB1_mpi_5_mA_2p40_ctau_100/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
     "scenarioB1_mpi_5_mA_2p40_ctau_1p0": "/scenarioB1_mpi_5_mA_2p40_ctau_1p0/tafoyava-DIGIRAW_2023_postBPix-ext-614897caf85b1c921818c344b3586ba0/USER",
}

for name, dataset in datasets.items():
    if os.path.exists(f"2023_AOD_postBPix-ext/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2023_AOD_postBPix-ext/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("crab submit 2023_AOD_postBPix-ext/crab_submit_%s.py" % name)

