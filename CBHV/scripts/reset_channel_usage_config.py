from org.csstudio.opibuilder.scriptUtil import PVUtil

# This script causes the 'WriteInUse' pvs for every channel to
# process. These pvs hold the values for the channel usage as they are
# set in the cbhv.sub file. Hence when executing this script, the
# values for the channel usage are set to the initial ones.

box = 1

while box < 19:
    
    level = 0
    
    while level < 5:
        
        channel = 0
    
        while channel < 8:          

            getpv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:WriteInUse" % (box, level, channel))
            newvalue = PVUtil.getLong(getpv)
            print newvalue
            newvalue = int(newvalue)
            setpv = widget.getPVByName("CB:CB:HV:BOX:%s:%s:%s:InUse" % (box, level, channel))
            setpv.setValue(newvalue)
            
            channel+=1
            
        level+=1
        
    box+=1
            
            

