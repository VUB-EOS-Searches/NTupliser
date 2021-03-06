from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'DIGI2RAW_HLT_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS100_2017_ext1_200915'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step1_DIGIPREMIX_S2_DATAMIX_L1_DIGI2RAW_HLT_2017.py'
config.JobType.maxMemoryMB = 9500
config.JobType.numCores = 8
config.JobType.maxJobRuntimeMin = 1500

config.Data.inputDataset = '/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS100_2017_ext1_200914/almorton-CRAB3_GEN-SIM_NLO_HZJ_MH125_MS1_ctauS100_2017_ext1_200914-259dac6953bd821054f31195fa9b813c/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/almorton/MC/DIGI2RAW_HLT/'

config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_DIGI2RAW_HLT_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS100_2017_ext1_200915'

config.Site.storageSite = 'T2_BE_IIHE' #T2_UK_London_IC, T2_UK_London_Brunel, T2_BE_IIHE
#config.Site.blacklist = ['T2_UK_London_Brunel']
