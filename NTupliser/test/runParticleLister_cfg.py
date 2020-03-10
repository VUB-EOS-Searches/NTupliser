#Setting up various environmental stuff that makes all of this jazz actually work.
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')
options.setDefault('maxEvents', 3)
options.parseArguments()

process = cms.Process("USER")

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
#	'file:/scratch/eepgadm/data/tZq/AOD.root',	
        'file:/vols/cms/adm10/MC/NLO_HToSSTobbbb_MH125_MS2_ctauS10_13TeV/RAW2DIGI_RECO_EI/step2_2017_10K.root',
        )
)

## Events to process
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )


process.printTree = cms.EDAnalyzer("ParticleListDrawer",
  maxEventsToPrint = cms.untracked.int32(3),
  printVertex = cms.untracked.bool(False),
  src = cms.InputTag("genParticles")
)

process.p = cms.Path(process.printTree)
