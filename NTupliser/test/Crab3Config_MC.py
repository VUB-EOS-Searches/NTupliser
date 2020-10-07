# -*- coding: utf-8 -*-
from collections import namedtuple
from datetime import datetime

from CRABClient.UserUtilities import config

Dataset = namedtuple("Dataset", "process dataset")

## 2017 Datasets

# HToSS
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1",         "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_2017_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_2017_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_ext1",    "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_2017_ext1_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1_2017_ext1_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS1_ctauS10",        "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS10_2017_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS10_2017_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS1_ctauS10_ext1",   "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS10_2017_ext1_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS10_2017_ext1_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS1_ctauS100",       "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS100_2017_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS100_2017_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS1_ctauS100_ext1",  "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS100_2017_ext1_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS100_2017_ext1_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1000",      "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1000_2017_200925_v2/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1000_2017_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1000_ext1", "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1000_2017_ext1_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS1_ctauS1000_2017_ext1_200929-bad2de9deaf599d514e00022b724d349/USER")

#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1",         "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1_2017_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1_2017_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1_ext1",    "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1_2017_ext1_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1_2017_ext1_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS2_ctauS10",        "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS10_2017_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS10_2017_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS2_ctauS10_ext1",   "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS10_2017_ext1_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS10_2017_ext1_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS2_ctauS100",       "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS100_2017_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS100_2017_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS2_ctauS100_ext1",  "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS100_2017_ext1_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS100_2017_ext1_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1000",      "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1000_2017_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1000_2017_200929-bad2de9deaf599d514e00022b724d349/USER")
#dataset = Dataset("HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1000_ext1", "/NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1000_2017_ext1_200925/almorton-CRAB3_PAT_miniAOD_NLO_ggH_HToSS_SmuonHadronFiltered_MH125_MS2_ctauS1000_2017_ext1_200929-bad2de9deaf599d514e00022b724d349/USER")

###############

## tZq
#dataset = Dataset("tZq", "/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
## tZq single lepton
# dataset = Dataset("tZq_Zhad_Wlept", "/tZq_Zhad_Wlept_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## tHq
# dataset = Dataset("tHq", "/THQ_4f_Hincl_13TeV_madgraph_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## tWZ/tWll
# dataset = Dataset("tWz_tWll", "/ST_tWll_5f_LO_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM")
## ttZ
# dataset = Dataset("ttZ_ll", "/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttZ_ll_correctPartonsInBorn", "/TTZToLLNuNu_M-10_TuneCP5_PSweights_correctnPartonsInBorn_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttZ_ll_TuneCP5down", "/TTZToLLNuNu_M-10_TuneCP5down_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttZ_ll_TuneCP5ip", "/TTZToLLNuNu_M-10_TuneCP5up_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttZ_qq", "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("ttZ_qq_ext", "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM")
## ttW
# dataset = Dataset("ttW_lnu", "/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttW_qq", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
## ttH (bb)
# dataset = Dataset("ttH_bb", "/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM"
# ## ttH (non bb)
# dataset = Dataset("ttH_nonbb", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# ttγ
# dataset = Dataset("ttgamma", "/TTGamma_Dilept_TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# W+jets
# dataset = Dataset("Wjets_HT_70To100", "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("Wjets_HT_100_to_200", "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("Wjets_HT_200_to_400", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("Wjets_HT_400_to_600", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("Wjets_HT_600_to_800", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("Wjets_HT_800_to_1200", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("Wjets_HT_1200_to_2500", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("Wjets_HT_2500_to_inf", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM")
## W+jets alt.
# dataset = Dataset("Wjets_v3", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM")
# dataset = Dataset("Wjets_v2", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("Wjets_v2_ext1", "/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM")
## WW (2l2nu)
# dataset = Dataset("WW_2l2nu",             "/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM")
# dataset = Dataset("WW_2l2nu_TuneCP5Down", "/WWTo2L2Nu_NNPDF31_TuneCP5Down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM")
# dataset = Dataset("WW_2l2nu_TuneCP5Up",   "/WWTo2L2Nu_NNPDF31_TuneCP5Up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM")
## WW (lnu2q)
# dataset = Dataset("WW_lnu2q", "/WWToLNuQQ_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM")
## WZ (3lnu + up to 1 jet)
# dataset = Dataset("WZ_3lnu", "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## WZ (2l2q)
# dataset = Dataset("WZ_2l2q", "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## WZ (lnu2q)
# dataset = Dataset("WZ_lnu2q", "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("WZ_l3nu",  "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8_v2/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## ZZ (4l)
# dataset = Dataset("ZZ_4l", "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## ZZ (2l2nu)
# dataset = Dataset("ZZ_2l2nu", "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## ZZ (2l2q)
# dataset = Dataset("ZZ_2l2q", "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## WWW
# dataset = Dataset("WWW", "/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
## WWZ
# dataset = Dataset("WWZ", "/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
## WZZ
# dataset = Dataset("WZZ", "WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## ZZZ
# dataset = Dataset("ZZZ", "/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
## ttjets  (2l2v) (aMC@NLO)
# dataset = Dataset("ttjets_2l2v", "/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## ttbar
# dataset = Dataset("ttbar_hadronic", "/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttbar_hadronic_TuneCP5down", "/TTToHadronic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("ttbar_hadronic_TuneCP5up", "/TTToHadronic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttbar_hadronic_hdampDOWN, "/TTToHadronic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttbar_hadronic_hdampUP", "/TTToHadronic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("ttbar_semileptonic", "/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("ttbar_semileptonic_TuneCP5down", "/TTToSemiLeptonic_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("ttbar_semileptonic_TuneCP5up", "/TTToSemiLeptonic_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("ttbar_semileptonic_hdampDOWN", "/TTToSemiLeptonic_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("ttbar_semileptonic_hdampUP", "/TTToSemiLeptonic_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("ttbar_2l2v", "/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("ttbar_2l2v_TuneCP5down", "/TTTo2L2Nu_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttbar_2l2v_TuneCP5up", "/TTTo2L2Nu_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttbar_2l2v_hdampDOWN", "/TTTo2L2Nu_hdampDOWN_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ttbar_2l2v_hdampUP", "/TTTo2L2Nu_hdampUP_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## tW
# dataset = Dataset("tW", "/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("tW_TuneCP5down", "/ST_tW_top_5f_inclusiveDecays_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("tW_TuneCP5up", "/ST_tW_top_5f_inclusiveDecays_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## tbarW
# dataset = Dataset("tbarW", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("tbarW_scale_up", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("tbarW_scale_down", "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## t s-channel
# dataset = Dataset("ST_s_channel", "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("ST_s_channel_correctnPartonsInBorn", "/ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_correctnPartonsInBorn/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
#dataset = Dataset("ST_s_channel_TuneCP5down", "/ST_s-channel_4f_leptonDecays_TuneCP5down_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
#dataset = Dataset("ST_s_channel_TuneCP5up", "/ST_s-channel_4f_leptonDecays_TuneCP5up_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# t t-channel
# dataset = Dataset("t_t_channel", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("t_t_channel_TuneCP5down", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("t_t_channel_TuneCP5up", "/ST_t-channel_top_4f_InclusiveDecays_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("t_t_channel_hdampdown", "/ST_t-channel_top_4f_hdampdown_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("t_t_channel_hdampup", "/ST_t-channel_top_4f_hdampup_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
## tbar t-channel
# dataset = Dataset("tbar_t_channel", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("tbar_t_channel_TuneCP5down", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5down_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("tbar_t_channel_TuneCP5up", "/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5up_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("tbar_t_channel_hdampdown", "/ST_t-channel_antitop_4f_hdampdown_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("tbar_t_channel_hdampup", "/ST_t-channel_antitop_4f_hdampup_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# Zjets
# dataset = Dataset("DYJetsToLL_M-10to50", "/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_ext1", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM")
# Zjets ht binned
# dataset = Dataset("DYJetsToLL_M-50_HT-40to70", "/DYJetsToLL_M-50_HT-40to70_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-70to100", "/DYJetsToLL_M-50_HT-70to100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-100to200", "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-100to200_ext1", "/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-200to400", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-200to400_ext1", "/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-400to600", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-400to600_ext1", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-600to800", "/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-800to1200", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-1200to2500", "/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_M-50_HT-2500toInf", "/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM")
# Zjets pt binned
# dataset = Dataset("DYJetsToLL_Pt_0To50",    "/DYJetsToLL_Pt-0To50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")### CURRENTLY NOT VALID BUT PRODUCTION
# dataset = Dataset("DYJetsToLL_Pt-50To100",  "/DYJetsToLL_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_Pt-100To250", "/DYJetsToLL_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_Pt-250To400", "/DYJetsToLL_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_Pt-400To650", "/DYJetsToLL_Pt-400To650_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("DYJetsToLL_Pt-650ToInf", "/DYJetsToLL_Pt-650ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")

# WG?
# dataset = Dataset("WG_lnug", "/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# ZG?
# dataset = Dataset("ZG_llg","/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM")

# QCD MuEnrichedPt15
# dataset = Dataset("QCD_Pt-20toInf_MuEnrichedPt15", "/QCD_Pt-20toInf_MuEnrichedPt15_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")

# QCD MuEnrichedPt5
# dataset = Dataset("QCD_Pt-15to20_MuEnrichedPt5", "/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-20to30_MuEnrichedPt5", "/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-30to50_MuEnrichedPt5", "/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-50to80_MuEnrichedPt5", "/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-80to120_MuEnrichedPt5", "/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-120to170_MuEnrichedPt5", "/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-170to300_MuEnrichedPt5", "/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-300to470_MuEnrichedPt5", "/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-470to600_MuEnrichedPt5", "/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-600to800_MuEnrichedPt5", "/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-800to1000_MuEnrichedPt5", "/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")
# dataset = Dataset("QCD_Pt-1000toInf_MuEnrichedPt5", "/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM")

time = datetime.now().strftime("%Y%m%d%H%M%S")

config = config()

config.General.requestName = '{}_{}'.format(dataset.process, time)
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'nTupliserMC_miniAOD_cfg.py'

config.Data.inputDataset = dataset.dataset
#config.Data.inputDBS = 'phys03' ## private production MC
config.Data.inputDBS = 'global' ## normal centrally generated MC

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/almorton/MC/nTuples/'

config.Data.publication = False
config.Data.outputDatasetTag = "CRAB3_MC_nTupilisation_{}_{}".format(dataset.process, time)

config.Data.allowNonValidInputDataset = False

config.Site.storageSite = 'T2_BE_IIHE' #T2_UK_London_IC, T2_UK_London_Brunel, T2_BE_IIHE
#config.Site.blacklist = ['T2_UK_London_Brunel']

