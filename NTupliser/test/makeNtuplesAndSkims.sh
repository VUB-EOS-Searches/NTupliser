#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }

echo "Start of job on " `date`

cd /home/hep/adm10/CMSSW/CMSSW_9_4_8/src/NTupliser/NTupliser/test

source /cvmfs/cms.cern.ch/cmsset_default.sh

eval `scramv1 runtime -sh`

export LD_LIBRARY_PATH=`pwd`/lib/:`pwd`/lib64/:${LD_LIBRARY_PATH}

bash nTuples_HZJ.sh 
bash nTuples_ggH.sh
bash nTuples_ggHZ.sh
bash nTuples_ggHZ_inclusive.sh  

rm /vols/cms/adm10/skims2017/HZJ/*/*
rm /vols/cms/adm10/skims2017/ggH/*/*
rm /vols/cms/adm10/skims2017/ggHZ/*/*

bash skim_HZJ.sh
bash skim_ggH.sh
bash skim_ggHZ.sh
bash skim_ggHZ_inclusive.sh

echo "\nEnd of job on " `date` "\n"

