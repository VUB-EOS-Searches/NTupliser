/// -*- C++ -*-
//
// Package:    MakeTopologyNtuple
// Class:      MakeTopologyNtuple
//
// Original Author:  Freya Blekman
// Modified by: Duncan Leggat, Alexander Morton
//         Created:  Wed April 22 19:23:10 CET 2009
// $Id: MakeTopologyNtuple.h,v 1.68 2010/11/05 15:32:16 chadwick Exp $
//
//

#ifndef __MAKE_TOPOLOGY_NTUPLE_MINIAOD_H__
#define __MAKE_TOPOLOGY_NTUPLE_MINIAOD_H__

#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

class EffectiveAreas;
class TTree;

class MakeTopologyNtupleMiniAOD : public edm::EDAnalyzer
{
    public:
    explicit MakeTopologyNtupleMiniAOD(const edm::ParameterSet&);
    ~MakeTopologyNtupleMiniAOD();

    private:
    //  virtual void beginJob(const edm::EventSetup&) ;
    virtual void beginJob();
    virtual void analyze(const edm::Event&, const edm::EventSetup&);
    virtual void endJob();

    // ----------member data ---------------------------

    edm::Service<TFileService> fs;
    std::map<std::string, TH1D*>
        histocontainer_; // simple map to contain all histograms. Histograms
                         // are booked in the beginJob() method
    std::map<std::string, TH2D*>
        histocontainer2D_; // simple map to contain all histograms. Histograms
                           // are booked in the beginJob() method (2D)

    edm::EDGetTokenT<reco::BeamSpot> beamSpotToken_;
    edm::EDGetTokenT<std::vector<pat::PackedCandidate>> packedCandToken_;
    edm::EDGetTokenT<std::vector<pat::IsolatedTrack>> isolatedTrackToken_;
    edm::EDGetTokenT<reco::ConversionCollection> conversionsToken_;

    edm::EDGetTokenT<pat::ElectronCollection> eleLabel_;
    edm::EDGetTokenT<pat::PhotonCollection> phoLabel_;
    edm::EDGetTokenT<pat::PhotonCollection> ootPhoLabel_;
    edm::InputTag muoLabel_;
    edm::InputTag jetLabel_;
    //  edm::InputTag genJetTag_; // Need to replace
    edm::EDGetTokenT<reco::GenJetCollection> genJetsToken_;
    edm::InputTag tauLabel_;
    edm::InputTag metLabel_;

    edm::EDGetTokenT<pat::PhotonCollection> patPhotonsToken_;
    edm::EDGetTokenT<pat::PhotonCollection> patOOTphotonsToken_;
    edm::EDGetTokenT<pat::ElectronCollection> patElectronsToken_;
    edm::InputTag tauPFTag_;
    edm::EDGetTokenT<pat::MuonCollection> patMuonsToken_;
    //  edm::InputTag jetPFTag_;	// Need to replace
    edm::EDGetTokenT<pat::JetCollection> patJetsToken_;
    edm::InputTag jetPFRecoTag_;
    edm::EDGetTokenT<pat::METCollection> patMetToken_;
    edm::InputTag jetJPTTag_;
    edm::InputTag metJPTTag_;

    edm::EDGetTokenT<edm::TriggerResults> trigToken_;
    edm::EDGetTokenT<edm::TriggerResults> metFilterToken_;
    std::vector<std::string> fakeTrigLabelList_;
    std::vector<std::string> bTagList_;
    std::vector<std::string> triggerList_;
    std::vector<std::string> metFilterList_;

    edm::InputTag l1TrigLabel_;
    edm::EDGetTokenT<reco::GenParticleCollection> genParticlesToken_;
    edm::EDGetTokenT<reco::GenParticleCollection> genSimParticlesToken_;
    edm::EDGetTokenT<reco::VertexCollection> pvLabel_;
    edm::EDGetTokenT<reco::VertexCompositePtrCandidateCollection> svLabel_;
    edm::EDGetTokenT<reco::VertexCompositePtrCandidateCollection> kshortToken_;
    edm::EDGetTokenT<reco::VertexCompositePtrCandidateCollection> lambdaToken_;
    edm::EDGetTokenT<double> rhoToken_;
    EffectiveAreas effectiveAreaInfo_;
    edm::EDGetTokenT<std::vector<PileupSummaryInfo>> pileupToken_;
    const bool hasGeneralTracks_;
    edm::EDGetTokenT<reco::TrackCollection> generalTracksToken_;

    // Sets stuff for 2016 rereco, namely ele IDs
    const bool is2016rereco_{};

    // Sets whether the sample is ttbar or not. Default is false. This affects
    // top pt reweighting of the sample.
    const bool isttbar_{};
    edm::InputTag ttGenEvent_;

    // Generator level info
    edm::EDGetTokenT<LHEEventProduct> externalLHEToken_;
    int pdfIdStart_{};
    int pdfIdEnd_{};
    int alphaIdStart_{};
    int alphaIdEnd_{};
    edm::EDGetTokenT<GenEventInfoProduct> pdfInfoToken_;
    edm::EDGetTokenT<GenEventInfoProduct> generatorToken_;

    std::map<std::string, int> hltpasses_;
    std::vector<std::string> hltnames_;
    std::vector<std::string> metFilterNames_;

    bool filledBIDInfo_{};
    bool runMCInfo_{};
    bool runPUReWeight_{};
    bool doCuts_{};
    bool doSynch_{};

    // jet cuts
    double jetPtCut_{};
    double jetEtaCut_{};

    bool runPDFUncertainties_{};
    bool useResidualJEC_{};

    int minLeptons_{};
    double elePtCut_{};
    double eleEtaCut_{};
    double eleIsoCut_{};
    double muoPtCut_{};
    double muoEtaCut_{};
    double muoIsoCut_{};
    double metCut_{};
    double rhoIso{};

    bool ran_jetloop_{};
    bool ran_eleloop_{};
    bool ran_muonloop_{};
    bool ran_mcloop_{};
    bool ran_postloop_{};
    bool ran_PV_{};
    bool ran_BS_{};
    bool ran_tracks_{};
    bool ran_isotracks_{};
    bool ran_packedCands_{};
    bool ran_photonTau_{};
    bool check_triggers_;
    std::string muoIDquality_;
    bool flavorHistoryTag_{};
    double dREleGeneralTrackMatch_{};
    double magneticField_{};
    double correctFactor_{};
    double maxDist_{};
    double maxDcot_{};
    edm::InputTag ebRecHits_;
    edm::InputTag eeRecHits_;
    const bool isMCatNLO_{};
    const bool isLHEflag_{};
    const bool hasAlphaWeightFlag_{};

    // and an ntuple (filling in the methods)
    void fillBeamSpot(const edm::Event&, const edm::EventSetup&);
    void fillJets(const edm::Event&,
                  const edm::EventSetup&,
                  edm::EDGetTokenT<pat::JetCollection>,
                  const std::string&);
    void fillBTagInfo(const pat::Jet& jet,
                      const size_t jetindex,
                      const std::string& ID);
    void fillOtherJetInfo(const pat::Jet& jet,
                          const size_t jetindex,
                          const std::string& ID,
                          const edm::Event& iEvent);
    void fillMCJetInfo(const reco::GenJet& jet,
                       const size_t jetindex,
                       const std::string& ID,
                       bool runMC);
    void fillMCJetInfo(int empty,
                       const size_t jetindex,
                       const std::string& ID,
                       bool fillMC);
    void fillMuons          (const edm::Event&, const edm::EventSetup&, edm::EDGetTokenT<pat::MuonCollection>, const std::string&);
    void fillMuonTrackPairs (const edm::Event&, const edm::EventSetup&, edm::EDGetTokenT<pat::MuonCollection>, const std::string&);
    void fillElectrons(const edm::Event&,
                       const edm::EventSetup&,
                       edm::EDGetTokenT<pat::ElectronCollection>,
                       const std::string&,
                       edm::EDGetTokenT<pat::ElectronCollection>);
    void fillPhotons(const edm::Event&,
                       const edm::EventSetup&,
                       edm::EDGetTokenT<pat::PhotonCollection>,
                       const std::string&,
                       edm::EDGetTokenT<pat::PhotonCollection>);
    void fillMissingET(const edm::Event&,
                       const edm::EventSetup&,
                       edm::EDGetTokenT<pat::METCollection>,
                       const std::string&);
    void fillEventInfo(const edm::Event&, const edm::EventSetup&);
    void fillPV(const edm::Event&, const edm::EventSetup&);
    void fillSV(const edm::Event&, const edm::EventSetup&);
    void fillMCInfo(const edm::Event&, const edm::EventSetup&);
    void fillTriggerData(const edm::Event&);
    void fillSummaryVariables(void); // should only be called after all other functions.
    void fillGeneralTracks(const edm::Event&, const edm::EventSetup&);
    void fillIsolatedTracks(const edm::Event&, const edm::EventSetup&);
//    void fillLostTracksCands(const edm::Event&, const edm::EventSetup&);
    void fillPackedCands(const edm::Event&, const edm::EventSetup&);

    // Helper functions
    void bookBranches(void); // does all the branching.
    void bookJetBranches(const std::string& ID,
                         const std::string& name); // called by bookBranches,
                                                   // makes jet branches.
    void bookBIDInfoBranches(const std::string&,
                             const std::string&); // called by bookJetBranches,
                                                  // makes branches for B-ID.
    void bookPFJetBranches(const std::string& ID,
                           const std::string& name); // called by bookBranches,
                                                     // makes jet branches.
    void bookTauBranches(const std::string& ID, const std::string& name);
    void bookPhotonBranches(const std::string& ID, const std::string& name);
    void bookElectronBranches(
        const std::string& ID,
        const std::string&
            name); // called by bookBranches, makes electron branches.
    void bookMuonBranches(const std::string& ID,
                          const std::string& name); // called by bookBranches,
                                                    // makes muon branches.
    void bookMETBranches(const std::string& ID,
                         const std::string& name); // called by bookBranches ,
                                                   // makes MET branches
    void bookCaloMETBranches(const std::string& ID,
                             const std::string& name); // called by bookBranches
                                                       // , makes MET branches
    void bookMCBranches(void); // called by bookBranches, makes MC branches.
    void bookGeneralTracksBranches(void); // called by bookBranches, makes generalTracks branches.
    void bookIsolatedTracksBranches(void); // called by bookBranches, makes isolatedTracks branches.
//    void bookLostTracksBranches(void); // called by bookBranches, makes lostTracks branches.
    void bookPackedCandsBranches(void); // called by bookBranches, makes packedCands branches.
    void bookPVbranches(void); // called by bookBranches, makes PV branches.
    void bookSVbranches(void); // called by bookBranches, makes SV branches.

    TTree* mytree_{};

    double weight_muF0p5_{};
    double weight_muF2_{};
    double weight_muR0p5_{};
    double weight_muR2_{};
    double weight_muF0p5muR0p5_{};
    double weight_muF2muR2_{};

    double isrRedHi{};
    double fsrRedHi{};
    double isrRedLo{};
    double fsrRedLo{};
    double isrDefHi{};
    double fsrDefHi{};
    double isrDefLo{};
    double fsrDefLo{};
    double isrConHi{};
    double fsrConHi{};
    double isrConLo{};
    double fsrConLo{};

    double origWeightForNorm_{};

    double weight_pdfMax_{};
    double weight_pdfMin_{};
    double weight_alphaMax_{};
    double weight_alphaMin_{};

    int processId_{};
    int genMyProcId{};
    float processPtHat_{};

    double weight_{};
    double topPtReweight{};

    int numGeneralTracks{};
    int numIsolatedTracks{};
    int numPackedCands{};
    std::map<std::string, int> numJet;
    std::map<std::string, int> numEle;
    std::map<std::string, int> numPho;
    std::map<std::string, int> numMuo;

    math::XYZPoint beamSpotPoint_;
    math::XYZPoint vertexPoint_;
    reco::Vertex* vertexPrimary_;

    unsigned int flavorHistory{};

    template<class C>
    struct IndexSorter
    {
        IndexSorter(const C& values, bool decreasing = true)
            : values_(values), decrease_(decreasing)
        {
        }
        std::vector<size_t> operator()() const
        {
            std::vector<size_t> result;
            result.reserve(values_.size());
            for (size_t i = 0; i < values_.size(); ++i)
                result.emplace_back(i);
            sort(result.begin(), result.end(), *this);
            return result;
        }
        bool operator()(int a, int b)
        {
            if (decrease_)
                return values_[a] > values_[b];
            else
                return values_[a] < values_[b];
        }
        const C& values_;
        bool decrease_;
    };

    void cleararrays(void); // used to set everything in the following arrays
                            // to zero or unphysical numbers
    void clearPVarrays(void); // clearing PV info, used by cleararrays
    void clearSVarrays(void); // clearing SV info, used by cleararrays
    void clearjetarrays(const std::string&); // clearing jet info, used by cleararrays]
    void clearTauArrays(const std::string&);
    void clearPhotonArrays(const std::string&);
    void clearelectronarrays(const std::string&); // clearing electron info, used by cleararrays
    void clearmuonarrays(const std::string&); // clearing muon info, used by cleararrays
    void clearMetArrays(const std::string&); // clearing met info
    void clearMCarrays(void); // clearing MC info
    void clearGeneralTracksArrays(void); // clearing generalTracks info, used by cleararrays
    void clearIsolatedTracksArrays(void); // clearing isolatedTracks info, used by cleararrays
//    void clearLostTracksArrays(void); // clearing lostTracks info, used by cleararrays
    void clearPackedCandsArrays(void); // clearing packedCands info, used by cleararrays

    std::vector<float> electronEts; // just used for sorting
    std::vector<float> photonEts; // just used for sorting
    std::vector<float> muonEts; // just used for sorting
    std::vector<float> correctedJetEts; // just used for sorting

    float beamSpotX{};
    float beamSpotY{};
    float beamSpotZ{};

    static constexpr size_t NPVSMAX{80};
    int numPVs{};
    float pvX[NPVSMAX]{};
    float pvY[NPVSMAX]{};
    float pvZ[NPVSMAX]{};
    float pvDX[NPVSMAX]{};
    float pvDY[NPVSMAX]{};
    float pvDZ[NPVSMAX]{};
    float pvRho[NPVSMAX]{};
    int pvIsFake[NPVSMAX]{};
    float pvChi2[NPVSMAX]{};	
    float pvNdof[NPVSMAX]{};
    int pvNtracks[NPVSMAX]{};
    int pvNtracksW05[NPVSMAX]{};

    static constexpr size_t NSVSMAX{20};
    int numSVs{};
    float svPt[NSVSMAX]{};
    float svPx[NSVSMAX]{};
    float svPy[NSVSMAX]{};
    float svPz[NSVSMAX]{};
    float svMass[NSVSMAX]{};
    float svE[NSVSMAX]{};
    float svEta[NSVSMAX]{};
    float svTheta[NSVSMAX]{};
    float svPhi[NSVSMAX]{};
    float svX[NSVSMAX]{};
    float svY[NSVSMAX]{};
    float svZ[NSVSMAX]{};
    float svVertexChi2[NSVSMAX]{};
    float svVertexNdof[NSVSMAX]{};
    int svNtracks[NSVSMAX]{};
    float svDist3D[NSVSMAX]{};
    float svDist3DSig[NSVSMAX]{};
    float svDist3DError[NSVSMAX]{};
    float svDistXY[NSVSMAX]{};
    float svDistXYSig[NSVSMAX]{};
    float svDistXYError[NSVSMAX]{};
    float svAnglePV[NSVSMAX]{};
    int svIsLambda[NSVSMAX]{};
    int svIsKshort[NSVSMAX]{};
    

    std::map<std::string, int> nzcandidates;
    std::map<std::string, std::vector<float>>
        zcandidatesvector; // stores the Z candidates

    // hardcoded, do NOT change unless you also change the size of the arrays
    // that are saved in the root tree...
    static constexpr size_t NELECTRONSMAX{30};

    std::map<std::string, std::vector<float>> electronSortedE;
    std::map<std::string, std::vector<float>> electronSortedEt;
    std::map<std::string, std::vector<float>> electronSortedEta;
    std::map<std::string, std::vector<float>> electronSortedPt;
    std::map<std::string, std::vector<float>> electronSortedTheta;
    std::map<std::string, std::vector<float>> electronSortedPhi;
    std::map<std::string, std::vector<float>> electronSortedPx;
    std::map<std::string, std::vector<float>> electronSortedPy;
    std::map<std::string, std::vector<float>> electronSortedPz;
    std::map<std::string, std::vector<int>> electronSortedCharge;

    std::map<std::string, std::vector<int>> electronSortedCutIdVeto;
    std::map<std::string, std::vector<int>> electronSortedCutIdLoose;
    std::map<std::string, std::vector<int>> electronSortedCutIdMedium;
    std::map<std::string, std::vector<int>> electronSortedCutIdTight;
    std::map<std::string, std::vector<int>> electronSortedMvaIdWp80;
    std::map<std::string, std::vector<int>> electronSortedMvaIdWp90;
    std::map<std::string, std::vector<int>> electronSortedMvaIdWpLoose;
    std::map<std::string, std::vector<int>> electronSortedMvaIdNoIsoWp80;
    std::map<std::string, std::vector<int>> electronSortedMvaIdNoIsoWp90;
    std::map<std::string, std::vector<int>> electronSortedMvaIdWpNoIsoLoose;

    std::map<std::string, std::vector<float>> electronSortedChargedHadronIso;
    std::map<std::string, std::vector<float>> electronSortedNeutralHadronIso;
    std::map<std::string, std::vector<float>> electronSortedPhotonIso;
    std::map<std::string, std::vector<float>> electronSortedTrackPt;
    std::map<std::string, std::vector<float>> electronSortedTrackEta;
    std::map<std::string, std::vector<float>> electronSortedTrackPhi;
    std::map<std::string, std::vector<float>> electronSortedTrackChi2;
    std::map<std::string, std::vector<float>> electronSortedTrackNDOF;
    std::map<std::string, std::vector<float>> electronSortedTrackD0;
    std::map<std::string, std::vector<float>>
        electronSortedBeamSpotCorrectedTrackD0;
    std::map<std::string, std::vector<float>>
        electronSortedDBBeamSpotCorrectedTrackD0;

    // std::map< std::string, std::vector<float> > electronSortedDBInnerTrackD0;

    std::map<std::string, std::vector<float>> electronSortedTrackDz;
    std::map<std::string, std::vector<float>> electronSortedTrackD0PV;
    std::map<std::string, std::vector<float>> electronSortedTrackDZPV;
    std::map<std::string, std::vector<float>> electronSortedVtxZ;
    std::map<std::string, std::vector<float>>
        electronSortedBeamSpotCorrectedTrackDz;
    std::map<std::string, std::vector<int>> electronSortedIsGsf;
    std::map<std::string, std::vector<float>> electronSortedGsfPx;
    std::map<std::string, std::vector<float>> electronSortedGsfPy;
    std::map<std::string, std::vector<float>> electronSortedGsfPz;
    std::map<std::string, std::vector<float>> electronSortedGsfE;
    std::map<std::string, std::vector<float>> electronSortedEcalEnergy;

    std::map<std::string, std::vector<float>> electronSortedSuperClusterEta;
    std::map<std::string, std::vector<float>> electronSortedSuperClusterE;
    std::map<std::string, std::vector<float>> electronSortedSuperClusterPhi;
    std::map<std::string, std::vector<float>> electronSortedSuperClusterEoverP;
    std::map<std::string, std::vector<float>>
        electronSortedSuperClusterSigmaEtaEta;
    std::map<std::string, std::vector<float>> electronSortedSuperClusterE1x5;
    std::map<std::string, std::vector<float>> electronSortedSuperClusterE2x5max;
    std::map<std::string, std::vector<float>> electronSortedSuperClusterE5x5;
    std::map<std::string, std::vector<float>>
        electronSortedSuperClusterSigmaIEtaIEta;
    std::map<std::string, std::vector<float>>
        electronSortedSuperClusterSigmaIEtaIEta5x5;
    std::map<std::string, std::vector<float>> electronSortedTrackIso04;
    std::map<std::string, std::vector<float>> electronSortedECalIso04;
    std::map<std::string, std::vector<float>> electronSortedHCalIso04;
    std::map<std::string, std::vector<float>> electronSortedTrackIso03;
    std::map<std::string, std::vector<float>> electronSortedECalIso03;
    std::map<std::string, std::vector<float>> electronSortedHCalIso03;
    std::map<std::string, std::vector<float>> electronSorteddr04EcalRecHitSumEt;
    std::map<std::string, std::vector<float>> electronSorteddr03EcalRecHitSumEt;
    std::map<std::string, std::vector<float>> electronSortedECalIsoDeposit;
    std::map<std::string, std::vector<float>> electronSortedHCalIsoDeposit;
    std::map<std::string, std::vector<float>> electronSortedCaloIso;
    std::map<std::string, std::vector<float>> electronSortedTriggerMatch;
    std::map<std::string, std::vector<float>> electronSortedJetOverlap;
    std::map<std::string, std::vector<float>> electronSortedComRelIso;
    std::map<std::string, std::vector<float>> electronSortedComRelIsodBeta;
    std::map<std::string, std::vector<float>> electronSortedComRelIsoRho;
    std::map<std::string, std::vector<float>> electronSortedChHadIso;
    std::map<std::string, std::vector<float>> electronSortedNtHadIso;
    std::map<std::string, std::vector<float>> electronSortedGammaIso;
    std::map<std::string, std::vector<float>> electronSortedRhoIso;
    std::map<std::string, std::vector<float>> electronSortedAEff03;
    std::map<std::string, std::vector<int>> electronSortedMissingInnerLayers;
    std::map<std::string, std::vector<float>> electronSortedHoverE;
    std::map<std::string, std::vector<float>> electronSortedDeltaPhiSC;
    std::map<std::string, std::vector<float>> electronSortedDeltaEtaSC;
    std::map<std::string, std::vector<float>> electronSortedDeltaEtaSeedSC;
    std::map<std::string, std::vector<int>> electronSortedIsBarrel;
    std::map<std::string, std::vector<int>> electronSortedPhotonConversionTag;
    std::map<std::string, std::vector<int>> electronSortedPhotonConversionTagCustom;
    std::map<std::string, std::vector<float>> electronSortedPhotonConversionDcot;
    std::map<std::string, std::vector<float>> electronSortedPhotonConversionDist;
    std::map<std::string, std::vector<int>> electronSortedPhotonConversionVeto;
    std::map<std::string, std::vector<float>> electronSortedPhotonConversionDcotCustom;
    std::map<std::string, std::vector<float>> electronSortedPhotonConversionDistCustom;

    std::map<std::string, std::vector<float>> electronSortedImpactTransDist;
    std::map<std::string, std::vector<float>> electronSortedImpactTransError;
    std::map<std::string, std::vector<float>> electronSortedImpactTransSignificance;
    std::map<std::string, std::vector<float>> electronSortedImpact3DDist;
    std::map<std::string, std::vector<float>> electronSortedImpact3DError;
    std::map<std::string, std::vector<float>> electronSortedImpact3DSignificance;

    //  std::map< std::string, std::vector<float> > electronSortedIDResults_;

    std::map<std::string, std::vector<float>> genElectronSortedPt;
    std::map<std::string, std::vector<float>> genElectronSortedEt;
    std::map<std::string, std::vector<float>> genElectronSortedEta;
    std::map<std::string, std::vector<float>> genElectronSortedTheta;
    std::map<std::string, std::vector<float>> genElectronSortedPhi;
    std::map<std::string, std::vector<float>> genElectronSortedPx;
    std::map<std::string, std::vector<float>> genElectronSortedPy;
    std::map<std::string, std::vector<float>> genElectronSortedPz;
    std::map<std::string, std::vector<int>> genElectronSortedCharge;
    std::map<std::string, std::vector<int>> genElectronSortedPdgId;
    std::map<std::string, std::vector<int>> genElectronSortedMotherId;
    std::map<std::string, std::vector<int>> genElectronSortedPromptDecayed;
    std::map<std::string, std::vector<int>> genElectronSortedPromptFinalState;
    std::map<std::string, std::vector<int>> genElectronSortedHardProcess;

    // hardcoded, do NOT change unless you also change the size of the arrays
    // that are saved in the root tree...
    static constexpr size_t NPHOTONSMAX{30};

    std::map<std::string, std::vector<float>> photonSortedE;
    std::map<std::string, std::vector<float>> photonSortedSigmaE;
    std::map<std::string, std::vector<float>> photonSortedET;
    std::map<std::string, std::vector<float>> photonSortedPhi;
    std::map<std::string, std::vector<float>> photonSortedEta;
    std::map<std::string, std::vector<float>> photonSortedTheta;
    std::map<std::string, std::vector<float>> photonSortedPt;
    std::map<std::string, std::vector<float>> photonSortedPx;
    std::map<std::string, std::vector<float>> photonSortedPy;
    std::map<std::string, std::vector<float>> photonSortedPz;
    std::map<std::string, std::vector<float>> photonSortedCalibE;
    std::map<std::string, std::vector<float>> photonSortedCalibEt;
    std::map<std::string, std::vector<float>> photonSortedSCE;
    std::map<std::string, std::vector<float>> photonSortedSCRawE;
    std::map<std::string, std::vector<float>> photonSortedESEnP1;
    std::map<std::string, std::vector<float>> photonSortedESEnP2;
    std::map<std::string, std::vector<float>> photonSortedSCEta;
    std::map<std::string, std::vector<float>> photonSortedSCEtaWidth;
    std::map<std::string, std::vector<float>> photonSortedSCPhi;
    std::map<std::string, std::vector<float>> photonSortedSCPhiWidth;
    std::map<std::string, std::vector<float>> photonSortedSCBrem;
    std::map<std::string, std::vector<int>> photonSortedHasPixelSeed;
    std::map<std::string, std::vector<int>> photonSortedEleVeto;
    std::map<std::string, std::vector<float>> photonSortedR9;
    std::map<std::string, std::vector<float>> photonSortedHoverE;
    std::map<std::string, std::vector<float>> photonSortedESEffSigmaRR;
    std::map<std::string, std::vector<float>> photonSortedSigmaIEtaIEtaFull5x5;
    std::map<std::string, std::vector<float>> photonSortedSigmaIEtaIPhiFull5x5;
    std::map<std::string, std::vector<float>> photonSortedSigmaIPhiIPhiFull5x5;
    std::map<std::string, std::vector<float>> photonSortedE2x2Full5x5;
    std::map<std::string, std::vector<float>> photonSortedE5x5Full5x5;
    std::map<std::string, std::vector<float>> photonSortedR9Full5x5;
    std::map<std::string, std::vector<float>> photonSortedPFChIso;
    std::map<std::string, std::vector<float>> photonSortedPFPhoIso;
    std::map<std::string, std::vector<float>> photonSortedPFNeuIso;
    std::map<std::string, std::vector<float>> photonSortedPFChWorstIso;
    std::map<std::string, std::vector<float>> photonSortedMIPTotEnergy;    
    std::map<std::string, std::vector<int>> photonSortedCutIdLoose;
    std::map<std::string, std::vector<int>> photonSortedCutIdMedium;
    std::map<std::string, std::vector<int>> photonSortedCutIdTight;
    std::map<std::string, std::vector<int>> photonSortedMvaIdWp80;
    std::map<std::string, std::vector<int>> photonSortedMvaIdWp90;

    std::map<std::string, std::vector<float>> genPhotonSortedPt;
    std::map<std::string, std::vector<float>> genPhotonSortedET;
    std::map<std::string, std::vector<float>> genPhotonSortedEta;
    std::map<std::string, std::vector<float>> genPhotonSortedTheta;
    std::map<std::string, std::vector<float>> genPhotonSortedPhi;
    std::map<std::string, std::vector<float>> genPhotonSortedPx;
    std::map<std::string, std::vector<float>> genPhotonSortedPy;
    std::map<std::string, std::vector<float>> genPhotonSortedPz;
    std::map<std::string, std::vector<int>> genPhotonSortedCharge;
    std::map<std::string, std::vector<int>> genPhotonSortedPdgId;
    std::map<std::string, std::vector<int>> genPhotonSortedMotherId;
    std::map<std::string, std::vector<int>> genPhotonSortedIsPhoton;
    std::map<std::string, std::vector<int>> genPhotonSortedIsConvertedPhoton;
    std::map<std::string, std::vector<int>> genPhotonSortedIsJet;

    // gen branches


    // MC Truth
    size_t nT{};
    size_t nThadronic{};
    size_t nb{};
    size_t nWhadronic{};
    size_t nTleptonic{};
    size_t nWleptonic{};
    int VQQBosonAbsId{};

    static constexpr size_t NTOPMCINFOSMAX{20};
    float T_hadronicMCTruthE[NTOPMCINFOSMAX]{};
    float T_hadronicMCTruthEt[NTOPMCINFOSMAX]{};
    float T_hadronicMCTruthPx[NTOPMCINFOSMAX]{};
    float T_hadronicMCTruthPy[NTOPMCINFOSMAX]{};
    float T_hadronicMCTruthPz[NTOPMCINFOSMAX]{};
    int T_hadronicMotherIndex[NTOPMCINFOSMAX]{};

    float T_leptonicMCTruthE[NTOPMCINFOSMAX]{};
    float T_leptonicMCTruthEt[NTOPMCINFOSMAX]{};
    float T_leptonicMCTruthPx[NTOPMCINFOSMAX]{};
    float T_leptonicMCTruthPy[NTOPMCINFOSMAX]{};
    float T_leptonicMCTruthPz[NTOPMCINFOSMAX]{};
    int T_leptonicMotherIndex[NTOPMCINFOSMAX]{};

    float bMCTruthE[NTOPMCINFOSMAX]{};
    float bMCTruthEt[NTOPMCINFOSMAX]{};
    float bMCTruthPx[NTOPMCINFOSMAX]{};
    float bMCTruthPy[NTOPMCINFOSMAX]{};
    float bMCTruthPz[NTOPMCINFOSMAX]{};
    int bMCTruthMother[NTOPMCINFOSMAX]{};

    float W_hadronicMCTruthE[NTOPMCINFOSMAX]{};
    float W_hadronicMCTruthEt[NTOPMCINFOSMAX]{};
    float W_hadronicMCTruthPx[NTOPMCINFOSMAX]{};
    float W_hadronicMCTruthPy[NTOPMCINFOSMAX]{};
    float W_hadronicMCTruthPz[NTOPMCINFOSMAX]{};
    int W_hadronicMCTruthPID[NTOPMCINFOSMAX]{};
    int W_hadronicMCTruthMother[NTOPMCINFOSMAX]{};

    float W_leptonicMCTruthE[NTOPMCINFOSMAX]{};
    float W_leptonicMCTruthEt[NTOPMCINFOSMAX]{};
    float W_leptonicMCTruthPx[NTOPMCINFOSMAX]{};
    float W_leptonicMCTruthPy[NTOPMCINFOSMAX]{};
    float W_leptonicMCTruthPz[NTOPMCINFOSMAX]{};
    int W_leptonicMCTruthPID[NTOPMCINFOSMAX]{};
    int W_leptonicMCTruthMother[NTOPMCINFOSMAX]{};

    int isElePlusJets{};

    //  float remainingEnergy[20];

    std::map<std::string, double> metE;
    std::map<std::string, double> metEt;
    std::map<std::string, double> metEtRaw;
    std::map<std::string, double> metPhi;
    std::map<std::string, double> metPt;
    std::map<std::string, double> metPx;
    std::map<std::string, double> metPy;
    std::map<std::string, double> metPz;
    std::map<std::string, float> metSignificance;
    std::map<std::string, float> metScalarEt;
    std::map<std::string, float> metEtUncorrected;
    std::map<std::string, float> metPhiUncorrected;
    std::map<std::string, float> metUnclusteredEnUp;
    std::map<std::string, float> metUnclusteredEnDown;
    std::map<std::string, float> metMaxEtEM;
    std::map<std::string, float> metMaxEtHad;
    std::map<std::string, float> metEtFracHad;
    std::map<std::string, float> metEtFracEM;
    std::map<std::string, float> metHadEtHB;
    std::map<std::string, float> metHadEtHO;
    std::map<std::string, float> metHadEtHE;
    std::map<std::string, float> metEmEtEE;
    std::map<std::string, float> metEmEtEB;
    std::map<std::string, float> metEmEtHF;
    std::map<std::string, float> metHadEtHF;
    std::map<std::string, float> genMetE;
    std::map<std::string, float> genMetEt;
    std::map<std::string, float> genMetPhi;
    std::map<std::string, float> genMetPt;
    std::map<std::string, float> genMetPx;
    std::map<std::string, float> genMetPy;
    std::map<std::string, float> genMetPz;

    int numVert{};

    float mhtPx{};
    float mhtPy{};
    float mhtPt{};
    float mhtPhi{};
    float mhtSumEt{};
    float mhtSignif{};

    static constexpr size_t NMUONSMAX{20};
    std::map<std::string, std::vector<float>> muonSortedE;
    std::map<std::string, std::vector<float>> muonSortedEt;
    std::map<std::string, std::vector<float>> muonSortedPt;
    std::map<std::string, std::vector<float>> muonSortedEta;
    std::map<std::string, std::vector<float>> muonSortedTheta;
    std::map<std::string, std::vector<float>> muonSortedPhi;
    std::map<std::string, std::vector<float>> muonSortedPx;
    std::map<std::string, std::vector<float>> muonSortedPy;
    std::map<std::string, std::vector<float>> muonSortedPz;
    std::map<std::string, std::vector<int>> muonSortedCharge;
    std::map<std::string, std::vector<int>> muonSortedLooseCutId;
    std::map<std::string, std::vector<int>> muonSortedMediumCutId;
    std::map<std::string, std::vector<int>> muonSortedTightCutId;
    std::map<std::string, std::vector<int>> muonSortedPfIsoVeryLoose;
    std::map<std::string, std::vector<int>> muonSortedPfIsoLoose;
    std::map<std::string, std::vector<int>> muonSortedPfIsoMedium;
    std::map<std::string, std::vector<int>> muonSortedPfIsoTight;
    std::map<std::string, std::vector<int>> muonSortedPfIsoVeryTight;
    std::map<std::string, std::vector<int>> muonSortedTkIsoLoose;
    std::map<std::string, std::vector<int>> muonSortedTkIsoTight;
    std::map<std::string, std::vector<int>> muonSortedMvaLoose;
    std::map<std::string, std::vector<int>> muonSortedMvaMedium;
    std::map<std::string, std::vector<int>> muonSortedMvaTight;

    std::map<std::string, std::vector<float>> muonSortedGlobalID;
    std::map<std::string, std::vector<float>> muonSortedTrackID;
    std::map<std::string, std::vector<float>> muonSortedChi2;
    std::map<std::string, std::vector<float>> muonSortedD0;
    std::map<std::string, std::vector<float>> muonSortedDBBeamSpotCorrectedTrackD0;
    std::map<std::string, std::vector<float>> muonSortedDBInnerTrackD0;
    std::map<std::string, std::vector<float>> muonSortedBeamSpotCorrectedD0;
    std::map<std::string, std::vector<int>> muonSortedTrackNHits;
    std::map<std::string, std::vector<int>> muonSortedValidHitsGlobal;
    std::map<std::string, std::vector<float>> muonSortedNDOF; // n_d.o.f

    // Extra muon variables used for ID and stuff
    std::map<std::string, std::vector<int>> muonSortedTkLysWithMeasurements;
    std::map<std::string, std::vector<float>> muonSortedGlbTkNormChi2;
    std::map<std::string, std::vector<float>> muonSortedBestTkNormChi2;
    std::map<std::string, std::vector<float>> muonSortedDBPV;
    std::map<std::string, std::vector<float>> muonSortedDBPVError;
    std::map<std::string, std::vector<float>> muonSortedDZPV;
    std::map<std::string, std::vector<float>> muonSortedDZPVError;
    std::map<std::string, std::vector<int>> muonSortedVldPixHits;
    std::map<std::string, std::vector<int>> muonSortedMatchedStations;

    // Vertex location information. For dZ cuts.
    std::map<std::string, std::vector<float>> muonSortedVertX;
    std::map<std::string, std::vector<float>> muonSortedVertY;
    std::map<std::string, std::vector<float>> muonSortedVertZ;

    // Best muon track information
    std::map<std::string, std::vector<float>> muonSortedBestTkPt;
    std::map<std::string, std::vector<float>> muonSortedBestTkPx;
    std::map<std::string, std::vector<float>> muonSortedBestTkPy;
    std::map<std::string, std::vector<float>> muonSortedBestTkPz;
    std::map<std::string, std::vector<float>> muonSortedBestTkEta;
    std::map<std::string, std::vector<float>> muonSortedBestTkPhi;

    std::map<std::string, std::vector<float>> muonSortedChargedHadronIso;
    std::map<std::string, std::vector<float>> muonSortedNeutralHadronIso;
    std::map<std::string, std::vector<float>> muonSortedPhotonIso;

    std::map<std::string, std::vector<float>> muonSortedTrackIso;
    std::map<std::string, std::vector<float>> muonSortedECalIso;
    std::map<std::string, std::vector<float>> muonSortedHCalIso;
    std::map<std::string, std::vector<float>> muonSortedComRelIso;
    std::map<std::string, std::vector<float>> muonSortedComRelIsodBeta;
    std::map<std::string, std::vector<int>> muonSortedIsPFMuon;
    std::map<std::string, std::vector<int>> muonSortedNumPackedCands;
    std::map<std::string, std::vector<int>> muonSortedPackedCandsIndex;

    std::map<std::string, std::vector<int>> muonSortedNumChambers;
    std::map<std::string, std::vector<int>> muonSortedNumMatches;

    // Extra variables used for ICHEP ID during HIP issue stuff
    std::map<std::string, std::vector<float>> muonValidFraction;
    std::map<std::string, std::vector<float>> muonChi2LocalPosition;
    std::map<std::string, std::vector<float>> muonTrkKick;
    std::map<std::string, std::vector<float>> muonSegmentCompatibility;


    std::map<std::string, std::vector<float>> genMuonSortedPt;
    std::map<std::string, std::vector<float>> genMuonSortedEt;
    std::map<std::string, std::vector<float>> genMuonSortedEta;
    std::map<std::string, std::vector<float>> genMuonSortedTheta;
    std::map<std::string, std::vector<float>> genMuonSortedPhi;
    std::map<std::string, std::vector<float>> genMuonSortedPx;
    std::map<std::string, std::vector<float>> genMuonSortedPy;
    std::map<std::string, std::vector<float>> genMuonSortedPz;
    std::map<std::string, std::vector<int>> genMuonSortedCharge;
    std::map<std::string, std::vector<int>> genMuonSortedPdgId;
    std::map<std::string, std::vector<int>> genMuonSortedMotherId;
    std::map<std::string, std::vector<int>> genMuonSortedPromptDecayed;
    std::map<std::string, std::vector<int>> genMuonSortedPromptFinalState;
    std::map<std::string, std::vector<int>> genMuonSortedHardProcess;

    static constexpr size_t NMUONTRACKPAIRSMAX{190};

    static constexpr size_t NJETSMAX{40};

    // JEC to be initialised once per collection.
    FactorizedJetCorrector* jecCalo{};
    FactorizedJetCorrector* jecPF{};
    FactorizedJetCorrector* jecJPT{};
    JetCorrectionUncertainty* jecCaloUncertainty{};
    JetCorrectionUncertainty* jecPFUncertainty{};
    JetCorrectionUncertainty* jecJPTUncertainty{};

    std::map<std::string, std::vector<double>> jetSortedE;
    std::map<std::string, std::vector<double>> jetSortedEt;
    std::map<std::string, std::vector<double>> jetSortedPt;
    std::map<std::string, std::vector<double>> jetSortedPtRaw;
    std::map<std::string, std::vector<double>> jetSortedUnCorEt;
    std::map<std::string, std::vector<double>> jetSortedUnCorPt;
    std::map<std::string, std::vector<double>> jetSortedEta;
    std::map<std::string, std::vector<double>> jetSortedTheta;
    std::map<std::string, std::vector<double>> jetSortedPhi;
    std::map<std::string, std::vector<double>> jetSortedPx;
    std::map<std::string, std::vector<double>> jetSortedPy;
    std::map<std::string, std::vector<double>> jetSortedPz;
    std::map<std::string, std::vector<double>> jetSortedMass;
    std::map<std::string, std::vector<int>> jetSortedID;
    std::map<std::string, std::vector<double>> jetSortedClosestLepton;
    std::map<std::string, std::vector<int>> jetSortedNtracksInJet;
    std::map<std::string, std::vector<float>> jetSortedJetCharge;
    std::map<std::string, std::vector<float>> jetSortedfHPD;
    std::map<std::string, std::vector<float>>
        jetSortedCorrFactor; // only include full JES corrections for now.
    std::map<std::string, std::vector<float>> jetSortedCorrResidual;
    std::map<std::string, std::vector<float>> jetSortedL2L3ResErr;
    std::map<std::string, std::vector<float>>
        jetSortedCorrErrLow; // JES uncertainty
    std::map<std::string, std::vector<float>> jetSortedCorrErrHi;
    std::map<std::string, std::vector<float>> jetSortedN90Hits;
    std::map<std::string, std::vector<float>> jetSortedTriggered;
    std::map<std::string, std::vector<float>> jetSortedSVX;
    std::map<std::string, std::vector<float>> jetSortedSVY;
    std::map<std::string, std::vector<float>> jetSortedSVZ;
    std::map<std::string, std::vector<float>> jetSortedSVDX;
    std::map<std::string, std::vector<float>> jetSortedSVDY;
    std::map<std::string, std::vector<float>> jetSortedSVDZ;
    std::map<std::string, std::vector<int>> jetSortedNConstituents;

    // Calo Jet
    std::map<std::string, std::vector<float>> jetSortedEMEnergyInEB;
    std::map<std::string, std::vector<float>> jetSortedEMEnergyInEE;
    std::map<std::string, std::vector<float>> jetSortedEMEnergyFraction;
    std::map<std::string, std::vector<float>> jetSortedEMEnergyInHF;
    std::map<std::string, std::vector<float>> jetSortedHadEnergyInHB;
    std::map<std::string, std::vector<float>> jetSortedHadEnergyInHE;
    std::map<std::string, std::vector<float>> jetSortedHadEnergyInHF;
    std::map<std::string, std::vector<float>> jetSortedHadEnergyInHO;
    std::map<std::string, std::vector<float>> jetSortedN60;
    std::map<std::string, std::vector<float>> jetSortedN90;
    // PF Specific
    std::map<std::string, std::vector<float>> jetSortedNeutralEmEnergy;
    std::map<std::string, std::vector<float>> jetSortedMuEnergy;
    std::map<std::string, std::vector<float>> jetSortedMuEnergyFraction;
    std::map<std::string, std::vector<int>> jetSortedChargedMultiplicity;
    std::map<std::string, std::vector<float>> jetSortedNeutralHadEnergy;

    std::map<std::string, std::vector<int>> jetSortedNeutralMultiplicity;
    std::map<std::string, std::vector<float>>
        jetSortedChargedHadronEnergyFraction;
    std::map<std::string, std::vector<float>>
        jetSortedNeutralHadronEnergyFraction;
    std::map<std::string, std::vector<float>> jetSortedChargedEmEnergyFraction;
    std::map<std::string, std::vector<float>> jetSortedNeutralEmEnergyFraction;
    std::map<std::string, std::vector<float>> jetSortedMuonFraction;
    std::map<std::string, std::vector<float>>
        jetSortedChargedHadronEnergyFractionCorr;
    std::map<std::string, std::vector<float>>
        jetSortedNeutralHadronEnergyFractionCorr;
    std::map<std::string, std::vector<float>>
        jetSortedChargedEmEnergyFractionCorr;
    std::map<std::string, std::vector<float>>
        jetSortedNeutralEmEnergyFractionCorr;
    std::map<std::string, std::vector<float>> jetSortedMuonFractionCorr;

    // more detailed BID info for a few algorithms.
    std::map<std::string, std::vector<float>> jetSortedBtagSoftMuonPtRel;
    std::map<std::string, std::vector<float>> jetSortedBtagSoftMuonQuality;
    std::map<std::string, std::vector<float>>
        jetSortedBIDParams_; // stores the parameter (db) output
    std::map<std::string, float> bidParamsDiscCut_;

    std::map<std::string, std::vector<float>> genJetSortedE;
    std::map<std::string, std::vector<float>> genJetSortedEt;
    std::map<std::string, std::vector<float>> genJetSortedPt;
    std::map<std::string, std::vector<float>> genJetSortedEta;
    std::map<std::string, std::vector<float>> genJetSortedTheta;
    std::map<std::string, std::vector<float>> genJetSortedPhi;
    std::map<std::string, std::vector<float>> genJetSortedPx;
    std::map<std::string, std::vector<float>> genJetSortedPy;
    std::map<std::string, std::vector<float>> genJetSortedPz;
    std::map<std::string, std::vector<float>> genJetSortedMass;
    std::map<std::string, std::vector<int>> genJetSortedID;
    std::map<std::string, std::vector<int>> jetSortedPID;
    std::map<std::string, std::vector<int>> genJetSortedPID;
    std::map<std::string, std::vector<int>> genJetSortedMotherPID;
    std::map<std::string, std::vector<int>> genJetSortedScalarAncestor;
    std::map<std::string, std::vector<float>> genJetSortedClosestB;
    std::map<std::string, std::vector<float>> genJetSortedClosestC;

    std::map<std::string, float> fixedGridRhoFastjetAll;

    // generalTracks are drawn from AOD collection
    static constexpr size_t NTRACKSMAX{1000};
    float generalTracksPt[NTRACKSMAX]{};
    float generalTracksPx[NTRACKSMAX]{};
    float generalTracksPy[NTRACKSMAX]{};
    float generalTracksPz[NTRACKSMAX]{};
    float generalTracksEta[NTRACKSMAX]{};
    float generalTracksTheta[NTRACKSMAX]{};
    float generalTracksPhi[NTRACKSMAX]{};
    float generalTracksCharge[NTRACKSMAX]{};
    float generalTracksVx[NTRACKSMAX]{};
    float generalTracksVy[NTRACKSMAX]{};
    float generalTracksVz[NTRACKSMAX]{};
    float generalTracksBeamSpotCorrectedD0[NTRACKSMAX]{};

    // isoTracks that are drawn from packedPFCands, lostTracks and packedCands
    static constexpr size_t NISOTRACKSMAX{40};
    float isoTracksPt[NISOTRACKSMAX]{};
    float isoTracksPx[NISOTRACKSMAX]{};
    float isoTracksPy[NISOTRACKSMAX]{};
    float isoTracksPz[NISOTRACKSMAX]{};
    float isoTracksE[NISOTRACKSMAX]{};
    float isoTracksEta[NISOTRACKSMAX]{};
    float isoTracksTheta[NISOTRACKSMAX]{};
    float isoTracksPhi[NISOTRACKSMAX]{};
    int isoTracksCharge[NISOTRACKSMAX]{};
    int isoTracksPdgId[NISOTRACKSMAX]{};
    float isoTracksMatchedCaloJetEmEnergy[NISOTRACKSMAX]{};
    float isoTracksMatchedCaloJetHadEnergy[NISOTRACKSMAX]{};
    float isoTracksDz[NISOTRACKSMAX]{};
    float isoTracksDxy[NISOTRACKSMAX]{};
    float isoTracksDzError[NISOTRACKSMAX]{};
    float isoTracksDxyError[NISOTRACKSMAX]{};
    int isoTracksFromPV[NISOTRACKSMAX]{};
    int isoTracksVx[NISOTRACKSMAX]{};
    int isoTracksVy[NISOTRACKSMAX]{};
    int isoTracksVz[NISOTRACKSMAX]{};
    int isoTracksHighPurity[NISOTRACKSMAX]{};
    int isoTracksTight[NISOTRACKSMAX]{};
    int isoTracksLoose[NISOTRACKSMAX]{};
    float isoTracksDeltaEta[NISOTRACKSMAX]{};
    float isoTracksDeltaPhi[NISOTRACKSMAX]{};

    // packedCands are used to subtract photon conversion background
    static constexpr size_t NPACKEDCANDSMAX{1000};
    float packedCandsPt[NPACKEDCANDSMAX]{};
    float packedCandsPx[NPACKEDCANDSMAX]{};
    float packedCandsPy[NPACKEDCANDSMAX]{};
    float packedCandsPz[NPACKEDCANDSMAX]{};
    float packedCandsE[NPACKEDCANDSMAX]{};
    float packedCandsM[NPACKEDCANDSMAX]{};
    float packedCandsEta[NPACKEDCANDSMAX]{};
    float packedCandsTheta[NPACKEDCANDSMAX]{};
    float packedCandsPhi[NPACKEDCANDSMAX]{};
    int packedCandsCharge[NPACKEDCANDSMAX]{};
    int packedCandsPdgId[NPACKEDCANDSMAX]{};
    float packedCandsTime[NPACKEDCANDSMAX]{};
    int packedCandsFromPV[NPACKEDCANDSMAX]{};
    int packedCandsPVquality[NPACKEDCANDSMAX]{};
    float packedCandsVx[NPACKEDCANDSMAX]{};
    float packedCandsVy[NPACKEDCANDSMAX]{};
    float packedCandsVz[NPACKEDCANDSMAX]{};
    float packedCandsVEta[NPACKEDCANDSMAX]{};
    float packedCandsVPhi[NPACKEDCANDSMAX]{};
    float packedCandsBeamSpotCorrectedD0[NPACKEDCANDSMAX]{};
    float packedCandsDz[NPACKEDCANDSMAX]{};
    float packedCandsDxy[NPACKEDCANDSMAX]{};
    float packedCandsDzAssocPV[NPACKEDCANDSMAX]{};
    float packedCandsVtxChi2Norm[NPACKEDCANDSMAX]{};
    int packedCandsHasTrackDetails[NPACKEDCANDSMAX]{};
    float packedCandsPtTrk[NPACKEDCANDSMAX]{};
    float packedCandsDzError[NPACKEDCANDSMAX]{};
    float packedCandsDxyError[NPACKEDCANDSMAX]{};
    float packedCandsTimeError[NPACKEDCANDSMAX]{};
    int packedCandsNumberOfHits[NPACKEDCANDSMAX]{};
    int packedCandsNumberOfPixelHits[NPACKEDCANDSMAX]{};
    int packedCandsPixelLayersWithMeasurement[NPACKEDCANDSMAX]{};
    int packedCandsStripLayersWithMeasurement[NPACKEDCANDSMAX]{};
    int packedCandsTrackerLayersWithMeasurement[NPACKEDCANDSMAX]{};
    float packedCandsPseudoTrkPt[NPACKEDCANDSMAX]{};
    float packedCandsPseudoTrkPx[NPACKEDCANDSMAX]{};
    float packedCandsPseudoTrkPy[NPACKEDCANDSMAX]{};
    float packedCandsPseudoTrkPz[NPACKEDCANDSMAX]{};
    float packedCandsPseudoTrkEta[NPACKEDCANDSMAX]{};
    float packedCandsPseudoTrkPhi[NPACKEDCANDSMAX]{};
    int packedCandsPseudoTrkCharge[NPACKEDCANDSMAX]{};
    float packedCandsPseudoTrkVx[NPACKEDCANDSMAX]{};
    float packedCandsPseudoTrkVy[NPACKEDCANDSMAX]{};
    float packedCandsPseudoTrkVz[NPACKEDCANDSMAX]{};
    float packedCandsPseudoTrkChi2Norm[NPACKEDCANDSMAX]{};
    int packedCandsPseudoTrkNumberOfHits[NPACKEDCANDSMAX]{};
    int packedCandsPseudoTrkNumberOfPixelHits[NPACKEDCANDSMAX]{};
    int packedCandsPseudoTrkPixelLayersWithMeasurement[NPACKEDCANDSMAX]{};
    int packedCandsPseudoTrkStripLayersWithMeasurement[NPACKEDCANDSMAX]{};
    int packedCandsPseudoTrkTrackerLayersWithMeasurement[NPACKEDCANDSMAX]{};
    int packedCandsHighPurityTrack[NPACKEDCANDSMAX]{};

    // gen particle vars
    static constexpr size_t NGENPARMAX{1000};
    size_t nGenPar{};
    int genParStatus[NGENPARMAX]{}; 
    float genParEta[NGENPARMAX]{};
    float genParPhi[NGENPARMAX]{};
    float genParE[NGENPARMAX]{};
    float genParPt[NGENPARMAX]{};
    int genParId[NGENPARMAX]{};
    int genParVx[NGENPARMAX]{};
    int genParVy[NGENPARMAX]{};
    int genParVz[NGENPARMAX]{};
    int genParNumMothers[NGENPARMAX]{}; 
    int genParMotherId[NGENPARMAX]{}; 
    int genParMotherIndex[NGENPARMAX]{}; 
    int genParNumDaughters[NGENPARMAX]{};
    int genParDaughterId1[NGENPARMAX]{};
    int genParDaughterId2[NGENPARMAX]{};
    int genParDaughter1Index[NGENPARMAX]{};
    int genParDaughter2Index[NGENPARMAX]{};
    int genParCharge[NGENPARMAX]{};
    // PDF info
    float genPDFScale{};
    float genPDFx1{};
    float genPDFx2{};
    int genPDFf1{};
    int genPDFf2{};
    // CTEQ_6.6 general purpose
    float genCTEQ66_Weight[44]{};
    // MRST98 NLO
    float genMRST2006nnlo_Weight[31]{};

    // basic 4-vectors for photons,taus as we're not interested in them.
    static constexpr size_t NTAUSMAX{20};
    std::map<std::string, int> numTaus;
    std::map<std::string, std::vector<float>> tau_e;
    std::map<std::string, std::vector<float>> tau_phi;
    std::map<std::string, std::vector<float>> tau_eta;
    std::map<std::string, std::vector<float>> tau_pt;

    std::map<std::string, std::map<std::string, std::vector<float>>> bTagRes;
    std::vector<int> triggerRes;
    std::vector<int> metFilterRes;
    std::vector<int> HLT_fakeTriggerValues;

    static constexpr size_t NTRIGGERBITSMAX{700};
    int nTriggerBits{};
    int TriggerBits[NTRIGGERBITSMAX]{};

    float topo_sphericity{};
    float topo_aplanarity{};
    float topo_sphericitye{};
    float topo_aplanaritye{};
    float topo_oblateness{};
    float topo_sqrts{};
    float topo_sqrtse{};
    float topo_ht3{};
    float topo_hte{};
    float topo_ht{};

    int evtRun{};
    int evtnum{};
    float evtlumiblock{};
    int eventCount{};

    int bTags{};
    int softTags{};
};

namespace LHAPDF
{
    enum SetType
    {
        EVOLVE = 0,
        LHPDF = 0,
        INTERPOLATE = 1,
        LHGRID = 1
    };
    enum Verbosity
    {
        SILENT = 0,
        LOWKEY = 1,
        DEFAULT = 2
    };
    void setVerbosity(Verbosity noiselevel);
    void initPDFSet(int nset, const std::string& filename, int member = 0);
    void initPDFSet(const std::string& name,
                    LHAPDF::SetType type,
                    int member = 0);
    void initPDFSet(int nset,
                    const std::string& name,
                    LHAPDF::SetType type,
                    int member = 0);
    int numberPDF(int nset);
    void usePDFMember(int nset, int member);
    void usePDFMember(int member);
    double xfx(int nset, double x, double Q, int fl);
    double xfx(double x, double Q, int fl);
    double getXmin(int nset, int member);
    double getXmax(int nset, int member);
    double getQ2min(int nset, int member);
    double getQ2max(int nset, int member);
    void extrapolate(bool extrapolate = true);
} // namespace LHAPDF

#endif
