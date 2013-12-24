# This script is called to save or load either the voltage or channel
# usage configuration.

from org.csstudio.opibuilder.scriptUtil import PVUtil
import os

# First the picked option is obtained.

save_load_configs_pv = widget.getPVByName("loc://save_load_configs")

save_load_option = PVUtil.getString(save_load_configs_pv)

message = ""

# Then the behaviour for the 4 options is defined using if cases.

if save_load_option == "Save voltage configuration":

# First the entered filepath and name are checked. If nothing was
# entered in at least one field an error message is displayed and
# nothing more happens.
    
    filepath_pv = display.getWidget("save_load_configs_filepath").getPV()
    filepath = PVUtil.getString(filepath_pv)
    
    filename_pv = display.getWidget("save_load_configs_filename").getPV()
    filename = PVUtil.getString(filename_pv)
    
    if filename=="" or filepath == "":
        
        message = 'Please choose directory and/ or filename first.'
        
    else:

# In case a path and filename is set, the combination for box, level,
# channel and voltage of every channel is written to the corresponding
# file.
        
        message = ""
        
        file = filepath + "/" + filename
        
        f= open(file, "w")        
        
        box = 1        
        
        while box < 19:
            
            level = 0
            
            while level < 5:
                
                channel = 0
                
                while channel < 8:
                    
                    voltage_pv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:LatestSetVolt" % (box, level, channel))
                    voltage = PVUtil.getLong(voltage_pv)
                    f.write("%s %s %s %s\n" % (box, level, channel, voltage))
                    
                    channel+=1
                    
                level+=1
                
            box+=1
            
        f.close()
        
        filename_pv.setValue("")
        filepath_pv.setValue("")
        
if save_load_option == "Save channel usage configuration":

# First the entered filepath and name are checked. If nothing was
# entered in at least one field an error message is displayed and
# nothing more happens.
    
    filepath_pv = display.getWidget("save_load_configs_filepath").getPV()
    filepath = PVUtil.getString(filepath_pv)
    
    filename_pv = display.getWidget("save_load_configs_filename").getPV()
    filename = PVUtil.getString(filename_pv)
    
    if filename=="" or filepath == "":
        
        message = 'Please choose directory and/ or filename first.'
        
    else:

# In case a path and filename is set, the combination for box, level,
# channel and usage of every channel is written to the corresponding
# file.
        
        message = ""
        
        file = filepath + "/" + filename
        
        f= open(file, "w")        
        
        box = 1        
        
        while box < 19:
            
            level = 0
            
            while level < 5:
                
                channel = 0
                
                while channel < 8:
                    
                    usage_pv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:InUse" % (box, level, channel))
                    usage = PVUtil.getLong(usage_pv)
                    f.write("%s %s %s %s\n" % (box, level, channel, usage))
                    
                    channel+=1
                    
                level+=1
                
            box+=1
            
        f.close()
        
        filename_pv.setValue("")
        filepath_pv.setValue("")
        
if save_load_option == "Load voltage configuration":

# First it is verified that there really is a file at the specified
# path. In case there is none, an error message is displayed and
# nothing more happens.
    
    filepath_pv = display.getWidget("save_load_configs_filepath").getPV()
    filepath = PVUtil.getString(filepath_pv)
    check_filepath = os.path.isfile(filepath)
    
    if check_filepath == False:
        
        message = 'Please choose file first.'
        
    else:

# When there is a file, the script assumes that the syntax in the file
# is the one created when saving files, it reads every line, creates
# the correpsonding pv and sets the according voltage value.
        
        message = ""
        
        f= open(filepath, "r")
        lines = f.readlines()
        f.close()       
        
        linecount = 0
        
        while linecount < len(lines):
        
            lineparts = lines[linecount].split()
            voltage_pv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:LatestSetVolt" % (lineparts[0], lineparts[1], lineparts[2]))
            voltage = voltage_pv.setValue(lineparts[3])
            
            linecount+=1
            
        filepath_pv.setValue("")
            
if save_load_option == "Load channel usage configuration":

# First it is verified that there really is a file at the specified
# path. In case there is none, an error message is displayed and
# nothing more happens.
    
    filepath_pv = display.getWidget("save_load_configs_filepath").getPV()
    filepath = PVUtil.getString(filepath_pv)
    check_filepath = os.path.isfile(filepath)
    
    print check_filepath
    
    if check_filepath == False:
        
        message = 'Please choose file first.'
        
    else:

# When there is a file, the script assumes that the syntax in the file
# is the one created when saving files, it reads every line, creates
# the correpsonding pv and sets the according channel usage value.
        
        message = ""
        
        f= open(filepath, "r")
        lines = f.readlines()
        f.close()       
        
        linecount = 0
        
        while linecount < len(lines):
        
            lineparts = lines[linecount].split()
            usage_pv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:InUse" % (lineparts[0], lineparts[1], lineparts[2]))
            usage = usage_pv.setValue(lineparts[3])
            
            linecount+=1
            
        filepath_pv.setValue("")
        
display.getWidget("configuration_message").setPropertyValue("text", "%s" % message)

# The last line resets the pv, so there is no option for saving or
# loading a configuration is ticked any more - this way it is made
# sure, that nothing happens accidentally.

widget.getPVByName("loc://save_load_configs").setValue("")
                    