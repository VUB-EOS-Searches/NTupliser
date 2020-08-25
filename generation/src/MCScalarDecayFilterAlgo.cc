#include "NTupliser/generation/interface/MCScalarDecayFilterAlgo.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include <iostream>
#include <cmath>
#include <cstdlib>


MCScalarDecayFilterAlgo::MCScalarDecayFilterAlgo(const edm::ParameterSet& iConfig, edm::ConsumesCollector&& iC) 
    : genParticleToken_{iC.consumes<reco::GenParticleCollection>(iConfig.getParameter<edm::InputTag>("genParticles"))} 
{
}


MCScalarDecayFilterAlgo::~MCScalarDecayFilterAlgo()
{
}


// ------------ method called to filter events  ------------
bool MCScalarDecayFilterAlgo::filter(const edm::Event& iEvent) const
{
    bool accepted = false;

    edm::Handle<reco::GenParticleCollection> genParticles;
    iEvent.getByToken(genParticleToken_, genParticles);

    // Flags for processes in event
    bool ZmuPlus {false}, ZmuMinus{false}, ZmuonDecays {false};

    for (reco::GenParticleCollection::const_iterator p = genParticles->begin(); p != genParticles->end(); ++p) {

        // Check for Z->mu+mu-
        // mu+ check first
        if ( p->pdgId() == 13 ) { // if mu+
            if ( hasZAncestors(*p) ) ZmuPlus = true;
        }
        else if ( p->pdgId() == -13 ) { // if mu+
            if ( hasZAncestors(*p) ) ZmuMinus= true;
        }

        if ( ZmuPlus && ZmuMinus ) ZmuonDecays = true;

        // check for S->mumu, S->KK, K->pionpion

    }

    if ( ZmuonDecays ) accepted = true;

    return accepted;
}

bool MCScalarDecayFilterAlgo::hasZAncestors(const reco::GenParticle& gp) const {

    bool hasZancestor {false};

    // stop condition : this particle has no mothers
    if (gp.numberOfMothers() == 0) return hasZancestor;

    // otherwise continue and check parents

    for (uint32_t im = 0; im < gp.numberOfMothers(); im++) {
        if ( gp.mother(im)->pdgId() == 23 ) hasZancestor = true;
    }

    if (hasZancestor) return hasZancestor;
    else hasZAncestors(*gp.motherRef(0));

    return hasZancestor;

}

bool MCScalarDecayFilterAlgo::hasScalarAncestors(const reco::GenParticle& gp) const {
/*
    // stop condition : this particle has no mothers
    if (gp.numberOfMothers() == 0) return false;

    // otherwise continue and check parents
    bool hasSancestor {false};

    for (uint32_t im = 0; im < gp.numberOfMothers(); im++) {
        if ( gp.mother(im)->pdgId() == 9000006 ) hasSancestor = true;
    }

    if (hasSancestor) return hasSancestor;
    else hasScalarAncestors(*gp.motherRef(im));
*/
    return false;
}
