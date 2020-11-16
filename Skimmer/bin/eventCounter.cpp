#include <TChain.h>
#include <boost/filesystem.hpp>
#include <boost/range/iterator_range.hpp>
#include <iostream>
#include <regex>

namespace fs = boost::filesystem;

int main(int argc, char* argv[])
{
    const std::regex mask{R"(.*\.root)"};
    TChain datasetChain{"makeTopologyNtupleMiniAOD/tree"};

    for (int i{1}; i < argc; i++)
    { // for each directory given on the command line
        const std::string inDir{argv[i]};

        for (const auto& file :
             boost::make_iterator_range(fs::directory_iterator{inDir}, {}))
        { // for each file
            if (!fs::is_regular_file(file.status())
                || !std::regex_match(file.path().string(), mask))
            {
                continue; // skip if not a root file
            }

            datasetChain.Add(file.path().string().c_str());
        }
    }

    std::cout << "Found " << datasetChain.GetEntries() << " events."
              << std::endl;
}
