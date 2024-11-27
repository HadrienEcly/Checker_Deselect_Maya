# Select Nth Edge Tool for Maya

This tool is inspired by advanced selection tools from other 3D software. It enables users to select every nth edge on a loop, ring, or border interactively. Additionally, users can grow the selection across the entire loop, ring, or border for efficient modeling workflows.

## Features

- **Flexible Edge Selection**:  
  Select every nth edge along a loop, ring, or border, providing complete control over the selection pattern.  

- **Grow Selection**:  
  Extend your selection across the entire loop, ring, or border with a single click.  

- **Interactive Use**:  
  Customize selection interactively by adjusting parameters like the interval (nth edge) or selection mode (loop, ring, or border).  

## Usage

1. **Select an Edge**:  
   Begin by selecting an edge on a model.

2. **Use the Tool**:  
   - Adjust the interval to select every nth edge.
   - Choose the desired selection mode: loop, ring, or border.
   - Optionally, grow the selection across the entire edge type.


## Installation

1. **Download the Tool**
   - Place the `SelectNthEdge` script file in your Maya user scripts folder:
     - **Windows:** `C:\Users\<YourUsername>\Documents\maya\<maya_version>\scripts`
     - **macOS:** `/Users/<YourUsername>/Library/Preferences/Autodesk/maya/<maya_version>/scripts`
     - **Linux:** `/home/<YourUsername>/maya/<maya_version>/scripts`
2. **Restart Maya**  
3. **Installation in Maya**
   - Copy this in the script editor and add it to a shelf for easier access:

`from SelectNthEdge import everyNthedge_script as ene  
ene.selectNthedge_window()`

