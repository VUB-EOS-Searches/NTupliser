#qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 batch_test.sh
#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }

echo "Start of job on " `date`

cd /home/hep/adm10/CMSSW/CMSSW_9_4_8/src/NTupliser/generation/test/ggH/MS55_ctauS1/

source /cvmfs/cms.cern.ch/cmsset_default.sh

eval `scramv1 runtime -sh`

export LD_LIBRARY_PATH=`pwd`/lib/:`pwd`/lib64/:${LD_LIBRARY_PATH}

cmsRun NLO_ggHToSS_MH125_SinclusiveLeptonic_Vleptonic_2017.py outputFile=file:/vols/cms/adm10/MC/ggH/NLO_ggH_HToSS_SinclusiveLeptonic_M125_MS55_ctauS1_13TeV/GEN-SIM/ggH_MS55_ctauS1.root

echo "\nEnd of job on " `date` "\n"

