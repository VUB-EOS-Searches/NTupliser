from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_2017_200907'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'ggH/MS1_ctauS1/NLO_ggHToSS_MH125_SmuonHadronFiltered_2017.py'
config.JobType.maxMemoryMB = 14000
config.JobType.numCores = 8
config.JobType.maxJobRuntimeMin = 1500

config.Data.outputPrimaryDataset = 'NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_2017_200907'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
NJOBS = 100  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/almorton/MC/GEN-SIM/'

config.Data.publication = False
config.Data.outputDatasetTag = "CRAB3_GEN-SIM_NLO_HZJ_MH125_MS1_ctauS1_2017_200907"

config.Site.storageSite = 'T2_BE_IIHE' #T2_UK_London_IC, T2_UK_London_Brunel, T2_BE_IIHE
#config.Site.blacklist = ['T2_UK_London_Brunel']

