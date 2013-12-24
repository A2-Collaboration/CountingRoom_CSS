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


macroInput = DataUtil.createMacrosInput(True)

elementpv = widget.getPVByName("loc://map_element")

elementvalue = PVUtil.getLong(elementpv)

macroInput.put("ELEMENTNO", "%s" % elementvalue)
macroInput.put("P", "CB:CB:HV")

widgetController.setPropertyValue("macros", macroInput)

widgetController.setPropertyValue("opi_file", 
    widgetController.getPropertyValue("opi_file"), True)

