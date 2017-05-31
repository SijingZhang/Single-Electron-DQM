import FWCore.ParameterSet.Config as cms

hltElectronOfflineAnalyzer = cms.EDAnalyzer("HLTElectronOfflineAnalyzer",

    ## Used when fetching triggerSummary and triggerResults
    hltProcessName = cms.string("HLT"),

    ## Location of plots in DQM
    FolderName = cms.string("HLT/EG/Distributions/TightIDElectrons"),
#    destination = cms.untracked.string("HLT/EG/Distributions/TightIDElectrons"),

    ## HLT paths passing any one of these regular expressions will be included
    hltPathsToCheck = cms.vstring(
      "HLT_Ele32_eta2p1_WPTight_Gsf_v8",
      "HLT_Ele32_WPTight_Gsf_v1",
    ),

    ## All input tags are specified in this pset for convenience
    inputTags = cms.PSet(
    	electrons = cms.InputTag("gedGsfElectrons"), 
        rho            = cms.InputTag("fixedGridRhoFastjetAll"), # step3.root(event)
        convs          = cms.InputTag("allConversions"), #conversions
        beamSpot       = cms.InputTag("offlineBeamSpot"),
        offlinePVs     = cms.InputTag("offlinePrimaryVertices"),
        triggerSummary = cms.InputTag("hltTriggerSummaryAOD"),
       triggerResults = cms.InputTag("TriggerResults")
    ),

     # generic trigger event flag
# defination in "DataFormats/Scalers/interface/DcsStatus.h"
    genericTriggerEventDCSPSet = cms.PSet(
        andOr         = cms.bool( False ),
        dcsInputTag   = cms.InputTag( "scalersRawToDigi" ),
#        dcsPartitions = cms.vint32 ( 24, 25, 26, 27, 28, 29 ), # 24-27: strip, 28-29: pixel, we should add all other detectors !
        dcsPartitions = cms.vint32 ( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 20, 22, 24, 25, 26, 27, 28, 29, 30, 31 ), # 0-3:EB,EE, 24-27: strip, 28-29: pixel, 30-31:ES, we should add all other detectors !
        andOrDcs      = cms.bool( False ),
        errorReplyDcs = cms.bool( True ),
        verbosityLevel = cms.uint32(1),
    ),

    ## Both 1D and 2D plots use the binnings defined here
    binParams = cms.untracked.PSet(
        ## parameters for fixed-width plots
        NVertex    = cms.untracked.vdouble( 20,  1,   50),
        eta        = cms.untracked.vdouble( 30,  -3.,     3.  ),
        phi        = cms.untracked.vdouble( 20,  -3.14,   3.14),
#        z0         = cms.untracked.vdouble( 10, -15.00,  15.00),
#        d0         = cms.untracked.vdouble( 10,  -0.50,   0.50),
        zMass      = cms.untracked.vdouble( 50,  65.00, 115.00),
#        jpsiMass   = cms.untracked.vdouble( 60,   0.00,   6.00),
        charge     = cms.untracked.vdouble(  2,  -2.00,   2.00),
        deltaR     = cms.untracked.vdouble( 20,   0.00,   0.05),
        phiCoarse  = cms.untracked.vdouble( 10,  -3.14,   3.14),
        resolutionRel = cms.untracked.vdouble( 40,  -0.30,   0.30),
        resolutionEta = cms.untracked.vdouble( 20,  -0.01,   0.01),
        resolutionPhi = cms.untracked.vdouble( 20,  -0.01,   0.01),
        ## parameters for variable-width plots
        etaCoarse = cms.untracked.vdouble(-3.0,-2.5, -2.1, -1.6, -1.2, -0.8, 0.0,
                                           0.8,  1.2,  1.6,  2.1,  2.5, 3.0),
        ptCoarse = cms.untracked.vdouble(10.0, 20.0, 40.0, 60.0, 80.0, 100.0, 200.0),
        pt = cms.untracked.vdouble(  0.0,   2.0,   4.0, 
                                     6.0,   8.0,  10.0, 
                                    20.0,  30.0,  40.0, 
                                   100.0, 200.0, 400.0),
    ),
#
    ## These parameters define which objects are used to fill plots
    plotCuts = cms.PSet(
        ## not applied on eta plots
        maxEta = cms.untracked.double(2.5),
        ## only fill plots for muons with pt > ceil(hltThreshold * minPtFactor)
        ## ex: for HLT_Mu17, ceil(17 * 1.2 ) = 21, so we require pT > 21
        minPtFactor = cms.untracked.double(1.20),
        ## deltaR cuts
#        L1DeltaR = cms.untracked.double(0.30),
#        L2DeltaR = cms.untracked.double(0.30),
#        L3DeltaR = cms.untracked.double(0.05),
        DeltaR = cms.untracked.double(0.30),
    ),

    ## Only events passing all these triggers will be considered
    requiredTriggers = cms.untracked.vstring(),
    effAreasConfigFile = cms.FileInPath("RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt"),
    ## This collection is used to fill most distributions
    targetParams = cms.PSet(
        ## The d0 and z0 cuts are required for the inner track of the
        ## reco muons, taken with respect to the beamspot
#        d0Cut = cms.untracked.double(2.0),
#        z0Cut = cms.untracked.double(25.0),
        ## cuts
#        recoCuts = cms.untracked.string("abs(eta) < 3.0"),
#        hltCuts  = cms.untracked.string("abs(eta) < 2.5"),
        recoCuts = cms.untracked.string("abs(eta) < 2.5"),
        hltCuts  = cms.untracked.string("abs(eta) < 2.5"),
    ),
#
    ## If this PSet is empty, then no "tag and probe" plots are produced;
    ## the cuts used for the tags are specified by targetParams
    probeParams = cms.PSet(
        ## The d0 and z0 cuts are required for the inner track of the
        ## reco muons, taken with respect to the beamspot
#        d0Cut = cms.untracked.double(2.0),
#        z0Cut = cms.untracked.double(25.0),
        ## cuts
#        recoCuts = cms.untracked.string("abs(eta) < 2.1"),
        recoCuts = cms.untracked.string("abs(eta) < 2.5"),
        hltCuts  = cms.untracked.string("abs(eta) < 2.5"),
    ),

    ## Working Poingt 80% selection criteria
#        recoCuts = cms.untracked.string("(isEB && full5x5_sigmaIetaIeta < 0.00998 && fabs(deltaEtaSeedClusterTrackAtVtx) < 0.00308 && abs(deltaPhiSuperClusterTrackAtVtx) < 0.0816 && H_E < 0.0414 &&  < 0.0588 && EInverseMinusPInverse < 0.0129 && mHits <= 1 && isPassConveVeto ) 
#	  ||   ( isEE && full5x5_sigmaIetaIeta < 0.0292 && fabs(EtaSeedClusterTrackAtVtx) < 0.00605 && abs    (dPhiSuperClusterTrackAtVtx) < 0.0394 && H_E < 0.0641 && EInverseMinusPInverse < 0.0129 && mHits <= 1 && isPassConveVeto )"),
#	  isoPFValueCorr< 0.0588 // for EB
#	  isoPFValueCorr< 0.0571 // for EE

)
