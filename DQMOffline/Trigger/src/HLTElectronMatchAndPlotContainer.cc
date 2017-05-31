#ifndef DQMOffline_Trigger_HLTElectronMatchAndPlotContainer_CC
#define DQMOffline_Trigger_HLTElectronMatchAndPlotContainer_CC
/** \file DQMOffline/Trigger/HLTElectronMatchAndPlotContainer.cc
 *
 */

#include "DQMOffline/Trigger/interface/HLTElectronMatchAndPlotContainer.h"

//////////////////////////////////////////////////////////////////////////////
//////// Namespaces and Typedefs /////////////////////////////////////////////

using namespace std;
using namespace edm;
using namespace reco;
using namespace trigger;

//////////////////////////////////////////////////////////////////////////////
///Container Class Members (this is what is used by the DQM module) //////////

/// Constructor
HLTElectronMatchAndPlotContainer::HLTElectronMatchAndPlotContainer(ConsumesCollector && iC, const ParameterSet & pset) 
{

  plotters_.clear();

  string hltProcessName  = pset.getParameter<string>("hltProcessName");

  ParameterSet inputTags = pset.getParameter<ParameterSet>("inputTags");

  InputTag resTag = inputTags.getParameter<InputTag>("triggerResults");
  InputTag sumTag = inputTags.getParameter<InputTag>("triggerSummary");
  resTag = InputTag(resTag.label(), resTag.instance(), hltProcessName);
  sumTag = InputTag(sumTag.label(), sumTag.instance(), hltProcessName);
  
  trigSummaryToken_ = iC.consumes<TriggerEvent>(sumTag);
  trigResultsToken_ = iC.consumes<TriggerResults>(resTag);
   
  rhoToken_   = iC.consumes<double>(inputTags.getParameter<InputTag>("rho"));
  convsToken_   = iC.consumes<ConversionCollection>(inputTags.getParameter<InputTag>("convs"));
  bsToken_   = iC.consumes<BeamSpot>(inputTags.getParameter<InputTag>("beamSpot"));
  eleToken_ = iC.mayConsume<reco::GsfElectronCollection>(inputTags.getParameter<InputTag>("electrons"));
  pvToken_   = iC.consumes<VertexCollection>(inputTags.getParameter<InputTag>("offlinePVs"));

}


/// Add a HLTElectronMatchAndPlot for a given path
// path: hltPathsToCheck, in Analyzer.cc line 155;
void HLTElectronMatchAndPlotContainer::addPlotter(const edm::ParameterSet &pset , std::string path,
					      std::string label, bool islastfilter)
{

  plotters_.push_back(HLTElectronMatchAndPlot(pset,path,label,islastfilter));

}


void HLTElectronMatchAndPlotContainer::beginRun(DQMStore::IBooker & iBooker,
					    const edm::Run & iRun, 
					    const edm::EventSetup & iSetup)
{

  vector<HLTElectronMatchAndPlot>::iterator iter = plotters_.begin();
  vector<HLTElectronMatchAndPlot>::iterator end  = plotters_.end();

  for (; iter != end; ++iter) 
    {
      iter->beginRun(iBooker, iRun, iSetup);
    }

}


void HLTElectronMatchAndPlotContainer::endRun(const edm::Run & iRun, 
					  const edm::EventSetup & iSetup)
{

  vector<HLTElectronMatchAndPlot>::iterator iter = plotters_.begin();
  vector<HLTElectronMatchAndPlot>::iterator end  = plotters_.end();

  for (; iter != end; ++iter) 
    {
      iter->endRun(iRun, iSetup);
    }
  
}


void HLTElectronMatchAndPlotContainer::analyze(const edm::Event & iEvent, 
					   const edm::EventSetup & iSetup)
{  

  // Get objects from the event.  
  Handle<TriggerEvent> triggerSummary;
  iEvent.getByToken(trigSummaryToken_, triggerSummary);

  if(!triggerSummary.isValid()) 
  {
    LogError("HLTElectronMatchAndPlot")<<"Missing triggerSummary collection" << endl;
    return;
  }

  Handle<TriggerResults> triggerResults;
  iEvent.getByToken(trigResultsToken_, triggerResults);

  if(!triggerResults.isValid()) 
  {
    LogError("HLTElectronMatchAndPlot")<<"Missing triggerResults collection" << endl;
    return;
  }

//get the rho information from events;
  Handle<double> rho;
  iEvent.getByToken(rhoToken_, rho);

  if(!rho.isValid()) 
  {
    LogError("HLTElectronMatchAndPlot")<<"Missing rho collection " << endl;
    return;
  }

//get the conversion information from events;
  Handle<ConversionCollection> convs;
  iEvent.getByToken(convsToken_, convs);

  if(!convs.isValid()) 
  {
    LogError("HLTElectronMatchAndPlot")<<"Missing conversion collection " << endl;
    return;
  }
//get the beamSpot information from events;
  Handle<BeamSpot> beamSpot;
  iEvent.getByToken(bsToken_, beamSpot);

  if(!beamSpot.isValid()) 
  {
    LogError("HLTElectronMatchAndPlot")<<"Missing beam spot collection " << endl;
    return;
  }

  edm::Handle<reco::GsfElectronCollection> eleHandle;
  iEvent.getByToken(eleToken_, eleHandle);

  if(!eleHandle.isValid()) 
  {
    LogError("HLTElectronMatchAndPlot")<<"Missing electron collection " << endl;
    return;
  }

  Handle<VertexCollection> vertices;
  iEvent.getByToken(pvToken_, vertices);

  if(!vertices.isValid()) 
  {
    LogError("HLTElectronMatchAndPlot")<<"Missing vertices collection " << endl;
    return;
  }
  

  vector<HLTElectronMatchAndPlot>::iterator iter = plotters_.begin();
  vector<HLTElectronMatchAndPlot>::iterator end  = plotters_.end();

  for (; iter != end; ++iter) 
    {
      iter->analyze(eleHandle, rho, convs, beamSpot, vertices, triggerSummary, triggerResults);
    }
  
}
#endif
