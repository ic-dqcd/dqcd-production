import os

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '{aux_path}/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'CMSSW_10_6_26/src/nanotron/NANOProducer/test/produceNANO.py'
config.JobType.pyCfgParams = ['year=2018', 'isData=False']

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/jleonhol/samples/nanotron/'
config.Data.publication = True
config.Data.outputDatasetTag = 'nanotron_ext'

config.Site.storageSite = 'T2_UK_London_IC'
"""

def submit(name, dataset, aux_path="."):
    if os.path.exists(f"{aux_path}/{name}/crab_{name}"):
        return
    os.system(f"mkdir -p {aux_path}")
    with open(f"{aux_path}/crab_submit_{name}.py", "w+") as f:
        f.write(crab.format(name=name, dataset=dataset, aux_path=aux_path))
    #os.system(f"crab submit {aux_path}/crab_submit_{name}.py")

if __name__ == "__main__":
    datasets = {
        "scenarioA_mpi_4_mA_1p33_ctau_10": "/scenarioA_mpi_4_mA_1p33_ctau_10/jleonhol-AODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_10_mA_1p00_ctau_0p1": "/scenarioA_mpi_10_mA_1p00_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_10_mA_1p00_ctau_10": "/scenarioA_mpi_10_mA_1p00_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_10_mA_1p00_ctau_100": "/scenarioA_mpi_10_mA_1p00_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_10_mA_1p00_ctau_1p0": "/scenarioA_mpi_10_mA_1p00_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_10_mA_3p33_ctau_0p1": "/scenarioA_mpi_10_mA_3p33_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_10_mA_3p33_ctau_10": "/scenarioA_mpi_10_mA_3p33_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_10_mA_3p33_ctau_100": "/scenarioA_mpi_10_mA_3p33_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_10_mA_3p33_ctau_1p0": "/scenarioA_mpi_10_mA_3p33_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_1_mA_0p33_ctau_0p1": "/scenarioA_mpi_1_mA_0p33_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_1_mA_0p33_ctau_10": "/scenarioA_mpi_1_mA_0p33_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_1_mA_0p33_ctau_100": "/scenarioA_mpi_1_mA_0p33_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_1_mA_0p33_ctau_1p0": "/scenarioA_mpi_1_mA_0p33_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_2_mA_0p67_ctau_0p1": "/scenarioA_mpi_2_mA_0p67_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_2_mA_0p67_ctau_10": "/scenarioA_mpi_2_mA_0p67_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_2_mA_0p67_ctau_100": "/scenarioA_mpi_2_mA_0p67_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_2_mA_0p67_ctau_1p0": "/scenarioA_mpi_2_mA_0p67_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_4_mA_0p40_ctau_0p1": "/scenarioA_mpi_4_mA_0p40_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_4_mA_0p40_ctau_10": "/scenarioA_mpi_4_mA_0p40_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_4_mA_0p40_ctau_100": "/scenarioA_mpi_4_mA_0p40_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_4_mA_0p40_ctau_1p0": "/scenarioA_mpi_4_mA_0p40_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_4_mA_1p33_ctau_0p1": "/scenarioA_mpi_4_mA_1p33_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_4_mA_1p33_ctau_100": "/scenarioA_mpi_4_mA_1p33_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioA_mpi_4_mA_1p33_ctau_1p0": "/scenarioA_mpi_4_mA_1p33_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_1_mA_0p33_ctau_0p1": "/scenarioB1_mpi_1_mA_0p33_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_1_mA_0p33_ctau_10": "/scenarioB1_mpi_1_mA_0p33_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_1_mA_0p33_ctau_100": "/scenarioB1_mpi_1_mA_0p33_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_1_mA_0p33_ctau_1p0": "/scenarioB1_mpi_1_mA_0p33_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_2_mA_0p40_ctau_0p1": "/scenarioB1_mpi_2_mA_0p40_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_2_mA_0p40_ctau_10": "/scenarioB1_mpi_2_mA_0p40_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_2_mA_0p40_ctau_100": "/scenarioB1_mpi_2_mA_0p40_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_2_mA_0p40_ctau_1p0": "/scenarioB1_mpi_2_mA_0p40_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_2_mA_0p67_ctau_0p1": "/scenarioB1_mpi_2_mA_0p67_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_2_mA_0p67_ctau_10": "/scenarioB1_mpi_2_mA_0p67_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_2_mA_0p67_ctau_100": "/scenarioB1_mpi_2_mA_0p67_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_2_mA_0p67_ctau_1p0": "/scenarioB1_mpi_2_mA_0p67_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_4_mA_0p80_ctau_0p1": "/scenarioB1_mpi_4_mA_0p80_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_4_mA_0p80_ctau_10": "/scenarioB1_mpi_4_mA_0p80_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_4_mA_0p80_ctau_100": "/scenarioB1_mpi_4_mA_0p80_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_4_mA_0p80_ctau_1p0": "/scenarioB1_mpi_4_mA_0p80_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_4_mA_1p33_ctau_0p1": "/scenarioB1_mpi_4_mA_1p33_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_4_mA_1p33_ctau_10": "/scenarioB1_mpi_4_mA_1p33_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_4_mA_1p33_ctau_100": "/scenarioB1_mpi_4_mA_1p33_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB1_mpi_4_mA_1p33_ctau_1p0": "/scenarioB1_mpi_4_mA_1p33_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_1_mA_0p60_ctau_0p1": "/scenarioB2_mpi_1_mA_0p60_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_1_mA_0p60_ctau_10": "/scenarioB2_mpi_1_mA_0p60_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_1_mA_0p60_ctau_100": "/scenarioB2_mpi_1_mA_0p60_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_1_mA_0p60_ctau_1p0": "/scenarioB2_mpi_1_mA_0p60_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_2_mA_1p10_ctau_0p1": "/scenarioB2_mpi_2_mA_1p10_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_2_mA_1p10_ctau_10": "/scenarioB2_mpi_2_mA_1p10_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_2_mA_1p10_ctau_100": "/scenarioB2_mpi_2_mA_1p10_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_2_mA_1p10_ctau_1p0": "/scenarioB2_mpi_2_mA_1p10_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_4_mA_2p10_ctau_0p1": "/scenarioB2_mpi_4_mA_2p10_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_4_mA_2p10_ctau_10": "/scenarioB2_mpi_4_mA_2p10_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_4_mA_2p10_ctau_100": "/scenarioB2_mpi_4_mA_2p10_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioB2_mpi_4_mA_2p10_ctau_1p0": "/scenarioB2_mpi_4_mA_2p10_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_10_mA_8p00_ctau_0p1": "/scenarioC_mpi_10_mA_8p00_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_10_mA_8p00_ctau_10": "/scenarioC_mpi_10_mA_8p00_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_10_mA_8p00_ctau_100": "/scenarioC_mpi_10_mA_8p00_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_10_mA_8p00_ctau_1p0": "/scenarioC_mpi_10_mA_8p00_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_2_mA_1p60_ctau_0p1": "/scenarioC_mpi_2_mA_1p60_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_2_mA_1p60_ctau_10": "/scenarioC_mpi_2_mA_1p60_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_2_mA_1p60_ctau_100": "/scenarioC_mpi_2_mA_1p60_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_2_mA_1p60_ctau_1p0": "/scenarioC_mpi_2_mA_1p60_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_4_mA_3p20_ctau_0p1": "/scenarioC_mpi_4_mA_3p20_ctau_0p1/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_4_mA_3p20_ctau_10": "/scenarioC_mpi_4_mA_3p20_ctau_10/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_4_mA_3p20_ctau_100": "/scenarioC_mpi_4_mA_3p20_ctau_100/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
        "scenarioC_mpi_4_mA_3p20_ctau_1p0": "/scenarioC_mpi_4_mA_3p20_ctau_1p0/jleonhol-MINIAODSIM-07bb2832fd9cf08ee8da01c42829422a/USER",
    }

    for name, dataset in datasets.items():
        submit(name, dataset)

