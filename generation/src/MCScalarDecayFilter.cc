/** \class MCScalarDecayFilter


 * \author A D Morton, VUB
 * this is just the wrapper around the filtering algorithm
 * found in MCScalarDecayFilterAlgo
 *
 ************************************************************/

#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/global/EDFilter.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "NTupliser/generation/interface/MCScalarDecayFilterAlgo.h"

class MCScalarDecayFilter : public edm::global::EDFilter<> {
    public:
        explicit MCScalarDecayFilter (const edm::ParameterSet&);
        bool filter(edm::StreamID, edm::Event&, const edm::EventSetup&) const override;

    private:
        const MCScalarDecayFilterAlgo MCScalarDecayFilterAlgo_;

};

MCScalarDecayFilter::MCScalarDecayFilter(const edm::ParameterSet& iConfig) 
    : MCScalarDecayFilterAlgo_(iConfig.getParameter<edm::ParameterSet>("filterAlgoPSet"), consumesCollector()) {}

bool MCScalarDecayFilter::filter(edm::StreamID, edm::Event& iEvent, const edm::EventSetup&) const {
    return MCScalarDecayFilterAlgo_.filter(iEvent);
}

DEFINE_FWK_MODULE(MCScalarDecayFilter);
