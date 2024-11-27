# Checker/Pattern Deselecter Tool for Maya

This tool is inspired by Blender's equivalent. It allows you to apply a pattern to selected components (vertices, edges, faces, etc.) based on the steps of selected and deselected faces. 

## Features
- **Works with every components**:
The script detects which of faces, vertices or edges are selected
- **Simple Use**:  
  The "offset" cursor adjusts the position of the base component and the applied pattern.
  
- **Advanced Pattern Customization**:  
  For more complex patterns, you can select the same component type and activate "Custom Mode" to replace the base components with your selection.
  
- **Original Selection Retention**:  
  The tool preserves the original selection, ensuring that it remains unaffected while applying the pattern.

## Usage

1. **Select Components**:  
   Choose a component type (e.g., face, edge, or vertex) as the base selection.
   
2. **Use script**:  
   Use the step select, step deselect and offset cursor as you please to get the desired pattern

3. **Custom Mode for Complex Patterns**:  
   Select the same component type you want to customize.
   Tap the "Custom Mode" button to replace the base component with your selection.


> **Note**: The tool keeps the original selection intact, so you can modify the pattern without altering your initial selection.

## Installation

1. **Download the Tool**
   - Place the `CheckerDeselectTool` script file in your Maya user scripts folder:
     - **Windows:** `C:\Users\<YourUsername>\Documents\maya\<maya_version>\scripts`
     - **macOS:** `/Users/<YourUsername>/Library/Preferences/Autodesk/maya/<maya_version>/scripts`
     - **Linux:** `/home/<YourUsername>/maya/<maya_version>/scripts`
2. **Restart Maya**   
3. **Installation in Maya**
  - Copy this in the script editor and add it to a shelf to a easier use !
`import CheckerDeselectTool.CheckerDeselectTool.py as cdt
cdt.open_checker_select_ui()`


## License

This tool is free to use, is used in another script please credit Hadrien Clement and put a link to my github https://github.com/HadrienEcly. 
If it is used as part of a paid script please reach out to me first.
