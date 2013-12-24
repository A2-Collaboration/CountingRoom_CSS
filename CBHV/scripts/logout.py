from org.csstudio.opibuilder.scriptUtil import PVUtil

# Below the things are listed that are done when clicking the button
# to log out in the subtab 'Voltage' of the 'Control' tab.

display.getWidget("tabbed_container").setPropertyValue("tab_1_enabled", False)
display.getWidget("enable_controls").setPropertyValue("enabled", True)
display.getWidget("tabbed_container").setActiveTabIndex(0)

    