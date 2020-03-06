#Set up the pat environment
import FWCore.ParameterSet.Config as cms
process = cms.Process("customPAT")

from PhysicsTools.PatAlgos.tools.coreTools import *

#Setting up various environmental stuff that makes all of this jazz actually work.

###############################
####### Global Setup ##########
###############################

process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('PhysicsTools.PatAlgos.slimming.unpackedTracksAndVertices_cfi')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.load("TrackingTools/TransientTrack/TransientTrackBuilder_cfi")

process.load('RecoBTag.Configuration.RecoBTag_cff')
process.load('RecoJets.Configuration.RecoJetAssociations_cff')
process.load('RecoJets.Configuration.RecoJetAssociations_cff')
process.load('TrackingTools.TransientTrack.TransientTrackBuilder_cfi')

process.load("FWCore.Framework.test.cmsExceptionsFatal_cff")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load('Configuration.StandardSequences.Services_cff')

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.destinations = ['cerr']
process.MessageLogger.statistics = []
process.MessageLogger.fwkJobReports = []
process.MessageLogger.categories=cms.untracked.vstring('FwkJob'
                                                       ,'FwkReport'
                                                       ,'FwkSummary'
                                                       )

process.MessageLogger.cerr.INFO = cms.untracked.PSet(limit = cms.untracked.int32(0))
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(10000)
process.options = cms.untracked.PSet(
                     wantSummary = cms.untracked.bool(True)
                     )

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag.globaltag = cms.string('80X_dataRun2_2016SeptRepro_v7') #RunsA-F 80X_dataRun2_2016SeptRepro_v7; RunH 80X_dataRun2_Prompt_v16

#There's a bit in here about some btau tags that the code looks for. I don't know if this is significant, however. I'm going to ignore it for now.

#Import jet reco things. Apparently this makes cmsRun crash.
process.load('RecoJets.Configuration.RecoPFJets_cff')

process.ak4JetTracksAssociatorAtVertexPF.jets = cms.InputTag("ak4PFJetsCHS")
process.ak4JetTracksAssociatorAtVertexPF.tracks = cms.InputTag("unpackedTracksAndVertices")
process.impactParameterTagInfos.primaryVertex = cms.InputTag("unpackedTracksAndVertices")
process.inclusiveSecondaryVertexFinderTagInfos.extSVCollection = cms.InputTag("unpackedTracksAndVertices","secondary","")


#Now do cool fast jet correction things!

process.ak4PFJets.doRhoFastjet = True

from PhysicsTools.SelectorUtils.pvSelector_cfi import pvSelector

###############################
########Jet corrections########
###############################

from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection

updateJetCollection(
   process,
   jetSource = cms.InputTag('slimmedJets'),
   labelName = 'UpdatedJEC',
   jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']), 'None'),
)

process.jetCorrection = cms.Sequence( process.patJetCorrFactorsUpdatedJEC * process.updatedPatJetsUpdatedJEC )

###############################
########EGM Regression#########
###############################

from EgammaAnalysis.ElectronTools.regressionWeights_cfi import regressionWeights
process = regressionWeights(process)
process.load('EgammaAnalysis.ElectronTools.regressionApplication_cff')

###############################
#########EGM Smearing##########
###############################

process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
                                                   calibratedPatElectrons  = cms.PSet( initialSeed = cms.untracked.uint32(81),
                                                                                       engineName = cms.untracked.string('TRandom3'),
                                                                                       ),
                                                   )

process.load('EgammaAnalysis.ElectronTools.calibratedPatElectronsRun2_cfi')

process.calibratedPatElectrons.isMC = cms.bool(False)
#process.calibratedPatElectrons.correctionFile = cms.string("Moriond17_23Jan")

###############################
###### Electron ID ############
###############################

process.load("RecoEgamma.ElectronIdentification.ElectronIDValueMapProducer_cfi")
process.load("RecoEgamma.ElectronIdentification.ElectronMVAValueMapProducer_cfi")

from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

switchOnVIDElectronIdProducer(process, DataFormat.MiniAOD)

# define which IDs we want to produce
my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Summer16_80X_V1_cff']

#add them to the VID producer
for idmod in my_id_modules:
    setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)

process.selectedElectrons = cms.EDFilter("PATElectronSelector",
    src = cms.InputTag("calibratedPatElectrons"),
    cut = cms.string("pt>5 && abs(superCluster.eta)<2.50")
                                         )

process.egmGsfElectronIDs.physicsObjectSrc = cms.InputTag("selectedElectrons")
process.electronIDValueMapProducer.srcMiniAOD = cms.InputTag('selectedElectrons')
process.electronRegressionValueMapProducer.srcMiniAOD = cms.InputTag('selectedElectrons')

process.processedElectrons = cms.Sequence( process.regressionApplication + process.calibratedPatElectrons + process.selectedElectrons + process.egmGsfElectronIDSequence + process.electronIDValueMapProducer + process.electronRegressionValueMapProducer )

###############################
##### MET Uncertainities ######
###############################

from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD

# If you only want to re-correct for JEC and get the proper uncertainties for the default MET
runMetCorAndUncFromMiniAOD(process,
                           isData=True
                           )

# Now you are creating the bad muon corrected MET
process.load('RecoMET.METFilters.badGlobalMuonTaggersMiniAOD_cff')
process.badGlobalMuonTaggerMAOD.taggingMode = cms.bool(True)
process.cloneGlobalMuonTaggerMAOD.taggingMode = cms.bool(True)

from PhysicsTools.PatUtils.tools.muonRecoMitigation import muonRecoMitigation

muonRecoMitigation(
    process = process,
    pfCandCollection = "packedPFCandidates", #input PF Candidate Collection
    runOnMiniAOD = True, #To determine if you are running on AOD or MiniAOD
    selection="", #You can use a custom selection for your bad muons. Leave empty if you would like to use the bad muon recipe definition.
    muonCollection="", #The muon collection name where your custom selection will be applied to. Leave empty if you would like to use the bad muon recipe definition.
    cleanCollName="cleanMuonsPFCandidates", #output pf candidate collection ame
    cleaningScheme="computeAllApplyClone", #Options are: "all", "computeAllApplyBad","computeAllApplyClone". Decides which (or both) bad muon collections to be used for MET cleaning coming from the bad muon recipe.
    postfix="" #Use if you would like to add a post fix to your muon / pf collections
    )

runMetCorAndUncFromMiniAOD(process,
                           isData=True,
                           pfCandColl="cleanMuonsPFCandidates",
                           recoMetFromPFCs=True,
                           postfix="MuClean"
                           )

process.mucorMET = cms.Sequence(                     
    process.badGlobalMuonTaggerMAOD *
    process.cloneGlobalMuonTaggerMAOD *
    #process.badMuons * # If you are using cleaning mode "all", uncomment this line
    process.cleanMuonsPFCandidates *
    process.fullPatMetSequenceMuClean
    )

# Now you are creating the e/g corrected MET on top of the bad muon corrected MET (on re-miniaod)
from PhysicsTools.PatUtils.tools.corMETFromMuonAndEG import corMETFromMuonAndEG
corMETFromMuonAndEG(process,
                    pfCandCollection="", #not needed                                                                                                                                                                                                                                                                                        
                    electronCollection="slimmedElectronsBeforeGSFix",
                    photonCollection="slimmedPhotonsBeforeGSFix",
                    corElectronCollection="slimmedElectrons",
                    corPhotonCollection="slimmedPhotons",
                    allMETEGCorrected=True,
                    muCorrection=False,
                    eGCorrection=True,
                    runOnMiniAOD=True,
                    postfix="MuEGClean"
                    )

process.slimmedMETsMuEGClean = process.slimmedMETs.clone()
process.slimmedMETsMuEGClean.src = cms.InputTag("patPFMetT1MuEGClean")
process.slimmedMETsMuEGClean.rawVariation =  cms.InputTag("patPFMetRawMuEGClean")
process.slimmedMETsMuEGClean.t1Uncertainties = cms.InputTag("patPFMetT1%sMuEGClean")

del process.slimmedMETsMuEGClean.caloMET

# If you are running in the scheduled mode:
process.egcorrMET = cms.Sequence(
    process.cleanedPhotonsMuEGClean+process.cleanedCorPhotonsMuEGClean+
    process.matchedPhotonsMuEGClean + process.matchedElectronsMuEGClean +
    process.corMETPhotonMuEGClean+process.corMETElectronMuEGClean+
    process.patPFMetT1MuEGClean+process.patPFMetRawMuEGClean+
    process.patPFMetT1SmearMuEGClean+process.patPFMetT1TxyMuEGClean+
    process.patPFMetTxyMuEGClean+process.patPFMetT1JetEnUpMuEGClean+
    process.patPFMetT1JetResUpMuEGClean+process.patPFMetT1SmearJetResUpMuEGClean+
    process.patPFMetT1ElectronEnUpMuEGClean+process.patPFMetT1PhotonEnUpMuEGClean+
    process.patPFMetT1MuonEnUpMuEGClean+process.patPFMetT1TauEnUpMuEGClean+
    process.patPFMetT1UnclusteredEnUpMuEGClean+process.patPFMetT1JetEnDownMuEGClean+
    process.patPFMetT1JetResDownMuEGClean+process.patPFMetT1SmearJetResDownMuEGClean+
    process.patPFMetT1ElectronEnDownMuEGClean+process.patPFMetT1PhotonEnDownMuEGClean+
    process.patPFMetT1MuonEnDownMuEGClean+process.patPFMetT1TauEnDownMuEGClean+
    process.patPFMetT1UnclusteredEnDownMuEGClean+process.slimmedMETsMuEGClean)

####
# The N-tupliser/cutFlow
####

process.load("NTupliser.NTupliser.MakeTopologyNtuple_miniAOD_cfi")
process.makeTopologyNtupleMiniAOD.flavorHistoryTag=cms.bool(False) # change to false at your convenience
process.makeTopologyNtupleMiniAOD.runMCInfo=cms.bool(False) # prevent checking gen info
process.makeTopologyNtupleMiniAOD.runPUReWeight=cms.bool(False) #Run the reweighting for MC. I think I'm doing this right, but I might check anyway.
process.makeTopologyNtupleMiniAOD.triggerToken = cms.InputTag("TriggerResults","","HLT") # or HLT, depends on file   

#settings to apply tight selection:
process.makeTopologyNtupleMiniAOD.minJetPt=cms.double(0.0)
process.makeTopologyNtupleMiniAOD.maxJetEta=cms.double(5.5)
process.makeTopologyNtupleMiniAOD.bDiscCut=cms.double(-1.0)
process.makeTopologyNtupleMiniAOD.minElePt=cms.double(9.0)
process.makeTopologyNtupleMiniAOD.maxEleEta=cms.double(2.7)
process.makeTopologyNtupleMiniAOD.eleRelIso=cms.double(0.50)
process.makeTopologyNtupleMiniAOD.minMuonPt=cms.double(9.0)
process.makeTopologyNtupleMiniAOD.maxMuonEta=cms.double(2.8)
process.makeTopologyNtupleMiniAOD.muonRelIso=cms.double(0.50)
process.makeTopologyNtupleMiniAOD.maxDistForPhotonRej=cms.double(0.04)
process.makeTopologyNtupleMiniAOD.maxDcotForPhotonRej=cms.double(0.03)
process.makeTopologyNtupleMiniAOD.fillAll=cms.bool(True)
#process.makeTopologyNtupleMiniAOD.btagParameterizationList = cms.vstring()
#process.makeTopologyNtupleMiniAOD.btagParameterizationMode = cms.vstring()

#Don't actually do cuts
process.makeTopologyNtupleMiniAOD.doCuts=cms.bool(True) # if set to false will skip ALL cuts. Z veto still applies electron cuts.
process.makeTopologyNtupleMiniAOD.minLeptons = cms.int32(2)

#Make the inputs for the n-tupliser right.
process.makeTopologyNtupleMiniAOD.electronPFToken = cms.InputTag("selectedElectrons")
process.makeTopologyNtupleMiniAOD.tauPFTag = cms.InputTag("slimmedTaus")
process.makeTopologyNtupleMiniAOD.muonPFToken = cms.InputTag("slimmedMuons")
process.makeTopologyNtupleMiniAOD.jetPFToken = cms.InputTag("updatedPatJetsUpdatedJEC") # Originally slimmedJets, patJetsReapplyJEC is the jet collection with reapplied JECs
process.makeTopologyNtupleMiniAOD.metPFToken = cms.InputTag("slimmedMETsMuEGClean","","customPAT")
process.makeTopologyNtupleMiniAOD.rhoToken = cms.InputTag("fixedGridRhoFastjetAll")
process.makeTopologyNtupleMiniAOD.conversionsToken = cms.InputTag("reducedEgamma", "reducedConversions")

## Source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring()
)

## Maximal Number of Events
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source.fileNames = [
#	'root://xrootd.unl.edu//store/data/Run2016B/DoubleEG/MINIAOD/PromptReco-v2/000/273/158/00000/0227DB1C-E719-E611-872C-02163E0141F9.root',
#	'root://xrootd.unl.edu//store/data/Run2016B/DoubleMuon/MINIAOD/PromptReco-v2/000/273/158/00000/2C8772DF-F319-E611-AEC1-02163E014122.root',
#	'root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleEG/MINIAOD/23Sep2016-v1/100000/206CD6B5-AE87-E611-8B2B-0CC47A4D769A.root',
#	'root://cms-xrd-global.cern.ch//store/data/Run2016D/DoubleEG/MINIAOD/03Feb2017-v1/100000/002CE21C-0BEB-E611-8597-001E67E6F8E6.root',
#	'file:/scratch/eepgadm/data/DoubleEG/Run2016D/002CE21C-0BEB-E611-8597-001E67E6F8E6.root',
	'file:/scratch/eepgadm/data/SingleElectron/Run2016D/00393BA2-6AEB-E611-8417-0CC47A4D7692.root',
	]

from PhysicsTools.PatAlgos.patEventContent_cff import *
from PhysicsTools.PatAlgos.patEventContent_cff import patEventContentNoCleaning

process.out = cms.OutputModule("PoolOutputModule",
                               fileName = cms.untracked.string('patTuple.root'),
                               ## save only events passing the full path
                               #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
                               ## save PAT output; you need a '*' to unpack the list of commands
                               outputCommands = cms.untracked.vstring('drop *', *patEventContentNoCleaning )
                               )

process.out.outputCommands += patEventContent
process.out.outputCommands += patTriggerEventContent
process.out.outputCommands += patExtraAodEventContent
process.out.outputCommands += cms.untracked.vstring('keep *_flavorHistoryFilter_*_*','keep *_TriggerResults_*_*','keep *_selectedPat*_*_*', 'keep *_*goodOfflinePrimaryVertices*_*_*','keep double_*_rho_*', 'keep patMuons_*_*_*', 'keep *MET*_*_*_*', 'keep *_*MET*_*_*')


#PAT output and various other outpath stuff which is a bit dumb coz I'm probably not even gonna use the outpath. Nevermind.
process.out.fileName = cms.untracked.string('Data_out.root')

#NTuple output
process.TFileService = cms.Service("TFileService", fileName = cms.string('Data_test.root') )
process.options.wantSummary = False
process.out.SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p'))

#Removing pat output (coz we really don't need it now)
#del process.out

process.p = cms.Path(
    process.processedElectrons *
    process.jetCorrection *
    process.mucorMET *
    process.fullPatMetSequence *
    process.egcorrMET *
    process.makeTopologyNtupleMiniAOD
    )

process.schedule = cms.Schedule( process.p )

process.outpath = cms.EndPath( process.out )

