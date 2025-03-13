import os

#p = "/home/hep/jtafoyav/production_2023/CMSSW_13_2_0/src/Configuration/GenProduction/data"
#files = os.listdir(p)

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '2023_GENSIM_postBPix/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'gensim_postBPix_cfg.py'
config.JobType.maxMemoryMB = 4500
# config.JobType.numCores = 8

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 500
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/tafoyava/samples/GENSIM/'
config.Data.publication = True
config.Data.outputDatasetTag = 'GENSIM_2023_postBPix'

config.Site.storageSite = 'T2_US_UCSD'
"""

datasets = {
    "scenarioA_mpi_10_mA_1p00_ctau_0p1": "/scenarioA_mpi_10_mA_1p00_ctau_0p1/tafoyava-scenarioA_mpi_10_mA_1p00_ctau_0p1_2023-622dffdc6a3cfe7c99a725908eb67d1a/USER",
    "scenarioA_mpi_10_mA_1p00_ctau_10": "/scenarioA_mpi_10_mA_1p00_ctau_10/tafoyava-scenarioA_mpi_10_mA_1p00_ctau_10_2023-92fc8450648ac9732769fd67327faf59/USER",
    "scenarioA_mpi_10_mA_1p00_ctau_100": "/scenarioA_mpi_10_mA_1p00_ctau_100/tafoyava-scenarioA_mpi_10_mA_1p00_ctau_100_2023-179be740ac7765208017bde447c05746/USER",
    "scenarioA_mpi_10_mA_1p00_ctau_1p0": "/scenarioA_mpi_10_mA_1p00_ctau_1p0/tafoyava-scenarioA_mpi_10_mA_1p00_ctau_1p0_2023-1f1f5879d53b84bd07e2e8dd8b5410f2/USER",
    "scenarioA_mpi_10_mA_2p00_ctau_0p1": "/scenarioA_mpi_10_mA_2p00_ctau_0p1/tafoyava-scenarioA_mpi_10_mA_2p00_ctau_0p1_2023-112f70d86b38e55f39a895623b2d0f36/USER",
    "scenarioA_mpi_10_mA_2p00_ctau_10": "/scenarioA_mpi_10_mA_2p00_ctau_10/tafoyava-scenarioA_mpi_10_mA_2p00_ctau_10_2023-043ad0c746102a5e8280787144da94c8/USER",
    "scenarioA_mpi_10_mA_2p00_ctau_100": "/scenarioA_mpi_10_mA_2p00_ctau_100/tafoyava-scenarioA_mpi_10_mA_2p00_ctau_100_2023-d524d386ee29464da696153d1d84b197/USER",
    "scenarioA_mpi_10_mA_2p00_ctau_1p0": "/scenarioA_mpi_10_mA_2p00_ctau_1p0/tafoyava-scenarioA_mpi_10_mA_2p00_ctau_1p0_2023-d3e5d3df5918fb0cf79175b7938683c4/USER",
    "scenarioA_mpi_10_mA_3p33_ctau_0p1": "/scenarioA_mpi_10_mA_3p33_ctau_0p1/tafoyava-scenarioA_mpi_10_mA_3p33_ctau_0p1_2023-6151aff9e573784b2033cbf19e62da5d/USER",
    "scenarioA_mpi_10_mA_3p33_ctau_10": "/scenarioA_mpi_10_mA_3p33_ctau_10/tafoyava-scenarioA_mpi_10_mA_3p33_ctau_10_2023-c74e6c0d79d235366fab259f4d78dc0c/USER",
    "scenarioA_mpi_10_mA_3p33_ctau_100": "/scenarioA_mpi_10_mA_3p33_ctau_100/tafoyava-scenarioA_mpi_10_mA_3p33_ctau_100_2023-6a08fb903e7381ec31abb07d637bdeb7/USER",
    "scenarioA_mpi_10_mA_3p33_ctau_1p0": "/scenarioA_mpi_10_mA_3p33_ctau_1p0/tafoyava-scenarioA_mpi_10_mA_3p33_ctau_1p0_2023-08421e84e8184e398a88fcc37311ed5e/USER",
    "scenarioA_mpi_10_mA_4p90_ctau_0p1": "/scenarioA_mpi_10_mA_4p90_ctau_0p1/tafoyava-scenarioA_mpi_10_mA_4p90_ctau_0p1_2023-cd9e2ca428507439ebaa6b3abd73785b/USER",
    "scenarioA_mpi_10_mA_4p90_ctau_10": "/scenarioA_mpi_10_mA_4p90_ctau_10/tafoyava-scenarioA_mpi_10_mA_4p90_ctau_10_2023-09b4e69b965c53a0f121dc048b05028d/USER",
    "scenarioA_mpi_10_mA_4p90_ctau_100": "/scenarioA_mpi_10_mA_4p90_ctau_100/tafoyava-scenarioA_mpi_10_mA_4p90_ctau_100_2023-be85c78df541f04f3ea5cd686b623a7a/USER",
    "scenarioA_mpi_10_mA_4p90_ctau_1p0": "/scenarioA_mpi_10_mA_4p90_ctau_1p0/tafoyava-scenarioA_mpi_10_mA_4p90_ctau_1p0_2023-351c7278fc7bd76fe55ed01cf1b529cd/USER",
    "scenarioA_mpi_1_mA_0p25_ctau_0p1": "/scenarioA_mpi_1_mA_0p25_ctau_0p1/tafoyava-scenarioA_mpi_1_mA_0p25_ctau_0p1_2023-41dbf095a5bdad0f312e965f73d3b0d7/USER",
    "scenarioA_mpi_1_mA_0p25_ctau_10": "/scenarioA_mpi_1_mA_0p25_ctau_10/tafoyava-scenarioA_mpi_1_mA_0p25_ctau_10_2023-a4593a15a7ddf5a25f2d44703940e488/USER",
    "scenarioA_mpi_1_mA_0p25_ctau_100": "/scenarioA_mpi_1_mA_0p25_ctau_100/tafoyava-scenarioA_mpi_1_mA_0p25_ctau_100_2023-142a4a559e46a5663ab508ece0acde4f/USER",
    "scenarioA_mpi_1_mA_0p25_ctau_1p0": "/scenarioA_mpi_1_mA_0p25_ctau_1p0/tafoyava-scenarioA_mpi_1_mA_0p25_ctau_1p0_2023-7a127569c3ffd9787cc297f204e6cb0a/USER",
    "scenarioA_mpi_1_mA_0p33_ctau_0p1": "/scenarioA_mpi_1_mA_0p33_ctau_0p1/tafoyava-scenarioA_mpi_1_mA_0p33_ctau_0p1_2023-7ebd81ac23a468b29f980ce2c22ab065/USER",
    "scenarioA_mpi_1_mA_0p33_ctau_10": "/scenarioA_mpi_1_mA_0p33_ctau_10/tafoyava-scenarioA_mpi_1_mA_0p33_ctau_10_2023-21385a669a5fceafa8ddd2b8993f6bb4/USER",
    "scenarioA_mpi_1_mA_0p33_ctau_100": "/scenarioA_mpi_1_mA_0p33_ctau_100/tafoyava-scenarioA_mpi_1_mA_0p33_ctau_100_2023-3d071212b9272df72ab59cb08c26da12/USER",
    "scenarioA_mpi_1_mA_0p33_ctau_1p0": "/scenarioA_mpi_1_mA_0p33_ctau_1p0/tafoyava-scenarioA_mpi_1_mA_0p33_ctau_1p0_2023-2dc95f2d18a2c57201cba40997ab138c/USER",
    "scenarioA_mpi_1_mA_0p45_ctau_0p1": "/scenarioA_mpi_1_mA_0p45_ctau_0p1/tafoyava-scenarioA_mpi_1_mA_0p45_ctau_0p1_2023-be84dce5437151f399fecd370e6916ec/USER",
    "scenarioA_mpi_1_mA_0p45_ctau_10": "/scenarioA_mpi_1_mA_0p45_ctau_10/tafoyava-scenarioA_mpi_1_mA_0p45_ctau_10_2023-237a18171e8ab3ab662ae5770ff1f5e3/USER",
    "scenarioA_mpi_1_mA_0p45_ctau_100": "/scenarioA_mpi_1_mA_0p45_ctau_100/tafoyava-scenarioA_mpi_1_mA_0p45_ctau_100_2023-f19b9d51ccaa6478470fa7fcfb0cafc3/USER",
    "scenarioA_mpi_1_mA_0p45_ctau_1p0": "/scenarioA_mpi_1_mA_0p45_ctau_1p0/tafoyava-scenarioA_mpi_1_mA_0p45_ctau_1p0_2023-eca444876d100d49410534f015a42a5a/USER",
    "scenarioA_mpi_2_mA_0p25_ctau_0p1": "/scenarioA_mpi_2_mA_0p25_ctau_0p1/tafoyava-scenarioA_mpi_2_mA_0p25_ctau_0p1_2023-234288db2bd59106762a287fe3f4fc49/USER",
    "scenarioA_mpi_2_mA_0p25_ctau_10": "/scenarioA_mpi_2_mA_0p25_ctau_10/tafoyava-scenarioA_mpi_2_mA_0p25_ctau_10_2023-f744a9e133ec826fb07a41bd25af103e/USER",
    "scenarioA_mpi_2_mA_0p25_ctau_100": "/scenarioA_mpi_2_mA_0p25_ctau_100/tafoyava-scenarioA_mpi_2_mA_0p25_ctau_100_2023-520558b2ca89a62d7168bc59fae78c8a/USER",
    "scenarioA_mpi_2_mA_0p25_ctau_1p0": "/scenarioA_mpi_2_mA_0p25_ctau_1p0/tafoyava-scenarioA_mpi_2_mA_0p25_ctau_1p0_2023-419b807d42406a84122caa76c3d702cc/USER",
    "scenarioA_mpi_2_mA_0p40_ctau_0p1": "/scenarioA_mpi_2_mA_0p40_ctau_0p1/tafoyava-scenarioA_mpi_2_mA_0p40_ctau_0p1_2023-7048accea014f1fbc354e87e6215ed5d/USER",
    "scenarioA_mpi_2_mA_0p40_ctau_10": "/scenarioA_mpi_2_mA_0p40_ctau_10/tafoyava-scenarioA_mpi_2_mA_0p40_ctau_10_2023-abaeccba75dc1446205be63d59bfc59e/USER",
    "scenarioA_mpi_2_mA_0p40_ctau_100": "/scenarioA_mpi_2_mA_0p40_ctau_100/tafoyava-scenarioA_mpi_2_mA_0p40_ctau_100_2023-a0bcd8022d9f603f57393d6cc5e17cb2/USER",
    "scenarioA_mpi_2_mA_0p40_ctau_1p0": "/scenarioA_mpi_2_mA_0p40_ctau_1p0/tafoyava-scenarioA_mpi_2_mA_0p40_ctau_1p0_2023-c008140cd899246b0a39528e83157330/USER",
    "scenarioA_mpi_2_mA_0p50_ctau_0p1": "/scenarioA_mpi_2_mA_0p50_ctau_0p1/tafoyava-scenarioA_mpi_2_mA_0p50_ctau_0p1_2023-d6306c727b5b5b01b0e2deef24670e69/USER",
    "scenarioA_mpi_2_mA_0p50_ctau_10": "/scenarioA_mpi_2_mA_0p50_ctau_10/tafoyava-scenarioA_mpi_2_mA_0p50_ctau_10_2023-ef3548d859bf3eb83bf6d73cdbfa9cff/USER",
    "scenarioA_mpi_2_mA_0p50_ctau_100": "/scenarioA_mpi_2_mA_0p50_ctau_100/tafoyava-scenarioA_mpi_2_mA_0p50_ctau_100_2023-d0077080f3a88db8c57c26e79dfd9042/USER",
    "scenarioA_mpi_2_mA_0p50_ctau_1p0": "/scenarioA_mpi_2_mA_0p50_ctau_1p0/tafoyava-scenarioA_mpi_2_mA_0p50_ctau_1p0_2023-4d227703c1cc7c23aa918075b039d86b/USER",
    "scenarioA_mpi_2_mA_0p67_ctau_0p1": "/scenarioA_mpi_2_mA_0p67_ctau_0p1/tafoyava-scenarioA_mpi_2_mA_0p67_ctau_0p1_2023-32f5ce9d099e38d0bb295f5b28a6dd15/USER",
    "scenarioA_mpi_2_mA_0p67_ctau_10": "/scenarioA_mpi_2_mA_0p67_ctau_10/tafoyava-scenarioA_mpi_2_mA_0p67_ctau_10_2023-5194246155c9a6b96eaf2fb7ba8eb5ed/USER",
    "scenarioA_mpi_2_mA_0p67_ctau_100": "/scenarioA_mpi_2_mA_0p67_ctau_100/tafoyava-scenarioA_mpi_2_mA_0p67_ctau_100_2023-eb17d9c61fdfdad9ed4d9bd7afec81da/USER",
    "scenarioA_mpi_2_mA_0p67_ctau_1p0": "/scenarioA_mpi_2_mA_0p67_ctau_1p0/tafoyava-scenarioA_mpi_2_mA_0p67_ctau_1p0_2023-cdc005981cf275077266b7d319278b8f/USER",
    "scenarioA_mpi_2_mA_0p90_ctau_0p1": "/scenarioA_mpi_2_mA_0p90_ctau_0p1/tafoyava-scenarioA_mpi_2_mA_0p90_ctau_0p1_2023-fc89ddd49bfce411527887b1326dfe63/USER",
    "scenarioA_mpi_2_mA_0p90_ctau_10": "/scenarioA_mpi_2_mA_0p90_ctau_10/tafoyava-scenarioA_mpi_2_mA_0p90_ctau_10_2023-9337b7e88c2b70e79d82917e5faf531a/USER",
    "scenarioA_mpi_2_mA_0p90_ctau_100": "/scenarioA_mpi_2_mA_0p90_ctau_100/tafoyava-scenarioA_mpi_2_mA_0p90_ctau_100_2023-84cccf575398ce5129fa24b2e9fa799b/USER",
    "scenarioA_mpi_2_mA_0p90_ctau_1p0": "/scenarioA_mpi_2_mA_0p90_ctau_1p0/tafoyava-scenarioA_mpi_2_mA_0p90_ctau_1p0_2023-7470b614597d363a642df596155e6ad4/USER",
    "scenarioA_mpi_4_mA_0p25_ctau_0p1": "/scenarioA_mpi_4_mA_0p25_ctau_0p1/tafoyava-scenarioA_mpi_4_mA_0p25_ctau_0p1_2023-aac2cb83f3f995b237dd4f43b0548b9d/USER",
    "scenarioA_mpi_4_mA_0p25_ctau_10": "/scenarioA_mpi_4_mA_0p25_ctau_10/tafoyava-scenarioA_mpi_4_mA_0p25_ctau_10_2023-ca06f15dbe755d2a87f83c252fe50f78/USER",
    "scenarioA_mpi_4_mA_0p25_ctau_100": "/scenarioA_mpi_4_mA_0p25_ctau_100/tafoyava-scenarioA_mpi_4_mA_0p25_ctau_100_2023-3fa0556cbe95d158b07744bfe4db4de1/USER",
    "scenarioA_mpi_4_mA_0p25_ctau_1p0": "/scenarioA_mpi_4_mA_0p25_ctau_1p0/tafoyava-scenarioA_mpi_4_mA_0p25_ctau_1p0_2023-93ffeaa63dc8d1d5a765ad3026011000/USER",
    "scenarioA_mpi_4_mA_0p40_ctau_0p1": "/scenarioA_mpi_4_mA_0p40_ctau_0p1/tafoyava-scenarioA_mpi_4_mA_0p40_ctau_0p1_2023-151ef4aa158830955a30eab7184abffc/USER",
    "scenarioA_mpi_4_mA_0p40_ctau_10": "/scenarioA_mpi_4_mA_0p40_ctau_10/tafoyava-scenarioA_mpi_4_mA_0p40_ctau_10_2023-fab278bbb6d9fc89122002aed2f8f34c/USER",
    "scenarioA_mpi_4_mA_0p40_ctau_100": "/scenarioA_mpi_4_mA_0p40_ctau_100/tafoyava-scenarioA_mpi_4_mA_0p40_ctau_100_2023-c136c75f1c7fb45dcd882e090b2ef67b/USER",
    "scenarioA_mpi_4_mA_0p40_ctau_1p0": "/scenarioA_mpi_4_mA_0p40_ctau_1p0/tafoyava-scenarioA_mpi_4_mA_0p40_ctau_1p0_2023-12fdcd412cfc5a8265d4ac26d2ee9a8b/USER",
    "scenarioA_mpi_4_mA_0p80_ctau_0p1": "/scenarioA_mpi_4_mA_0p80_ctau_0p1/tafoyava-scenarioA_mpi_4_mA_0p80_ctau_0p1_2023-6aee024e3a91026bab049ae818aa4684/USER",
    "scenarioA_mpi_4_mA_0p80_ctau_10": "/scenarioA_mpi_4_mA_0p80_ctau_10/tafoyava-scenarioA_mpi_4_mA_0p80_ctau_10_2023-9f45ea2a858581d7db6be2f27345210d/USER",
    "scenarioA_mpi_4_mA_0p80_ctau_100": "/scenarioA_mpi_4_mA_0p80_ctau_100/tafoyava-scenarioA_mpi_4_mA_0p80_ctau_100_2023-801e2367d079af991b242e2edb0694c4/USER",
    "scenarioA_mpi_4_mA_0p80_ctau_1p0": "/scenarioA_mpi_4_mA_0p80_ctau_1p0/tafoyava-scenarioA_mpi_4_mA_0p80_ctau_1p0_2023-50f8aa18e5d1050bc75476f0a1bd6299/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_0p1": "/scenarioA_mpi_4_mA_1p33_ctau_0p1/tafoyava-scenarioA_mpi_4_mA_1p33_ctau_0p1_2023-f14f49dc71c966985c7058fccd47ef16/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_10": "/scenarioA_mpi_4_mA_1p33_ctau_10/tafoyava-scenarioA_mpi_4_mA_1p33_ctau_10_2023-d5465824a0e8cba1c4f320675fc44b5b/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_100": "/scenarioA_mpi_4_mA_1p33_ctau_100/tafoyava-scenarioA_mpi_4_mA_1p33_ctau_100_2023-902b18d4ce4a9daa49ea04e47bf98dfa/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_1p0": "/scenarioA_mpi_4_mA_1p33_ctau_1p0/tafoyava-scenarioA_mpi_4_mA_1p33_ctau_1p0_2023-9a63a973d4e6b25aca3cfc1630f1e07b/USER",
    "scenarioA_mpi_4_mA_1p90_ctau_0p1": "/scenarioA_mpi_4_mA_1p90_ctau_0p1/tafoyava-scenarioA_mpi_4_mA_1p90_ctau_0p1_2023-bcc904b627c77509d3017c75703490f3/USER",
    "scenarioA_mpi_4_mA_1p90_ctau_10": "/scenarioA_mpi_4_mA_1p90_ctau_10/tafoyava-scenarioA_mpi_4_mA_1p90_ctau_10_2023-b8fe99eef01b47e08488e7a8ca9d8271/USER",
    "scenarioA_mpi_4_mA_1p90_ctau_100": "/scenarioA_mpi_4_mA_1p90_ctau_100/tafoyava-scenarioA_mpi_4_mA_1p90_ctau_100_2023-826aea77f2e5915cc9edda82508ea443/USER",
    "scenarioA_mpi_4_mA_1p90_ctau_1p0": "/scenarioA_mpi_4_mA_1p90_ctau_1p0/tafoyava-scenarioA_mpi_4_mA_1p90_ctau_1p0_2023-8e7d80d893961a221f80f7320d55e5f8/USER",
    "scenarioA_mpi_5_mA_0p50_ctau_0p1": "/scenarioA_mpi_5_mA_0p50_ctau_0p1/tafoyava-scenarioA_mpi_5_mA_0p50_ctau_0p1_2023-ac9499467a732089d1a8e86eed630c38/USER",
    "scenarioA_mpi_5_mA_0p50_ctau_10": "/scenarioA_mpi_5_mA_0p50_ctau_10/tafoyava-scenarioA_mpi_5_mA_0p50_ctau_10_2023-face6697a3ec565951cafa2216b2bfcd/USER",
    "scenarioA_mpi_5_mA_0p50_ctau_100": "/scenarioA_mpi_5_mA_0p50_ctau_100/tafoyava-scenarioA_mpi_5_mA_0p50_ctau_100_2023-e0e51f424ec8d47c7fbe756a4f63c806/USER",
    "scenarioA_mpi_5_mA_0p50_ctau_1p0": "/scenarioA_mpi_5_mA_0p50_ctau_1p0/tafoyava-scenarioA_mpi_5_mA_0p50_ctau_1p0_2023-697fd8662109be62cfa07f8b45a4e009/USER",
    "scenarioA_mpi_5_mA_1p00_ctau_0p1": "/scenarioA_mpi_5_mA_1p00_ctau_0p1/tafoyava-scenarioA_mpi_5_mA_1p00_ctau_0p1_2023-34f04cddf71f5b5f02930b8dcc0c5e6d/USER",
    "scenarioA_mpi_5_mA_1p00_ctau_10": "/scenarioA_mpi_5_mA_1p00_ctau_10/tafoyava-scenarioA_mpi_5_mA_1p00_ctau_10_2023-02756c67a5aaebb1939643efe4358cf8/USER",
    "scenarioA_mpi_5_mA_1p00_ctau_100": "/scenarioA_mpi_5_mA_1p00_ctau_100/tafoyava-scenarioA_mpi_5_mA_1p00_ctau_100_2023-dbcb103328e2280fdd2ff73a48eafcff/USER",
    "scenarioA_mpi_5_mA_1p00_ctau_1p0": "/scenarioA_mpi_5_mA_1p00_ctau_1p0/tafoyava-scenarioA_mpi_5_mA_1p00_ctau_1p0_2023-d9ca6d501c964d8a603d1e9da8e83729/USER",
    "scenarioA_mpi_5_mA_1p67_ctau_0p1": "/scenarioA_mpi_5_mA_1p67_ctau_0p1/tafoyava-scenarioA_mpi_5_mA_1p67_ctau_0p1_2023-304ea38ea42c8b2979f8b60f197c5f04/USER",
    "scenarioA_mpi_5_mA_1p67_ctau_10": "/scenarioA_mpi_5_mA_1p67_ctau_10/tafoyava-scenarioA_mpi_5_mA_1p67_ctau_10_2023-ee6803a613f7ef93c8d419f8618a278f/USER",
    "scenarioA_mpi_5_mA_1p67_ctau_100": "/scenarioA_mpi_5_mA_1p67_ctau_100/tafoyava-scenarioA_mpi_5_mA_1p67_ctau_100_2023-661dd662b121e3e2c2584a747dba6168/USER",
    "scenarioA_mpi_5_mA_1p67_ctau_1p0": "/scenarioA_mpi_5_mA_1p67_ctau_1p0/tafoyava-scenarioA_mpi_5_mA_1p67_ctau_1p0_2023-426713bbe94048b19a82fefcc98f5496/USER",
    "scenarioA_mpi_5_mA_2p40_ctau_0p1": "/scenarioA_mpi_5_mA_2p40_ctau_0p1/tafoyava-scenarioA_mpi_5_mA_2p40_ctau_0p1_2023-dedf5cef89346b6f71d8d9ad333fb2f8/USER",
    "scenarioA_mpi_5_mA_2p40_ctau_10": "/scenarioA_mpi_5_mA_2p40_ctau_10/tafoyava-scenarioA_mpi_5_mA_2p40_ctau_10_2023-cedeab11f2c54f62be3e115eb5aff571/USER",
    "scenarioA_mpi_5_mA_2p40_ctau_100": "/scenarioA_mpi_5_mA_2p40_ctau_100/tafoyava-scenarioA_mpi_5_mA_2p40_ctau_100_2023-a65a95fcf24996ec7e521215127880f6/USER",
    "scenarioA_mpi_5_mA_2p40_ctau_1p0": "/scenarioA_mpi_5_mA_2p40_ctau_1p0/tafoyava-scenarioA_mpi_5_mA_2p40_ctau_1p0_2023-3b5f70d7698a878739630ce35749045a/USER",
    "scenarioB1_mpi_1_mA_0p33_ctau_0p1": "/scenarioB1_mpi_1_mA_0p33_ctau_0p1/tafoyava-scenarioB1_mpi_1_mA_0p33_ctau_0p1_2023-c051d1f5c89ac65c4582be188b45c688/USER",
    "scenarioB1_mpi_1_mA_0p33_ctau_10": "/scenarioB1_mpi_1_mA_0p33_ctau_10/tafoyava-scenarioB1_mpi_1_mA_0p33_ctau_10_2023-403edc560e8f86462a0ea791078c1b92/USER",
    "scenarioB1_mpi_1_mA_0p33_ctau_100": "/scenarioB1_mpi_1_mA_0p33_ctau_100/tafoyava-scenarioB1_mpi_1_mA_0p33_ctau_100_2023-c8a219975acf5e312504570c9a88374b/USER",
    "scenarioB1_mpi_1_mA_0p33_ctau_1p0": "/scenarioB1_mpi_1_mA_0p33_ctau_1p0/tafoyava-scenarioB1_mpi_1_mA_0p33_ctau_1p0_2023-fd1398ae2456dc684e817a54ec62d73a/USER",
    "scenarioB1_mpi_1_mA_0p40_ctau_0p1": "/scenarioB1_mpi_1_mA_0p40_ctau_0p1/tafoyava-scenarioB1_mpi_1_mA_0p40_ctau_0p1_2023-e608c20901d330926d0a69a41b26eacc/USER",
    "scenarioB1_mpi_1_mA_0p40_ctau_10": "/scenarioB1_mpi_1_mA_0p40_ctau_10/tafoyava-scenarioB1_mpi_1_mA_0p40_ctau_10_2023-5059235b9a68a7a1871aabd24dbfeb60/USER",
    "scenarioB1_mpi_1_mA_0p40_ctau_100": "/scenarioB1_mpi_1_mA_0p40_ctau_100/tafoyava-scenarioB1_mpi_1_mA_0p40_ctau_100_2023-a50d9157f578be533d836864934982b0/USER",
    "scenarioB1_mpi_1_mA_0p40_ctau_1p0": "/scenarioB1_mpi_1_mA_0p40_ctau_1p0/tafoyava-scenarioB1_mpi_1_mA_0p40_ctau_1p0_2023-e47c5212acd283b7896eed61193cd118/USER",
    "scenarioB1_mpi_2_mA_0p33_ctau_0p1": "/scenarioB1_mpi_2_mA_0p33_ctau_0p1/tafoyava-scenarioB1_mpi_2_mA_0p33_ctau_0p1_2023-ac2124dd2b36c13a67772679d7aa3061/USER",
    "scenarioB1_mpi_2_mA_0p33_ctau_10": "/scenarioB1_mpi_2_mA_0p33_ctau_10/tafoyava-scenarioB1_mpi_2_mA_0p33_ctau_10_2023-d8dd5d881f935982cfb470709fbfcbe6/USER",
    "scenarioB1_mpi_2_mA_0p33_ctau_100": "/scenarioB1_mpi_2_mA_0p33_ctau_100/tafoyava-scenarioB1_mpi_2_mA_0p33_ctau_100_2023-3b1a1df6bfd06b15aa7db285ba55aa7f/USER",
    "scenarioB1_mpi_2_mA_0p33_ctau_1p0": "/scenarioB1_mpi_2_mA_0p33_ctau_1p0/tafoyava-scenarioB1_mpi_2_mA_0p33_ctau_1p0_2023-aa65c88a74a092fe91b8cb8345fb3492/USER",
    "scenarioB1_mpi_2_mA_0p40_ctau_0p1": "/scenarioB1_mpi_2_mA_0p40_ctau_0p1/tafoyava-scenarioB1_mpi_2_mA_0p40_ctau_0p1_2023-ff1a2d3849539cca0672a719e05a68ca/USER",
    "scenarioB1_mpi_2_mA_0p40_ctau_10": "/scenarioB1_mpi_2_mA_0p40_ctau_10/tafoyava-scenarioB1_mpi_2_mA_0p40_ctau_10_2023-a0b4ee1f5ae425693fd5f70c6de064b4/USER",
    "scenarioB1_mpi_2_mA_0p40_ctau_100": "/scenarioB1_mpi_2_mA_0p40_ctau_100/tafoyava-scenarioB1_mpi_2_mA_0p40_ctau_100_2023-12756ce88ffea6a456cbe36b713a99c4/USER",
    "scenarioB1_mpi_2_mA_0p40_ctau_1p0": "/scenarioB1_mpi_2_mA_0p40_ctau_1p0/tafoyava-scenarioB1_mpi_2_mA_0p40_ctau_1p0_2023-451c1a1577aaba485012f7b105bcf61b/USER",
    "scenarioB1_mpi_2_mA_0p67_ctau_0p1": "/scenarioB1_mpi_2_mA_0p67_ctau_0p1/tafoyava-scenarioB1_mpi_2_mA_0p67_ctau_0p1_2023-dffafdeb59dbd85f3e4f36397e71173f/USER",
    "scenarioB1_mpi_2_mA_0p67_ctau_10": "/scenarioB1_mpi_2_mA_0p67_ctau_10/tafoyava-scenarioB1_mpi_2_mA_0p67_ctau_10_2023-4c68cd49d97b06e98cf7581fcf0c1e2b/USER",
    "scenarioB1_mpi_2_mA_0p67_ctau_100": "/scenarioB1_mpi_2_mA_0p67_ctau_100/tafoyava-scenarioB1_mpi_2_mA_0p67_ctau_100_2023-d738325abe1ef1053abe69883cf869b6/USER",
    "scenarioB1_mpi_2_mA_0p67_ctau_1p0": "/scenarioB1_mpi_2_mA_0p67_ctau_1p0/tafoyava-scenarioB1_mpi_2_mA_0p67_ctau_1p0_2023-3109fb65dd34e4ce43177c349d2bba60/USER",
    "scenarioB1_mpi_2_mA_0p90_ctau_0p1": "/scenarioB1_mpi_2_mA_0p90_ctau_0p1/tafoyava-scenarioB1_mpi_2_mA_0p90_ctau_0p1_2023-f832492d3424995ba464bb9e145d57e5/USER",
    "scenarioB1_mpi_2_mA_0p90_ctau_10": "/scenarioB1_mpi_2_mA_0p90_ctau_10/tafoyava-scenarioB1_mpi_2_mA_0p90_ctau_10_2023-b9ca154e3ca27ddd6db5b24d38e64da1/USER",
    "scenarioB1_mpi_2_mA_0p90_ctau_100": "/scenarioB1_mpi_2_mA_0p90_ctau_100/tafoyava-scenarioB1_mpi_2_mA_0p90_ctau_100_2023-6cacaec5cf08c9a0d1ae477d8c8e22ce/USER",
    "scenarioB1_mpi_2_mA_0p90_ctau_1p0": "/scenarioB1_mpi_2_mA_0p90_ctau_1p0/tafoyava-scenarioB1_mpi_2_mA_0p90_ctau_1p0_2023-1c4dcd43659c56de596307ef0786b4f0/USER",
    "scenarioB1_mpi_4_mA_0p67_ctau_0p1": "/scenarioB1_mpi_4_mA_0p67_ctau_0p1/tafoyava-scenarioB1_mpi_4_mA_0p67_ctau_0p1_2023-d1adfdad8ec1e127af82d3e79d0bff1f/USER",
    "scenarioB1_mpi_4_mA_0p67_ctau_10": "/scenarioB1_mpi_4_mA_0p67_ctau_10/tafoyava-scenarioB1_mpi_4_mA_0p67_ctau_10_2023-9476eb1d3d0f61517c60989fc7512222/USER",
    "scenarioB1_mpi_4_mA_0p67_ctau_100": "/scenarioB1_mpi_4_mA_0p67_ctau_100/tafoyava-scenarioB1_mpi_4_mA_0p67_ctau_100_2023-864b80049e758fb91e728b834e2e2a1e/USER",
    "scenarioB1_mpi_4_mA_0p67_ctau_1p0": "/scenarioB1_mpi_4_mA_0p67_ctau_1p0/tafoyava-scenarioB1_mpi_4_mA_0p67_ctau_1p0_2023-5c78f293cefed4720653054fb80b5b30/USER",
    "scenarioB1_mpi_4_mA_0p80_ctau_0p1": "/scenarioB1_mpi_4_mA_0p80_ctau_0p1/tafoyava-scenarioB1_mpi_4_mA_0p80_ctau_0p1_2023-a321e04bd04e702a86dc7d0e0bb9f13d/USER",
    "scenarioB1_mpi_4_mA_0p80_ctau_10": "/scenarioB1_mpi_4_mA_0p80_ctau_10/tafoyava-scenarioB1_mpi_4_mA_0p80_ctau_10_2023-a5e84d961bbcb675b72cc3fd41fe77bf/USER",
    "scenarioB1_mpi_4_mA_0p80_ctau_100": "/scenarioB1_mpi_4_mA_0p80_ctau_100/tafoyava-scenarioB1_mpi_4_mA_0p80_ctau_100_2023-5177b69d83b8becf58196cd1567a9a68/USER",
    "scenarioB1_mpi_4_mA_0p80_ctau_1p0": "/scenarioB1_mpi_4_mA_0p80_ctau_1p0/tafoyava-scenarioB1_mpi_4_mA_0p80_ctau_1p0_2023-6266018272030c388ad5ddf1e71bfb44/USER",
    "scenarioB1_mpi_4_mA_1p33_ctau_0p1": "/scenarioB1_mpi_4_mA_1p33_ctau_0p1/tafoyava-scenarioB1_mpi_4_mA_1p33_ctau_0p1_2023-dafdd8602c5f05dcaeaf5c894550595d/USER",
    "scenarioB1_mpi_4_mA_1p33_ctau_10": "/scenarioB1_mpi_4_mA_1p33_ctau_10/tafoyava-scenarioB1_mpi_4_mA_1p33_ctau_10_2023-27e9a2bb2ff8de9cdcf85d54b4873597/USER",
    "scenarioB1_mpi_4_mA_1p33_ctau_100": "/scenarioB1_mpi_4_mA_1p33_ctau_100/tafoyava-scenarioB1_mpi_4_mA_1p33_ctau_100_2023-9ea7f9eba0647b78f6d506cce8ad2fb4/USER",
    "scenarioB1_mpi_4_mA_1p33_ctau_1p0": "/scenarioB1_mpi_4_mA_1p33_ctau_1p0/tafoyava-scenarioB1_mpi_4_mA_1p33_ctau_1p0_2023-828de422f4a30565eee642d7f5a9adcb/USER",
    "scenarioB1_mpi_4_mA_1p90_ctau_0p1": "/scenarioB1_mpi_4_mA_1p90_ctau_0p1/tafoyava-scenarioB1_mpi_4_mA_1p90_ctau_0p1_2023-b796849d336252dcfcc4cfeb6f1dac09/USER",
    "scenarioB1_mpi_4_mA_1p90_ctau_10": "/scenarioB1_mpi_4_mA_1p90_ctau_10/tafoyava-scenarioB1_mpi_4_mA_1p90_ctau_10_2023-1cc51a111648dcd52f5157421867d5ef/USER",
    "scenarioB1_mpi_4_mA_1p90_ctau_100": "/scenarioB1_mpi_4_mA_1p90_ctau_100/tafoyava-scenarioB1_mpi_4_mA_1p90_ctau_100_2023-7dbccc9ffed56e4471bf9e63fba4acc3/USER",
    "scenarioB1_mpi_4_mA_1p90_ctau_1p0": "/scenarioB1_mpi_4_mA_1p90_ctau_1p0/tafoyava-scenarioB1_mpi_4_mA_1p90_ctau_1p0_2023-63984009f593549592d51526b9ad7430/USER",
    "scenarioB1_mpi_5_mA_0p83_ctau_0p1": "/scenarioB1_mpi_5_mA_0p83_ctau_0p1/tafoyava-scenarioB1_mpi_5_mA_0p83_ctau_0p1_2023-e5f82c1a27ff96c637dabf86ee9cf545/USER",
    "scenarioB1_mpi_5_mA_0p83_ctau_10": "/scenarioB1_mpi_5_mA_0p83_ctau_10/tafoyava-scenarioB1_mpi_5_mA_0p83_ctau_10_2023-4ac7e9da6861b86f73855cad6845a8e3/USER",
    "scenarioB1_mpi_5_mA_0p83_ctau_100": "/scenarioB1_mpi_5_mA_0p83_ctau_100/tafoyava-scenarioB1_mpi_5_mA_0p83_ctau_100_2023-232563465495de3a1370afb32c3da7ec/USER",
    "scenarioB1_mpi_5_mA_0p83_ctau_1p0": "/scenarioB1_mpi_5_mA_0p83_ctau_1p0/tafoyava-scenarioB1_mpi_5_mA_0p83_ctau_1p0_2023-6daa3b0198dbb5ba103151198bdabfc0/USER",
    "scenarioB1_mpi_5_mA_1p00_ctau_0p1": "/scenarioB1_mpi_5_mA_1p00_ctau_0p1/tafoyava-scenarioB1_mpi_5_mA_1p00_ctau_0p1_2023-b09b6b4293e53e189a9267dedbaf5fc2/USER",
    "scenarioB1_mpi_5_mA_1p00_ctau_10": "/scenarioB1_mpi_5_mA_1p00_ctau_10/tafoyava-scenarioB1_mpi_5_mA_1p00_ctau_10_2023-536f1d79915b49eeb8136a86f7a0be84/USER",
    "scenarioB1_mpi_5_mA_1p00_ctau_100": "/scenarioB1_mpi_5_mA_1p00_ctau_100/tafoyava-scenarioB1_mpi_5_mA_1p00_ctau_100_2023-aaeca14cc0bde47c84554dd5602a55a1/USER",
    "scenarioB1_mpi_5_mA_1p00_ctau_1p0": "/scenarioB1_mpi_5_mA_1p00_ctau_1p0/tafoyava-scenarioB1_mpi_5_mA_1p00_ctau_1p0_2023-88ba0157e898df1c331127da907a378c/USER",
    "scenarioB1_mpi_5_mA_1p67_ctau_0p1": "/scenarioB1_mpi_5_mA_1p67_ctau_0p1/tafoyava-scenarioB1_mpi_5_mA_1p67_ctau_0p1_2023-d84e18befc581fba01f0dc8b0d3c569d/USER",
    "scenarioB1_mpi_5_mA_1p67_ctau_10": "/scenarioB1_mpi_5_mA_1p67_ctau_10/tafoyava-scenarioB1_mpi_5_mA_1p67_ctau_10_2023-3cfb384c221abe94571cf7a63c5cfc16/USER",
    "scenarioB1_mpi_5_mA_1p67_ctau_100": "/scenarioB1_mpi_5_mA_1p67_ctau_100/tafoyava-scenarioB1_mpi_5_mA_1p67_ctau_100_2023-7192c39bf092b8543a04a8dfde6b8fae/USER",
    "scenarioB1_mpi_5_mA_1p67_ctau_1p0": "/scenarioB1_mpi_5_mA_1p67_ctau_1p0/tafoyava-scenarioB1_mpi_5_mA_1p67_ctau_1p0_2023-5dab6e5eda00ddbca0ac74576b77e2a1/USER",
    "scenarioB1_mpi_5_mA_2p40_ctau_0p1": "/scenarioB1_mpi_5_mA_2p40_ctau_0p1/tafoyava-scenarioB1_mpi_5_mA_2p40_ctau_0p1_2023-80b4fb22c3604f3acb75e325e3344b5c/USER",
    "scenarioB1_mpi_5_mA_2p40_ctau_10": "/scenarioB1_mpi_5_mA_2p40_ctau_10/tafoyava-scenarioB1_mpi_5_mA_2p40_ctau_10_2023-6b255153dfba8d014036ebdf9cf56a3c/USER",
    "scenarioB1_mpi_5_mA_2p40_ctau_100": "/scenarioB1_mpi_5_mA_2p40_ctau_100/tafoyava-scenarioB1_mpi_5_mA_2p40_ctau_100_2023-579c83aab542e76bc11fb09aa61af0ca/USER",
    "scenarioB1_mpi_5_mA_2p40_ctau_1p0": "/scenarioB1_mpi_5_mA_2p40_ctau_1p0/tafoyava-scenarioB1_mpi_5_mA_2p40_ctau_1p0_2023-9f26b681849e97c088ccaf9579454172/USER",
    "scenarioB2_mpi_1_mA_0p60_ctau_0p1": "/scenarioB2_mpi_1_mA_0p60_ctau_0p1/tafoyava-scenarioB2_mpi_1_mA_0p60_ctau_0p1_2023-57105624b8a05ea8ff0d47f4baf9f40b/USER",
    "scenarioB2_mpi_1_mA_0p60_ctau_10": "/scenarioB2_mpi_1_mA_0p60_ctau_10/tafoyava-scenarioB2_mpi_1_mA_0p60_ctau_10_2023-a50a0234394806ccedbf5e1c0046c122/USER",
    "scenarioB2_mpi_1_mA_0p60_ctau_100": "/scenarioB2_mpi_1_mA_0p60_ctau_100/tafoyava-scenarioB2_mpi_1_mA_0p60_ctau_100_2023-dd7465ececbc5cdf9e9051a361c14fa3/USER",
    "scenarioB2_mpi_1_mA_0p60_ctau_1p0": "/scenarioB2_mpi_1_mA_0p60_ctau_1p0/tafoyava-scenarioB2_mpi_1_mA_0p60_ctau_1p0_2023-1016b709f174d6898a6e1ff5b267d07e/USER",
    "scenarioB2_mpi_2_mA_1p10_ctau_0p1": "/scenarioB2_mpi_2_mA_1p10_ctau_0p1/tafoyava-scenarioB2_mpi_2_mA_1p10_ctau_0p1_2023-9ccad261ff9bf378c55e7319e0062efa/USER",
    "scenarioB2_mpi_2_mA_1p10_ctau_10": "/scenarioB2_mpi_2_mA_1p10_ctau_10/tafoyava-scenarioB2_mpi_2_mA_1p10_ctau_10_2023-6a1c63b0409bf234a544571144ceeff3/USER",
    "scenarioB2_mpi_2_mA_1p10_ctau_100": "/scenarioB2_mpi_2_mA_1p10_ctau_100/tafoyava-scenarioB2_mpi_2_mA_1p10_ctau_100_2023-52d5c2e6c318066539152ebf18518c55/USER",
    "scenarioB2_mpi_2_mA_1p10_ctau_1p0": "/scenarioB2_mpi_2_mA_1p10_ctau_1p0/tafoyava-scenarioB2_mpi_2_mA_1p10_ctau_1p0_2023-63c65e47e2c4a093e77b0da2ebb4d900/USER",
    "scenarioB2_mpi_4_mA_2p10_ctau_0p1": "/scenarioB2_mpi_4_mA_2p10_ctau_0p1/tafoyava-scenarioB2_mpi_4_mA_2p10_ctau_0p1_2023-ae6e145e6177392487dcdcf725c8a51b/USER",
    "scenarioB2_mpi_4_mA_2p10_ctau_10": "/scenarioB2_mpi_4_mA_2p10_ctau_10/tafoyava-scenarioB2_mpi_4_mA_2p10_ctau_10_2023-24f1d1e6a7f262c699007758fc2f15fe/USER",
    "scenarioB2_mpi_4_mA_2p10_ctau_100": "/scenarioB2_mpi_4_mA_2p10_ctau_100/tafoyava-scenarioB2_mpi_4_mA_2p10_ctau_100_2023-1e83d9b5f64e275415e30848ee88c5c6/USER",
    "scenarioB2_mpi_4_mA_2p10_ctau_1p0": "/scenarioB2_mpi_4_mA_2p10_ctau_1p0/tafoyava-scenarioB2_mpi_4_mA_2p10_ctau_1p0_2023-141377eae1b7c9e64265de713bfd406c/USER",
    "scenarioB2_mpi_5_mA_2p60_ctau_0p1": "/scenarioB2_mpi_5_mA_2p60_ctau_0p1/tafoyava-scenarioB2_mpi_5_mA_2p60_ctau_0p1_2023-2ec513a4e9b86e40f1751e62619a44f4/USER",
    "scenarioB2_mpi_5_mA_2p60_ctau_10": "/scenarioB2_mpi_5_mA_2p60_ctau_10/tafoyava-scenarioB2_mpi_5_mA_2p60_ctau_10_2023-3f4f5d8ab1ab5db19d6a84acfc25f0b9/USER",
    "scenarioB2_mpi_5_mA_2p60_ctau_100": "/scenarioB2_mpi_5_mA_2p60_ctau_100/tafoyava-scenarioB2_mpi_5_mA_2p60_ctau_100_2023-e62225cf077256e52ac6e1b2f3563ee9/USER",
    "scenarioB2_mpi_5_mA_2p60_ctau_1p0": "/scenarioB2_mpi_5_mA_2p60_ctau_1p0/tafoyava-scenarioB2_mpi_5_mA_2p60_ctau_1p0_2023-df662dcc3ed329b30cc34020a330d311/USER",
    "scenarioC_mpi_10_mA_8p00_ctau_0p1": "/scenarioC_mpi_10_mA_8p00_ctau_0p1/tafoyava-scenarioC_mpi_10_mA_8p00_ctau_0p1_2023-8d24f8a670bd30e7874672924bbbc978/USER",
    "scenarioC_mpi_10_mA_8p00_ctau_10": "/scenarioC_mpi_10_mA_8p00_ctau_10/tafoyava-scenarioC_mpi_10_mA_8p00_ctau_10_2023-149f25182876f02aafb7a09dffc4a827/USER",
    "scenarioC_mpi_10_mA_8p00_ctau_100": "/scenarioC_mpi_10_mA_8p00_ctau_100/tafoyava-scenarioC_mpi_10_mA_8p00_ctau_100_2023-05587ddc71ae69278d4b4a8cc3e5a38f/USER",
    "scenarioC_mpi_10_mA_8p00_ctau_1p0": "/scenarioC_mpi_10_mA_8p00_ctau_1p0/tafoyava-scenarioC_mpi_10_mA_8p00_ctau_1p0_2023-5c446ba3c9fa02ae1c9b146fdef582a7/USER",
    "scenarioC_mpi_2_mA_1p60_ctau_0p1": "/scenarioC_mpi_2_mA_1p60_ctau_0p1/tafoyava-scenarioC_mpi_2_mA_1p60_ctau_0p1_2023-4579548b260fd2982d89098b2b980616/USER",
    "scenarioC_mpi_2_mA_1p60_ctau_10": "/scenarioC_mpi_2_mA_1p60_ctau_10/tafoyava-scenarioC_mpi_2_mA_1p60_ctau_10_2023-bab638e0127bf707afee40b1c2d45c1b/USER",
    "scenarioC_mpi_2_mA_1p60_ctau_100": "/scenarioC_mpi_2_mA_1p60_ctau_100/tafoyava-scenarioC_mpi_2_mA_1p60_ctau_100_2023-fedf6dd4f2c11caca6c01ab2e8c6f22a/USER",
    "scenarioC_mpi_2_mA_1p60_ctau_1p0": "/scenarioC_mpi_2_mA_1p60_ctau_1p0/tafoyava-scenarioC_mpi_2_mA_1p60_ctau_1p0_2023-87873611a280302de8d1a763762d4fa8/USER",
    "scenarioC_mpi_4_mA_3p20_ctau_0p1": "/scenarioC_mpi_4_mA_3p20_ctau_0p1/tafoyava-scenarioC_mpi_4_mA_3p20_ctau_0p1_2023-3dd00a0898c0eb1b5a5d2609701f84a5/USER",
    "scenarioC_mpi_4_mA_3p20_ctau_10": "/scenarioC_mpi_4_mA_3p20_ctau_10/tafoyava-scenarioC_mpi_4_mA_3p20_ctau_10_2023-5ab2e9139443570cf39454056b9f73ae/USER",
    "scenarioC_mpi_4_mA_3p20_ctau_100": "/scenarioC_mpi_4_mA_3p20_ctau_100/tafoyava-scenarioC_mpi_4_mA_3p20_ctau_100_2023-9a80fb1b11bd479e43b7b106f93c3eed/USER",
    "scenarioC_mpi_4_mA_3p20_ctau_1p0": "/scenarioC_mpi_4_mA_3p20_ctau_1p0/tafoyava-scenarioC_mpi_4_mA_3p20_ctau_1p0_2023-e17e49ece3355f2429e97ea0a50c44f4/USER",
}

for name, dataset in datasets.items():
    # name = f.split(".")[0]
    # print(cmnd.format(name=name))
    # print(name)
    if os.path.exists(f"2023_GENSIM_postBPix/{name}/crab_{name}"):
        continue
    #os.system(cmnd.format(name=name))
    with open("2023_GENSIM_postBPix/crab_submit_%s.py" % name, "w+") as f:
        f.write(crab.format(name=name, dataset=dataset))
    os.system("crab submit 2023_GENSIM_postBPix/crab_submit_%s.py" % name)

