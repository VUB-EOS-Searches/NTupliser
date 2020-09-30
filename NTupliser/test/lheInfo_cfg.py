import FWCore.ParameterSet.Config as cms

##The line below always has to be included to make VarParsing work
import FWCore.ParameterSet.VarParsing as VarParsing

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

options = VarParsing.VarParsing ('analysis')
options.parseArguments()

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
#    fileNames = cms.untracked.vstring(
#        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/tZq_ll_4f_13TeV-amcatnlo-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/120000/04A3B6DA-91C0-E611-BFF9-002590E39D8A.root'
#        'file:/vols/cms/adm10/MC/NLO_HToSSTobbbb_MH125_MS2_ctauS10_13TeV/PAT_miniAOD/miniAOD_2017_10K.root'
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring()
)

process.lheInfo = cms.EDProducer('lheInfo')

  
process.p = cms.EndPath(process.lheInfo)

