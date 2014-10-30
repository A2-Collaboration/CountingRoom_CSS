//importPackage(Packages.java.lang);
importPackage(Packages.org.csstudio.opibuilder.scriptUtil);


widget.removeAllChildren();


var number_of_power_supplies = PVUtil.getDouble(pvs[2]);


for(var i=0; i< number_of_power_supplies; i++){
	
	//Create linking container
	var linkingContainer = WidgetUtil.createWidgetModel("org.csstudio.opibuilder.widgets.linkingContainer");
		
	//Set opi file to open
	linkingContainer.setPropertyValue("opi_file", "display.opi");
	
	//Set container properties
	linkingContainer.setPropertyValue("auto_size", true);
	linkingContainer.setPropertyValue("zoom_to_fit", false);
	linkingContainer.setPropertyValue("border_style", 1);
	
	//Add the prefix of the power supply (i.e. its generic name without its identifing number) 
	//to the counter variable (i.e. its identifying number)
	var powersupplyprefix = "TAGGER:LV";
	var powersupplyname = powersupplyprefix + i;
	
	//Set variable to its corresponding name
    linkingContainer.addMacro("P", powersupplyname);
	
	//Add new linking container to the bottom of the list
	widget.addChildToBottom(linkingContainer);
	
}

