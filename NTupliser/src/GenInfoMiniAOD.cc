// -*- C++ -*-
//
// Package:    GenInfo
// Class:      GenInfo
// %

// system include files
#include <cstdio>
#include <memory>
// user include files
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/Common/interface/View.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "Math/GenVector/PxPyPzM4D.h"
#include "NTupliser/NTupliser/interface/GenInfoMiniAOD.h"
#include "RecoEgamma/EgammaTools/interface/ConversionFinder.h"
#include "RecoEgamma/EgammaTools/interface/ConversionInfo.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/PdfInfo.h"
#include "TClonesArray.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TLorentzVector.h"

#include <cmath>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

GenInfoMiniAOD::GenInfoMiniAOD(const edm::ParameterSet& iConfig)
    : externalLHEToken_{consumes<LHEEventProduct>(
          iConfig.getParameter<edm::InputTag>("externalLHEToken"))}
    , pdfIdStart_{iConfig.getParameter<int>("pdfIdStart")}
    , pdfIdEnd_{iConfig.getParameter<int>("pdfIdEnd")}
    , alphaIdStart_{iConfig.getParameter<int>("alphaIdStart")}
    , alphaIdEnd_{iConfig.getParameter<int>("alphaIdEnd")}
    , isLHEflag_{iConfig.getParameter<bool>("isLHEflag")}
    , hasAlphaWeightFlag_{iConfig.getParameter<bool>("hasAlphaWeightFlag")}
{
    // now do what ever initialization is needed

    histocontainer_["eventcount"] =
        fs->make<TH1D>("eventcount", "events processed", 1, -0.5, +0.5);

    bookBranches(); // and fill tree
}

GenInfoMiniAOD::~GenInfoMiniAOD()
{
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
}

//
// member functions
//

void GenInfoMiniAOD::fillMCInfo(const edm::Event& iEvent,
                                const edm::EventSetup& /*iSetup*/)
{
    if (isLHEflag_)
    {
        edm::Handle<LHEEventProduct> EventHandle;
        iEvent.getByToken(externalLHEToken_, EventHandle);

        weight_muF0p5_ = EventHandle->weights()[2].wgt; // muF = 0.5 | muR = 1
        weight_muF2_ = EventHandle->weights()[1].wgt; // muF = 2 | muR = 1
        weight_muR0p5_ = EventHandle->weights()[6].wgt; // muF = 1 | muR = 0.5
        weight_muR2_ = EventHandle->weights()[3].wgt; // muF = 1 | muR = 2
        weight_muF0p5muR0p5_ =
            EventHandle->weights()[9].wgt; // muF = 0.5 | muR = 0.5
        weight_muF2muR2_ = EventHandle->weights()[5].wgt; // muF = 2 | muR = 2

        origWeightForNorm_ = EventHandle->originalXWGTUP();

        double pdfMax{1.0};
        double pdfMin{1.0};

        int intialIndex{pdfIdStart_};
        int finalIndex{pdfIdEnd_ + 1};
        for (int i{intialIndex}; i != finalIndex; i++)
        {
            for (unsigned int w{0}; w != EventHandle->weights().size(); ++w)
            {
                if (EventHandle->weights()[w].id == std::to_string(i))
                {
                    // std::cout << "pdf weight: "
                    //           << EventHandle->weights()[w].wgt
                    //                  / EventHandle->originalXWGTUP()
                    //           << std::endl;
                    if (EventHandle->weights()[w].wgt
                            / EventHandle->originalXWGTUP()
                        > pdfMax)
                    {
                        pdfMax = EventHandle->weights()[w].wgt
                                 / EventHandle->originalXWGTUP();
                    }
                    if (EventHandle->weights()[w].wgt
                            / EventHandle->originalXWGTUP()
                        < pdfMin)
                    {
                        pdfMin = EventHandle->weights()[w].wgt
                                 / EventHandle->originalXWGTUP();
                    }
                }
            }
        }

        weight_pdfMax_ = pdfMax;
        weight_pdfMin_ = pdfMin;

        if (hasAlphaWeightFlag_)
        {
            double alphaMax{1.0};
            double alphaMin{1.0};
            for (unsigned int w{0}; w != EventHandle->weights().size(); ++w)
            {
                if (EventHandle->weights()[w].id == alphaIdStart_)
                {
                    alphaMax = EventHandle->weights()[w].wgt
                               / EventHandle->originalXWGTUP();
                }
                if (EventHandle->weights()[w].id == alphaIdEnd_)
                {
                    alphaMin = EventHandle->weights()[w].wgt
                               / EventHandle->originalXWGTUP();
                }
            }
            if (alphaMax > alphaMin)
            {
                weight_alphaMax_ = alphaMax;
                weight_alphaMin_ = alphaMin;
            }
            else
            {
                weight_alphaMax_ = alphaMin;
                weight_alphaMin_ = alphaMax;
            }
        }
        else
        {
            weight_alphaMax_ = 1.0;
            weight_alphaMin_ = 1.0;
        }
    }

    else
    {
        weight_muF0p5_ = -999.0;
        weight_muF2_ = -999.0;
        weight_muR0p5_ = -999.0;
        weight_muR2_ = -999.0;
        weight_muF0p5muR0p5_ = -999.0;
        weight_muF2muR2_ = -999.0;
        origWeightForNorm_ = 0.0;
        weight_pdfMax_ = 1.0;
        weight_pdfMin_ = 1.0;
        weight_alphaMax_ = 1.0;
        weight_alphaMin_ = 1.0;
    }
}

// ------------ method called to for each event  ------------
void GenInfoMiniAOD::analyze(const edm::Event& iEvent,
                             const edm::EventSetup& iSetup)
{
    using namespace edm;
    // std::cout << iEvent.id().run() << " " << iEvent.luminosityBlock() << " "
    //           << iEvent.id().event() << std::endl;

    histocontainer_["eventcount"]->Fill(0.0);

    // std::cout << "now in loop" << std::endl;
    // std::cout << "cleared arrays." << std::endl;

    fillMCInfo(iEvent, iSetup);

    mytree_->Fill();
}

void GenInfoMiniAOD::bookBranches()
{
    // std::cout << "bookBranches CHECK" << std::endl;
    mytree_ = new TTree("tree", "tree");

    mytree_->Branch("weight_muF0p5", &weight_muF0p5_, "weight_muF0p5/D");
    mytree_->Branch("weight_muF2", &weight_muF2_, "weight_muF2/D");
    mytree_->Branch("weight_muR0p5", &weight_muR0p5_, "weight_muR0p5/D");
    mytree_->Branch("weight_muR2", &weight_muR2_, "weight_muR2/D");
    mytree_->Branch(
        "weight_muF0p5muR0p5", &weight_muF0p5muR0p5_, "weight_muF0p5muR0p5/D");
    mytree_->Branch("weight_muF2muR2", &weight_muF2muR2_, "weight_muF2muR2/D");
    mytree_->Branch(
        "origWeightForNorm", &origWeightForNorm_, "origWeightForNorm/D");
    mytree_->Branch("weight_pdfMax", &weight_pdfMax_, "weight_pdfMax/D");
    mytree_->Branch("weight_pdfMin", &weight_pdfMin_, "weight_pdfMin/D");
    mytree_->Branch("weight_alphaMax", &weight_alphaMax_, "weight_alphaMax/D");
    mytree_->Branch("weight_alphaMin", &weight_alphaMin_, "weight_alphaMin/D");
}

// ------------ method called once each job just before starting event loop
// ------------
void GenInfoMiniAOD::beginJob()
{
}

// ------------ method called once each job just after ending the event loop
// ------------
void GenInfoMiniAOD::endJob()
{
    std::cout << "+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+="
              << std::endl;
    std::cout << "\n\nJOB Summary:" << std::endl;
    std::cout << "number of events added to tree: " << mytree_->GetEntries()
              << std::endl;
    std::cout << "\n+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+="
              << std::endl;
}

// define this as a plug-in
DEFINE_FWK_MODULE(GenInfoMiniAOD);
