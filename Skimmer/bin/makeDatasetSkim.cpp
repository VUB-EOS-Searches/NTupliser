#include "../interface/AnalysisEvent.h"

#include <Compression.h>
#include <TChain.h>
#include <TFile.h>
#include <TH1I.h>
#include <TTree.h>
#include <TLorentzVector.h>
#include <array>
#include <boost/filesystem.hpp>
#include <boost/program_options.hpp>
#include <boost/progress.hpp>
#include <boost/range/iterator_range.hpp>
#include <iostream>
#include <limits>
#include <regex>
#include <string>
#include <vector>

using namespace std::string_literals;
namespace fs = boost::filesystem;

int main(int argc, char* argv[]) {
    TTree::SetMaxTreeSize(std::numeric_limits<Long64_t>::max());

    std::vector<std::string> inDirs;
    std::string datasetName;
    bool isMC {false};
    bool hasLHE {false};
    bool is2016 {false};

    TFile* inFile {nullptr};
    TH1I* generatorWeightPlot {nullptr};

    // Define command-line flags
    namespace po = boost::program_options;
    po::options_description desc("Options");
    desc.add_options()("help,h", "Print this message.")(
        "inDirs,i", po::value<std::vector<std::string>>(&inDirs)->multitoken()->required(), "Directories in which to look for crab output.")(
        "datasetName,o", po::value<std::string>(&datasetName)->required(), "Output dataset name.")(
        "LHE", po::bool_switch(&hasLHE), "Set for data with LHE weights.")(
        "2016", po::bool_switch(&is2016), "Set for 2016 data.")(
        "MC", po::bool_switch(&isMC), "Set for MC data.");
    po::variables_map vm;

    // Parse arguments
    try {
        po::store(po::parse_command_line(argc, argv, desc), vm);

        if (vm.count("help")) {
            std::cout << desc;
            return 0;
        }

        po::notify(vm);
    }
    catch (const po::error& e) {
        std::cerr << "ERROR: " << e.what() << std::endl;
        return 1;
    }

    const std::regex mask{R"(.*\.root)"};
    int fileNum{0};

    for (const auto& inDir : inDirs) { // for each input directory
        for (const auto& file : boost::make_iterator_range(fs::directory_iterator{inDir}, {})) { // for each file in directory
            const std::string path{file.path().string()};

            if (!fs::is_regular_file(file.status()) || !std::regex_match(path, mask))
                continue; // skip if not a root file

            const std::string numName{std::to_string(fileNum)};
//            const std::string numNamePlus{std::to_string(fileNum + 2)};
//            const std::string dataDir{"/vols/cms/adm10/"};

            const std::string outFilePath{datasetName + "/skimFile" + numName + ".root"};

            if (fs::is_regular_file(outFilePath)) { // don't overwrite existing skim files, except for the last two
                fileNum++;
                continue;
            }

            TH1I weightHisto{"sumNumPosMinusNegWeights",  "sumNumPosMinusNegWeights", 7, -3.5, 3.5};

            TChain datasetChain{"makeTopologyNtupleMiniAOD/tree"};
            datasetChain.Add(path.c_str());

            std::cout << path << std::endl;

            if (isMC && hasLHE) {
                inFile = new TFile (path.c_str(), "READ");
                generatorWeightPlot = (TH1I*)inFile->Get("makeTopologyNtupleMiniAOD/weightHisto");
            }

            TFile outFile{outFilePath.c_str(), "RECREATE"};
            outFile.SetCompressionSettings(ROOT::CompressionSettings(ROOT::kLZ4, 4));
            TTree* const outTree = datasetChain.CloneTree(0);

            outTree->SetAutoSave(-std::numeric_limits<Long64_t>::max());

//            std::cout << outFilePath << std::endl;

            const long long int numberOfEvents{datasetChain.GetEntries()};
            boost::progress_display progress(numberOfEvents, std::cout, outFilePath + "\n");
            AnalysisEvent event{isMC, "", &datasetChain, is2016};

            for (long long int i{0}; i < numberOfEvents; i++) {
                ++progress; // update progress bar (++ must be prefix)
                event.GetEntry(i);
                outTree->Fill();
            }

            if (isMC) {
                if (hasLHE) {
                    weightHisto.Fill(0.,  generatorWeightPlot->GetBinContent(1) - generatorWeightPlot->GetBinContent(2));
                    weightHisto.Fill(-1., generatorWeightPlot->GetBinContent(3) - generatorWeightPlot->GetBinContent(4));
                    weightHisto.Fill(-2., generatorWeightPlot->GetBinContent(5) - generatorWeightPlot->GetBinContent(6));
                    weightHisto.Fill(-3., generatorWeightPlot->GetBinContent(7) - generatorWeightPlot->GetBinContent(8));
                    weightHisto.Fill(1.,  generatorWeightPlot->GetBinContent(9) - generatorWeightPlot->GetBinContent(10));
                    weightHisto.Fill(2.,  generatorWeightPlot->GetBinContent(11) - generatorWeightPlot->GetBinContent(12));
                    weightHisto.Fill(3.,  generatorWeightPlot->GetBinContent(13) - generatorWeightPlot->GetBinContent(14));
                }
                else {
                    weightHisto.Fill(0., -666.);
                    weightHisto.Fill(-1., -666);
                    weightHisto.Fill(-2., -666);
                    weightHisto.Fill(-3., -666);
                    weightHisto.Fill(1., -666);
                    weightHisto.Fill(2., -666);
                    weightHisto.Fill(3., -666);
                }
            }

            outTree->FlushBaskets();
            if (isMC) weightHisto.Write();

            outFile.Write();
            outFile.Close();

            inFile->Close();
            inFile = nullptr;

            generatorWeightPlot = nullptr;

            fileNum++;

            std::cout << std::endl;
        }
    }
}
