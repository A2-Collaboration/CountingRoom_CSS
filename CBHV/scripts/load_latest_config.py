from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import GUIUtil
import os

# All load_<restoffilename>.py files work the same way. Take a look at
# the 'DynamicMacros' example, located in the Miscellaneous
# Folder. The script is usually called when a local pvs (check the CSS
# Help for more infos on local process variables) value changes. The
# value of this local pv is obtained and then passed on to another
# .opi file in a linking container as macro definition (again check
# the CSS Help for more info on this topic). This way the .opi file in
# the linking container displays infos about pvs which names depend on
# the macro.

filepath = display.getWidget("filepath").getValue()

check_filepath = os.path.isfile(filepath)

if check_filepath == True:
    
    user_ok = GUIUtil.openConfirmDialog("You are about to (re)load the configuration from:\n%s\nAre you sure, you really want to do that?" % filepath)
    
    if user_ok == True:
    
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
            
            if pv != None:
                
                pv.setValue(file_voltage)
                
            count = count + 1
            
    else:
        
        display.getWidget("monitor_info").setPropertyValue("text", "Hui - that was close!!.")
        
else:
    
    display.getWidget("monitor_info").setPropertyValue("text", "No file specified in control tab or file no longer exists.")

    


