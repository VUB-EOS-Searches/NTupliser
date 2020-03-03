//
// Original Author:  Alexander D J Morton
//         Created:  Fri, 24 Mar 2017 14:50:53 GMT
//
//

// system include files
#include <iostream>
#include <memory>

// user include files
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"

//
// class declaration
//

class lheInfo : public edm::stream::EDProducer<>
{
    public:
    explicit lheInfo(const edm::ParameterSet& /*iConfig*/);
    ~lheInfo() override;

    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    private:
    void beginStream(edm::StreamID /*unused*/) override;
    void produce(edm::Event& /*iEvent*/,
                 const edm::EventSetup& /*iSetup*/) override;
    void endStream() override;

    void beginRun(edm::Run const& iRun, edm::EventSetup const& iSetup) override;
    // virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
    // virtual void beginLuminosityBlock(edm::LuminosityBlock const&,
    //                                   edm::EventSetup const&) override;
    // virtual void endLuminosityBlock(edm::LuminosityBlock const&,
    //                                 edm::EventSetup const&) override;

    // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
lheInfo::lheInfo(const edm::ParameterSet& /*iConfig*/)
{
    // register your products
    /* Examples
       produces<ExampleData2>();

       //if do put with a label
       produces<ExampleData2>("label");

       //if you want to put into the Run
       produces<ExampleData2,InRun>();
    */
    // now do what ever other initialization is needed
    consumes<LHERunInfoProduct, edm::InRun>(
        edm::InputTag("externalLHEProducer"));
}

lheInfo::~lheInfo()
{
    // do anything here that needs to be done at destruction time
    // (e.g. close files, deallocate resources etc.)
}

//
// member functions
//

// ------------ method called to produce the data  ------------
void lheInfo::produce(edm::Event& /*iEvent*/, const edm::EventSetup& /*iSetup*/)
{
    using namespace edm;
    /* This is an event example
       //Read 'ExampleData' from the Event
       Handle<ExampleData> pIn;
       iEvent.getByLabel("example",pIn);

       //Use the ExampleData to create an ExampleData2 which
       // is put into the Event
       std::unique_ptr<ExampleData2> pOut(new ExampleData2(*pIn));
       iEvent.put(std::move(pOut));
    */

    /* this is an EventSetup example
       //Read SetupData from the SetupRecord in the EventSetup
       ESHandle<SetupData> pSetup;
       iSetup.get<SetupRecord>().get(pSetup);
    */
}

// ------------ method called once each stream before processing any runs, lumis
// or events  ------------
void lheInfo::beginStream(edm::StreamID /*unused*/)
{
}

// ------------ method called once each stream after processing all runs, lumis
// and events  ------------
void lheInfo::endStream()
{
}

// ------------ method called when starting to processes a run  ------------

void lheInfo::beginRun(edm::Run const& iRun, edm::EventSetup const& /*iSetup*/)
{
    edm::Handle<LHERunInfoProduct> run;
    using headers_const_iterator =
        std::vector<LHERunInfoProduct::Header>::const_iterator;

    iRun.getByLabel("externalLHEProducer", run);
    LHERunInfoProduct myLHERunInfoProduct{*(run.product())};

    for (auto iter{myLHERunInfoProduct.headers_begin()};
         iter != myLHERunInfoProduct.headers_end();
         iter++)
    {
        std::cout << iter->tag() << std::endl;
        std::vector<std::string> lines{iter->lines()};
        for (const auto& line : lines)
        {
            std::cout << line;
        }
    }
}

// ------------ method called when ending the processing of a run  ------------
// void lheInfo::endRun(edm::Run const&, edm::EventSetup const&)
// {
// }

// ------------ method called when starting to processes a luminosity block
// ------------
// void lheInfo::beginLuminosityBlock(edm::LuminosityBlock const&,
//                                    edm::EventSetup const&)
// {
// }

// ------------ method called when ending the processing of a luminosity block
// ------------
// void lheInfo::endLuminosityBlock(edm::LuminosityBlock const&,
//                                  edm::EventSetup const&)
// {
// }

// ------------ method fills 'descriptions' with the allowed parameters for the
// module  ------------
void lheInfo::fillDescriptions(edm::ConfigurationDescriptions& descriptions)
{
    // The following says we do not know what parameters are allowed so do no
    // validation
    // Please change this to state exactly what you do use, even if it is no
    // parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

// define this as a plug-in
DEFINE_FWK_MODULE(lheInfo);
