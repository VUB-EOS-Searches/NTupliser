#qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 batch_test.sh
#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }

echo "Start of job on " `date`

cd /home/hep/adm10/CMSSW/CMSSW_9_4_8/src/NTupliser/generation/test/

source /cvmfs/cms.cern.ch/cmsset_default.sh

eval `scramv1 runtime -sh`

export LD_LIBRARY_PATH=`pwd`/lib/:`pwd`/lib64/:${LD_LIBRARY_PATH}

cmsRun step3_PAT_miniAOD_2017.py inputFiles=file:/vols/cms/adm10/MC/HZJ/NLO_HZJ_HToSS_Shadronic_Vleptonic_M125_MS2_ctauS10_13TeV/RAW2DIGI_RECO_EI/step2_2017_3p5K.root outputFile=file:/vols/cms/adm10/MC/HZJ/NLO_HZJ_HToSS_Shadronic_Vleptonic_M125_MS2_ctauS10_13TeV/PAT_miniAOD/miniAOD_2017_3p5K.root

echo "\nEnd of job on " `date` "\n"

