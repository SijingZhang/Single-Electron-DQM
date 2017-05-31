import FWCore.ParameterSet.Config as cms

jetMETHLTOfflineClientAK4 = cms.EDAnalyzer("JetMETHLTOfflineClient",

                                 processname = cms.string("HLT"),
                                 DQMDirName=cms.string("HLT/JetMET"),
                                 hltTag = cms.string("HLT")

)

jetMETHLTOfflineClientAK4 = cms.EDAnalyzer("DQMGenericClient",
    subDirs        = cms.untracked.vstring("HLT/JetMET/*"),
    verbose        = cms.untracked.uint32(0), # Set to 2 for all messages
    resolution     = cms.vstring(),
    efficiency     = cms.vstring(
"ME_EfficiencyEta                  'efficiency vs eta;           eta; efficiency'                     ME_NumeratorEta                   ME_DenominatorEta                              ",
"ME_EfficiencyEtaBarrel            'efficiency vs eta (barrel);  eta; efficiency'                     ME_NumeratorEtaBarrel             ME_DenominatorEtaBarrel                        ",
"ME_EfficiencyEtaEndcap            'efficiency vs eta (endcap);  eta; efficiency'                     ME_NumeratorEtaEndcap             ME_DenominatorEtaEndcap                        ",
"ME_EfficiencyEtaForward           'efficiency vs eta (forward); eta; efficiency'                     ME_NumeratorEtaForward            ME_DenominatorEtaForward                       ",
"ME_EfficiencyEtaPhi               'efficiency vs eta-phi; eta; phi [rad]; efficiency'                ME_NumeratorEtaPhi                ME_DenominatorEtaPhi                           ",
"ME_EfficiencyEtaPhi_HighpTcut     'efficiency vs eta-phi (high p_{T}); eta; phi [rad]; efficiency'   ME_NumeratorEtaPhi_HighpTcut      ME_DenominatorEtaPhi_HighpTcut                 ",
"ME_EfficiencyEtaPhi_LowpTcut      'efficiency vs eta-phi (low p_{T});  eta; phi [rad]; efficiency'   ME_NumeratorEtaPhi_LowpTcut       ME_DenominatorEtaPhi_LowpTcut                  ",
"ME_EfficiencyEtaPhi_MedpTcut      'efficiency vs eta-phi (med p_{T});  eta; phi [rad]; efficiency'   ME_NumeratorEtaPhi_MedpTcut       ME_DenominatorEtaPhi_MedpTcut                  ",
"ME_EfficiencyEta_HighpTcut        'efficiency vs eta (high p_{T}); eta; efficiency'                  ME_NumeratorEta_HighpTcut         ME_DenominatorEta_HighpTcut                    ",
"ME_EfficiencyEta_LowpTcut         'efficiency vs eta (low p_{T});  eta; efficiency'                  ME_NumeratorEta_LowpTcut          ME_DenominatorEta_LowpTcut                     ",
"ME_EfficiencyEta_MedpTcut         'efficiency vs eta (med p_{T});  eta; efficiency'                  ME_NumeratorEta_MedpTcut          ME_DenominatorEta_MedpTcut                     ",
"ME_EfficiencyPhi                  'efficiency vs phi;              #phi [rad]; efficiency'           ME_NumeratorPhi                   ME_DenominatorPhi                              ",
"ME_EfficiencyPhiBarrel            'efficiency vs phi (barrel);     #phi [rad]; efficiency'           ME_NumeratorPhiBarrel             ME_DenominatorPhiBarrel                        ",
"ME_EfficiencyPhiEndcap            'efficiency vs phi (endcap);     #phi [rad]; efficiency'           ME_NumeratorPhiEndcap             ME_DenominatorPhiEndcap                        ",
"ME_EfficiencyPhiForward           'efficiency vs phi (forward);    #phi [rad]; efficiency'           ME_NumeratorPhiForward            ME_DenominatorPhiForward                       ",
"ME_EfficiencyPhi_HighpTcut        'efficiency vs phi (high p_{T}); #phi [rad]; efficiency'           ME_NumeratorPhi_HighpTcut         ME_DenominatorPhi_HighpTcut                    ",
"ME_EfficiencyPhi_LowpTcut         'efficiency vs phi (low p_{T});  #phi [rad]; efficiency'           ME_NumeratorPhi_LowpTcut          ME_DenominatorPhi_LowpTcut                     ",
"ME_EfficiencyPhi_MedpTcut         'efficiency vs phi (med p_{T});  #phi [rad]; efficiency'           ME_NumeratorPhi_MedpTcut          ME_DenominatorPhi_MedpTcut                     ",
"ME_EfficiencyPt                   'efficiency vs p_{T};           p_{T} [GeV]; efficiency'           ME_NumeratorPt                    ME_DenominatorPt                               ",
"ME_EfficiencyPtBarrel             'efficiency vs p_{T} (barrel);  p_{T} [GeV]; efficiency'           ME_NumeratorPtBarrel              ME_DenominatorPtBarrel                         ",
"ME_EfficiencyPtEndcap             'efficiency vs p_{T} (endcap);  p_{T} [GeV]; efficiency'           ME_NumeratorPtEndcap              ME_DenominatorPtEndcap                         ",
"ME_EfficiencyPtForward            'efficiency vs p_{T} (forward); p_{T} [GeV]; efficiency'           ME_NumeratorPtForward             ME_DenominatorPtForward                        ",
    ),
    efficiencyProfile = cms.untracked.vstring(
    ),
  
)

jetMETHLTOfflineClientAK8 = jetMETHLTOfflineClientAK4.clone( DQMDirName = cms.string('HLT/JetMET/AK8'))
jetMETHLTOfflineClientAK8 = jetMETHLTOfflineClientAK4.clone( subDirs = cms.untracked.vstring('HLT/JetMET/AK8/*'))

jetMETHLTOfflineClient = cms.Sequence( jetMETHLTOfflineClientAK4 * jetMETHLTOfflineClientAK8 )
