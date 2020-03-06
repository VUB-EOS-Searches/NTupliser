/// -*- C++ -*-
//
// Package:    GenInfo
// Class:      GenInfo
// %

#ifndef __GENINFO_MINIAOD_H__
#define __GENINFO_MINIAOD_H__


class GenInfoMiniAOD : public edm::EDAnalyzer {
public:
  explicit GenInfoMiniAOD(const edm::ParameterSet&);
  ~GenInfoMiniAOD();


private:
//  virtual void beginJob(const edm::EventSetup&) ;
  virtual void beginJob() ;
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;

  // ----------member data ---------------------------

  edm::Service<TFileService> fs;
  std::map<std::string,TH1D*> histocontainer_; // simple map to contain all histograms. Histograms are booked in the beginJob() method

  // Generator level info
  edm::EDGetTokenT<LHEEventProduct> externalLHEToken_;
  int pdfIdStart_;
  int pdfIdEnd_;
  int alphaIdStart_;
  int alphaIdEnd_;

  bool isLHEflag_;
  bool hasAlphaWeightFlag_;

  // and an ntuple (filling in the methods)
  void fillMCInfo(const edm::Event&, const edm::EventSetup&);

  void bookBranches(void);// does all the branching.
  
  TTree *mytree_;

  double weight_muF0p5_;
  double weight_muF2_;
  double weight_muR0p5_;
  double weight_muR2_;
  double weight_muF0p5muR0p5_;
  double weight_muF2muR2_;

  double origWeightForNorm_;

  double weight_pdfMax_;
  double weight_pdfMin_;
  double weight_alphaMax_;
  double weight_alphaMin_;

};

#endif
