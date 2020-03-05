from CRABClient.UserUtilities import config, getUsernameFromSiteDB

config = config()

config.General.requestName = 'ST_TZ_2L_Kappa_Zct_RunIISpring16MiniAODv2_161020'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'prodAODtoMINIAOD.py'
config.JobType.maxMemoryMB = 2500

config.Data.inputDataset = '/ST_TZ_2L_Kappa_Zct_161006/almorton-CRAB3_MC_ST_TZ_2L_Kappa_Zct_161006-491cc9c0c16244aa3248937bd6af6e2c/USER'
config.Data.inputDBS = 'phys03'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())

config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_MC_TT_TopLeptonicDecay_TZ_2L_Kappa_Zct_RunIISpring16MiniAODv2_161020'

config.Site.storageSite = 'T2_UK_London_Brunel'
