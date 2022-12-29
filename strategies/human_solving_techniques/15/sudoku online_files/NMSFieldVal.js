// <!--
// JavaScript Document

var realbgc;

function isDate(dateStr) {

  var datePat = /^(\d{1,2})(\/|-)(\d{1,2})(\/|-)(\d{4})$/;
  var matchArray = dateStr.match(datePat); // is format OK?

  if (matchArray == null) {
    alert("Please enter date as either dd/mm/yyyy or dd-mm-yyyy.");
    return false;
  }

  // parse date into variables
  month = matchArray[3];
  day = matchArray[1];
  year = matchArray[5];

  if (month < 1 || month > 12) { // check month range
    alert("Month must be between 1 and 12.");
    return false;
  }

  if (day < 1 || day > 31) {
    alert("Day must be between 1 and 31.");
    return false;
  }

  if ((month==4 || month==6 || month==9 || month==11) && day==31) {
    alert("Month " + month + " doesn't have 31 days!")
    return false;
  }

  if (month == 2) { // check for february 29th
    var isleap = (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0));
    if (day > 29 || (day==29 && !isleap)) {
      alert("February " + year + " doesn't have " + day + " days!");
      return false;
    }
  }
  return true;  // date is valid
}
function SetCol(okay)
{
	if( okay ) return realbgc;
	return "#ffff00";
}

function display_name(item) {
     var strDisplay = item.getAttribute("DisplayName");
     if (strDisplay==null || strDisplay=="")
         strDisplay="Field";
     return strDisplay;
}

 //=========================================================

 function default_value(item) {
     var strDefault = item.defaultValue;
     if (strDefault==null || strDefault=="")
         strDefault="";
     return strDefault;
 }

 //=========================================================

 function trim_string() {
     var ichar, icount;
     var strValue = this;
     ichar = strValue.length - 1;
     icount = -1;
     while (strValue.charAt(ichar)==' ' && ichar > icount)
         --ichar;
     if (ichar!=(strValue.length-1))
         strValue = strValue.slice(0,ichar+1);
     ichar = 0;
     icount = strValue.length - 1;
     while (strValue.charAt(ichar)==' ' && ichar < icount)
         ++ichar;
     if (ichar!=0)
         strValue = strValue.slice(ichar,strValue.length);
     return strValue;
 }

 //=========================================================

 function date_toSimpleForm() {
     var toSimpleForm = new String;
     toSimpleForm = this.toLocaleString();
     toSimpleForm = toSimpleForm.substring(0,toSimpleForm.indexOf(' '));
     return toSimpleForm;
 }

 //=========================================================

 function es_non_blank(displayname) {
     var strErrorMsg = displayname + " should not be left empty";
     var item = event.srcElement;
     var okay = vs_non_blank(item);
     if( !okay )
     {
         item.focus();
         item.select();
         alert(strErrorMsg);
     }
     event.returnValue = okay;
 }

 //=========================================================

function vs_non_blank(item)
{
    var okay = true;
	item.value=item.value.Trim();
	if (item.value.length==0) okay = false;
	item.style.backgroundColor = SetCol(okay);
	return okay;
}

 //=========================================================

 function es_valid_number(displayname,minimum,do_convert)
 {
	var se_val; // Sterling Equivalent
    var item = event.srcElement;
	var okay = vs_valid_number(item,minimum);
    if( !okay )
    {
        item.focus();
        item.select();
        alert(displayname + " must be a valid number");
    }
    else if( do_convert )
    {
		se_val = item.value / document.projform.item('HiddenExchangeRate').value;
		document.projform.item(item.name + '_SE').value = '£ ' + Math.round(se_val);
    }
    event.returnValue = okay;
 }

 //=========================================================

function vs_valid_number(item,minimum)
{
	var strDefault = default_value(item);
	var okay = true;
	if (strDefault.length==0) {
	    strDefault="0";
	}
	item.value=item.value.Trim();
	if (item.value.length==0)
	    item.value=strDefault;
	var num = "-.0123456789";
	for (var intLoop = 0; intLoop < item.value.length; intLoop++) {
	    if (num.indexOf(item.value.charAt(intLoop)) == -1) okay = false;
	}
	if( okay && item.value.indexOf(".")!=item.value.lastIndexOf(".") ) okay = false;
	if( okay && item.value < minimum ) okay = false;
	item.style.backgroundColor = SetCol(okay);
	return okay;
}

 //=========================================================
/*function ForceDateFormat( adate )
{
	var s, d
	var monname = Array('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec');
	if( jsIsDate(adate) == false ) return;
	d = new Date(adate)
	s = d.toDateString();
//	s = d.getDay() + '-' + monname[d.getMonth()] + '-' + d.getYear();
	return(s);
}*/

function es_valid_date(displayname,blankokay) {
    var item = event.srcElement;
	var okay = vs_valid_date(item,blankokay);
    if( !okay )
    {
        item.focus();
        item.select();
        alert(displayname + " must be a valid Date in dd-mmm-yyyy format (and between 1900 and 2100)");
    }
//    item.value = ForceDateFormat(item.value);
    event.returnValue = okay;
}

//=========================================================
function vs_valid_date(item,blankokay)
{
	var okay = isDate(item.value);
	if( blankokay == true && item.value.length == 0 )
		okay = true;
	item.style.backgroundColor = SetCol(okay);
	return okay;
}

 //=========================================================

 function es_item_selected() {
     var item = event.srcElement;
     event.returnValue = vs_item_selected(item);
 }

 //=========================================================

 function vs_item_selected(item) {
     var strErrorMsg = display_name(item) + " must be a valid selection";
     if (item.selectedIndex==0) {
  //       item.focus();
         item.style.backgroundColor = SetCol(false);
 //        alert(strErrorMsg);
         return false;
     }
     return true;
 }

 //=========================================================

 function es_valid_zip() {
     var item = event.srcElement;
     event.returnValue = vs_valid_zip(item);
 }

 //=========================================================

 function vs_valid_zip(item) {
     var strErrorMsg = display_name(item) + " must be of the form 99999-9999";
     item.value=item.value.Trim();


     if (!(/^\d{5}$/.test(item.value) || /^\d{5}-\d{4}$/.test(item.value))) {
         item.focus();
         alert(strErrorMsg);
         return false;
     }
     return true;
 } //=========================================================
  function es_valid_ssnbr() {
     var item = event.srcElement;
     event.returnValue = vs_valid_ssnbr(item);
 } //=========================================================
  function vs_valid_ssnbr(item) {
     var strErrorMsg = display_name(item) + " must be of the form 999-99-9999";
     item.value=item.value.Trim();
     if (!(/^\d{3}-\d{2}-\d{4}$/.test(item.value))) {
         item.focus();
         alert(strErrorMsg);
         return false;
     }
     return true;
 } //=========================================================
 function es_valid_email() {
     var item = event.srcElement;
     event.returnValue = vs_valid_email(item);
 } //=========================================================
 function vs_valid_email(item) {
     var strErrorMsg = item.value + " is not a valid Email";
     item.value=item.value.Trim();
//     if (!(/^[\w\.]+@[a-z\.\-]+$/.test(item.value))) {
	 if (!(/^[A-Za-z0-9](([_\.\-]?[a-zA-Z0-9_]+)*)@([A-Za-z0-9]+)(([\.\-]?[a-zA-Z0-9]+)*)\.([A-Za-z]{2,})$/.test(item.value))) {
         item.focus();
         alert(strErrorMsg);
		 item.style.backgroundColor = SetCol(false);
         return false;
     }
	 item.style.backgroundColor = SetCol(true);
     return true;
 } //=========================================================
 // build the validation object
 function validation_setup()
 {
    this.eventNonBlank = es_non_blank;
    this.nonBlank = vs_non_blank;
    this.eventValidNumber = es_valid_number;
    this.validNumber = vs_valid_number;
    this.eventValidDate = es_valid_date;
    this.validDate = vs_valid_date;
    this.eventItemSelected = es_item_selected;
    this.itemSelected = vs_item_selected;
    this.eventValidZip = es_valid_zip;
    this.validZip = vs_valid_zip;
    this.eventValidSSNbr = es_valid_ssnbr;
    this.validSSNbr = vs_valid_ssnbr;
    this.eventValidEmail = es_valid_email;
    this.validEmail = vs_valid_email;
    return this;
 } //=========================================================

 // Extend the string object to include a trim function
 String.prototype.Trim = trim_string;
 // Extend the date object to include a simple form string conversion
 Date.prototype.toSimpleForm = date_toSimpleForm;

 // Construct the validation object
 var validation = new Object;
 validation = validation_setup();
// -->