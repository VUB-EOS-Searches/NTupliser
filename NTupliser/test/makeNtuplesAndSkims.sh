#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }

echo "Start of job on " `date`

cd /home/hep/adm10/CMSSW/CMSSW_9_4_8/src/NTupliser/NTupliser/test

source /cvmfs/cms.cern.ch/cmsset_default.sh

eval `scramv1 runtime -sh`

export LD_LIBRARY_PATH=`pwd`/lib/:`pwd`/lib64/:${LD_LIBRARY_PATH}

bash nTuples_HZJ_Shadronic.sh 
bash nTuples_HZJ_Sleptonic.sh 

bash nTuples_ggH_Shadronic.sh
bash nTuples_ggH_Sleptonic.sh

bash nTuples_ggHZ_Shadronic.sh  
bash nTuples_ggHZ_Sleptonicic.sh  

rm /vols/cms/adm10/skims2017/HZJ/*/*
rm /vols/cms/adm10/skims2017/ggH/*/*
rm /vols/cms/adm10/skims2017/ggHZ/*/*

bash skim_HZJ_Shadronic.sh
bash skim_HZJ_Sleptonic.sh

bash skim_ggH_Shardonic.sh
bash skim_ggH_Sleptonic.sh

bash skim_ggHZ_Shadronic.sh
bash skim_ggHZ_Sleptonic.sh

echo "\nEnd of job on " `date` "\n"

