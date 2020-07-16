#!/bin/bash

qsub -q hep.q -l h_rt=3600 -m ea -M adm10@ic.ac.uk -pe hep.pe 8 /home/hep/adm10/CMSSW/CMSSW_9_4_8/src/NTupliser/NTupliser/test/makeNtuplesAndSkims.sh
