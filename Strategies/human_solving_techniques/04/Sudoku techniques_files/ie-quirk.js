function loadFlashObject(movie, width, height, bgcol, flashvars, tid, tclass, wmode) {
	if (bgcol=="") {
		if (document.body.bgColor)
			bgcol = document.body.bgColor;
		else if (document.body.style.backgroundColor)
			bgcol = document.body.style.backgroundColor;
	}
	document.write(
		'<object ' + (tid ? ('id="' + tid + '" name="' + tid + '" ') : '') + (tclass ? ('class="' + tclass + '" ') : '') + 'type="application/x-shockwave-flash" data="' + movie + '" width="' + width + '" height="' + height + '">' +
			'<param name="quality" value="high" />' +
			'<param name="movie" value="' + movie + '" />' +
			'<param name="bgcolor" value="' + bgcol + '" />' +
			'<param name="base" value="" />' +
			'<param name="wmode" value="' + wmode + '" />' +
			'<param name="flashVars" value="' + flashvars + '" />' +
		'</object>'
	);
}

function isOpera()
{
	return navigator.appName.indexOf("Opera") != -1;
}

function popup(url, resizable)
{
	if (isOpera())
	{
		window.open(url);
	}
	else
	{
		window.open(url,'','width=500,height=500,left=0,top=0,toolbar=No,scrollbars=No,location=No,status=No,resizable=Yes,fullscreen=No');
	}
}

function sizedPopup(url, width, height, scrollbars)
{
	if (isOpera())
	{
        window.open(url);
    }
	else
	{
		window.open(url,'','width=' + width + ',height=' + height + ',left=0,top=0,toolbar=No,scrollbars=' + scrollbars + ',location=No,status=No,resizable=No,fullscreen=No');
    }
}

function newWindow(url)
{
	window.open(url,'','toolbar=Yes,location=Yes,directories=Yes,resizable=Yes,scrollbars=Yes,status=Yes,menubar=Yes');
}

function showCreditValueExamples(clicked_package){
	var packId = $("input[name='package']:checked").val();
	$(".package_example").hide();
	if (packId.length != 0) {
		$("#package" + packId).show();
	}
}

function choosePaymentMethod() {
	$("#card, #paypal, #robokassa, #package_warning").hide();
	checkPaymentMethod();
}

function checkPaymentMethod(){
	var chosen = $("input[name='method_select']:checked").val();
	if (chosen !== undefined && chosen.length != 0) {
		//if (chosen == "card" && qs("package") == 1) {
		//	$("#package_warning, #temp_buttons").show();
		//}
		//else {
			$("#" + chosen).show();
			$("#temp_buttons").hide();
		//}
	}
}
/* get query string parameter */
function qs(key) {
	key = key.replace(/[*+?^$.\[\]{}()|\\\/]/g, "\\$&"); // escape RegEx meta chars
	var match = location.search.match(new RegExp("[?&]" + key + "=([^&]+)(&|$)"));
	return match && decodeURIComponent(match[1].replace(/\+/g, " "));
}

function checkAccountFilter() {
	var checkedvalue = getFilterParam(document.myaccount);
	if (checkedvalue == "all"){
		disableFilter(true);
	}
	if (checkedvalue == "filtered"){
		disableFilter(false);	
	}
}

function disableFilter(val) {
	document.myaccount.monthfrom.disabled = val;
	document.myaccount.dayfrom.disabled = val;
	document.myaccount.yearfrom.disabled = val;
	document.myaccount.monthto.disabled = val;
	document.myaccount.dayto.disabled = val;
	document.myaccount.yearto.disabled = val;
}

function getFilterParam(form) {
	var filterradio = form.filter;
	var checked = "";
	for(var i = 0; i < filterradio.length; i++) {
		if(filterradio[i].checked) {
			checked = filterradio[i].value;
		}
	}
	return checked;
}

function checkFilterSelection(form) {
	if (getFilterParam(form) == "filtered"){
		if (form.monthfrom.selectedIndex == 0 ||
			form.dayfrom.selectedIndex == 0 ||
			form.yearfrom.selectedIndex == 0 ||
			form.monthto.selectedIndex == 0 ||
			form.dayto.selectedIndex == 0 ||
			form.yearto.selectedIndex == 0){
			alert("Please select all fields for the dates.");
			valid = false;
		}
		else{
			valid = true;
		}
	}
	else {
		valid = true;
	}
	return valid;
}

function addLoadEvent(func) {
	var oldonload = window.onload;
	if (typeof window.onload != 'function') {
		window.onload = func;
	} else {
		window.onload = function() {
			if (oldonload) {
				oldonload();
			}
			func();
		}
	}
}

function changeLanguage(lang) {
	var date = new Date();
	date.setTime(date.getTime() + (3650 * 24 * 60 * 60 * 1000));
	var cookie = "Language=lang=" + lang + "; expires=" + date.toGMTString() + "; path=/";
	document.cookie = cookie;
}

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for (var i = 0; i < ca.length; i++) {
		var c = ca[i];
		while (c.charAt(0) == ' ') c = c.substring(1, c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
	}
	return null;
}

function pageIllustrations(id, insideImages, step) {
	var bookForm = document.getElementById("pageForm_" + id);
	var pagingForm = document.pagingForm;
	var currIndex = Number(bookForm.currentImage.value);
	var nextIndex;
	nextIndex = currIndex + 1 * step;
	var back = document.getElementById("backButton_" + id);
	var forth = document.getElementById("forthButton_" + id);
	if (nextIndex + step < 0) {
		// disable back button
		back.getElementsByTagName("img")[0].src = pagingForm.backendImage.value;
		disableLink(back);
	}
	else {
		back.getElementsByTagName("img")[0].src = pagingForm.backImage.value;
		enableLink(back, "pageBack_" + id + "()");
	}
	if (nextIndex + step >= insideImages.length) {
		// disable forward button
		forth.getElementsByTagName("img")[0].src = pagingForm.forthendImage.value;
		disableLink(forth);
	}
	else {
		forth.getElementsByTagName("img")[0].src = pagingForm.forthImage.value;
		enableLink(forth);
	}
	if (insideImages[nextIndex] != null) {
		document.getElementById("illustration_" + id).getElementsByTagName("img")[0].src = insideImages[nextIndex].src;
		document.getElementById("illustration_" + id).getElementsByTagName("img")[0].alt = insideImages[nextIndex].alt;
		document.getElementById("illustration_" + id).getElementsByTagName("img")[0].title = insideImages[nextIndex].alt;
		bookForm.currentImage.value = nextIndex;
	}
}

function disableLink(elem) {
	var link = elem.getElementsByTagName("a")[0];
	link.style.cursor = "default";
	removeOutline(elem);
}

function enableLink(elem) {
	var link = elem.getElementsByTagName("a")[0];
	link.style.cursor = "pointer";
	removeOutline(elem);
}

function removeOutline(elem) {
	if (elem.attachEvent)
		elem.attachEvent('onmousedown', function () {
			event.srcElement.hideFocus = true
		});
	}

function filterBooks() {
	var chosen = document.filterForm.bookfilter[document.filterForm.bookfilter.selectedIndex].value;
	var url = window.location.href.substring(0, window.location.href.indexOf(window.location.search));
	window.location.href = url + "?uri=book/filter/" + encodeURIComponent(chosen);
}

function checkDeleteProfile() {
	var formObj = document.forms.deleteuser;
	var agreetext = formObj.agreetext.value;
	var passwordtext = formObj.insertpasswordtext.value;
	var noDelete = false;
	if (!formObj.cond1.checked || !formObj.cond2.checked || !formObj.cond3.checked) {
		alert(agreetext);
		noDelete = true;
	}
	else if (formObj.deletepassword.value.length == 0) {
		alert(passwordtext);
		noDelete = true;
	}
	return !noDelete;
}
function qsToJson(a) {
    if (a == "") return {};
    var b = {};
    for (var ind = 0; ind < a.length; ++ind) {
        
        var i = a[ind].indexOf('=');
        var splits = [a[ind].slice(0, i), a[ind].slice(i + 1)];

        if (splits.length == 1)
            b[splits[0]] = "";
        else
            b[splits[0]] = decodeURIComponent(splits[1].replace(/\+/g, " "));
    }
    return b;
}