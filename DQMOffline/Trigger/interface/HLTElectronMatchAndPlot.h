#ifndef DQMOffline_Trigger_HLTElectronMatchAndPlot_H
#define DQMOffline_Trigger_HLTElectronMatchAndPlot_H


/** \class HLTElectronMatchAndPlot
 *  Match reconstructed muons to HLT objects and plot efficiencies.
 *
 *  Note that this is not a true EDAnalyzer;
 *
 *  Documentation available on the CMS TWiki:
 *  https://twiki.cern.ch/twiki/bin/view/CMS/MuonHLTOfflinePerformance
 *
 *  
 *  \author  J. Slaunwhite, Jeff Klukas
 */

// Base Class Headers

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/Common/interface/Handle.h"

#include "DQMServices/Core/interface/DQMStore.h"
#include "DQMServices/Core/interface/MonitorElement.h"

#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/HLTReco/interface/TriggerEventWithRefs.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/BeamSpot/interface/BeamSpot.h"
#include "DataFormats/Math/interface/deltaR.h"

#include "PhysicsTools/SelectorUtils/interface/CutApplicatorWithEventContentBase.h"
#include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
#include "DataFormats/EgammaCandidates/interface/Conversion.h"
#include "RecoEgamma/EgammaTools/interface/ConversionTools.h"
#include "RecoEgamma/EgammaTools/interface/EffectiveAreas.h"

#include "CommonTools/Utils/interface/StringCutObjectSelector.h"

#include <vector>
#include "TFile.h"
#include "TNtuple.h"
#include "TString.h"
#include "TPRegexp.h"


//////////////////////////////////////////////////////////////////////////////
//////// Typedefs and Constants //////////////////////////////////////////////

typedef math::XYZTLorentzVector LorentzVector;

const double NOMATCH = 999.;
const std::string EFFICIENCY_SUFFIXES[2] = {"denom", "numer"};


//////////////////////////////////////////////////////////////////////////////
//////// HLTElectronMatchAndPlot Class Definition ////////////////////////////////

class HLTElectronMatchAndPlot 
{

 public:

  /// Constructor
  HLTElectronMatchAndPlot(const edm::ParameterSet &, std::string,std::string, bool);

  // Analyzer Methods
  void beginRun(DQMStore::IBooker &, const edm::Run &, const edm::EventSetup &);
  void analyze(edm::Handle<reco::GsfElectronCollection> &, edm::Handle<double> &, 
      	       edm::Handle<reco::ConversionCollection> &, edm::Handle<reco::BeamSpot> &, 
	       edm::Handle<reco::VertexCollection> &, edm::Handle<trigger::TriggerEvent> &, 
	       edm::Handle<edm::TriggerResults> &);
  void endRun(const edm::Run &, const edm::EventSetup &);

  // Helper Methods
  void fillEdges(size_t & nBins, float * & edges, const std::vector<double>& binning);
  template <class T> void 
    fillMapFromPSet(std::map<std::string, T> &, const edm::ParameterSet&, std::string);
  template <class T1, class T2> std::vector<size_t> 
    matchByDeltaR(const std::vector<T1> &, const std::vector<T2> &, 
                  const double maxDeltaR = NOMATCH);
  
 private:

  // Internal Methods
  void book1D(DQMStore::IBooker &, std::string, std::string, std::string);
  void book2D(DQMStore::IBooker &, std::string, std::string, std::string, std::string);
  reco::GsfElectronCollection selectedElectrons(
    const reco::GsfElectronCollection &,
    const reco::BeamSpot &,
    bool,    
    const StringCutObjectSelector<reco::GsfElectron> &);

  trigger::TriggerObjectCollection selectedTriggerObjects(
    const trigger::TriggerObjectCollection &,
    const trigger::TriggerEvent &,
    bool hasTriggerCuts,
    const StringCutObjectSelector<trigger::TriggerObject> triggerSelector);

  
  // Input from Configuration File
  std::string hltProcessName_;
  std::string folderName_;
  std::vector<std::string> requiredTriggers_;
  std::map<std::string, std::vector<double> > binParams_;
  std::map<std::string, double> plotCuts_;
  edm::ParameterSet targetParams_;
  edm::ParameterSet probeParams_;

  // Member Variables
  std::string triggerLevel_;
  unsigned int cutMinPt_;
  std::string hltPath_;
  std::string moduleLabel_;
  bool isLastFilter_;
  std::map<std::string, MonitorElement *> hists_;
  
  // Selectors
  bool hasTargetRecoCuts;                                                                                                                                                                                                                                                    
  bool hasProbeRecoCuts;
    
  StringCutObjectSelector<reco::GsfElectron> targetElectronSelector_;
//  double targetZ0Cut_; 
//  double targetD0Cut_;
  double targetptCutZ_;
//  double targetptCutJpsi_;
  StringCutObjectSelector<reco::GsfElectron> probeElectronSelector_;
//  double probeZ0Cut_; 
//  double probeD0Cut_;

  StringCutObjectSelector<trigger::TriggerObject> triggerSelector_;
  bool hasTriggerCuts_;
  EffectiveAreas effectiveAreas_;

};

#endif
