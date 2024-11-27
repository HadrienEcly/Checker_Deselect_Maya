## Created by Hadrien_Ecly (Hadrien Clement) https://github.com/HadrienEcly


import maya.cmds as cmds

######Functions

#detect selection and if its an edge
def selection_is_an_edge():
     # Get the current selection
    selection = cmds.ls(selection=True, flatten=True)
    print(selection)
    
    # Ensure the selection is valid and consists of edges
    selection = cmds.filterExpand(selection, selectionMask=32)
    if not selection:
        cmds.warning("Please select edges to convert.")
        print("No valid edges found in the selection. Exiting.")
        return
    return selection


#keep only the number of the edge
def strip_selection(which):
    if not which:
        return
    stripped_selection=[int(comp.split('[')[-1][:-1]) for comp in which]
    return(stripped_selection)


#convert an edge on a loop/ring/border        
def expand_selection(what):
    selection = selection_is_an_edge()
    if not selection:
        return

    if what == "loop":
        cmds.polySelect(edgeLoop=strip_selection(selection), add=True)
    elif what == "ring":
        cmds.polySelect(edgeRing=strip_selection(selection), add=True)
    elif what == "border":
        cmds.polySelect(edgeBorder=strip_selection(selection), add=True)
    elif what == "loopandborder":
        cmds.polySelect(edgeLoopOrBorder=strip_selection(selection), add=True)

def select_everyN(offset, what):
    selection = selection_is_an_edge()

    if not selection:
        return
        
    if what == "loop":
        cmds.polySelect(everyN=offset, edgeLoop=strip_selection(selection), add=True)
    elif what == "ring":
        cmds.polySelect(everyN=offset, edgeRing=strip_selection(selection), add=True)
    elif what == "border":
        cmds.polySelect(everyN=offset, edgeBorder=strip_selection(selection), add=True)


######UI

def selectNthedge_window():
    if cmds.window("SelectPatternToolWindow", exists=True):
        cmds.deleteUI("SelectPatternToolWindow")
    
    window = cmds.window("SelectPatternToolWindow", title="Selection Patterns Tools", widthHeight=(200, 270),sizeable=False)
    layout = cmds.columnLayout(adjustableColumn=True, rowSpacing=5)
    
    # Add buttons for "Select N Edge"
    cmds.text(label="Select N Edge Tool", font="boldLabelFont")

    cmds.separator()
    
    cmds.text(label="Set Offset Value:")
    offset_field = cmds.intField(value=2,width=100)
    
    cmds.button(label="Loop", command=lambda x: select_everyN(cmds.intField(offset_field, query=True, value=True),"loop"))
    cmds.button(label="Border", command=lambda x: select_everyN(cmds.intField(offset_field, query=True, value=True),"border"))
    cmds.button(label="Ring", command=lambda x: select_everyN(cmds.intField(offset_field, query=True, value=True), "ring"))
 
    
    # Add button to expand the selection
    cmds.text(label="Expand Selection:")
    cmds.button(label="Expand in Loop", command=lambda x: expand_selection("loop"),bgc=(0.5,0.3,0.3))
    cmds.button(label="Expand in Border", command=lambda x: expand_selection("border"),bgc=(0.3,0.5,0.3))
    cmds.button(label="Expand in Ring", command=lambda x: expand_selection("ring"),bgc=(0.3,0.3,0.5))
    
    # Show the window
    cmds.showWindow(window)

## SCRIPT
selectNthedge_window()




