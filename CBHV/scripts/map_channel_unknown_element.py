from org.csstudio.opibuilder.scriptUtil import PVUtil

# When choosing an element, there may be no corresponding box, level
# and channelnumber as not all element numbers are assigend to a
# channel. Hence this script checks if there is a channel assigned or
# not and either displays it or a warning message.

pv = widget.getPV().getValue()

if pv == None:
    
    display.getWidget("map_channel").setPropertyValue("visible", False)
    display.getWidget("map_channel_info").setPropertyValue("visible", True)
    
else:
    
    display.getWidget("map_channel").setPropertyValue("visible", True)
    display.getWidget("map_channel_info").setPropertyValue("visible", False)