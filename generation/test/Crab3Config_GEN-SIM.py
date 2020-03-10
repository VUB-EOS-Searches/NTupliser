from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'NLO_ggHToSSTobbbb_MH125_MS_2017_200210'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'NLO_ggHToSSTobbbb_MH125_MS2_2017.py'
config.JobType.maxMemoryMB = 2500

config.Data.outputPrimaryDataset = 'NLO_ggHToSSTobbbb_MH125_MS2_2017_200310'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 10000
NJOBS = 1  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = False
config.Data.outputDatasetTag = "CRAB3_GEN-SIM_HToSTobbbb_S2_2017_200310"

config.Site.storageSite = 'T2_UK_London_IC' #T2_UK_London_IC
#config.Site.blacklist = ['T2_UK_London_Brunel']
