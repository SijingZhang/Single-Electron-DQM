import FWCore.ParameterSet.Config as cms

hltElectronEfficiencies = cms.EDAnalyzer("DQMGenericClient",

    subDirs        = cms.untracked.vstring("HLT/EG/Distributions.*"),
    verbose        = cms.untracked.uint32(0), # Set to 2 for all messages
    outputFileName = cms.untracked.string(''),
    commands       = cms.vstring(),
    resolution     = cms.vstring(),
    efficiency     = cms.vstring(
        "efficiencyPhiVsEta 'Efficiency to Match Reco Electrons to Trigger Objects; #eta^{reco}; #phi^{reco}' efficiencyPhiVsEta_numer efficiencyPhiVsEta_denom",
    ),

    efficiencyProfile = cms.untracked.vstring(
        "efficiencyVertex 'Efficiency to Match Reco Electrons to Trigger Objects; NVertex^{reco}; N(ele matched to trigger object) / N(ele)' efficiencyVertex_numer efficiencyVertex_denom",
        "efficiencyEta 'Efficiency to Match Reco Electrons to Trigger Objects; #eta^{reco}; N(ele matched to trigger object) / N(ele)' efficiencyEta_numer efficiencyEta_denom",
        "efficiencyPhi 'Efficiency to Match Reco Electrons to Trigger Objects; #phi^{reco}; N(ele matched to trigger object) / N(ele)' efficiencyPhi_numer efficiencyPhi_denom",
        "efficiencyTurnOn 'Efficiency to Match Reco Electrons to Trigger Objects; p_{T}^{reco}; N(ele matched to trigger object) / N(ele)' efficiencyTurnOn_numer efficiencyTurnOn_denom",
#        "efficiencyD0 'Efficiency to Match Reco Electrons to Trigger Objects; d0^{reco}; N(ele matched to trigger object) / N(ele)' efficiencyD0_numer efficiencyD0_denom",
#        "efficiencyZ0 'Efficiency to Match Reco Electrons to Trigger Objects; z0^{reco}; N(ele matched to trigger object) / N(ele)' efficiencyZ0_numer efficiencyZ0_denom",
        "efficiencyCharge 'Efficiency to Match Reco Electrons to Trigger Objects; q^{reco}; N(ele matched to trigger object) / N(ele)' efficiencyCharge_numer efficiencyCharge_denom",
        "fakerateVertex 'Trigger Fake Rate; NVertex^{trigger}; N(unmatched trigger objects) / N(trigger objects)' fakerateVertex_numer fakerateVertex_denom",
        "fakerateEta 'Trigger Fake Rate; #eta^{trigger}; N(unmatched trigger objects) / N(trigger objects)' fakerateEta_numer fakerateEta_denom",
        "fakeratePhi 'Trigger Fake Rate; #phi^{trigger}; N(unmatched trigger objects) / N(trigger objects)' fakeratePhi_numer fakeratePhi_denom",
        "fakerateTurnOn 'Trigger Fake Rate; p_{T}^{trigger}; N(unmatched trigger objects) / N(trigger objects)' fakerateTurnOn_numer fakerateTurnOn_denom",
        "TPefficiencyEtaZ 'Tag & Probe efficiency; #eta; N(tt) / N(tp)' massVsEtaZ_numer massVsEtaZ_denom",
        "TPefficiencyPtZ 'Tag & Probe efficiency; p_{T}; N(tt) / N(tp)' massVsPtZ_numer massVsPtZ_denom",
        "TPefficiencyVertexZ 'Tag & Probe efficiency; NVertex; N(tt) / N(tp)' massVsVertexZ_numer massVsVertexZ_denom"
    ),

)

hltElectronPostVal = cms.Sequence(
    hltElectronEfficiencies
)





