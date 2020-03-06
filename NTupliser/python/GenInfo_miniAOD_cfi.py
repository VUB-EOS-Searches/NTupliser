import FWCore.ParameterSet.Config as cms

GenInfoMiniAOD = cms.EDAnalyzer('GenInfoMiniAOD',
					   isLHEflag = cms.bool(True),
					   externalLHEToken = cms.InputTag("externalLHEProducer"), # "externalLHEProducer", "source" for THQ 

					   pdfIdStart = cms.int32(2001),
					   pdfIdEnd = cms.int32(2100),
					   hasAlphaWeightFlag = cms.bool(True),
					   alphaIdStart = cms.int32(2101),
					   alphaIdEnd = cms.int32(2102),

                                           )# end of GenInfoMiniAOD
