import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *

import os
f = os.environ["CMSSW_BASE"] + "/src/Configuration/GenProduction/data/scenarioB1_mpi_4_mA_1p90_ctau_0p1.slha"

with open(f) as f:
    params = [line.strip() for line in f.readlines()]


generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    crossSection = cms.untracked.double(1.),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
        pythia8PSweightsSettingsBlock,
        processParameters = cms.vstring(params),
        parameterSets = cms.vstring('processParameters', 'pythia8PSweightsSettings')
    )
)
