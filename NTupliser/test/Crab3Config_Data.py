from datetime import datetime
from CRABClient.UserUtilities import config, getUsernameFromSiteDB


time = datetime.now().strftime("%Y%m%d%H%M%S")

config = config()

config.General.requestName = "2017F_DoubleEG_Golden38T_Data__{}".format(time)
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserData_miniAOD_cfg.py'

config.Data.inputDataset = '/DoubleEG/Run2017F-31Mar2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 100
config.Data.lumiMask = '/afs/cern.ch/user/c/choad/public/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'

## ICHEP
# Golden JSON: /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt
# NoL1T Unprescaled (for Single + Double EG): /afs/cern.ch/user/j/jfernan/public/TOPtriggerJSONS2016/TOP_Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON_NoL1T_UnprescaledPaths.txt

## Full year
# Golden JSON: /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt
# NoL1T Unprescaled (for Double EG): /afs/cern.ch/user/j/jfernan/public/TOPtriggerJSONS2016/5Dic/ReducedJSONS_from_FullReRecoCertFile/LSforPath_HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_withLowestSeed_L1_DoubleEG_23_10_OR_L1_DoubleEG_22_12.json
# NoL1T Unprescaled (for Single EG): /afs/cern.ch/user/j/jfernan/public/TOPtriggerJSONS2016/5Dic/ReducedJSONS_from_FullReRecoCertFile/LSforPath_HLT_Ele32_eta2p1_WPTight_Gsf_withLowestSeed_L1_SingleIsoEG22er_OR_L1_SingleIsoEG24er_OR_L1_SingleIsoEG26er_OR_L1_SingleIsoEG28er_OR_L1_SingleIsoEG30er.json
# NoL1T Unprescaled + L1_SingleIsoEG32er (for Single EG): /afs/cern.ch/user/j/jfernan/public/TOPtriggerJSONS2016/5Dic/ReducedJSONS_from_FullReRecoCertFile/LSforPath_HLT_Ele32_eta2p1_WPTight_Gsf_withLowestSeed_L1_SingleIsoEG22er_OR_L1_SingleIsoEG24er_OR_L1_SingleIsoEG26er_OR_L1_SingleIsoEG28er_OR_L1_SingleIsoEG30er_OR_L1_SingleIsoEG32er.json

# config.Data.runRange = "294927-306462"
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = False
config.Data.outputDatasetTag = "CRAB3_Data_nTupilisation_2017F_DoubleEG_Golden38T_Data__{}".format(time)

config.Site.storageSite = 'T2_UK_London_Brunel' #'T2_UK_London_Brunel','T2_UK_London_IC'
