# Single-Electron-DQM
single electron trigger efficiency code

analysis package:   DQMOffline/Trigger/

(1). single Electron code:
a. main analysis code:

src/HLTElectronMatchAndPlot.cc(main code)

src/HLTElectronMatchAndPlotContainer.cc

src/HLTElectronOfflineAnalyzer.cc


configuration file:

python/HLTElectronOfflineAnalyzer_cff.py

python/HLTElectronOfflineAnalyzer_cfi.py



header file:

interface/HLTElectronMatchAndPlot.h

interface/HLTElectronMatchAndPlotContainer.h



b. for efficiency:
general analysis code:
 
 
 
configuration file:

     python/ElectronPostProcessor_cff.py
     
     python/DQMGenericTnPClient_EG_cfi.py
