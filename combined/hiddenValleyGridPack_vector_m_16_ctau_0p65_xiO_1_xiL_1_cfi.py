import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *




generator = cms.EDFilter("Pythia8ConcurrentGeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(1.),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8PSweightsSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            "HiggsSM:gg2H = on",
            "25:m0 =125",
            "25:addChannel = 1 1.0 102 4900101 -4900101",
            "25:0:onMode=0",
            "25:1:onMode=0",
            "25:2:onMode=0",
            "25:3:onMode=0",
            "25:4:onMode=0",
            "25:5:onMode=0",
            "25:6:onMode=0",
            "25:7:onMode=0",
            "25:8:onMode=0",
            "25:9:onMode=0",
            "25:10:onMode=0",
            "25:11:onMode=0",
            "25:12:onMode=0",
            "25:13:onMode=0",
            "HiddenValley:Ngauge = 3                          ! number of colors",
            "HiddenValley:nFlav = 1                           ! number of flavors",
            "HiddenValley:fragment = on",
            "HiddenValley:FSR = on",
            "HiddenValley:alphaOrder = 1                      ! use running coupling",
            "HiddenValley:Lambda = 16.0                        ! dark confinement scale",
            "HiddenValley:pTminFSR = 17.6                      ! pT cut off on dark shower (IR regulator)",
            "HiddenValley:spinFv=0                            ! spin of bifundamentals, which are not used, but set for consistency",
            "HiddenValley:probVector=0.75",
            "4900101:m0 = 6.4                                ! Dark Quark Mass, pythia 8 crashes if this is < 0.4 GeV",
            "4900111:m0 = 16.0                                ! Setting pi'0  Mass",
            "4900113:m0 = 16                                ! Setting omega'0 Mass",
            "4900113:addChannel = 1 0.05 91 1 -1                 ! pi0' -> d dbar",
            "4900113:addChannel = 1 0.2 91 2 -2                 ! pi0' -> u ubar",
            "4900113:addChannel = 1 0.05 91 3 -3                 ! pi0' -> s sbar",
            "4900113:addChannel = 1 0.2 91 4 -4                 ! pi0' -> c cbar",
            "4900113:addChannel = 1 0.049 91 5 -5                 ! pi0' -> b bbar",
            "4900113:addChannel = 1 0.15 91 11 -11                 ! pi0' -> e+ e-",
            "4900113:addChannel = 1 0.15 91 13 -13                 ! pi0' -> mu+ mu-",
            "4900113:addChannel = 1 0.15 91 15 -15                 ! pi0' -> tau+ tau-",
            "4900113:tau0 = 0.65                                         ! proper lifetime, in mm",
            "4900111:onMode = 0                                                ! pi'0, stable",
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'processParameters',
            'pythia8PSweightsSettings',
            'pythia8CP5Settings',
        ),
    )
)
generator.PythiaParameters.pythia8CommonSettings.extend(['ParticleDecays:limitTau0 = off'])
MuMuFilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(2, 2),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleID1 = cms.untracked.vint32(13,-13),
)
ProductionFilterSequence = cms.Sequence(generator*MuMuFilter)
