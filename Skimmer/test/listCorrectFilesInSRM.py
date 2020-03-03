#A simple script that will copy the output files of crab job (argv[1]) to a
#directory of your choice

import subprocess
import sys

crabDir = sys.argv[1]
outputFile =  sys.argv[2]

subprocess.call("rm tempcrabfjrs.txt",shell=True)
subprocess.call("ls "+crabDir+"/res/crab_fjr* >> tempcrabfjrs.txt",shell=True)

files = open("tempcrabfjrs.txt","r")
outFile = open(outputFile,"w")

for file in files:
    fjr = open(file[:-1],"r")
    for line in fjr:
        if "PFN Value" in line:
            outFile.write(line[14:-4] + "\n")#.split("/")[-1])
#            subprocess.call("lcg-cp "+line[14:-4] + " "+copyDir+"/"+line[14:-4].split("/")[-1],shell=True)

