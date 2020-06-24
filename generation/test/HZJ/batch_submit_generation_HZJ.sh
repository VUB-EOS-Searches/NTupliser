#qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 batch_test.sh
#!/bin/bash

qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS1_ctauS1/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS1_ctauS10/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS1_ctauS100/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS1_ctauS1000/batch_HZJ.sh

qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS2_ctauS1/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS2_ctauS10/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS2_ctauS100/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS2_ctauS1000/batch_HZJ.sh

qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS40_ctauS1/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS40_ctauS10/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS40_ctauS100/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS40_ctauS1000/batch_HZJ.sh

qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS55_ctauS1/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS55_ctauS10/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS55_ctauS100/batch_HZJ.sh
qsub -q hep.q -l h_rt=35640 -pe hep.pe 8 MS55_ctauS1000/batch_HZJ.sh

