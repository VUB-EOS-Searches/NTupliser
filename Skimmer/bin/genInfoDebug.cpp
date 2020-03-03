#include "../interface/GenInfoEvent.h"

#include <TChain.h>
#include <TFile.h>
#include <TH1I.h>
#include <TTree.h>
#include <array>
#include <boost/filesystem.hpp>
#include <boost/program_options.hpp>
#include <boost/progress.hpp>
#include <boost/range/iterator_range.hpp>
#include <iostream>
#include <regex>
#include <string>
#include <vector>

namespace fs = boost::filesystem;

int main(int argc, char* argv[])
{
    std::vector<std::string> inDirs;
    std::string datasetName;

    // Define command-line flags
    namespace po = boost::program_options;
    po::options_description desc("Options");
    desc.add_options()("help,h", "Print this message.")(
        "inDirs,i",
        po::value<std::vector<std::string>>(&inDirs)->multitoken()->required(),
        "Directories in which to look for crab output.");
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

    const std::regex mask{R"(.*\.root)"};

    std::array<unsigned int, 14> summedWeights{};

    for (const auto& inDir : inDirs) // for each input directory
    {
        for (const auto& file :
             boost::make_iterator_range(fs::directory_iterator{inDir}, {}))
        { // for each file in directory
            const std::string path{file.path().string()};

            if (!fs::is_regular_file(file.status())
                || !std::regex_match(path, mask))
            {
                continue; // skip if not a root file
            }

            TChain datasetChain{"GenInfoMiniAOD/tree"};
            datasetChain.Add(path.c_str());

            const long long int numberOfEvents{datasetChain.GetEntries()};
            GenInfoEvent event{"", &datasetChain};

            for (long long int i{0}; i < numberOfEvents; i++)
            {
                event.GetEntry(i);

                // Get number of positive and negative amc@nlo weights
                event.origWeightForNorm >= 0.0 ? summedWeights[0]++
                                               : summedWeights[1]++;
                event.weight_muF0p5 >= 0.0 ? summedWeights[2]++
                                           : summedWeights[3]++;
                event.weight_muR0p5 >= 0.0 ? summedWeights[4]++
                                           : summedWeights[5]++;
                event.weight_muF0p5muR0p5 >= 0.0 ? summedWeights[6]++
                                                 : summedWeights[7]++;
                event.weight_muF2 >= 0.0 ? summedWeights[8]++
                                         : summedWeights[9]++;
                event.weight_muR2 >= 0.0 ? summedWeights[10]++
                                         : summedWeights[11]++;
                event.weight_muF2muR2 >= 0.0 ? summedWeights[12]++
                                             : summedWeights[13]++;
            }
        }

        std::cout << std::endl;
    }

    // Print output
    std::cout << "sum of all the positive weights: " << summedWeights[0]
              << std::endl;
    std::cout << "sum of all the negative weights: " << summedWeights[1]
              << std::endl;
}
