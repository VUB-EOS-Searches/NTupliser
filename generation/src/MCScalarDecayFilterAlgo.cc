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
    // Z decays
    bool ZmuPlus {false}, ZmuMinus{false}, ZmuonDecays {false};

    // Scalar decays
    bool muPlusSplus {false}, muNegSplus {false}, muPlusSneg {false}, muNegSneg {false}; // muon flags 
    bool kPlusSplus {false}, kNegSplus {false}, kPlusSneg {false}, kNegSneg {false}; // charged kaon flags
    bool kShortSplus {false}, kbarShortSplus {false}, kShortSneg {false}, kbarShortSneg {false}; // kShort flags
    bool piPlusSplus {false}, piNegSplus {false}, piPlusSneg {false}, piNegSneg {false}; // pion flags

    int it = 1;

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

        //// check for S->mumu, S->KK, K->pionpion

        // check for S->mumu
        if ( p->pdgId() == 13 ) {
            if ( hasScalarAncestors(*p) ) muPlusSplus = true;
            if ( hasScalarbarAncestors(*p) ) muPlusSneg  = true;
        }
        else if ( p->pdgId() == -13 ) {
            if ( hasScalarAncestors(*p) ) muNegSplus = true;
            if ( hasScalarbarAncestors(*p) ) muNegSneg  = true;
        }

        // check for S->K+K-
        else if ( p->pdgId() == 321 ) {
            if ( hasScalarAncestors(*p) ) kPlusSplus = true;
            if ( hasScalarbarAncestors(*p) ) kPlusSneg  = true;
        }
        else if ( p->pdgId() == -321 ) {
            if ( hasScalarAncestors(*p) ) kNegSplus = true;
            if ( hasScalarbarAncestors(*p) ) kNegSneg  = true;
        }

        // check for S->kShort kBarShort
        else if ( p->pdgId() == 310 ) {
            if ( hasScalarAncestors(*p) ) kShortSplus = true;
            if ( hasScalarbarAncestors(*p) ) kShortSneg  = true;
        }
        else if ( p->pdgId() == -310 ) {
            if ( hasScalarAncestors(*p) ) kbarShortSplus = true;
            if ( hasScalarbarAncestors(*p) ) kbarShortSneg  = true;
        }

        // check for S->pi+pi-
        else if ( p->pdgId() == 211 ) {
            if ( hasScalarAncestors(*p) ) piPlusSplus = true;
            if ( hasScalarbarAncestors(*p) ) piPlusSneg  = true;
        }
        else if ( p->pdgId() == -211 ) {
            if ( hasScalarAncestors(*p)  ) piNegSplus = true;
            if ( hasScalarbarAncestors(*p) ) piNegSneg  = true;
        }
    } // end loop over gen particles in event

    // Combinatorics

    // ggH or ggHZ/HZJ where S->mu+mu-  i.e. no Z->mu+mu- decay
    if (!ZmuonDecays) {
        // mu+mu- pair
        if (muPlusSplus && muNegSplus && muPlusSneg && muNegSneg) accepted = true; /// S->mu+mu- AND Sbar->mu+mu-

        // mu+mu- AND K+K-
        if (muPlusSplus && muNegSplus && kPlusSneg && kNegSneg) accepted = true; /// S->mu+mu- AND Sbar->K+K-

        // mu+mu- AND kShort kbarShort
        if (muPlusSplus && muNegSplus && kShortSneg && kbarShortSneg) accepted = true;   /// S->mu+mu-	AND kShort kbarShort

        // mu+mu- AND pi+pi-
        if (muPlusSplus && muNegSplus && piPlusSneg && piNegSneg) accepted = true; /// S->mu+mu-  AND Sbar->pi+pi-
    }

    // ggHZ or ZH
    else {
        // mu+mu- pair
        if (muPlusSplus && muNegSplus && muPlusSneg && muNegSneg) accepted = true; /// S->mu+mu- AND Sbar->mu+mu-

        // mu+mu- AND K+K-
        if (muPlusSplus && muNegSplus && kPlusSneg && kNegSneg) accepted = true;

        // mu+mu- AND kShort kbarShort
        if (muPlusSplus && muNegSplus && kShortSneg && kbarShortSneg) accepted = true;
        if (muPlusSneg && muNegSneg &&  kShortSplus && kbarShortSplus) accepted = true;

        // mu+mu- AND pi+pi-
        if (muPlusSplus && muNegSplus && piPlusSneg && piNegSneg) accepted = true;
        if (muPlusSneg && muNegSneg && piPlusSplus && piNegSplus) accepted = true;

        // K+K- pair
        if (kPlusSplus && kNegSplus && kPlusSneg && kNegSneg) accepted = true;

        // kShort kbarShort pair
        if (kShortSplus && kbarShortSplus && kShortSneg && kbarShortSneg) accepted = true;

        // pi+pi- pair
        if (piPlusSplus && piNegSplus && piPlusSneg && piNegSneg) accepted = true;

        // K+K- AND kShort kbarShort
        if (kPlusSplus && kNegSplus && kShortSneg && kbarShortSneg) accepted = true;
        if (kPlusSneg && kNegSneg && kShortSplus && kbarShortSplus) accepted = true;

        // K+K- AND pi+pi-
        if (kPlusSplus && kNegSplus && piPlusSneg && piNegSneg) accepted = true;
        if (kPlusSneg && kNegSneg && piPlusSplus && piNegSplus) accepted = true;

        // kShort kbarShort AND pi+pi-
        if (kShortSplus && kbarShortSplus && piPlusSneg && piNegSneg) accepted = true;
        if (kShortSneg && kbarShortSneg && piPlusSplus && piNegSplus) accepted = true;
    }

    return accepted;
}

bool MCScalarDecayFilterAlgo::hasZAncestors(const reco::GenParticle& gp) const {

    bool hasZancestor {false};

    // stop condition : this particle has no mothers
    if (gp.numberOfMothers() == 0) return false;

    // otherwise continue and check parents

    for (uint32_t im = 0; im < gp.numberOfMothers(); im++) {
        if ( gp.mother(im)->pdgId() == 23 ) hasZancestor = true;
    }

    if (hasZancestor) return true;
    else hasZAncestors(*gp.motherRef(0));

    return hasZancestor;

}

bool MCScalarDecayFilterAlgo::hasScalarAncestors(const reco::GenParticle& gp) const {

    bool hasSancestor {false};

    // stop condition : this particle has no mothers
    if (gp.numberOfMothers() == 0) return false;

    // otherwise continue and check parents


    for (uint32_t im = 0; im < gp.numberOfMothers(); im++) {
        const int motherId {gp.mother(im)->pdgId()};

        if ( motherId == 9000006 ) hasSancestor = true;
    }

    if (hasSancestor) return true;
    else hasScalarAncestors(*gp.motherRef(0));

    return hasSancestor;
}

bool MCScalarDecayFilterAlgo::hasScalarbarAncestors(const reco::GenParticle& gp) const {

    bool hasSancestor {false};

    // stop condition : this particle has no mothers
    if (gp.numberOfMothers() == 0) return false;

    // otherwise continue and check parents


    for (uint32_t im = 0; im < gp.numberOfMothers(); im++) {
        const int motherId {gp.mother(im)->pdgId()};

        if ( motherId == -9000006 ) hasSancestor = true;
    }

    if (!hasSancestor) return hasScalarbarAncestors(*gp.motherRef(0));

    return hasSancestor;
}
