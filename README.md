# NR Capacity Dimensioning Tool

NR Capacity Dimensioning Tool is a simple application for cellular network (5G/NR) capacity planning. It helps you quickly estimate the required number of base stations (sites) and sectors (cells) based on key technical and business parameters.
Project Contents

## 1. Repository contains
   ### `nr_capacity_gui.py` 
   
   A graphical user interface (GUI) based on tkinter for easy parameter entry and result display.

   ### `nr_capacity_tool.py`
   
   The core calculation logic: contains the capacity planning model, functions for traffic and cell throughput calculations, and estimation of required sites and cells.

## 2. How to Run

> [!CAUTION]
>  Before you start, make sure you've already install thinker library and Python
>
> Requirements:
>  - Python 3.x
>  - `thinker`

### 2.1 Running the Application:

Run in the terminal:

'''bash
python nr_capacity_gui.py
'''

And the GUI window will appear. 

### 2.2 Fill in all required parameters

The parameters:

- Area (km²)
- Subscriber Density (users/km²)
- Busy Hour DL Traffic (GB/sub)
- Busy Hour UL Traffic (GB/sub)
- eMBB Ratio (0–1)
- URLLC Ratio (0–1)
- mMTC Ratio (0–1)
- FR1 Bandwidth (MHz)
- FR2 Bandwidth (MHz)
- FR1 MIMO Gain
- FR2 MIMO Gain
- FR1 Spectral Efficiency
- FR2 Spectral Efficiency"
  
### 2.3 Click the `Run Dimensioning` button.

### 2.4 Output:

The tool will display:

   - Total Traffic (Mbps)
   - FR1 Cell Throughput
   - FR2 Cell Throughput
   - Estimated Cells Required
   - Estimated Sites Required
