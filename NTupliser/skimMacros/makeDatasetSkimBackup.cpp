#include<iostream>
#include<string>
#include<fstream>
#include"AnalysisEvent.h"
#include<sstream>
#include<sys/stat.h>
#include<TH1.h>

int main(int argc, char* argv[]){
  
  std::string fileName = argv[1];
  std::string datasetName = argv[2];
  bool isMC (false);
  if ( argc == 4 ) isMC = std::stoi(argv[3]);

  std::ifstream fileList(fileName.c_str());
  std::string line;             

  int fileNum = 0;
  while(getline(fileList,line)){

    std::string numName, numNamePlus;
    std::ostringstream convert, convert1;
    convert << fileNum;
    convert1 << fileNum+2;
    numName = convert.str();
    numNamePlus = convert1.str();
    
    struct stat buffer;
    if (stat(("/scratch/data/tZqSkimsRun2016/" + datasetName + "/skimFile"+numNamePlus+".root").c_str(), &buffer) == 0) {
      fileNum++;
      continue;
    }

    unsigned int summedWeights [14] {};
    TH1I* weightHisto = new TH1I ("sumNumPosMinusNegWeights","sumNumPosMinusNegWeights", 7, -3.5, 3.5);

    TChain * datasetChain = new TChain("makeTopologyNtupleMiniAOD/tree");
    datasetChain->Add(line.c_str());
    
    //    std::cout << line;
    //TFile inFile(line.c_str());    

    TTree * outTree = datasetChain->CloneTree(0);

    //stupid long conversion between int and string.

    TFile outFile(("/scratch/data/tZqSkimsRun2016/" + datasetName + "/skimFile"+numName+".root").c_str(),"RECREATE");
  
    int numberOfEvents = datasetChain->GetEntries();
    AnalysisEvent * event = new AnalysisEvent(isMC,"",datasetChain);
    for (int i = 0; i < numberOfEvents; i++){
      if (i % 500 < 0.01) std::cerr << i << "/" << numberOfEvents << " (" << 100*float(i)/numberOfEvents << "%)\r";
    
      event->GetEntry(i);

      // Get number of positive and negative amc@nlo weights
      if ( isMC ) {
	if ( event->origWeightForNorm >= 0.0 ) summedWeights[0]++;
	else summedWeights[1]++;
	if ( event->weight_muF0p5 >= 0.0 ) summedWeights[2]++;
	else summedWeights[3]++;
	if ( event->weight_muR0p5 >= 0.0 ) summedWeights[4]++;
	else summedWeights[5]++;
	if ( event->weight_muF0p5muR0p5 >= 0.0 ) summedWeights[6]++;
	else summedWeights[7]++;
	if ( event->weight_muF2 >= 0.0 ) summedWeights[8]++;
	else summedWeights[9]++;
	if ( event->weight_muR2 >= 0.0 ) summedWeights[10]++;
	else summedWeights[11]++;
	if ( event->weight_muF2muR2 >= 0.0 ) summedWeights[12]++;
	else summedWeights[13]++;
      }

      int numLeps = 0;
      for (int j = 0; j < event->numElePF2PAT; j++){
	if (event->elePF2PATPT[j] < 9) continue;
	if (fabs(event->elePF2PATEta[j]) > 2.7) continue;
	if (event->elePF2PATComRelIsoRho[j] > 0.5) continue;
	numLeps++;
      }
      for (int j = 0; j < event->numMuonPF2PAT; j++){
	if (event->muonPF2PATPt[j] < 9) continue;
	if (event->muonPF2PATComRelIsodBeta[j] > 0.5) continue;
	if (fabs(event->muonPF2PATEta[j]) > 2.8) continue;
	numLeps++;
      }
      if (numLeps >= 2) outTree->Fill();
    } 

    if ( isMC ) {

      weightHisto->Fill(0., summedWeights[0]-summedWeights[1]);
      weightHisto->Fill(-1., summedWeights[2]-summedWeights[3]);
      weightHisto->Fill(-2., summedWeights[4]-summedWeights[5]);
      weightHisto->Fill(-3., summedWeights[6]-summedWeights[7]);
      weightHisto->Fill(1., summedWeights[8]-summedWeights[9]);
      weightHisto->Fill(2., summedWeights[10]-summedWeights[11]);
      weightHisto->Fill(3., summedWeights[12]-summedWeights[13]);
/*
      weightHisto->Fill(0., -666.);
      weightHisto->Fill(-1., -666);
      weightHisto->Fill(-2., -666);
      weightHisto->Fill(-3., -666);
      weightHisto->Fill(1., -666);
      weightHisto->Fill(2., -666);
      weightHisto->Fill(3., -666);
*/
    }

    outFile.cd();
    outTree->Write();
    if (isMC) weightHisto->Write();

    outFile.Write();
    outFile.Close();
    //    inFile.Close();
    
    delete datasetChain;
    delete event;
    delete outTree;
    delete weightHisto;
    fileNum++;
    std::cerr << "" << std::endl;
  }

}

