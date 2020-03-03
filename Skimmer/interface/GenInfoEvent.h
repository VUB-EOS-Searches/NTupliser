//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Thu Jan 23 14:04:00 2014 by ROOT version 5.32/00
// from TChain tree/
//////////////////////////////////////////////////////////

#ifndef _GenInfoEvent_hpp_
#define _GenInfoEvent_hpp_

#include <TChain.h>
#include <TFile.h>
#include <TLorentzVector.h>
#include <TROOT.h>
#include <iostream>
#include <string>

// Header file for the classes stored in the TTree if any.

// Fixed size dimensions of array or collections stored in the TTree if any.

class GenInfoEvent
{
    public:
    TTree* fChain; //! pointer to the analyzed TTree or TChain
    Int_t fCurrent; //! current Tree number in a TChain

    Double_t weight_muF0p5;
    Double_t weight_muF2;
    Double_t weight_muR0p5;
    Double_t weight_muR2;
    Double_t weight_muF0p5muR0p5;
    Double_t weight_muF2muR2;
    Double_t origWeightForNorm;
    Double_t weight_pdfMax;
    Double_t weight_pdfMin;
    Double_t weight_alphaMax;
    Double_t weight_alphaMin;

    TBranch* b_weight_muF0p5; //!
    TBranch* b_weight_muF2; //!
    TBranch* b_weight_muR0p5; //!
    TBranch* b_weight_muR2; //!
    TBranch* b_weight_muF0p5muR0p5; //!
    TBranch* b_weight_muF2muR2; //!
    TBranch* b_origWeightForNorm; //!
    TBranch* b_weight_pdfMax; //!
    TBranch* b_weight_pdfMin; //!
    TBranch* b_weight_alphaMax; //!
    TBranch* b_weight_alphaMin; //!

    GenInfoEvent(std::string triggerFlag = "", TTree* tree = 0);
    virtual ~GenInfoEvent();
    virtual Int_t Cut(Long64_t entry);
    virtual Int_t GetEntry(Long64_t entry);
    virtual Long64_t LoadTree(Long64_t entry);
    virtual void Init(std::string triggerFlag, TTree* tree);
    virtual void Loop();
    virtual Bool_t Notify();
    virtual void Show(Long64_t entry = -1);
    float getEventWeight(Long64_t entry);
};

#endif

#ifdef GenInfoEvent_cxx
GenInfoEvent::GenInfoEvent(std::string triggerFlag, TTree* tree) : fChain(0)
{
    // if parameter tree is not specified (or zero), connect the file
    // used to generate this class and read the Tree.
    if (tree == 0)
    {
#ifdef SINGLE_TREE
        // The following code should be used if you want this class to access
        // a single tree instead of a chain
        TFile* f = (TFile*)gROOT->GetListOfFiles()->FindObject(
            "/data1/tW2012/mc/ttbarInclusive/MC_Ntuple_out_9_0_MJP_skim.root");
        if (!f || !f->IsOpen())
        {
            f = new TFile("/data1/tW2012/mc/ttbarInclusive/"
                          "MC_Ntuple_out_9_0_MJP_skim.root");
        }
        f->GetObject("tree", tree);

#else // SINGLE_TREE

        // The following code should be used if you want this class to access a
        // chain of trees.
        TChain* chain = new TChain("tree", "");
        chain->Add("/data1/tW2012/mc/ttbarInclusive/"
                   "MC_Ntuple_out_100_0_Gu6_skim.root/tree");
        tree = chain;
#endif // SINGLE_TREE
    }
    Init(triggerFlag, tree);
}

GenInfoEvent::~GenInfoEvent()
{
    if (!fChain)
        return;
    delete fChain->GetCurrentFile();
}

Int_t GenInfoEvent::GetEntry(Long64_t entry)
{
    // Read contents of entry.
    if (!fChain)
        return 0;
    return fChain->GetEntry(entry);
}

Long64_t GenInfoEvent::LoadTree(Long64_t entry)
{
    // Set the environment to read one entry
    if (!fChain)
        return -5;
    Long64_t centry = fChain->LoadTree(entry);
    if (centry < 0)
        return centry;
    if (fChain->GetTreeNumber() != fCurrent)
    {
        fCurrent = fChain->GetTreeNumber();
        Notify();
    }
    return centry;
}

void GenInfoEvent::Init(std::string triggerFlag, TTree* tree)
{
    // The Init() function is called when the selector needs to initialize
    // a new tree or chain. Typically here the branch addresses and branch
    // pointers of the tree will be set.
    // It is normally not necessary to make changes to the generated
    // code, but the routine can be extended by the user if needed.
    // Init() will be called many times when running on PROOF
    // (once per file to be processed).

    // Set branch addresses and branch pointers
    if (!tree)
        return;
    fChain = tree;
    fCurrent = -1;
    fChain->SetMakeClass(1);

    fChain->SetBranchAddress("weight_muF0p5", &weight_muF0p5, &b_weight_muF0p5);
    fChain->SetBranchAddress("weight_muF2", &weight_muF2, &b_weight_muF2);
    fChain->SetBranchAddress("weight_muR0p5", &weight_muR0p5, &b_weight_muR0p5);
    fChain->SetBranchAddress("weight_muR2", &weight_muR2, &b_weight_muR2);
    fChain->SetBranchAddress(
        "weight_muF0p5muR0p5", &weight_muF0p5muR0p5, &b_weight_muF0p5muR0p5);
    fChain->SetBranchAddress(
        "weight_muF2muR2", &weight_muF2muR2, &b_weight_muF2muR2);
    fChain->SetBranchAddress(
        "origWeightForNorm", &origWeightForNorm, &b_origWeightForNorm);
    fChain->SetBranchAddress("weight_pdfMax", &weight_pdfMax, &b_weight_pdfMax);
    fChain->SetBranchAddress("weight_pdfMin", &weight_pdfMin, &b_weight_pdfMin);
    fChain->SetBranchAddress(
        "weight_alphaMax", &weight_alphaMax, &b_weight_alphaMax);
    fChain->SetBranchAddress(
        "weight_alphaMin", &weight_alphaMin, &b_weight_alphaMin);

    Notify();
}

Bool_t GenInfoEvent::Notify()
{
    //  std::cout << "Does the notify." << std::endl;
    // The Notify() function is called when a new file is opened. This
    // can be either for a new TTree in a TChain or when when a new TTree
    // is started when using PROOF. It is normally not necessary to make changes
    // to the generated code, but the routine can be extended by the
    // user if needed. The return value is currently not used.

    return kTRUE;
}

void GenInfoEvent::Show(Long64_t entry)
{
    // Print contents of entry.
    // If entry is not specified, print current entry
    if (!fChain)
        return;
    fChain->Show(entry);
}
Int_t GenInfoEvent::Cut(Long64_t entry)
{
    // This function may be called from Loop.
    // returns  1 if entry is accepted.
    // returns -1 otherwise.
    return 1;
}
#endif // #ifdef GenInfoEvent_cxx
