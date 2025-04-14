import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunesRun3ECM13p6TeV.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *




generator = cms.EDFilter("Pythia8ConcurrentGeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13600.0),
    crossSection = cms.untracked.double(1.),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8PSweightsSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            "HiggsSM:gg2H = on",
            "25:m0 =125",
            "25:addChannel = 1 0.5 102 4900101 -4900101",
            "25:addChannel = 1 0.5 102 4900102 -4900102",
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
            "HiddenValley:nFlav = 2                           ! number of flavors",
            "HiddenValley:fragment = on",
            "HiddenValley:FSR = on",
            "HiddenValley:alphaOrder = 1                      ! use running coupling",
            "HiddenValley:setLambda = on                      ! only for pythia 8.309 and higher",
            "HiddenValley:Lambda = 40              ! dark confinement scale",
            "HiddenValley:pTminFSR = 44.0        ! pT cut off on dark shower (IR regulator)",
            "HiddenValley:spinFv=0                            ! spin of bifundamentals: not used, but set for consistency",
            "HiddenValley:probVector=0.75                     ! fraction of hadronization to spin 1",
            "HiddenValley:separateFlav = on                   ! allow for non-degenerate mesons",
            "HiddenValley:probKeepEta1 = 1.0                  ! suppression factor for eta hadronization",
            "4900101:m0 = 41.123088337103745          ! Dark Quark Mass, following arXiv:2203.09503",
            "4900102:m0 = 41.376911662896255          ! Dark Quark Mass, following arXiv:2203.09503",
            "4900111:m0 = 10                        ! Setting pion Mass",
            "4900211:m0 = 10                        ! Setting pion Mass",
            "4900221:m0 = 40                        ! Setting eta Mass",
            "4900113:m0 = 40                       ! Setting rho Mass",
            "4900213:m0 = 40                       ! Setting rho Mass",
            "4900113:addChannel = 1 1.00 91 4900211 -4900211",
            "4900213:addChannel = 1 1.00 91 4900211 4900111",
            "9900015:all = GeneralResonance void 1 0 0 4.9 0.001 0. 0. 0.        ! dark photon A'",
            "9900015:addChannel = 1 0.054 91 1 -1              ! A' -> d dbar",
            "9900015:addChannel = 1 0.216 91 2 -2              ! A' -> u ubar",
            "9900015:addChannel = 1 0.054 91 3 -3              ! A' -> s sbar",
            "9900015:addChannel = 1 0.211 91 4 -4              ! A' -> c cbar",
            "9900015:addChannel = 1 0.162 91 11 -11              ! A' -> e+ e-",
            "9900015:addChannel = 1 0.162 91 13 -13              ! A' -> mu+ mu-",
            "9900015:addChannel = 1 0.141 91 15 -15              ! A' -> tau+ tau-",
            "9900015:tau0 = 60.0                            ! proper lifetime, in mm",
            "4900221:addChannel = 1 0.5 91 4900211 4900211 4900111              ! eta -> pi1 pi1 pi3",
            "4900221:addChannel = 1 0.5 91 -4900211 -4900211 4900111              ! eta -> pi2 pi2 pi3",
            "4900221:tau0 = 0.0                            ! proper lifetime, in mm",
            "4900111:addChannel = 1 1.0 91 9900015 9900015              ! pi3 -> A'A'",
            "4900111:tau0 = 0.0001099000159900015999                            ! proper lifetime, in mm",
            "4900211:onMode = 0",
        ),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'processParameters',
            'pythia8PSweightsSettings',
            'pythia8CP5Settings',
        ),
    )
)

MuMuFilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(1, 1),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleID1 = cms.untracked.vint32(13,-13),
)

ProductionFilterSequence = cms.Sequence(generator*MuMuFilter)
generator.PythiaParameters.pythia8CommonSettings.extend(['ParticleDecays:limitTau0 = off'])
MuMuFilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(2, 2),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleID1 = cms.untracked.vint32(13,-13),
)
ProductionFilterSequence = cms.Sequence(generator*MuMuFilter)
