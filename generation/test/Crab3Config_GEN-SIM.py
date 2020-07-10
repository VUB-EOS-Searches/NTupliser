from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'NLO_HZJ_MH125_MS1_ctauS10_2017_200710'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'NLO_HZJ_HToSTodddd_MH125_Vleptonic_2017.py'
config.JobType.maxMemoryMB = 14000
config.JobType.numCores = 8
config.JobType.maxJobRuntimeMin = 375

config.Data.outputPrimaryDataset = 'NLO_HZJ_MH125_MS1_ctauS10_2017_200710'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 50
NJOBS = 100  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/almorton/'

config.Data.publication = False
config.Data.outputDatasetTag = "CRAB3_GEN-SIM_NLO_HZJ_MH125_MS1_ctauS10_2017_200710"

config.Site.storageSite = 'T2_UK_London_IC' #T2_UK_London_IC
#config.Site.blacklist = ['T2_UK_London_Brunel']

