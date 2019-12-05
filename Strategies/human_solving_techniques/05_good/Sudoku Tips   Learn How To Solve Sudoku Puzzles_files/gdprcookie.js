(function(){var config={};config.enabled=1;config.text='Cookies help us deliver our services. By using our services, you agree to our use of cookies.';config.moreLinkUrl='/privacy-policy.html';config.moreLinkLabel='Learn more';config.buttonLabel='Got it!';config.position='top';var EXPLICIT_CONSENT_COOKIE_VALUE='EXPLICIT_CONSENT';var SOFT_CONSENT_COOKIE_VALUE='SOFT_CONSENT';var GDPR_CONSENT_COOKIE_NAME='gdprcookieconsent';if(config.enabled){var euCookieInitialized=false;var hasCookie=function(sKey){if(!sKey||/^(?:expires|max\-age|path|domain|secure)$/i.test(sKey)){return false;}return(new RegExp("(?:^|;\\s*)"+encodeURIComponent(sKey).replace(/[\-\.\+\*]/g,"\\$&")+"\\s*\\=")).test(document.cookie);};var getCookie=function(sKey){if(!sKey){return null;}return decodeURIComponent(document.cookie.replace(new RegExp("(?:(?:^|.*;)\\s*"+encodeURIComponent(sKey).replace(/[\-\.\+\*]/g,"\\$&")+"\\s*\\=\\s*([^;]*).*$)|^.*$"),"$1"))||null;};var addEuCookieWidget=function(config){var cookieValue=getCookie(GDPR_CONSENT_COOKIE_NAME);if((hasCookie(GDPR_CONSENT_COOKIE_NAME)&&cookieValue!==null&&cookieValue.indexOf(EXPLICIT_CONSENT_COOKIE_VALUE+"|")!==-1)||euCookieInitialized){return;}var body=document.querySelector('body');var head=document.querySelector('head');var css=document.createElement('STYLE');var widgetBar=document.createElement('DIV');var widgetText=document.createElement('P');var widgetMoreLink=document.createElement('A');var widgetButton=document.createElement('button');widgetBar.className='eucookiebar';if(config.position==='bottom'){widgetBar.className=widgetBar.className+' bottom';}widgetText.innerHTML=config.text+' ';widgetMoreLink.href=config.moreLinkUrl;widgetMoreLink.target='_blank';widgetMoreLink.innerHTML=config.moreLinkLabel;widgetButton.innerHTML=config.buttonLabel;widgetText.appendChild(widgetMoreLink);widgetText.innerHTML+='.';widgetBar.appendChild(widgetText);widgetBar.appendChild(widgetButton);css.type='text/css';css.innerHTML='.eucookiebar button,.eucookiebar p{display:inline-block;margin:.25em .5em !important;font-family:"Lucida Grande",Geneva,Arial,Verdana,sans-serif !important;}'+'.eucookiebar{text-align:center;position:absolute;top:-250px;left:0;right:0;background:#fff;padding:.5% 2%;box-shadow:0 4px 10px 1px rgba(0,0,0,.2);z-index:9999;font-size:12px;font-family:"Lucida Grande",Geneva,Arial,Verdana,sans-serif;color:#666;transition:top .5s ease,bottom .5s ease, opacity .5s ease}'+'.eucookiebar a{color:#00f;font-weight:400;text-decoration:underline}'+'.eucookiebar a:visited{color:#551A8B}'+'.eucookiebar a:active{color:red}'+'.eucookiebar button{background:#eee;border:1px solid #888;border-radius:4px;font-size:100%;font-weight:700;color:#666}'+'.eucookiebar button:hover{background:#666;color:#fff}'+'.eucookiebar.show{top:0;opacity:1;}'+'.eucookiebar.hide{top:-250px;opacity:0;pointer-events:none;}'+'.eucookiebar.bottom{top:auto;bottom:-250px;position:fixed;}'+'.eucookiebar.bottom.show{bottom:0;}'+'.eucookiebar.bottom.hide{bottom:-250px;}';head.appendChild(css);body.appendChild(widgetBar);setTimeout(function(){widgetBar.className=widgetBar.className+' show';},10);widgetButton.addEventListener("click",function(){widgetBar.className=widgetBar.className+' hide';loadURL("/bin/gdpr-consent.pl",function(){var expires=new Date();var status=this.status;var json;try{json=JSON.parse(this.responseText);if(status===200){if(typeof json==="object"){if(json.id&&json.consent===EXPLICIT_CONSENT_COOKIE_VALUE){expires.setFullYear(expires.getFullYear()+10);document.cookie=GDPR_CONSENT_COOKIE_NAME+'='+EXPLICIT_CONSENT_COOKIE_VALUE+'|'+json.id+'; expires='+expires.toUTCString();}}}}catch(e){}},function(){},'post','consent='+EXPLICIT_CONSENT_COOKIE_VALUE);},false);euCookieInitialized=true;};var euCookieInit=function(){var isCookieSet=hasCookie(GDPR_CONSENT_COOKIE_NAME);if(isCookieSet&&getCookie(GDPR_CONSENT_COOKIE_NAME)===null){loadURL("/bin/gdpr-consent.pl",function(){var expires=new Date();var status=this.status;var json;try{json=JSON.parse(this.responseText);if(status===200){if(typeof json==="object"){if(json.id&&json.consent===SOFT_CONSENT_COOKIE_VALUE){expires.setFullYear(expires.getFullYear()+10);document.cookie=GDPR_CONSENT_COOKIE_NAME+'='+SOFT_CONSENT_COOKIE_VALUE+'|'+json.id+'; expires='+expires.toUTCString();}}}}catch(e){}},function(){},'post','consent='+SOFT_CONSENT_COOKIE_VALUE);}else if(!isCookieSet){var expires=new Date();expires.setFullYear(expires.getFullYear()+10);document.cookie=GDPR_CONSENT_COOKIE_NAME+'=; expires='+expires.toUTCString();}document.addEventListener("DOMContentLoaded",function(){addEuCookieWidget(config);},false);if(!euCookieInitialized&&document.body){addEuCookieWidget(config);}};var xhrSuccess=function(){this.callback.apply(this,this.arguments);};var xhrError=function(){if(!this.errorCallback){return;}this.errorCallback.apply(this,this.arguments);};var loadURL=function(sURL,fCallback,fErrorCallback,sMethod,sData){var oReq=new XMLHttpRequest();oReq.callback=fCallback;oReq.errorCallback=fErrorCallback;oReq.arguments=Array.prototype.slice.call(arguments,2);oReq.onload=xhrSuccess;oReq.onerror=xhrError;oReq.open(sMethod||"get",sURL,true);oReq.setRequestHeader("Content-type","application/x-www-form-urlencoded");oReq.send(sData);};euCookieInit();}}());