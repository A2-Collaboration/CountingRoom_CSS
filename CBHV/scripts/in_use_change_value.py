from org.csstudio.opibuilder.scriptUtil import PVUtil

# This script is used to change the InUse value of a channel. The script is called when the user clicks on an channel indicator in the 'Channel Usage' area in the subtab 'Configuration' in the 'Control' tab.

# First the name of the pv that should be changed is obtained.

widgetname = widget.getPropertyValue("pv_name")

# Then box, level and channel of the pv are extracted and the corresponding InUse pvname is created.

nameparts = widgetname.split(":")

pvname = "CB:CB:HV:BOX:%s:%s:%s:InUse" % (nameparts[4],nameparts[5],nameparts[6])

# The next code lines are needed to get the current value of the InUse
# pv.

pv = widget.getPVByName("%s" % pvname)

pvvalue = PVUtil.getLong(pv)

# Now depending on the value, the new value is obtained and set. The
# variable 'newpvvalue' is initialized with zero to check if it was
# really changed (initializing it with for example 0 could be a
# problem - in case there is a problem it would be 0 by default making
# it maybe harder to find out why it is not working - as it does no
# harm the value -1 on initiation was kept for the final version of
# the script.

newpvvalue = -1

if pvvalue == 0:
    
    newpvvalue = 1
    
elif pvvalue == 1:
    
    newpvvalue = 0

# There are other ways to create the pv(name) too. However this
# version was found to be working an is also used in other scripts.

pv = widget.getPVByName("%s" % pvname)

pv.setValue(newpvvalue)
