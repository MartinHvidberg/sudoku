// JavaScript Document
<!--
function openAWindow( pageToLoad, winName, width, height, center)
{
	xposition=0; yposition=0;
	if ((parseInt(navigator.appVersion) >= 4 ) && (center)){
		xposition = (screen.width - width) / 2;
		yposition = (screen.height - height) / 2;
	}
	args = "width=" + width + ","
	+ "height=" + height + ","
	+ "location=0,"
	+ "menubar=0,"
	+ "resizable=1,"
	+ "scrollbars=1,"
	+ "status=0,"
	+ "titlebar=0,"
	+ "toolbar=0,"
	+ "hotkeys=0,"
	+ "screenx=" + xposition + ","  //NN Only
	+ "screeny=" + yposition + ","  //NN Only
	+ "left=" + xposition + ","     //IE Only
	+ "top=" + yposition;           //IE Only
	window.open( pageToLoad,winName,args );
}
function LinkToFile()
{
	var iIndex = document.dropdown.pdfLinks.selectedIndex;
	window.open( document.dropdown.pdfLinks.options[iIndex].value );
}
function validateFeedback(formname)
{
	var okay = true;
	var Solution, actualSol, i;
	var aform = document.forms(formname);
	// These values must be filled in
	realbgc = aform("isName").style.backgroundColor;
	if (!validation.nonBlank(aform("isName"),false)) okay = false;
	if (!validation.nonBlank(aform("isBody"),false)) okay = false;
	if (!validation.validEmail(aform("isEmail"),false)) okay = false;
	if( !okay ) alert("Some of the fields are not correct - these have been highlighted in yellow");
	return okay;
}

// -->
