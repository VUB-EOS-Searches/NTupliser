from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'RAW2DIGI_RECO_EI_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_2017_200910'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_RAW2DIGI_RECO_EI_2017.py'
config.JobType.maxMemoryMB = 9500
config.JobType.numCores = 8
config.JobType.maxJobRuntimeMin = 1500

config.Data.inputDataset = '/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_2017_200908/almorton-CRAB3_DIGI2RAW_HLT_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_2017_200909-e97ff4a481181e605c5fa03c6b65a2f9/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.outLFNDirBase = '/store/user/almorton/MC/RAW2DIGI_RECO_EI/'

config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_RAW2DIGI_RECO_EI_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_2017_200910'

config.Site.storageSite = 'T2_BE_IIHE' #T2_UK_London_IC, T2_UK_London_Brunel, T2_BE_IIHE
#config.Site.blacklist = ['T2_UK_London_Brunel']
