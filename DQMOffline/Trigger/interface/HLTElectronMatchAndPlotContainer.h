#ifndef DQMOffline_Trigger_HLTElectronMatchAndPlotContainer_H
#define DQMOffline_Trigger_HLTElectronMatchAndPlotContainer_H

/** \class HLTElectronMatchAndPlot
 *  Contanier class to handle vector of reconstructed electrons matched to 
 *  HLT objects used to plot efficiencies.
 *
 *  Note that this is not a true EDAnalyzer; rather, the intent is that one
 *  EDAnalyzer would call an instance  of HLTElectronMatchAndPlotContainer
 *
 *  Documentation available on the CMS TWiki:
 *  https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLTOfflinePerformance
 *
 *  
 *  \author  C. Battilana
 */

// Base Class Headers

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"

#include "DQMOffline/Trigger/interface/HLTElectronMatchAndPlot.h"

#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerEventWithRefs.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Math/interface/deltaR.h"

#include<vector>
#include<string>


//////////////////////////////////////////////////////////////////////////////
///Container Class Definition (this is what is used by the DQM module) ///////

class HLTElectronMatchAndPlotContainer 
{

 public:

  /// Constructor
  HLTElectronMatchAndPlotContainer(edm::ConsumesCollector &&, const edm::ParameterSet &);

  /// Destructor
  ~HLTElectronMatchAndPlotContainer() { plotters_.clear(); };

  /// Add a HLTElectronMatchAndPlot for a given path
  void addPlotter(const edm::ParameterSet &, std::string, std::string, bool);

  // Analyzer Methods
  void beginRun(DQMStore::IBooker &, const edm::Run &, const edm::EventSetup &);
  void analyze(const edm::Event &, const edm::EventSetup &);
  void endRun(const edm::Run &, const edm::EventSetup &);

 private:

  std::vector<HLTElectronMatchAndPlot> plotters_;

  edm::EDGetTokenT<double> rhoToken_;
  edm::EDGetTokenT<reco::ConversionCollection> convsToken_;
  edm::EDGetTokenT<reco::BeamSpot> bsToken_;
  edm::EDGetTokenT<reco::GsfElectronCollection> eleToken_;
  edm::EDGetTokenT<reco::VertexCollection> pvToken_;

  edm::EDGetTokenT<trigger::TriggerEvent> trigSummaryToken_;
  edm::EDGetTokenT<edm::TriggerResults>   trigResultsToken_;
  
};

#endif
 

