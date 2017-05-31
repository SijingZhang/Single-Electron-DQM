import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.HLTElectronOfflineAnalyzer_cfi import hltElectronOfflineAnalyzer

electronTightIDParams = cms.PSet(
#    d0Cut = cms.untracked.double(0.2),
#    z0Cut = cms.untracked.double(0.5),
    recoCuts = cms.untracked.string(' && '.join([
	"abs(eta) < 2.5",
        ])),
    hltCuts  = cms.untracked.string("abs(eta) < 2.5"),
)

eleTightIDAnalyzer = hltElectronOfflineAnalyzer.clone() # Line 3
eleTightIDAnalyzer.FolderName= "HLT/EG/DistributionsTightID" #fixed!!
eleTightIDAnalyzer.targetParams = electronTightIDParams

hltElectronOfflineAnalyzers = cms.Sequence( # new hltElectronOfflineAnalyzer 
    eleTightIDAnalyzer
)
