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
        "fakeratePhiVsEta 'Trigger Fake Rate; p_{T}^{trigger}; N(unmatched trigger objects) / N(trigger objects)' fakeratePhiVsEta_numer fakeratePhiVsEta_denom",

        "TPefficiencymassZ_EB 'Tag & Probe efficiency; mass; N(tt) / N(tp)' massVsmassZ_EB_numer massVsmassZ_EB_denom",
        "TPefficiencyEtaZ_EB 'Tag & Probe efficiency; #eta; N(tt) / N(tp)' massVsEtaZ_EB_numer massVsEtaZ_EB_denom",
        "TPefficiencyPtZ_EB 'Tag & Probe efficiency; p_{T}; N(tt) / N(tp)' massVsPtZ_EB_numer massVsPtZ_EB_denom",
        "TPefficiencyVertexZ_EB 'Tag & Probe efficiency; NVertex; N(tt) / N(tp)' massVsVertexZ_EB_numer massVsVertexZ_EB_denom",
        "TPefficiencyPhiVsEtaZ_EB 'Tag & Probe efficiency; #Phi#Eta; N(tt) / N(tp)' massVsPhiVsEtaZ_EB_numer massVsPhiVsEtaZ_EB_denom",
        "TPefficiencySigmaIetaIetaZ_EB 'Tag & Probe efficiency; SigmaIetaIeta; N(tt) / N(tp)' massVsSigmaIetaIetaZ_EB_numer massVsSigmaIetaIetaZ_EB_denom",
        "TPefficiencyHoEZ_EB 'Tag & Probe efficiency; HoE; N(tt) / N(tp)' massVsHoEZ_EB_numer massVsHoEZ_EB_denom",
        "TPefficiencyisoPFCorrRelZ_EB 'Tag & Probe efficiency; isoPFCorrRel; N(tt) / N(tp)' massVsisoPFCorrRelZ_EB_numer massVsisoPFCorrRelZ_EB_denom",

	"TPefficiencymassZ_EE 'Tag & Probe efficiency; mass; N(tt) / N(tp)' massVsmassZ_EE_numer massVsmassZ_EE_denom",
        "TPefficiencyEtaZ_EE 'Tag & Probe efficiency; #eta; N(tt) / N(tp)' massVsEtaZ_EE_numer massVsEtaZ_EE_denom",
        "TPefficiencyPtZ_EE 'Tag & Probe efficiency; p_{T}; N(tt) / N(tp)' massVsPtZ_EE_numer massVsPtZ_EE_denom",
        "TPefficiencyVertexZ_EE 'Tag & Probe efficiency; NVertex; N(tt) / N(tp)' massVsVertexZ_EE_numer massVsVertexZ_EE_denom",
        "TPefficiencyPhiVsEtaZ_EE 'Tag & Probe efficiency; #Phi#Eta; N(tt) / N(tp)' massVsPhiVsEtaZ_EE_numer massVsPhiVsEtaZ_EE_denom",
        "TPefficiencySigmaIetaIetaZ_EE 'Tag & Probe efficiency; SigmaIetaIeta; N(tt) / N(tp)' massVsSigmaIetaIetaZ_EE_numer massVsSigmaIetaIetaZ_EE_denom",
        "TPefficiencyHoEZ_EE 'Tag & Probe efficiency; HoE; N(tt) / N(tp)' massVsHoEZ_EE_numer massVsHoEZ_EE_denom",
        "TPefficiencyisoPFCorrRelZ_EE 'Tag & Probe efficiency; isoPFCorrRel; N(tt) / N(tp)' massVsisoPFCorrRelZ_EE_numer massVsisoPFCorrRelZ_EE_denom"
    ),

)

hltElectronPostVal = cms.Sequence(
    hltElectronEfficiencies
)





