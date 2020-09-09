#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }

echo "Start of job on " `date`

cd /home/hep/adm10/CMSSW_9_4_8/src/NTupliser/NTupliser/test

source /cvmfs/cms.cern.ch/cmsset_default.sh

eval `scramv1 runtime -sh`

#export LD_LIBRARY_PATH=`pwd`/lib/:`pwd`/lib64/:${LD_LIBRARY_PATH}

#bash nTuples_HZJ_Shadronic.sh 
#bash nTuples_HZJ_Sleptonic.sh 
#bash nTuples_HZJ_Sneutrino.sh 
#bash nTuples_HZJ_SinclusiveLeptonic.sh 

#bash nTuples_ggH_Shadronic.sh
#bash nTuples_ggH_Sleptonic.sh
#bash nTuples_ggH_Sneutrino.sh
#bash nTuples_ggH_SinclusiveLeptonic.sh

bash nTuples_ggH_SinclusiveFiltered.sh
bash nTuples_ggH_SmuonicFiltered.sh
bash nTuples_ggH_SmuonHadronFiltered.sh

#bash nTuples_ggHZ_Shadronic.sh  
#bash nTuples_ggHZ_Sleptonic.sh  
#bash nTuples_ggHZ_Sneutrino.sh  
#bash nTuples_ggHZ_SinclusiveLeptonic.sh  

#rm /vols/cms/adm10/skims2017/HZJ/*/*
#rm /vols/cms/adm10/skims2017/ggHZ/*/*

rm /vols/cms/adm10/skims2017/ggH/NLO_ggH_HToSS_SinclusiveFiltered_M125_MS*/*
rm /vols/cms/adm10/skims2017/ggH/NLO_ggH_HToSS_SmuonicFiltered_M125_MS*/*
rm /vols/cms/adm10/skims2017/ggH/NLO_ggH_HToSS_SmuonHadronFiltered_M125_MS*/*

#bash skim_HZJ_Shadronic.sh
#bash skim_HZJ_Sleptonic.sh
#bash skim_HZJ_Sneutrino.sh
#bash skim_HZJ_SinclusiveLeptonic.sh

#bash skim_ggH_Shadronic.sh
#bash skim_ggH_Sleptonic.sh
#bash skim_ggH_Sneutrino.sh
#bash skim_ggH_SinclusiveLeptonic.sh

bash skim_ggH_SinclusiveFiltered.sh
bash skim_ggH_SmuonicFiltered.sh
bash skim_ggH_SmuonHadronFiltered.sh

#bash skim_ggHZ_Shadronic.sh
#bash skim_ggHZ_Sleptonic.sh
#bash skim_ggHZ_Sneutrino.sh
#bash skim_ggHZ_SinclusiveLeptonic.sh

echo "\nEnd of job on " `date` "\n"

