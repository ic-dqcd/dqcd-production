import os

crab = """
from CRABClient.UserUtilities import config
config = config()

config.General.requestName = '{name}'
config.General.workArea = '{aux_path}/{name}'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'simdigi_cfg.py'
# config.JobType.maxMemoryMB = '1000' 

config.Data.inputDataset = '{dataset}'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.inputDBS = 'phys03'

config.Data.outLFNDirBase = '/store/user/jleonhol/samples/GEN-SIM-DIGI/'
config.Data.publication = True
config.Data.outputDatasetTag = 'GEN-SIM-DIGI_ext'

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
        "scenarioA_mpi_4_mA_1p33_ctau_10": "/scenarioA_mpi_4_mA_1p33_ctau_10/jleonhol-scenarioA_mpi_4_mA_1p33_ctau_10-ca7f4e31cdcb479a036e6ed2e361d16c/USER",
        "scenarioA_mpi_10_mA_1p00_ctau_0p1": "/scenarioA_mpi_10_mA_1p00_ctau_0p1/jleonhol-scenarioA_mpi_10_mA_1p00_ctau_0p1-6a5ca733fd686f07d4b945bd894b672e/USER",
        "scenarioA_mpi_10_mA_1p00_ctau_10": "/scenarioA_mpi_10_mA_1p00_ctau_10/jleonhol-scenarioA_mpi_10_mA_1p00_ctau_10-96181d73bfa67b80f77f667b0cf9631f/USER",
        "scenarioB1_mpi_1_mA_0p33_ctau_0p1": "/scenarioB1_mpi_1_mA_0p33_ctau_0p1/jleonhol-scenarioB1_mpi_1_mA_0p33_ctau_0p1-29f624779dea0339fcba32dcf6676fd6/USER",
        "scenarioA_mpi_10_mA_1p00_ctau_100": "/scenarioA_mpi_10_mA_1p00_ctau_100/jleonhol-scenarioA_mpi_10_mA_1p00_ctau_100-c76e3daf41fe28bf425b955c396fde8e/USER",
        "scenarioA_mpi_10_mA_1p00_ctau_1p0": "/scenarioA_mpi_10_mA_1p00_ctau_1p0/jleonhol-scenarioA_mpi_10_mA_1p00_ctau_1p0-4d355dc77802766c0f02c095958de04c/USER",
        "scenarioA_mpi_10_mA_3p33_ctau_0p1": "/scenarioA_mpi_10_mA_3p33_ctau_0p1/jleonhol-scenarioA_mpi_10_mA_3p33_ctau_0p1-bbd4c2bc3a89071f8b371cf3da9539c6/USER",
        "scenarioA_mpi_10_mA_3p33_ctau_10": "/scenarioA_mpi_10_mA_3p33_ctau_10/jleonhol-scenarioA_mpi_10_mA_3p33_ctau_10-32a0b8af01e769b2f2b2a75795dc397a/USER",
        "scenarioA_mpi_10_mA_3p33_ctau_100": "/scenarioA_mpi_10_mA_3p33_ctau_100/jleonhol-scenarioA_mpi_10_mA_3p33_ctau_100-4f096502794b6ac34cad7ce232d18bcc/USER",
        "scenarioA_mpi_10_mA_3p33_ctau_1p0": "/scenarioA_mpi_10_mA_3p33_ctau_1p0/jleonhol-scenarioA_mpi_10_mA_3p33_ctau_1p0-6146e3642e8e5e44db0d3b0acbef88d6/USER",
        "scenarioA_mpi_1_mA_0p33_ctau_0p1": "/scenarioA_mpi_1_mA_0p33_ctau_0p1/jleonhol-scenarioA_mpi_1_mA_0p33_ctau_0p1-af6b6ef0cb33ef3c6ef59d8cf1b92279/USER",
        "scenarioA_mpi_1_mA_0p33_ctau_10": "/scenarioA_mpi_1_mA_0p33_ctau_10/jleonhol-scenarioA_mpi_1_mA_0p33_ctau_10-2801f5090f20ed4b6f2ab74209699daa/USER",
        "scenarioA_mpi_1_mA_0p33_ctau_100": "/scenarioA_mpi_1_mA_0p33_ctau_100/jleonhol-scenarioA_mpi_1_mA_0p33_ctau_100-aee0d45c687e80551ccdb574775935f9/USER",
        "scenarioA_mpi_1_mA_0p33_ctau_1p0": "/scenarioA_mpi_1_mA_0p33_ctau_1p0/jleonhol-scenarioA_mpi_1_mA_0p33_ctau_1p0-d5e7cf1df82a2653736d7a181bef65c6/USER",
        "scenarioA_mpi_2_mA_0p67_ctau_0p1": "/scenarioA_mpi_2_mA_0p67_ctau_0p1/jleonhol-scenarioA_mpi_2_mA_0p67_ctau_0p1-5e92cc25b029a555d8eda4eaa244256d/USER",
        "scenarioA_mpi_2_mA_0p67_ctau_10": "/scenarioA_mpi_2_mA_0p67_ctau_10/jleonhol-scenarioA_mpi_2_mA_0p67_ctau_10-c0aa0b0e4368747fb8e0dfb9d9ac523c/USER",
        "scenarioA_mpi_2_mA_0p67_ctau_100": "/scenarioA_mpi_2_mA_0p67_ctau_100/jleonhol-scenarioA_mpi_2_mA_0p67_ctau_100-c484a45e9df5323728a89153feb4b124/USER",
        "scenarioA_mpi_2_mA_0p67_ctau_1p0": "/scenarioA_mpi_2_mA_0p67_ctau_1p0/jleonhol-scenarioA_mpi_2_mA_0p67_ctau_1p0-0103db35dc98979c7b5e79ef7e17e61d/USER",
        "scenarioA_mpi_4_mA_0p40_ctau_0p1": "/scenarioA_mpi_4_mA_0p40_ctau_0p1/jleonhol-scenarioA_mpi_4_mA_0p40_ctau_0p1-b76b5a11a8f975adb40c591745c392cd/USER",
        "scenarioA_mpi_4_mA_0p40_ctau_10": "/scenarioA_mpi_4_mA_0p40_ctau_10/jleonhol-scenarioA_mpi_4_mA_0p40_ctau_10-62f1d1c2e0aa126ff7bfdbeea6fca6c1/USER",
        "scenarioA_mpi_4_mA_0p40_ctau_100": "/scenarioA_mpi_4_mA_0p40_ctau_100/jleonhol-scenarioA_mpi_4_mA_0p40_ctau_100-27f02cf0b768aaf7ae7a22feff862c3c/USER",
        "scenarioA_mpi_4_mA_0p40_ctau_1p0": "/scenarioA_mpi_4_mA_0p40_ctau_1p0/jleonhol-scenarioA_mpi_4_mA_0p40_ctau_1p0-7ce760d73dc7d9baa0328ea31b23dd5c/USER",
        "scenarioA_mpi_4_mA_1p33_ctau_0p1": "/scenarioA_mpi_4_mA_1p33_ctau_0p1/jleonhol-scenarioA_mpi_4_mA_1p33_ctau_0p1-3fd0ca41ead0b4a8f4b1589ca78de36d/USER",
        "scenarioA_mpi_4_mA_1p33_ctau_100": "/scenarioA_mpi_4_mA_1p33_ctau_100/jleonhol-scenarioA_mpi_4_mA_1p33_ctau_100-3392092c59e0db7e9148b18575260462/USER",
        "scenarioA_mpi_4_mA_1p33_ctau_1p0": "/scenarioA_mpi_4_mA_1p33_ctau_1p0/jleonhol-scenarioA_mpi_4_mA_1p33_ctau_1p0-7bc93fd67611f30f2890973030d6598e/USER",
        "scenarioB1_mpi_1_mA_0p33_ctau_0p1": "/scenarioB1_mpi_1_mA_0p33_ctau_0p1/jleonhol-scenarioB1_mpi_1_mA_0p33_ctau_0p1-29f624779dea0339fcba32dcf6676fd6/USER",
        "scenarioB1_mpi_1_mA_0p33_ctau_10": "/scenarioB1_mpi_1_mA_0p33_ctau_10/jleonhol-scenarioB1_mpi_1_mA_0p33_ctau_10-7015bf286039933181b85f18786a502d/USER",
        "scenarioB1_mpi_1_mA_0p33_ctau_100": "/scenarioB1_mpi_1_mA_0p33_ctau_100/jleonhol-scenarioB1_mpi_1_mA_0p33_ctau_100-d6fd87f2eb2c50f7bcab593c08a38307/USER",
        "scenarioB1_mpi_1_mA_0p33_ctau_1p0": "/scenarioB1_mpi_1_mA_0p33_ctau_1p0/jleonhol-scenarioB1_mpi_1_mA_0p33_ctau_1p0-eb6164002ffae29db0aea290caec710d/USER",
        "scenarioB1_mpi_2_mA_0p40_ctau_0p1": "/scenarioB1_mpi_2_mA_0p40_ctau_0p1/jleonhol-scenarioB1_mpi_2_mA_0p40_ctau_0p1-b56dcbf4c2b112052ec7b8d9da6c0faf/USER",
        "scenarioB1_mpi_2_mA_0p40_ctau_10": "/scenarioB1_mpi_2_mA_0p40_ctau_10/jleonhol-scenarioB1_mpi_2_mA_0p40_ctau_10-ec4ad4bacd61f40a1dee0bb312340207/USER",
        "scenarioB1_mpi_2_mA_0p40_ctau_100": "/scenarioB1_mpi_2_mA_0p40_ctau_100/jleonhol-scenarioB1_mpi_2_mA_0p40_ctau_100-fb0e31a8b76b2c884d305c0504e02d0d/USER",
        "scenarioB1_mpi_2_mA_0p40_ctau_1p0": "/scenarioB1_mpi_2_mA_0p40_ctau_1p0/jleonhol-scenarioB1_mpi_2_mA_0p40_ctau_1p0-037ffb1931c29c0599f204856a3c4b80/USER",
        "scenarioB1_mpi_2_mA_0p67_ctau_0p1": "/scenarioB1_mpi_2_mA_0p67_ctau_0p1/jleonhol-scenarioB1_mpi_2_mA_0p67_ctau_0p1-489b0e6f4b161c3e5c6c2f65528c190d/USER",
        "scenarioB1_mpi_2_mA_0p67_ctau_10": "/scenarioB1_mpi_2_mA_0p67_ctau_10/jleonhol-scenarioB1_mpi_2_mA_0p67_ctau_10-42935bf79899c1bd7c39579e5827307c/USER",
        "scenarioB1_mpi_2_mA_0p67_ctau_100": "/scenarioB1_mpi_2_mA_0p67_ctau_100/jleonhol-scenarioB1_mpi_2_mA_0p67_ctau_100-3144c7a5f99ee020da3bbe1f994fda85/USER",
        "scenarioB1_mpi_2_mA_0p67_ctau_1p0": "/scenarioB1_mpi_2_mA_0p67_ctau_1p0/jleonhol-scenarioB1_mpi_2_mA_0p67_ctau_1p0-a95946ffb96792297e66a97daf03a2d4/USER",
        "scenarioB1_mpi_4_mA_0p80_ctau_0p1": "/scenarioB1_mpi_4_mA_0p80_ctau_0p1/jleonhol-scenarioB1_mpi_4_mA_0p80_ctau_0p1-8dd101a700a4247f6ba6a5f076d26e2a/USER",
        "scenarioB1_mpi_4_mA_0p80_ctau_10": "/scenarioB1_mpi_4_mA_0p80_ctau_10/jleonhol-scenarioB1_mpi_4_mA_0p80_ctau_10-d7f624f4fe5ddcfbf32747026f536ee7/USER",
        "scenarioB1_mpi_4_mA_0p80_ctau_100": "/scenarioB1_mpi_4_mA_0p80_ctau_100/jleonhol-scenarioB1_mpi_4_mA_0p80_ctau_100-bd95015c9d10817dd232e9e88e6bc124/USER",
        "scenarioB1_mpi_4_mA_0p80_ctau_1p0": "/scenarioB1_mpi_4_mA_0p80_ctau_1p0/jleonhol-scenarioB1_mpi_4_mA_0p80_ctau_1p0-419d539e30919dc5e23e491f0e329a1d/USER",
        "scenarioB1_mpi_4_mA_1p33_ctau_0p1": "/scenarioB1_mpi_4_mA_1p33_ctau_0p1/jleonhol-scenarioB1_mpi_4_mA_1p33_ctau_0p1-bf803f9e0bdd56a2b7646ef71b6db1bb/USER",
        "scenarioB1_mpi_4_mA_1p33_ctau_10": "/scenarioB1_mpi_4_mA_1p33_ctau_10/jleonhol-scenarioB1_mpi_4_mA_1p33_ctau_10-55f79748a9f404206ebbf22b68289eec/USER",
        "scenarioB1_mpi_4_mA_1p33_ctau_100": "/scenarioB1_mpi_4_mA_1p33_ctau_100/jleonhol-scenarioB1_mpi_4_mA_1p33_ctau_100-30fcb20aa70ca8cee056e5a1ba7bd215/USER",
        "scenarioB1_mpi_4_mA_1p33_ctau_1p0": "/scenarioB1_mpi_4_mA_1p33_ctau_1p0/jleonhol-scenarioB1_mpi_4_mA_1p33_ctau_1p0-f9e46e71f03721a1d9ccd96e0d239222/USER",
        "scenarioB2_mpi_1_mA_0p60_ctau_0p1": "/scenarioB2_mpi_1_mA_0p60_ctau_0p1/jleonhol-scenarioB2_mpi_1_mA_0p60_ctau_0p1-5ff9831865db30ad1edb086d42dd7cb2/USER",
        "scenarioB2_mpi_1_mA_0p60_ctau_10": "/scenarioB2_mpi_1_mA_0p60_ctau_10/jleonhol-scenarioB2_mpi_1_mA_0p60_ctau_10-bc0859988bcd539981c5989b83b6c97b/USER",
        "scenarioB2_mpi_1_mA_0p60_ctau_100": "/scenarioB2_mpi_1_mA_0p60_ctau_100/jleonhol-scenarioB2_mpi_1_mA_0p60_ctau_100-a61d41933540850131c17c99696a263a/USER",
        "scenarioB2_mpi_1_mA_0p60_ctau_1p0": "/scenarioB2_mpi_1_mA_0p60_ctau_1p0/jleonhol-scenarioB2_mpi_1_mA_0p60_ctau_1p0-9e67bb97c7dadb4ec80b91cdfd875943/USER",
        "scenarioB2_mpi_2_mA_1p10_ctau_0p1": "/scenarioB2_mpi_2_mA_1p10_ctau_0p1/jleonhol-scenarioB2_mpi_2_mA_1p10_ctau_0p1-febb1cd59e8b47336828611b7f9d55b4/USER",
        "scenarioB2_mpi_2_mA_1p10_ctau_10": "/scenarioB2_mpi_2_mA_1p10_ctau_10/jleonhol-scenarioB2_mpi_2_mA_1p10_ctau_10-eea0a9d9f4ac47b6309b41c2e6234611/USER",
        "scenarioB2_mpi_2_mA_1p10_ctau_100": "/scenarioB2_mpi_2_mA_1p10_ctau_100/jleonhol-scenarioB2_mpi_2_mA_1p10_ctau_100-04a428eb0629bccaf45a0d8291392295/USER",
        "scenarioB2_mpi_2_mA_1p10_ctau_1p0": "/scenarioB2_mpi_2_mA_1p10_ctau_1p0/jleonhol-scenarioB2_mpi_2_mA_1p10_ctau_1p0-0660dffc560393b0b5ab43024e53b013/USER",
        "scenarioB2_mpi_4_mA_2p10_ctau_0p1": "/scenarioB2_mpi_4_mA_2p10_ctau_0p1/jleonhol-scenarioB2_mpi_4_mA_2p10_ctau_0p1-651de566e4501c765d0282f912df0b85/USER",
        "scenarioB2_mpi_4_mA_2p10_ctau_10": "/scenarioB2_mpi_4_mA_2p10_ctau_10/jleonhol-scenarioB2_mpi_4_mA_2p10_ctau_10-cd02df9e4d37e3aafd0828ef1d4f1ebd/USER",
        "scenarioB2_mpi_4_mA_2p10_ctau_100": "/scenarioB2_mpi_4_mA_2p10_ctau_100/jleonhol-scenarioB2_mpi_4_mA_2p10_ctau_100-1b53de7a4cfe8840731e61d69629ae08/USER",
        "scenarioB2_mpi_4_mA_2p10_ctau_1p0": "/scenarioB2_mpi_4_mA_2p10_ctau_1p0/jleonhol-scenarioB2_mpi_4_mA_2p10_ctau_1p0-6bdf5b4a84cc700d5bac7bd763e55915/USER",
        "scenarioC_mpi_10_mA_8p00_ctau_0p1": "/scenarioC_mpi_10_mA_8p00_ctau_0p1/jleonhol-scenarioC_mpi_10_mA_8p00_ctau_0p1-2bf8e704b9b2537ce09eb644d84d9078/USER",
        "scenarioC_mpi_10_mA_8p00_ctau_10": "/scenarioC_mpi_10_mA_8p00_ctau_10/jleonhol-scenarioC_mpi_10_mA_8p00_ctau_10-f5657d2a54f59ae58986cd49216cc6ab/USER",
        "scenarioC_mpi_10_mA_8p00_ctau_100": "/scenarioC_mpi_10_mA_8p00_ctau_100/jleonhol-scenarioC_mpi_10_mA_8p00_ctau_100-85cc5d429e102936ee46e10b957b67e7/USER",
        "scenarioC_mpi_10_mA_8p00_ctau_1p0": "/scenarioC_mpi_10_mA_8p00_ctau_1p0/jleonhol-scenarioC_mpi_10_mA_8p00_ctau_1p0-1069648626d8de4aeadbb4017de309db/USER",
        "scenarioC_mpi_2_mA_1p60_ctau_0p1": "/scenarioC_mpi_2_mA_1p60_ctau_0p1/jleonhol-scenarioC_mpi_2_mA_1p60_ctau_0p1-1f8626b4b73472954d875e0503ef206f/USER",
        "scenarioC_mpi_2_mA_1p60_ctau_10": "/scenarioC_mpi_2_mA_1p60_ctau_10/jleonhol-scenarioC_mpi_2_mA_1p60_ctau_10-4a22cf029080965060cdffbb8f48f901/USER",
        "scenarioC_mpi_2_mA_1p60_ctau_100": "/scenarioC_mpi_2_mA_1p60_ctau_100/jleonhol-scenarioC_mpi_2_mA_1p60_ctau_100-1a9062562dd60324e749eb9d05ed3df0/USER",
        "scenarioC_mpi_2_mA_1p60_ctau_1p0": "/scenarioC_mpi_2_mA_1p60_ctau_1p0/jleonhol-scenarioC_mpi_2_mA_1p60_ctau_1p0-c25add00b91e7dbc03158a169a323d5b/USER",
        "scenarioC_mpi_4_mA_3p20_ctau_0p1": "/scenarioC_mpi_4_mA_3p20_ctau_0p1/jleonhol-scenarioC_mpi_4_mA_3p20_ctau_0p1-11d5829d386ebffcc414e4b8d0db7e15/USER",
        "scenarioC_mpi_4_mA_3p20_ctau_10": "/scenarioC_mpi_4_mA_3p20_ctau_10/jleonhol-scenarioC_mpi_4_mA_3p20_ctau_10-9ec9fad397f88d928090b0ac3a6ea2e1/USER",
        "scenarioC_mpi_4_mA_3p20_ctau_100": "/scenarioC_mpi_4_mA_3p20_ctau_100/jleonhol-scenarioC_mpi_4_mA_3p20_ctau_100-837c0d87b1b94eb53d28ffec9251e254/USER",
        "scenarioC_mpi_4_mA_3p20_ctau_1p0": "/scenarioC_mpi_4_mA_3p20_ctau_1p0/jleonhol-scenarioC_mpi_4_mA_3p20_ctau_1p0-3243be927c76f52dfcc09acdc3697e71/USER",
        "testZPrime_ctau10": "/testZPrime_ctau10/jleonhol-testZPrime_ctau10-55a8b59ed758b23c4d986f9a9211ee68/USER",
        "hiddenValleyGridPack_vector_m_10_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_10_ctau_100_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_10_ctau_100_xiO_1_xiL_1-74753ad41ba10ecd43c59a5779e733bc/USER",
        "hiddenValleyGridPack_vector_m_10_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_10_ctau_10_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_10_ctau_10_xiO_1_xiL_1-36f037b63bf9621eb06d408bafe18208/USER",
        "hiddenValleyGridPack_vector_m_10_ctau_1_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_10_ctau_1_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_10_ctau_1_xiO_1_xiL_1-e7e16dd931cefcb9c897d60ef2738979/USER",
        "hiddenValleyGridPack_vector_m_10_ctau_500_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_10_ctau_500_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_10_ctau_500_xiO_1_xiL_1-02261d7298717e94a776ab7b739ffb4b/USER",
        "hiddenValleyGridPack_vector_m_10_ctau_50_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_10_ctau_50_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_10_ctau_50_xiO_1_xiL_1-abebee9c15b607a855bcb468d9516111/USER",
        "hiddenValleyGridPack_vector_m_15_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_15_ctau_100_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_15_ctau_100_xiO_1_xiL_1-afec4481a953679c640cbefb48369d0e/USER",
        "hiddenValleyGridPack_vector_m_15_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_15_ctau_10_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_15_ctau_10_xiO_1_xiL_1-beeea6f06205aeb75c03805a2baba8a8/USER",
        "hiddenValleyGridPack_vector_m_15_ctau_1_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_15_ctau_1_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_15_ctau_1_xiO_1_xiL_1-bbd8a02f04f79ae130ff5198dde89674/USER",
        "hiddenValleyGridPack_vector_m_15_ctau_500_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_15_ctau_500_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_15_ctau_500_xiO_1_xiL_1-1109018e8394f92b0083b878259a7a4f/USER",
        "hiddenValleyGridPack_vector_m_15_ctau_50_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_15_ctau_50_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_15_ctau_50_xiO_1_xiL_1-906eba16377fce8c873499e2444582b3/USER",
        "hiddenValleyGridPack_vector_m_20_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_20_ctau_100_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_20_ctau_100_xiO_1_xiL_1-e4a41b418bec0ea0c0e0fe8e66fbe8ac/USER",
        "hiddenValleyGridPack_vector_m_20_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_20_ctau_10_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_20_ctau_10_xiO_1_xiL_1-51415b9db257deec7013de7d4c865ccf/USER",
        "hiddenValleyGridPack_vector_m_20_ctau_1_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_20_ctau_1_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_20_ctau_1_xiO_1_xiL_1-d43d0d89e02fd88e34265d992d710a75/USER",
        "hiddenValleyGridPack_vector_m_20_ctau_500_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_20_ctau_500_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_20_ctau_500_xiO_1_xiL_1-b65f4bece58f462667d1125c34ba7992/USER",
        "hiddenValleyGridPack_vector_m_20_ctau_50_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_20_ctau_50_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_20_ctau_50_xiO_1_xiL_1-a287f968a461fb92957dd7d3df128b14/USER",
        "hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1-0caddfe9f064f9905638b0cccc72869a/USER",
        "hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_2_ctau_100_xiO_1_xiL_1-0caddfe9f064f9905638b0cccc72869a/USER",
        "hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1-db8b8f61b4258621edcd5bd648b458e8/USER",
        "hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_2_ctau_10_xiO_1_xiL_1-db8b8f61b4258621edcd5bd648b458e8/USER",
        "hiddenValleyGridPack_vector_m_2_ctau_1_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_1_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_2_ctau_1_xiO_1_xiL_1-813d847542887b6b9629126d4389aeb5/USER",
        "hiddenValleyGridPack_vector_m_2_ctau_500_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_500_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_2_ctau_500_xiO_1_xiL_1-c782ea20cfc7273a19eedcb226157c27/USER",
        "hiddenValleyGridPack_vector_m_2_ctau_50_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_2_ctau_50_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_2_ctau_50_xiO_1_xiL_1-6c79dd2c260a1c160853e4eeee2f4a8e/USER",
        "hiddenValleyGridPack_vector_m_5_ctau_100_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_5_ctau_100_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_5_ctau_100_xiO_1_xiL_1-573ed3231c4c39c641d0960929230fa8/USER",
        "hiddenValleyGridPack_vector_m_5_ctau_10_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_5_ctau_10_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_5_ctau_10_xiO_1_xiL_1-82aab1dd4085c9719a3066404b029c90/USER",
        "hiddenValleyGridPack_vector_m_5_ctau_1_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_5_ctau_1_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_5_ctau_1_xiO_1_xiL_1-1db07c4570dc6a60953a2e858df80eb8/USER",
        "hiddenValleyGridPack_vector_m_5_ctau_500_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_5_ctau_500_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_5_ctau_500_xiO_1_xiL_1-fe7789c45e0e3e058de267b25c7be69d/USER",
        "hiddenValleyGridPack_vector_m_5_ctau_50_xiO_1_xiL_1": "/hiddenValleyGridPack_vector_m_5_ctau_50_xiO_1_xiL_1/jleonhol-hiddenValleyGridPack_vector_m_5_ctau_50_xiO_1_xiL_1-6266b59384e8218ae9cc88271f38c2d7/USER",
    }

    for name, dataset in datasets.items():
        submit(name, dataset)

