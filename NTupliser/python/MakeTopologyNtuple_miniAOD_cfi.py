import FWCore.ParameterSet.Config as cms

makeTopologyNtupleMiniAOD = cms.EDAnalyzer('MakeTopologyNtupleMiniAOD',
					   is2016rereco = cms.bool(False),
                                           # "Calo"
                                           packedCandToken = cms.InputTag("packedPFCandidates"),
                                           electronTag     = cms.InputTag("slimmedElectrons"),
                                           tauTag          = cms.InputTag("slimmedTaus"),
                                           muonTag         = cms.InputTag("slimmedMuons"),
                                           jetLabel        = cms.InputTag("slimmedJets"),
                                           genJetToken     = cms.InputTag("slimmedGenJets"),
                                           photonTag       = cms.InputTag("slimmedPhotons"),
                                           ootPhotonTag    = cms.InputTag("slimmedOOTPhotons"),
                                           metTag          = cms.InputTag("patMETs"),
                                           # PF
					   beamSpotToken    = cms.InputTag("offlineBeamSpot"),
                                           isolatedTrackToken = cms.InputTag("isolatedTracks"),
                                           conversionsToken = cms.InputTag("reducedEgamma", "reducedConversions"),
                                           electronPFToken  = cms.InputTag("slimmedElectrons"),
                                           tauPFTag         = cms.InputTag("slimmedTaus"),
                                           muonPFToken      = cms.InputTag("slimmedMuons"),
                                           jetPFToken       = cms.InputTag("slimmedJets"),
                                           jetPFRecoTag     = cms.InputTag("slimmedJets"),
                                           photonPFToken    = cms.InputTag("slimmedPhotons"),
                                           ootPhotonPFToken = cms.InputTag("slimmedOOTPhotons"),
                                           metPFToken       = cms.InputTag("slimmedMETs"),
                                           # JPT
                                           #jetJPTTag       = cms.InputTag("selectedPatJetsAK4JPT"),
                                           #metJPTTag       = cms.InputTag("patMETsTC"),

                                           primaryVertexToken    = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                           secondaryVertexToken  = cms.InputTag("slimmedSecondaryVertices"),
                                           kshortToken           = cms.InputTag("slimmedKshortVertices"),
                                           lambdaToken           = cms.InputTag("slimmedLambdaVertices"),

                                           rhoToken           = cms.InputTag("fixedGridRhoFastjetAll"),
					   effAreasConfigFile =cms.FileInPath("RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt"),
					   pileupToken	      = cms.InputTag("slimmedAddPileupInfo"),
                                           triggerToken  = cms.InputTag("TriggerResults","","HLT"),
                                           metFilterToken  = cms.InputTag("TriggerResults", "", "PAT"),
                                           fakeTriggerList = cms.vstring(), # empty. You can add fake triggers that are run on the fly to this list. No check on the process name is made so when duplicates are available only the latest one is added.
					   isLHEflag = cms.bool(False),
					   externalLHEToken = cms.InputTag("externalLHEProducer"), # "externalLHEProducer", "source" for THQ 

					   pdfIdStart = cms.int32(2001),
					   pdfIdEnd = cms.int32(2102),
					   hasAlphaWeightFlag = cms.bool(True),
					   alphaIdStart = cms.int32(2101),
					   alphaIdEnd = cms.int32(2102),

					   pdfInfoFixingToken = cms.InputTag("pdfInfoFixing"),
					   generatorToken = cms.InputTag("generator"),
                                           minLeptons = cms.int32(0), ## currently deprecated

                                           hasGeneralTracks   = cms.bool(False),
                                           generalTracksToken = cms.InputTag("generalTracks"),
                                           
                                           bTagList = cms.vstring(
        'pfCombinedInclusiveSecondaryVertexV2BJetTags',        #CombinedSecondaryVertex v2
        'pfDeepCSVJetTags:probudsg',                           #Deep Flavour CSV
        'pfDeepCSVJetTags:probb',                              #Deep Flavour CSV
        'pfDeepCSVJetTags:probc',                              #Deep Flavour CSV
        'pfDeepCSVJetTags:probbb',                             #Deep Flavour CSV
        'pfDeepCSVJetTags:probcc',                             #Deep Flavour CSV
        'pfDeepCMVAJetTags:probudsg',                          #Deep Flavour CMVA
        'pfDeepCMVAJetTags:probb',                             #Deep Flavour CMVA
        'pfDeepCMVAJetTags:probc',                             #Deep Flavour CMVA
        'pfDeepCMVAJetTags:probbb',                            #Deep Flavour CMVA
        'pfDeepCMVAJetTags:probcc',                            #Deep Flavour CMVA
        'pfCombinedCvsLJetTags',                               #Charm vs Light jets
        'pfCombinedCvsBJetTags',                               #Charm vs B jets
        ),
                                           triggerList = cms.vstring(*[
	#Updated Triggers for 2017
#	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v1',
#	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v2',
#	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v3',
#	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v4',
#	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v5',
#	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v6',
#	'HLT_Ele32_WPTight_Gsf_L1DoubleEG_v7',
#	'HLT_Ele35_WPTight_Gsf_v1',
#	'HLT_Ele35_WPTight_Gsf_v2',
#	'HLT_Ele35_WPTight_Gsf_v3',
#	'HLT_Ele35_WPTight_Gsf_v4',
#	'HLT_Ele35_WPTight_Gsf_v5',
#	'HLT_Ele35_WPTight_Gsf_v6',
#	'HLT_Ele35_WPTight_Gsf_v7',

	'HLT_IsoMu27_v8', ## All Runs
	'HLT_IsoMu27_v9', ## All Runs
	'HLT_IsoMu27_v10', ## All Runs
	'HLT_IsoMu27_v11', ## All Runs
	'HLT_IsoMu27_v12', ## All Runs
	'HLT_IsoMu27_v13', ## All Runs
	'HLT_IsoMu27_v14', ## All Runs

#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v10', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v11', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v12', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v13', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v14', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v15', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v16', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v17', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v10', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v11', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v12', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v13', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v14', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v15', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v16', ## All Runs
#	'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v17', ## All Runs

	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v8', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v9', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v10', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v11', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v12', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v13', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v14', ## Runs A-B
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v1', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v2', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v3', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v4', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v7', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v8', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v1', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v2', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v3', ## Runs C onwards
	'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v4', ## Runs C onwards

	## All DZ and Mu23Ele12 non-DZ are unprescaled for All Runs
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v1',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v2',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v3',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v4',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v5',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v5',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v6',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v8',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v9',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v10',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v11',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v12',
#	'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v13',
#	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v5',
#	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v6',
#	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v8',
#	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v9',
#	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v10',
#	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v11',
#	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v12',
#	'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v13',
#	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v4',
#	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v6',
#	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v7',
#	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v8',
#	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v9',
#	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v10',
#	'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v11',

        ## Potential H->SS triggers

### displaced muons andLevel-2/muon chambers only triggers
        'HLT_DoubleL2Mu50_v2',#2017+2018
        'HLT_DoubleMu43NoFiltersNoVtx_v3', #2017
        'HLT_DoubleMu48NoFiltersNoVtx_v3', #2017

#        'HLT_DoubleL2Mu23NoVtx_2Cha_v2', #2018 only
#        'HLT_DoubleL2Mu25NoVtx_2Cha_Eta2p4_v2', #2018 only
#        'HLT_DoubleL2Mu25NoVtx_2Cha_v2', #2018 only
#        'HLT_DoubleL2Mu30NoVtx_2Cha_Eta2p4_v2', #2018 only
#        'HLT_DoubleMu33NoFiltersNoVtxDisplaced_v1', #2018 only
#        'HLT_DoubleMu40NoFiltersNoVtxDisplaced_v1', #2018 only
#        'HLT_DoubleMu43NoFiltersNoVtx_v4', #2018 only
#        'HLT_DoubleMu48NoFiltersNoVtx_v4', #2018 only

### photon and displaced jet triggers

#        'HLT_DoublePhoton33_CaloIdL_v5',
#        'HLT_DoublePhoton70_v5',
#        'HLT_DoublePhoton85_v13',
#        'HLT_TriplePhoton_20_20_20_CaloIdLV2_v2',
#        'HLT_TriplePhoton_20_20_20_CaloIdLV2_R9IdVL_v2',
#        'HLT_TriplePhoton_30_30_10_CaloIdLV2_v3',
#        'HLT_TriplePhoton_30_30_10_CaloIdLV2_R9IdVL_v3',
#        'HLT_TriplePhoton_35_35_5_CaloIdLV2_R9IdVL_v3',
#        'HLT_Photon25_v2',
#        'HLT_Photon33_v4',
#        'HLT_Photon50_v12',
#        'HLT_Photon75_v12',
#        'HLT_Photon90_v12',
#        'HLT_Photon120_v12',
#        'HLT_Photon150_v5',
#        'HLT_Photon175_v13',
#        'HLT_Photon200_v12',
#        'HLT_Photon50_R9Id90_HE10_IsoM_v13',
#        'HLT_Photon75_R9Id90_HE10_IsoM_v13',
#        'HLT_Photon90_R9Id90_HE10_IsoM_v13',
#        'HLT_Photon120_R9Id90_HE10_IsoM_v13',
#        'HLT_Photon165_R9Id90_HE10_IsoM_v14',
#        'HLT_Photon90_CaloIdL_PFHT700_v12',
#        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v12',
#        'HLT_Diphoton30_22_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass95_v12',
#        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_PixelVeto_Mass55_v13',
#        'HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_NoPixelVeto_Mass55_v12',
#        'HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_NoPixelVeto_Mass55_v12',
#        'HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_PixelVeto_Mass55_v13',

        'HLT_HT430_DisplacedDijet40_DisplacedTrack_v10',
        'HLT_HT430_DisplacedDijet60_DisplacedTrack_v10',
        'HLT_HT430_DisplacedDijet80_DisplacedTrack_v10',
        'HLT_HT400_DisplacedDijet40_DisplacedTrack_v10',
        'HLT_HT650_DisplacedDijet60_Inclusive_v10',
        'HLT_HT550_DisplacedDijet80_Inclusive_v8',
        'HLT_HT550_DisplacedDijet60_Inclusive_v10',
        'HLT_HT650_DisplacedDijet80_Inclusive_v11',
        'HLT_HT750_DisplacedDijet80_Inclusive_v11',
#        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_v4',
#        'HLT_Photon60_R9Id90_CaloIdL_IsoL_DisplacedIdL_PFHT350MinPFJet15_v7',
#        'HLT_Photon20_HoverELoose_v9',
#        'HLT_Photon30_HoverELoose_v9',
#        'HLT_Photon40_HoverELoose_v9',
#        'HLT_Photon50_HoverELoose_v9',
#        'HLT_Photon60_HoverELoose_v9',

	#Updated MET Triggers for 2017
	# Needs doing ...
        # 3.0
#        "HLT_MET105_IsoTrk50_v1",
#        "HLT_MET105_IsoTrk50_v3",
#        "HLT_MET105_IsoTrk50_v4",
#        "HLT_MET105_IsoTrk50_v5",
#        "HLT_MET105_IsoTrk50_v6",
#        "HLT_MET105_IsoTrk50_v7",
#        "HLT_MET105_IsoTrk50_v8",
#        "HLT_MET120_IsoTrk50_v1",
#        "HLT_MET120_IsoTrk50_v3",
#        "HLT_MET120_IsoTrk50_v4",
#        "HLT_MET120_IsoTrk50_v5",
#        "HLT_MET120_IsoTrk50_v6",
#        "HLT_MET120_IsoTrk50_v7",
#        "HLT_MET120_IsoTrk50_v8",

##        "HLT_HT430_DisplacedDijet40_DisplacedTrack_v10", ## in above list
        "HLT_HT430_DisplacedDijet40_DisplacedTrack_v11",
        "HLT_HT430_DisplacedDijet40_DisplacedTrack_v5",
        "HLT_HT430_DisplacedDijet40_DisplacedTrack_v6",
        "HLT_HT430_DisplacedDijet40_DisplacedTrack_v8",
        "HLT_HT430_DisplacedDijet40_DisplacedTrack_v9",
##        "HLT_HT430_DisplacedDijet60_DisplacedTrack_v10", ## in above list
        "HLT_HT430_DisplacedDijet60_DisplacedTrack_v11",
        "HLT_HT430_DisplacedDijet60_DisplacedTrack_v5",
        "HLT_HT430_DisplacedDijet60_DisplacedTrack_v6",
        "HLT_HT430_DisplacedDijet60_DisplacedTrack_v8",
        "HLT_HT430_DisplacedDijet60_DisplacedTrack_v9",
##        "HLT_HT430_DisplacedDijet80_DisplacedTrack_v10", ## in above list
        "HLT_HT430_DisplacedDijet80_DisplacedTrack_v11",
        "HLT_HT430_DisplacedDijet80_DisplacedTrack_v5",
        "HLT_HT430_DisplacedDijet80_DisplacedTrack_v6",
        "HLT_HT430_DisplacedDijet80_DisplacedTrack_v8",
        "HLT_HT430_DisplacedDijet80_DisplacedTrack_v9",
##        "HLT_HT650_DisplacedDijet60_Inclusive_v10", ## in above list
        "HLT_HT650_DisplacedDijet60_Inclusive_v11",
        "HLT_HT650_DisplacedDijet60_Inclusive_v5",
        "HLT_HT650_DisplacedDijet60_Inclusive_v6",
        "HLT_HT650_DisplacedDijet60_Inclusive_v8",
        "HLT_HT650_DisplacedDijet60_Inclusive_v9",
        "HLT_HT650_DisplacedDijet80_Inclusive_v10",
##        "HLT_HT650_DisplacedDijet80_Inclusive_v11", ## in above list
        "HLT_HT650_DisplacedDijet80_Inclusive_v12",
        "HLT_HT650_DisplacedDijet80_Inclusive_v6",
        "HLT_HT650_DisplacedDijet80_Inclusive_v7",
        "HLT_HT650_DisplacedDijet80_Inclusive_v9",
        "HLT_HT750_DisplacedDijet80_Inclusive_v10",
##        "HLT_HT750_DisplacedDijet80_Inclusive_v11", ## in above list
        "HLT_HT750_DisplacedDijet80_Inclusive_v12",
        "HLT_HT750_DisplacedDijet80_Inclusive_v6",
        "HLT_HT750_DisplacedDijet80_Inclusive_v7",
        "HLT_HT750_DisplacedDijet80_Inclusive_v9",

#        "HLT_PFMET120_PFMHT120_IDTight_HFCleaned_v1",
#        "HLT_PFMET120_PFMHT120_IDTight_HFCleaned_v2",
#        "HLT_PFMET120_PFMHT120_IDTight_L1ETMnoHF_v10",
#        "HLT_PFMET120_PFMHT120_IDTight_PFHT60_HFCleaned_v1",
#        "HLT_PFMET120_PFMHT120_IDTight_PFHT60_HFCleaned_v2",
#        "HLT_PFMET120_PFMHT120_IDTight_PFHT60_v2",
#        "HLT_PFMET120_PFMHT120_IDTight_PFHT60_v3",
#        "HLT_PFMET120_PFMHT120_IDTight_PFHT60_v4",
#        "HLT_PFMET120_PFMHT120_IDTight_PFHT60_v5",
#        "HLT_PFMET120_PFMHT120_IDTight_PFHT60_v6",
#        "HLT_PFMET120_PFMHT120_IDTight_PFHT60_v7",
#        "HLT_PFMET120_PFMHT120_IDTight_v11",
#        "HLT_PFMET120_PFMHT120_IDTight_v13",
#        "HLT_PFMET120_PFMHT120_IDTight_v14",
#        "HLT_PFMET120_PFMHT120_IDTight_v15",
#        "HLT_PFMET120_PFMHT120_IDTight_v16",
#        "HLT_PFMET120_PFMHT120_IDTight_v9",
#        "HLT_PFMET130_PFMHT130_IDTight_v11",
#        "HLT_PFMET130_PFMHT130_IDTight_v13",
#        "HLT_PFMET130_PFMHT130_IDTight_v14",
#        "HLT_PFMET130_PFMHT130_IDTight_v15",
#        "HLT_PFMET130_PFMHT130_IDTight_v16",
#        "HLT_PFMET130_PFMHT130_IDTight_v9",
#        "HLT_PFMET140_PFMHT140_IDTight_v11",
#        "HLT_PFMET140_PFMHT140_IDTight_v13",
#        "HLT_PFMET140_PFMHT140_IDTight_v14",
#        "HLT_PFMET140_PFMHT140_IDTight_v15",
#        "HLT_PFMET140_PFMHT140_IDTight_v16",
#        "HLT_PFMET140_PFMHT140_IDTight_v17",
#        "HLT_PFMET140_PFMHT140_IDTight_v18",
#        "HLT_PFMET140_PFMHT140_IDTight_v9",
#        "HLT_PFMET200_HBHE_BeamHaloCleaned_v5",
#        "HLT_PFMET200_HBHE_BeamHaloCleaned_v6",
#        "HLT_PFMET200_HBHE_BeamHaloCleaned_v7",
#        "HLT_PFMET250_HBHECleaned_v2",
#        "HLT_PFMET250_HBHECleaned_v3",
#        "HLT_PFMET250_HBHECleaned_v4",
#        "HLT_PFMET250_HBHECleaned_v5",
#        "HLT_PFMET250_HBHECleaned_v6",
#        "HLT_PFMET250_HBHECleaned_v7",
#        "HLT_PFMET300_HBHECleaned_v2",
#        "HLT_PFMET300_HBHECleaned_v3",
#        "HLT_PFMET300_HBHECleaned_v4",
#        "HLT_PFMET300_HBHECleaned_v5",
#        "HLT_PFMET300_HBHECleaned_v6",
#        "HLT_PFMET300_HBHECleaned_v7",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_HFCleaned_v1",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_HFCleaned_v2",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_L1ETMnoHF_v10",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v2",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v3",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v4",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v5",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v6",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_PFHT60_v7",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v11",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v13",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v14",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v15",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v16",
#        "HLT_PFMETNoMu120_PFMHTNoMu120_IDTight_v9",
#        "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v10",
#        "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v12",
#        "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v13",
#        "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v14",
#        "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v15",
#        "HLT_PFMETNoMu130_PFMHTNoMu130_IDTight_v9",
#        "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v10",
#        "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v12",
#        "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v13",
#        "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v14",
#        "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v15",
#        "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v16",
#        "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v17",
#        "HLT_PFMETNoMu140_PFMHTNoMu140_IDTight_v9",

#        "HLT_PFHT1050_v11",
#        "HLT_PFHT1050_v12",
#        "HLT_PFHT1050_v13",
#        "HLT_PFHT1050_v14",
#        "HLT_PFHT1050_v15",
#        "HLT_PFHT1050_v16",
#        "HLT_PFHT1050_v7",
#        "HLT_PFHT1050_v9",
#        "HLT_PFHT180_v7",
#        "HLT_PFHT500_PFMET100_PFMHT100_IDTight_v1",
#        "HLT_PFHT500_PFMET100_PFMHT100_IDTight_v10",
#        "HLT_PFHT500_PFMET100_PFMHT100_IDTight_v3",
#        "HLT_PFHT500_PFMET100_PFMHT100_IDTight_v5",
#        "HLT_PFHT500_PFMET100_PFMHT100_IDTight_v6",
#        "HLT_PFHT500_PFMET100_PFMHT100_IDTight_v7",
#        "HLT_PFHT500_PFMET100_PFMHT100_IDTight_v8",
#        "HLT_PFHT500_PFMET100_PFMHT100_IDTight_v9",
#        "HLT_PFHT500_PFMET110_PFMHT110_IDTight_v1",
#        "HLT_PFHT500_PFMET110_PFMHT110_IDTight_v10",
#        "HLT_PFHT500_PFMET110_PFMHT110_IDTight_v3",
#        "HLT_PFHT500_PFMET110_PFMHT110_IDTight_v5",
#        "HLT_PFHT500_PFMET110_PFMHT110_IDTight_v6",
#        "HLT_PFHT500_PFMET110_PFMHT110_IDTight_v7",
#        "HLT_PFHT500_PFMET110_PFMHT110_IDTight_v8",
#        "HLT_PFHT500_PFMET110_PFMHT110_IDTight_v9",
#        "HLT_PFHT700_PFMET85_PFMHT85_IDTight_v1",
#        "HLT_PFHT700_PFMET85_PFMHT85_IDTight_v10",
#        "HLT_PFHT700_PFMET85_PFMHT85_IDTight_v3",
#        "HLT_PFHT700_PFMET85_PFMHT85_IDTight_v5",
#        "HLT_PFHT700_PFMET85_PFMHT85_IDTight_v6",
#        "HLT_PFHT700_PFMET85_PFMHT85_IDTight_v7",
#        "HLT_PFHT700_PFMET85_PFMHT85_IDTight_v8",
#        "HLT_PFHT700_PFMET85_PFMHT85_IDTight_v9",
#        "HLT_PFHT700_PFMET95_PFMHT95_IDTight_v1",
#        "HLT_PFHT700_PFMET95_PFMHT95_IDTight_v10",
#        "HLT_PFHT700_PFMET95_PFMHT95_IDTight_v3",
#        "HLT_PFHT700_PFMET95_PFMHT95_IDTight_v5",
#        "HLT_PFHT700_PFMET95_PFMHT95_IDTight_v6",
#        "HLT_PFHT700_PFMET95_PFMHT95_IDTight_v7",
#        "HLT_PFHT700_PFMET95_PFMHT95_IDTight_v8",
#        "HLT_PFHT700_PFMET95_PFMHT95_IDTight_v9",
#        "HLT_PFHT800_PFMET75_PFMHT75_IDTight_v1",
#        "HLT_PFHT800_PFMET75_PFMHT75_IDTight_v10",
#        "HLT_PFHT800_PFMET75_PFMHT75_IDTight_v3",
#        "HLT_PFHT800_PFMET75_PFMHT75_IDTight_v5",
#        "HLT_PFHT800_PFMET75_PFMHT75_IDTight_v6",
#        "HLT_PFHT800_PFMET75_PFMHT75_IDTight_v7",
#        "HLT_PFHT800_PFMET75_PFMHT75_IDTight_v8",
#        "HLT_PFHT800_PFMET75_PFMHT75_IDTight_v9",
#        "HLT_PFHT800_PFMET85_PFMHT85_IDTight_v1",
#        "HLT_PFHT800_PFMET85_PFMHT85_IDTight_v10",
#        "HLT_PFHT800_PFMET85_PFMHT85_IDTight_v3",
#        "HLT_PFHT800_PFMET85_PFMHT85_IDTight_v5",
#        "HLT_PFHT800_PFMET85_PFMHT85_IDTight_v6",
#        "HLT_PFHT800_PFMET85_PFMHT85_IDTight_v7",
#        "HLT_PFHT800_PFMET85_PFMHT85_IDTight_v8",
#        "HLT_PFHT800_PFMET85_PFMHT85_IDTight_v9",
        ]),
                                           metFilterList = cms.vstring(		
	#MET Filters		
	'Flag_goodVertices',
	'Flag_globalTightHalo2016Filter',
	'Flag_HBHENoiseFilter',
	'Flag_HBHENoiseIsoFilter',
	'Flag_EcalDeadCellTriggerPrimitiveFilter',
	'Flag_BadPFMuonFilter',
	'Flag_BadChargedCandidateFilter',
	'Flag_eeBadScFilter',
	'Flag_ecalBadCalibFilter',
	),	
                                           l1TriggerTag = cms.InputTag("gtDigis"),                                    
                                           checkTriggers = cms.bool(True),
                                           genParticles = cms.InputTag("prunedGenParticles"),
					   genSimParticles = cms.InputTag("prunedGenParticles"),
                                           runMCInfo = cms.bool(True), # if set to true will skip MCInfo section
                                           runPUReWeight = cms.bool(False), #Run pile-up reweighting. Don't do if this is data I guess.
                                           doCuts = cms.bool(False), # if set to false will skip ALL cuts. Z veto still applies electron cuts.
                                           # default preselection settings! see https://twiki.cern.ch/twiki/bin/view/CMS/VplusJets for inspiration

                                           #Some jet cuts.
                                           minJetPt = cms.double(0.), #min jet pT in GeV/c
                                           maxJetEta = cms.double(5.5), # jet |eta|

                                           runSwissCross = cms.bool(True),
                                           runPDFUncertainties = cms.bool(False),
                                           useResidualJEC = cms.bool(False),
                                           minElePt = cms.double(9.0), #  electron pT in GeV
                                           maxEleEta = cms.double(2.70), #  electron |eta|
					   eleRelIso = cms.double(0.50), # electron combined rel track iso with rho corrections
                                           # muon identification
                                           minMuonPt = cms.double(6.0),
                                           maxMuonEta = cms.double(2.80),
                                           muoRelIso = cms.double(0.50), # muon combined track isolation with delta beta corrections
                                           metCut = cms.double(0.0),
                                           # photon rejection:
                                           dREleGeneralTrackMatchForPhotonRej=cms.double(0.3),
                                           magneticFieldForPhotonRej=cms.double(3.8),
                                           correctFactorForPhotonRej=cms.double(-0.003),
                                           maxDistForPhotonRej=cms.double(0),
                                           maxDcotForPhotonRej=cms.double(0),
                                           isMCatNLO=cms.bool(False),
                                           isttBar = cms.bool(True),# This affects reweighting things. If set to false, then has a weight of 1.
                                           ttGenEvent = cms.InputTag("null")
                                           )# end of MakeTopologyNtupleMiniAOD
