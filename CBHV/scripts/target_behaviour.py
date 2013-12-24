# This script was used before local pvs and rules controlled the
# behaviour of the 'Voltage' tab. It can be seen as a demo how to get
# things going using scripts when looking at the commented out
# lines. The only line still in use sets the pv loc://radio_source to
# 'File' as this cannot be done by a rule as rules cannot change pv
# values and hence this has to be done using a script.

from org.csstudio.opibuilder.scriptUtil import PVUtil

value = widget.getValue()

#if value == "Box":
    
#    display.getWidget("group_box").setPropertyValue("enabled", True)
#    display.getWidget("group_channel").setPropertyValue("enabled", False)
#    display.getWidget("group_element").setPropertyValue("enabled", False)
    
#elif value == "Channel":
    
#    display.getWidget("group_box").setPropertyValue("enabled", False)
#    display.getWidget("group_channel").setPropertyValue("enabled", True)
#    display.getWidget("group_element").setPropertyValue("enabled", False)
    
#elif value == "Element":
    
#    display.getWidget("group_box").setPropertyValue("enabled", False)
#    display.getWidget("group_channel").setPropertyValue("enabled", False)
#    display.getWidget("group_element").setPropertyValue("enabled", True)
    
if value == "From file":
    
#    display.getWidget("group_box").setPropertyValue("enabled", False)
#    display.getWidget("group_channel").setPropertyValue("enabled", False)
#    display.getWidget("group_element").setPropertyValue("enabled", False)
    display.getWidget("radio_source").getPV().setValue("File")
