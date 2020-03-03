import FWCore.ParameterSet.Config as cms

GenInfoMiniAOD = cms.EDAnalyzer('GenInfoMiniAOD',
					   isLHEflag = cms.bool(True),
					   externalLHEToken = cms.InputTag("externalLHEProducer"), # "externalLHEProducer", "source" for THQ 

					   pdfIdStart = cms.int32(1779),
					   pdfIdEnd = cms.int32(1879),
					   hasAlphaWeightFlag = cms.bool(True),
					   alphaIdStart = cms.int32(1880),
					   alphaIdEnd = cms.int32(1881),

                                           )# end of GenInfoMiniAOD
