from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import FileUtil
import os

# First some often used pvs are defined for easy use. For every
# combination of source and target a different if case was created.

combo_box = display.getWidget("combo_box").getValue()
combo_channel = display.getWidget("combo_channel").getValue()
combo_level = display.getWidget("combo_level").getValue()
element = int(display.getWidget("spinner_element").getValue())
filepath = display.getWidget("filepath").getValue()
message = display.getWidget("message")
numberofboxes = 18
radio_target = display.getWidget("radio_target").getValue()
radio_source = display.getWidget("radio_source").getValue()
voltage = int(display.getWidget("spinner_voltage").getValue())

if radio_source =="" or radio_target == "":
    
    message.setPropertyValue("text", "Specify source and/or target first")
    
else:
    
    ############################ Element -> selected Value #######################
    
    if radio_target == "Element" and radio_source == "selected Value":

# First it is made sure that the entered values are ok.
        
        if element == -1 and voltage != 0:
            
            message.setPropertyValue("text", "Choose an element.")
                      
        elif voltage == 0 and element != -1:
            
            message.setPropertyValue("text", "Choose a voltage value.") 
            
        elif voltage == 0 and element == -1:
            
            message.setPropertyValue("text", "Choose a voltage value and an element.")
            
        else:
            
            element_exists = widget.getPVByName("CB:CB:HV:ELEMENT:%s:SetVolt" % element)

# In case the element exists the variable 'element_exists' contains an
# alphaumeric code, created by CSS, representing the pv - if there is
# no such pv the value is 'None'.
              
            if element_exists == None:
                
                message.setPropertyValue("text", "Element not in use/ unknown - choose another one")
                
            else:

# If the element number exists/ is in use and there is a voltage value
# entered it is written to the corresponding pv.
                             
                message.setPropertyValue("text", "")    
                element_exists.setValue(voltage)
                    
    ######################## Element -> File ###########################
    
    elif radio_target == "Element" and radio_source == "File":

# First it is checked that the entered element number and filepath are
# valid.
        
        check_filepath = os.path.isfile(filepath)
    
        if element == -1 and check_filepath == True:
        
            message.setPropertyValue("text", "Choose an element.")
                  
        elif check_filepath == False and element != -1:
        
            message.setPropertyValue("text", "Choose a filepath.") 
        
        elif check_filepath == False and element == -1:
        
            message.setPropertyValue("text", "Choose a filepath and an element.")
            
        else:

# Then the file is read and the element numbers and corresponding voltages are obtained.
            
            f = open (filepath, "r")
            file_element_voltages = f.readlines()
            count = 0
            file_elementarray = []
            file_voltagearray = []

            while count < len(file_element_voltages):
                line = file_element_voltages[count].split()
                file_elementarray.append(int(line[0]))
                file_voltagearray.append(int(line[1]))  
                count+=1

# It is also checked if the desired element number is mentioned in the
# file.
                
            element_exists = widget.getPVByName("CB:CB:HV:ELEMENT:%s:SetVolt" % element)
            file_element_voltage_exist = element in file_elementarray
                           
            if element_exists == None and file_element_voltage_exist == True:
                              
                message.setPropertyValue("text", "Element not in use/ unknown - choose another one.")
                
            elif file_element_voltage_exist == False and element_exists != None:
                              
                message.setPropertyValue("text", "Element not listed in voltage file - choose another one.")
                
            elif element_exists == None and file_element_voltage_exist == False:
                              
                message.setPropertyValue("text", "Element not in use/ unknown and not listed in voltage file - choose another one.")
            
            else:
                
# If the element number and filecontent matches all the criteria the
# voltage value is set to the cooresponding pv.

                message.setPropertyValue("text", "")
                file_index = file_elementarray.index(element)
                file_voltage = file_voltagearray[file_index]             
                element_exists.setValue(file_voltage)
                
############################# Box -> selected Value ############################
    elif radio_target == "Box":
        
        boxcount = 0
        check_boxarray = []
        checked_boxes_numberarray = []

# Checking for ticked boxes: Creation of an array with all
# boxes. Checked ones get an entry 1, unchecked ones an entry 0. After
# that checking if 1 is in the array at least once reveals if at least
# one box is checked. This applies for both 'source' options.
            
        while boxcount < numberofboxes:
            
            check_boxarray.append(display.getWidget("check_box%d" % (boxcount+1)).getValue())
            boxcount+=1
            
            if check_boxarray[boxcount-1] == True:
                
                checked_boxes_numberarray.append(boxcount)             
                               
        one_box_checked = True in check_boxarray
    
        if radio_target == "Box" and radio_source == "selected Value":

# Checking if voltage value is ok and boxes are checked.
            
            if one_box_checked == False and voltage != 0:
                
                message.setPropertyValue("text", "Check at least one box.")
                          
            elif voltage == 0 and one_box_checked == True:
                
                message.setPropertyValue("text", "Choose a voltage value.") 
                
            elif voltage == 0 and one_box_checked == False:
                
                message.setPropertyValue("text", "Choose a voltage value and check at least one box.")
                
            else:

# In case all criteria are matched, the values are set to the checked
# boxes.
                
                message.setPropertyValue("text", "")
                
                boxcount = 0
                
                while boxcount < numberofboxes:
                    
                        
                    if check_boxarray[boxcount] == False:
                        
                        boxcount+=1
                    
                    elif check_boxarray[boxcount] == True:
                    
                        boxcount+=1
                        
                        level = 0
                        
                        while level < 5:
                            
                            channel = 0
                        
                            while channel < 8:
                                
                                box_channel_exists = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:SetVolt" % (boxcount, level, channel))
                                
                                if box_channel_exists != None:
                                    
                                    box_channel_exists.setValue(voltage)
                                    channel+=1
                                    
                                if box_channel_exists == None:
                                    
                                    channel+=1
                                    
                            level+=1                
     
        ######################## Box -> File ###########################
        
        if radio_target == "Box" and radio_source == "File":

# First it is checked that boxes are checked and the file exists.
            
            check_filepath = os.path.isfile(filepath)
            
            if one_box_checked == False and check_filepath == True:
                
                message.setPropertyValue("text", "Check at least one box.")
                          
            elif check_filepath == False and one_box_checked == True:
                
                message.setPropertyValue("text", "Choose a file.") 
                
            elif check_filepath == False and one_box_checked == False:
                
                message.setPropertyValue("text", "Choose a filepath and check at least one box.")
                
            else:
                
                check_file_element_voltages = os.path.isfile(filepath)
                
                if check_file_element_voltages == False:
                    
                    message.setPropertyValue("text", "Choose a filepath!")
                    
                else:

# Then the filecontent is obtained.
                    
                    f = open (filepath, "r")
                    file_element_voltages = f.readlines()
                    f.close()
                    count = 0
                    file_elementarray = []
                    file_voltagearray = []
        
                    while count < len(file_element_voltages):

# Then it is checked if there is a channel assigned to the element of
# every line of the file.
                        
                        line = file_element_voltages[count].split()
                        file_element = int(line[0])
                        file_voltage = int(line[1])
                        element_channel_pv = widget.getPVByName("CB:CB:HV:ELEMENT:%s:Channel" % file_element) 

# In case the element is assigned to a box, that was checked the
# according value is set to the corresponding channel.
                        
                        if element_channel_pv != None:
                        
                            box_level_channel = PVUtil.getString(element_channel_pv)
                            parts = box_level_channel.split(":")
                            box = int(parts[0])
                            check_element_selected_box = box in checked_boxes_numberarray
                            
                            if check_element_selected_box == True:
                                
                                widget.getPVByName("CB:CB:HV:ELEMENT:%s:SetVolt" % file_element).setValue(file_voltage)
                            
                        count+=1
                        
                    message.setPropertyValue("text", "")
###################################### Channel -> selected Value ############################
    
    elif radio_target == "Channel":
        
        ch_box = display.getWidget("combo_box").getValue()
        ch_level = display.getWidget("combo_level").getValue()
        ch_channel = display.getWidget("combo_channel").getValue()

# First it is checked that a voltage value and a combination of box,
# level and channel are set.
        
        if radio_target == "Channel" and radio_source == "selected Value":
            
            if ch_box == "" or ch_level == "" or ch_channel == "":
                
                channel_selected = False
                
            else:
                
                channel_selected = True
            
            if channel_selected == False and voltage != 0:
                
                message.setPropertyValue("text", "Choose a value for box, level and channel.")
                          
            elif voltage == 0 and channel_selected == True:
                
                message.setPropertyValue("text", "Choose a voltage value.") 
                
            elif voltage == 0 and channel_selected == False:
                
                message.setPropertyValue("text", "Choose a voltage value and a value for box, level and channel.")
                
            else:
                
                ch_exists = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:SetVolt" % (ch_box, ch_level, ch_channel))
                
                if ch_exists == None:
                    
                    message.setPropertyValue("text", "Chosen channel not known.")
                    
                else:

# If the channel and voltage match all the criteria the voltage value
# is set to the correspoding pv.
                    
                    message.setPropertyValue("text", "")
                    ch_exists.setValue(voltage)
                    
############################# Channel -> File ############################
                    
        if radio_target == "Channel" and radio_source == "File":

# First the channel and filepath are checked.
            
            check_filepath = os.path.isfile(filepath)
            
            if ch_box == "" or ch_level == "" or ch_channel == "":
                
                channel_selected = False
                
            else:
                
                channel_selected = True
            
            if channel_selected == False and check_filepath == True:
                
                message.setPropertyValue("text", "Choose a value for box, level and channel..")
                          
            elif check_filepath == False and channel_selected == True:
                
                message.setPropertyValue("text", "Choose a file.") 
                
            elif check_filepath == False and channel_selected == False:
                
                message.setPropertyValue("text", "Choose a file and a value for box, level and channel.")
                
            else:

# Then the filecontent is obtained.
                               
                f = open (filepath, "r")
                file_element_voltages = f.readlines()
                f.close()
                count = 0
                file_elementarray = []
                file_voltagearray = []
    
                while count < len(file_element_voltages):
                    
                    line = file_element_voltages[count].split()
                    file_elementarray.append(int(line[0]))
                    file_voltagearray.append(int(line[1]))  
                    count+=1

# It is checked if the entered channel is mentioned in the file -
# therefor the corresponding element number has to be looked up.
                
                                          
                message.setPropertyValue("text", "")
                ch_element_pv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:Element" % (ch_box, ch_level, ch_channel))                
                ch_element = PVUtil.getString(ch_element_pv)
                ch_element = int(ch_element)
                check_element_file = ch_element in file_elementarray
                
                print check_element_file

# In case the channel/ element is mentioned the voltage value is
# written to the pv.
                
                if check_element_file == True:
                    ch_exists = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:SetVolt" % (ch_box, ch_level, ch_channel))
                    file_voltage_index = file_elementarray.index(ch_element)
                    file_voltage = file_voltagearray[file_voltage_index]
                    ch_exists.setValue(file_voltage)
                        
################################# from file ###########################

    elif radio_target == "From file" and radio_source == "File":

# When using this option, all element mentioned in the file are set the corresponding values.
        
        filepath = display.getWidget("filepath").getValue()

# First it is checked if the file exists.

        check_filepath = os.path.isfile(filepath)

# Then the filecontent is obtained.

        if check_filepath == True:
            
            message.setPropertyValue("text", "")        

            f = open (filepath, "r")
            file_element_voltages = f.readlines()
            f.close()
            count = 0
            file_elementarray = []
            file_voltagearray = []
    
            while count < len(file_element_voltages):
                line = file_element_voltages[count].split()
                file_element = int(line[0])
                file_voltage = int(line[1]) 
                pv = display.getWidget("engage").getPVByName("CB:CB:HV:ELEMENT:%s:SetVolt" % file_element)

# In case the element number exists/ is assigned to a channel the
# voltage value is written to the corresponding pv.
                
                if pv != None:
                    
                    pv.setValue(file_voltage)
                    
                count+=1
                            
        else:
        
            message.setPropertyValue("text", "No file specified or file no longer exists.")
                            
    elif radio_target == "From file" and radio_source == "selected Value":
        
        message.setPropertyValue("text", "Wrong source target combination!")                 
                            
                    
                
                                    
        
                            
                        
                   
