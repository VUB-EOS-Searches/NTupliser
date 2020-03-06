#include <array>
#include <iostream>
#include <regex>
#include <string>
#include <vector>

#include <boost/filesystem.hpp>
#include <boost/program_options.hpp>
#include <boost/progress.hpp>
#include <boost/range/iterator_range.hpp>

#include <TChain.h>
#include <TFile.h>
#include <TH1I.h>
#include <TTree.h>

#include "AnalysisEvent.h"

//#define NO_LHE

namespace fs = boost::filesystem;


int main(int argc, char* argv[])
{
    std::vector<std::string> inDirs;
    std::string datasetName;
    bool isMC;

    // Define command-line flags
    namespace po = boost::program_options;
    po::options_description desc("Options");
    desc.add_options()
        ("help,h", "Print this message.")
        ("inDirs,i", po::value<std::vector<std::string>>
         (&inDirs)->multitoken()->required(),
         "Directories in which to look for crab output.")
        ("datasetName,o", po::value<std::string>(&datasetName)->required(),
         "Output dataset name.")
        ("MC", po::bool_switch(&isMC), "Set for MC data.");
    po::variables_map vm;

    // Parse arguments
    try
    {
        po::store(po::parse_command_line(argc, argv, desc), vm);

        if (vm.count("help"))
        {
            std::cout << desc;
            return 0;
        }

        po::notify(vm);
    }
    catch (const po::error& e)
    {
        std::cerr << "ERROR: " << e.what() << std::endl;
        return 1;
    }


    const std::regex mask{".*\\.root"};
    int fileNum{0};

    for (const auto& inDir: inDirs)  // for each input directory
    {
        for (const auto& file:
                boost::make_iterator_range(fs::directory_iterator{inDir}, {}))
        {  // for each file in directory
            const std::string path {file.path().string()};

            if (!fs::is_regular_file(file.status())
                    || !std::regex_match(path, mask))
            {
                continue;  // skip if not a root file
            }

            const std::string numName{std::to_string(fileNum)};
            const std::string numNamePlus{std::to_string(fileNum + 2)};

             if (fs::is_regular_file("/scratch/data/tZqSkimsRun2016/" +
                         datasetName + "/skimFile" + numNamePlus + ".root"))
             {  // don't overwrite existing skim files, except for the last two
                fileNum++;
                continue;
             }

            std::array<unsigned int, 14> summedWeights{};
            TH1I weightHisto{"sumNumPosMinusNegWeights",
                "sumNumPosMinusNegWeights", 7, -3.5, 3.5};

            TChain datasetChain{"makeTopologyNtupleMiniAOD/tree"};
            datasetChain.Add(path.c_str());

            // std::cout << path;
            // TFile inFile(path.c_str());

            TTree * const outTree = datasetChain.CloneTree(0);

            std::string outFilePath{"/scratch/data/tZqSkimsRun2016/"
                + datasetName + "/skimFile" + numName + ".root"};
            TFile outFile{outFilePath.c_str(), "RECREATE"};

            // std::cout << outFilePath << std::endl;

            const long long int numberOfEvents{datasetChain.GetEntries()};
            boost::progress_display progress{numberOfEvents, std::cout,
                outFilePath + "\n"};
            AnalysisEvent event{isMC, "", &datasetChain};

            for (long long int i{0}; i < numberOfEvents; i++)
            {
                ++progress;  // update progress bar (++ must be prefix)

                event.GetEntry(i);

#ifndef NO_LHE
                // Get number of positive and negative amc@nlo weights
                if (isMC)
                {
                    event.origWeightForNorm >= 0.0   ? summedWeights[0]++
                                                     : summedWeights[1]++;
                    event.weight_muF0p5 >= 0.0       ? summedWeights[2]++
                                                     : summedWeights[3]++;
                    event.weight_muR0p5 >= 0.0       ? summedWeights[4]++
                                                     : summedWeights[5]++;
                    event.weight_muF0p5muR0p5 >= 0.0 ? summedWeights[6]++
                                                     : summedWeights[7]++;
                    event.weight_muF2 >= 0.0         ? summedWeights[8]++
                                                     : summedWeights[9]++;
                    event.weight_muR2 >= 0.0         ? summedWeights[10]++
                                                     : summedWeights[11]++;
                    event.weight_muF2muR2 >= 0.0     ? summedWeights[12]++
                                                     : summedWeights[13]++;
                }
#endif
                // Lepton cuts
                int numLeps{0};
                for (int j = 0; j < event.numElePF2PAT; j++)
                {
                    if (event.elePF2PATPT[j] < 9
                            || std::abs(event.elePF2PATEta[j]) > 2.7
                            || event.elePF2PATComRelIsoRho[j] > 0.5)
                    {
                        continue;
                    }
                    numLeps++;
                }
                for (int j = 0; j < event.numMuonPF2PAT; j++)
                {
                    if (event.muonPF2PATPt[j] < 9
                            || std::abs(event.muonPF2PATEta[j]) > 2.8
                            || event.muonPF2PATComRelIsodBeta[j] > 0.5)
                    {
                        continue;
                    }
                    numLeps++;
                }
                if (numLeps >= 2)
                {
                    outTree->Fill();
                }
            }

            if (isMC)
            {
#ifndef NO_LHE
                weightHisto.Fill(0., summedWeights[0] - summedWeights[1]);
                weightHisto.Fill(-1., summedWeights[2] - summedWeights[3]);
                weightHisto.Fill(-2., summedWeights[4] - summedWeights[5]);
                weightHisto.Fill(-3., summedWeights[6] - summedWeights[7]);
                weightHisto.Fill(1., summedWeights[8] - summedWeights[9]);
                weightHisto.Fill(2., summedWeights[10] - summedWeights[11]);
                weightHisto.Fill(3., summedWeights[12] - summedWeights[13]);
#else
                weightHisto.Fill(0., -666.);
                weightHisto.Fill(-1., -666);
                weightHisto.Fill(-2., -666);
                weightHisto.Fill(-3., -666);
                weightHisto.Fill(1., -666);
                weightHisto.Fill(2., -666);
                weightHisto.Fill(3., -666);
#endif
            }

            outFile.cd();
            outTree->Write();
            if (isMC)
            {
                weightHisto.Write();
            }

            outFile.Write();
            outFile.Close();
            // inFile.Close();

            delete outTree;

            fileNum++;

            std::cout << std::endl;
        }
    }
}
