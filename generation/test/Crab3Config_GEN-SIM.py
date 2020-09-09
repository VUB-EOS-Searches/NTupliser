from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1000_2017_200908'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'ggH/MS2_ctauS1000/NLO_ggHToSS_MH125_SmuonHadronFiltered_2017.py'
config.JobType.maxMemoryMB = 9500
config.JobType.numCores = 8
config.JobType.maxJobRuntimeMin = 1500

config.Data.outputPrimaryDataset = 'NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1000_2017_200908'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
NJOBS = 100  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/almorton/MC/GEN-SIM/'

config.Data.publication = True
config.Data.outputDatasetTag = "CRAB3_GEN-SIM_NLO_HZJ_MH125_MS2_ctauS1000_2017_200908"

config.Site.storageSite = 'T2_BE_IIHE' #T2_UK_London_IC, T2_UK_London_Brunel, T2_BE_IIHE
#config.Site.blacklist = ['T2_UK_London_Brunel']

