from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import DataUtil

# All load_<restoffilename>.py files work the same way. Take a look at
# the 'DynamicMacros' example, located in the Miscellaneous
# Folder. The script is usually called when a local pvs (check the CSS
# Help for more infos on local process variables) value changes. The
# value of this local pv is obtained and then passed on to another
# .opi file in a linking container as macro definition (again check
# the CSS Help for more info on this topic). This way the .opi file in
# the linking container displays infos about pvs which names depend on
# the macro.

# In this case sometimes the pv whose value change calls this script
# can have a value that is not intended to reload the corresponding
# .opi file. Therefor an additinal if condition is used.


macroInput = DataUtil.createMacrosInput(True)

pvvalue = display.getWidget("eemem_read_box_combo").getValue()

if pvvalue != 'Box':

	pvname = int(pvvalue)

	print pvname

	macroInput.put("BOXNO", "%s" % pvname)

	widgetController.setPropertyValue("macros", macroInput)

	widgetController.setPropertyValue("opi_file", 
    		widgetController.getPropertyValue("opi_file"), True)

