#ifndef MCScalarDecayFilterAlgo_h
#define MCScalarDecayFilterAlgo_h

// -*- C++ -*-
//
// Package:    MCScalarDecayFilterAlgo
// Class:      MCScalarDecayFilterAlgo
// \author: A D J MORTON

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"

//
// class decleration
//

class MCScalarDecayFilterAlgo {
    public :
        MCScalarDecayFilterAlgo(const edm::ParameterSet&, edm::ConsumesCollector&& iC);
        ~MCScalarDecayFilterAlgo();

        bool filter(const edm::Event& iEvent) const;

    private:

      // ----------memeber function----------------------
      bool hasZAncestors(const reco::GenParticle& gp) const;
      bool hasScalarAncestors(const reco::GenParticle& gp, const bool scalarSign) const;

      // ----------member data ---------------------------
       edm::EDGetTokenT<reco::GenParticleCollection> genParticleToken_;

};
#endif
