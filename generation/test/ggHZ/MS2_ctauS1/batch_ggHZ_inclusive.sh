a#qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 batch_test.sh
#!/bin/bash
fail_exit() { echo "$@" 1>&2; exit 1; }

echo "Start of job on " `date`

cd /home/hep/adm10/CMSSW/CMSSW_9_4_8/src/NTupliser/generation/test/ggHZ/MS2_ctauS1/

source /cvmfs/cms.cern.ch/cmsset_default.sh

eval `scramv1 runtime -sh`

export LD_LIBRARY_PATH=`pwd`/lib/:`pwd`/lib64/:${LD_LIBRARY_PATH}

cmsRun NLO_ggHZToSS_MH125_Sinclusive_Vleptonic_MSAAAA_ctauSBBBB_2017.py outputFile=file:/vols/cms/adm10/MC/ggHZ/NLO_ggHZ_HToSS_Sinclusive_Vleptonic_M125_MS2_ctauS1_13TeV/GEN-SIM/ggHZ_MS2_ctauS1.root

echo "\nEnd of job on " `date` "\n"

