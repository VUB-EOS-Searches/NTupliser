from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1_2017_200911'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_PAT_miniAOD_2017.py'
config.JobType.maxMemoryMB = 9500
config.JobType.numCores = 8
config.JobType.maxJobRuntimeMin = 1500

config.Data.inputDataset = '/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1_2017_200908/almorton-CRAB3_RAW2DIGI_RECO_EI_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1_2017_200910-f1be97bf1746b23f5bdc2a8e8b347647/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/almorton/MC/PAT_miniAOD/'

config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1_2017_200911'

config.Site.storageSite = 'T2_BE_IIHE' #T2_UK_London_IC, T2_UK_London_Brunel, T2_BE_IIHE
#config.Site.blacklist = ['T2_UK_London_Brunel']
