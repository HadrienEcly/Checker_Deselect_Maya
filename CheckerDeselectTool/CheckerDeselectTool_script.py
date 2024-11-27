## Created by Hadrien_Ecly (Hadrien Clement) https://github.com/HadrienEcly


import maya.cmds as cmds

#UI

def open_checker_select_ui():
    global custom_mode
    custom_mode = False
    get_mask_first_selection()

    if not mask_firstsel :
        cmds.warning("Need a selection")
        return
    elif not cmds.filterExpand(mask_firstsel, sm=[34,31,32]) :
        cmds.warning("Please select components")
        return
    # Close the existing window if it's open
    if cmds.window("checkerSelectUI", exists=True):
        cmds.deleteUI("checkerSelectUI")

    # main window
    window = cmds.window("checkerSelectUI", title="Checker Select Tool", widthHeight=(200, 230),sizeable=False,toolbox=True)

    # main layout
    main_layout = cmds.columnLayout(adjustableColumn=True,h=200)
    
    # Step Select
    cmds.text(label="Step Select")
    step_select_slider = cmds.intSliderGrp(
        "stepSelectSlider",
        field=True,
        minValue=1,
        maxValue=20,
        value=1,
        width=20,
        p=main_layout
    )

    # Step Deselect
    cmds.text(label="Step Deselect:")
    step_deselect_slider = cmds.intSliderGrp(
        "stepDeselectSlider",
        field=True,
        minValue=1,
        maxValue=20,
        value=1,
        p=main_layout
    )
    
    #Separator_offset
    cmds.separator(h=5,st="single",p=main_layout)
    # Offset
    cmds.text(label="Offset")
    offset_slider = cmds.intSliderGrp(
        "OffsetSlider",
        field=True,
        minValue=0,
        maxValue=length_firstsel,
        value=0,
        p=main_layout,
    )
    cmds.button("customModeButton",label = "Custom mode",
        command=change_custom_mode,p=main_layout,bgc=(0.2,0.2,0.2))

    #Separator
    cmds.separator(h=10,st="single")
  
    # Max Iterations
    iteration_layout = cmds.rowLayout(
        numberOfColumns=2, columnWidth2=(80, 100), p=main_layout,cl2=("center","center")
    )
    cmds.text(label="Max Iterations:", align="left")
    max_iteration_field = cmds.intField(
        "maxIterationField",
        value=100,
        width=40
    )
    #Separator
    cmds.separator(h=10,st="single",p=main_layout)
    
    # Run Button
    cmds.button(
        label="Run Script",
        command=lambda _: run_checker_select(
            cmds.intSliderGrp(step_select_slider, query=True, value=True),
            cmds.intSliderGrp(step_deselect_slider, query=True, value=True),
            cmds.intSliderGrp(offset_slider, query=True, value=True),
            cmds.intField(max_iteration_field, query=True, value=True)
        ),
        p = main_layout,
        h = 50,
        bgc = (1.0,0.6,0.1)
    )

    # Show the window
    cmds.showWindow(window)

def run_checker_select(step_select, step_deselect, offset, max_iteration):
    checker_select(mask_firstsel, step_select, step_deselect, offset, max_iteration)

#################FUNCTIONS


def change_custom_mode(*args): #Change the custom mode
    global custom_mode
    global custom_selection
    global mask_firstsel 
    if cmds.ls(selection=True,flatten=True) == mask_firstsel:
        cmds.warning("Custom selection must be different than first selection")
    elif check_type(cmds.ls(selection=True,flatten=True)) is not check_type(mask_firstsel):
        cmds.warning("Please select same sort of component than base selection")

    elif custom_mode:
        custom_mode = False
        cmds.intSliderGrp("OffsetSlider", edit=True, enable=True)
        cmds.button("customModeButton",edit=True,bgc=(0.2,0.2,0.2))
        pass
    else:
        custom_mode = True
        custom_selection = cmds.ls(selection=True,flatten=True)
        cmds.intSliderGrp("OffsetSlider", edit=True, enable=False)
        cmds.button("customModeButton",edit=True,bgc=(0.8,0.8,0.8))
    
#Get first selection and pass it at global to always use it like a mask
def get_mask_first_selection():
    global mask_firstsel 
    mask_firstsel = cmds.ls(selection=True, flatten=True)
    #length_firstsel is the maximum output possible for the offset
    global length_firstsel
    length_firstsel = len(mask_firstsel) - 1 

#Little function that check the type of the selection
def check_type(sel):
    if cmds.filterExpand(sel, sm=34):
        return "face"
    elif cmds.filterExpand(sel, sm=31):
        return "vertex"
    elif cmds.filterExpand(sel, sm=32): 
        return "edge"

#Grow selection depending on the component selected
def grow_selection(sel): 
    if check_type(sel) == "face":  # 34 corresponds to Face selection
        converted_sel = cmds.polyListComponentConversion(sel, ff=True, toEdge=True)
        growed_sel = cmds.polyListComponentConversion(converted_sel, fe=True, toFace=True)
        flatten_sel = cmds.filterExpand(growed_sel, sm=34)
        return flatten_sel

    elif check_type(sel) == "vertex":  # 31 corresponds to Vertex selection
        converted_sel = cmds.polyListComponentConversion(sel, toEdge=True)
        growed_sel = cmds.polyListComponentConversion(converted_sel, toVertex=True)
        flatten_sel = cmds.filterExpand(growed_sel, sm=31)
        return flatten_sel
        
    elif check_type(sel) == "edge":  # 32 corresponds to Edge selection
        converted_sel = cmds.polyListComponentConversion(sel, toFace=True)
        growed_sel = cmds.polyListComponentConversion(converted_sel, toEdge=True)
        flatten_sel = cmds.filterExpand(growed_sel, sm=32)
        return flatten_sel

#Get the distance th component of the base_componnent (can be changed by the offset or custom mode)
def distant_component(sel, distance=1, offset=0):
    global custom_mode
    global custom_selection
    if custom_mode == True:
        base_component=custom_selection #get the custom selection as the base
        past_selected = set(base_component)
    else:
        base_component= sel[offset] #get the first componnent as the base
        past_selected = set([base_component]) 
        
    cmds.select(base_component, r=True) #selection that will grow
    
    # Grow selection distance th time
    for iteration in range(distance):
        new_selection = []

        expanded_selection = grow_selection(base_component)

        if expanded_selection is not None:
            # Remove previously selected faces from the expanded selection to get only new faces
            new_components = [component for component in expanded_selection if component not in past_selected]   
            new_selection.extend(new_components)
            past_selected.update(new_components)
        # Select the final list of components
        base_component = new_selection
    return new_selection


#Run distant_componnent depending on the step and offset set, the iteration is the number of time that it is runned
def checker_select(mask_sel, step_select=2, step_deselect=2, offset=0, max_iteration=10):
    global mask_firstsel
    all_deselected = [] 
    total_step = step_select + step_deselect
    previous_deselected =[]
    current_step = 0
    i = 0
    
    while i <= max_iteration:
        #Loop for step select, add the steps to the current step
        for _ in range(step_select):
            current_step = 1 + (total_step*i)
        #Loop for step_deselect, apply the formula depending on step_deselect
        for _ in range(step_deselect):
            if step_deselect > 1:
                current_step = current_step+1
            deselected = distant_component(sel=mask_sel, distance=current_step, offset=offset)
            #Track previous deselected state
            previous_deselected = list(all_deselected)
            all_deselected.extend(deselected)
            
            if all_deselected == previous_deselected or deselected and not any(component in mask_firstsel for component in deselected): # check si les nouvelles faces sont dans mask_first_sel sinon break
                break
        if all_deselected == previous_deselected or deselected and not any(component in mask_firstsel for component in deselected):
            break
        i += 1    
    cmds.select(mask_sel,r=True)
    if all_deselected:
        cmds.select(all_deselected, deselect=True)

# Open the main window
open_checker_select_ui()
