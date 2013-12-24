from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil
from org.csstudio.opibuilder.scriptUtil import GUIUtil

# The line below contains the super secret password protecting the
# high voltage control to be operated by uncool staff.

check = GUIUtil.openPasswordDialog("Password", "a2messung")

# In case the password was entered correctly, the button to call this
# script is disabled, the 'Control' tab is enabled and set as active
# tab.

if (check == True):
    
    display.getWidget("tabbed_container").setPropertyValue("tab_1_enabled", True)
    display.getWidget("enable_controls").setPropertyValue("enabled", False)
    display.getWidget("tabbed_container").setActiveTabIndex(1)
    