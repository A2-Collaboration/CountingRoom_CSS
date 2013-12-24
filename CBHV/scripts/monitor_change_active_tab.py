from org.csstudio.opibuilder.scriptUtil import PVUtil

# This script is called whenever clicking on one of the status leds
# for an entire box. It should be possible to acchieve the same
# behaviour using a rule, however I didn't manage to get that working.

display.getWidget("tabbed_container").setActiveTabIndex(0)