brunel-nTuples
==============

ntupliser for brunel group

the famous ntupliser passed down from one generation of brunel phd student to
the next. all our marks left indelibly on it, if no other reason than that the
next guy has no idea what we did.

enjoy, future students.

***

The CMSSW_9_4_8 branch contains code from CMSSW_8_0_25 branch which is modified
to work for Run 2 miniAODv2 94X data and MC. 

This is currently a work in progress left to be completed by the next generation.

Added since last version (8_0_27):
- Muon ID/Iso/etc bools
- Electron VIDs (see below under to be fixed)
- DeepCSV and DeepCMVA added to bTagger list

To be fixed:

- Check DeepCSV and DeepCMVA b-taggers actually work and include them in the skimmer's AnalysisEvent.h

## Additional setup info:

NOTE!!!! YOU DO NOT HAVE TO DO THIS!!!
Only if you want to recreate the EGM regression/smearing corrections that are already in the re-miniAODv2
```bash
git cms-merge-topic cms-egamma:EgammaPostRecoTools_940 #just adds in an extra file to have a setup function to make things easier
git cms-merge-topic cms-egamma:Egamma80XMiniAODV2_946 #adds the c++ changes necessary to enable 2016 scale & smearing corrections
```

***

#EXO - event generation
To get the generation package (including generation of cards):
```bash
git clone git@github.com:cms-sw/genproductions.git genproductions
```

The Higgs (gluon fusion produced) decay via scalars are found in bin/Powheg/production/2017/13TeV/Higgs/gg_H_quark-mass-effects_NNPDF31_13TeV and in
https://github.com/cms-sw/genproductions/tree/master/bin/Powheg/production/pre2017/13TeV/gg_H_quark-mass-effects_JHUGenV628_HWWLNuQQ_NNPDF30_13TeV

---

