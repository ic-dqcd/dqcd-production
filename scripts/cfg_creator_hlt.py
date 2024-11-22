import os

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '{aux_path}/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'hlt_test.py'
# config.JobType.maxMemoryMB = '1000' 

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/jleonhol/samples/GEN-SIM-RAW/'
config.Data.publication = True
config.Data.outputDatasetTag = 'GEN-SIM-RAW_ext'

config.Site.storageSite = 'T2_UK_London_IC'
"""

def submit(name, dataset, aux_path="."):
    if os.path.exists(f"{aux_path}/{name}/crab_{name}"):
        return
    os.system(f"mkdir -p {aux_path}")
    with open(f"{aux_path}/crab_submit_{name}.py", "w+") as f:
        f.write(crab.format(name=name, dataset=dataset, aux_path=aux_path))
    os.system(f"crab submit {aux_path}/crab_submit_{name}.py")

if __name__ == "__main__":
    datasets = {
    "scenarioA_mpi_4_mA_1p33_ctau_10": "/scenarioA_mpi_4_mA_1p33_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_10_mA_1p00_ctau_0p1": "/scenarioA_mpi_10_mA_1p00_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_10_mA_1p00_ctau_10": "/scenarioA_mpi_10_mA_1p00_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_1_mA_0p33_ctau_0p1": "/scenarioB1_mpi_1_mA_0p33_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_10_mA_1p00_ctau_100": "/scenarioA_mpi_10_mA_1p00_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_10_mA_1p00_ctau_1p0": "/scenarioA_mpi_10_mA_1p00_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_10_mA_3p33_ctau_0p1": "/scenarioA_mpi_10_mA_3p33_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_10_mA_3p33_ctau_10": "/scenarioA_mpi_10_mA_3p33_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_10_mA_3p33_ctau_100": "/scenarioA_mpi_10_mA_3p33_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_10_mA_3p33_ctau_1p0": "/scenarioA_mpi_10_mA_3p33_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_1_mA_0p33_ctau_0p1": "/scenarioA_mpi_1_mA_0p33_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_1_mA_0p33_ctau_10": "/scenarioA_mpi_1_mA_0p33_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_1_mA_0p33_ctau_100": "/scenarioA_mpi_1_mA_0p33_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_1_mA_0p33_ctau_1p0": "/scenarioA_mpi_1_mA_0p33_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_2_mA_0p67_ctau_0p1": "/scenarioA_mpi_2_mA_0p67_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_2_mA_0p67_ctau_10": "/scenarioA_mpi_2_mA_0p67_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_2_mA_0p67_ctau_100": "/scenarioA_mpi_2_mA_0p67_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_2_mA_0p67_ctau_1p0": "/scenarioA_mpi_2_mA_0p67_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_4_mA_0p40_ctau_0p1": "/scenarioA_mpi_4_mA_0p40_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_4_mA_0p40_ctau_10": "/scenarioA_mpi_4_mA_0p40_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_4_mA_0p40_ctau_100": "/scenarioA_mpi_4_mA_0p40_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_4_mA_0p40_ctau_1p0": "/scenarioA_mpi_4_mA_0p40_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_0p1": "/scenarioA_mpi_4_mA_1p33_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_100": "/scenarioA_mpi_4_mA_1p33_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioA_mpi_4_mA_1p33_ctau_1p0": "/scenarioA_mpi_4_mA_1p33_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_1_mA_0p33_ctau_0p1": "/scenarioB1_mpi_1_mA_0p33_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_1_mA_0p33_ctau_10": "/scenarioB1_mpi_1_mA_0p33_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_1_mA_0p33_ctau_100": "/scenarioB1_mpi_1_mA_0p33_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_1_mA_0p33_ctau_1p0": "/scenarioB1_mpi_1_mA_0p33_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_2_mA_0p40_ctau_0p1": "/scenarioB1_mpi_2_mA_0p40_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_2_mA_0p40_ctau_10": "/scenarioB1_mpi_2_mA_0p40_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_2_mA_0p40_ctau_100": "/scenarioB1_mpi_2_mA_0p40_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_2_mA_0p40_ctau_1p0": "/scenarioB1_mpi_2_mA_0p40_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_2_mA_0p67_ctau_0p1": "/scenarioB1_mpi_2_mA_0p67_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_2_mA_0p67_ctau_10": "/scenarioB1_mpi_2_mA_0p67_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_2_mA_0p67_ctau_100": "/scenarioB1_mpi_2_mA_0p67_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_2_mA_0p67_ctau_1p0": "/scenarioB1_mpi_2_mA_0p67_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_4_mA_0p80_ctau_0p1": "/scenarioB1_mpi_4_mA_0p80_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_4_mA_0p80_ctau_10": "/scenarioB1_mpi_4_mA_0p80_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_4_mA_0p80_ctau_100": "/scenarioB1_mpi_4_mA_0p80_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_4_mA_0p80_ctau_1p0": "/scenarioB1_mpi_4_mA_0p80_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_4_mA_1p33_ctau_0p1": "/scenarioB1_mpi_4_mA_1p33_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_4_mA_1p33_ctau_10": "/scenarioB1_mpi_4_mA_1p33_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_4_mA_1p33_ctau_100": "/scenarioB1_mpi_4_mA_1p33_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB1_mpi_4_mA_1p33_ctau_1p0": "/scenarioB1_mpi_4_mA_1p33_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_1_mA_0p60_ctau_0p1": "/scenarioB2_mpi_1_mA_0p60_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_1_mA_0p60_ctau_10": "/scenarioB2_mpi_1_mA_0p60_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_1_mA_0p60_ctau_100": "/scenarioB2_mpi_1_mA_0p60_ctau_100/jleonhol-GEN-SIM-DIGI-00000000000000000000000000000000/USER",
    "scenarioB2_mpi_1_mA_0p60_ctau_1p0": "/scenarioB2_mpi_1_mA_0p60_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_2_mA_1p10_ctau_0p1": "/scenarioB2_mpi_2_mA_1p10_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_2_mA_1p10_ctau_10": "/scenarioB2_mpi_2_mA_1p10_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_2_mA_1p10_ctau_100": "/scenarioB2_mpi_2_mA_1p10_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_2_mA_1p10_ctau_1p0": "/scenarioB2_mpi_2_mA_1p10_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_4_mA_2p10_ctau_0p1": "/scenarioB2_mpi_4_mA_2p10_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_4_mA_2p10_ctau_10": "/scenarioB2_mpi_4_mA_2p10_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_4_mA_2p10_ctau_100": "/scenarioB2_mpi_4_mA_2p10_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioB2_mpi_4_mA_2p10_ctau_1p0": "/scenarioB2_mpi_4_mA_2p10_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_10_mA_8p00_ctau_0p1": "/scenarioC_mpi_10_mA_8p00_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_10_mA_8p00_ctau_10": "/scenarioC_mpi_10_mA_8p00_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_10_mA_8p00_ctau_100": "/scenarioC_mpi_10_mA_8p00_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_10_mA_8p00_ctau_1p0": "/scenarioC_mpi_10_mA_8p00_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_2_mA_1p60_ctau_0p1": "/scenarioC_mpi_2_mA_1p60_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_2_mA_1p60_ctau_10": "/scenarioC_mpi_2_mA_1p60_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_2_mA_1p60_ctau_100": "/scenarioC_mpi_2_mA_1p60_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_2_mA_1p60_ctau_1p0": "/scenarioC_mpi_2_mA_1p60_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_4_mA_3p20_ctau_0p1": "/scenarioC_mpi_4_mA_3p20_ctau_0p1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_4_mA_3p20_ctau_10": "/scenarioC_mpi_4_mA_3p20_ctau_10/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_4_mA_3p20_ctau_100": "/scenarioC_mpi_4_mA_3p20_ctau_100/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "scenarioC_mpi_4_mA_3p20_ctau_1p0": "/scenarioC_mpi_4_mA_3p20_ctau_1p0/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_10_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_10_ctau_100_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_10_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_10_ctau_10_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_10_ctau_1_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_10_ctau_1_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_10_ctau_500_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_10_ctau_500_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_10_ctau_50_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_10_ctau_50_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_15_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_15_ctau_100_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_15_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_15_ctau_10_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_15_ctau_1_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_15_ctau_1_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_15_ctau_500_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_15_ctau_500_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_15_ctau_50_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_15_ctau_50_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_20_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_20_ctau_100_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_20_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_20_ctau_10_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_20_ctau_1_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_20_ctau_1_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_20_ctau_500_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_20_ctau_500_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_20_ctau_50_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_20_ctau_50_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_2_ctau_1_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_1_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_2_ctau_500_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_500_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_2_ctau_50_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_50_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_5_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_5_ctau_100_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_5_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_5_ctau_10_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_5_ctau_1_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_5_ctau_1_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_5_ctau_500_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_5_ctau_500_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",
    "hiddenValleyGridPack_vector_m_5_ctau_50_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_5_ctau_50_xiO_1_xiL_1/jleonhol-GEN-SIM-DIGI-b5536cdb2f3f941524a67b90e01f264f/USER",

    }

    for name, dataset in datasets.items():
        submit(name, dataset)
