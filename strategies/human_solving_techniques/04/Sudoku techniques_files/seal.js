var __Cascade={};__Cascade.PNG24=
/*@cc_on !(@_jscript_version<=5.6||(@_jscript_version==5.7&&!window.XMLHttpRequest))&& @*/
true;__Cascade.Loaded=__Cascade.Loaded||false;(function(l){var c="seal.digicert.com",d=c+"/seals/",h="https://"+c+"/seals/popup/",n="cascade",o="s",b="m",e="l",g="black",m="white",a=550,j=[1,2,8,9],p="log-errors",k="allow-test-seal",i=(function(){var q=[],u=function(){if(__Cascade.Loaded){return false}__Cascade.Loaded=true;q=__dcid||[];r()},r=function(){for(var L=0,M=q.length;L<M;L++){if(q[L].length!=5){continue}var F=q[L][0]||false,B=document.getElementById(F),J=parseInt(q[L][1],10)||3,z=q[L][2]||b,x=q[L][3]||g,E="";if(!B){continue}if(B.getElementsByTagName("DIV").length>0){B.id=F+"_"+L;B=document.getElementById(F)}if(!B){continue}E=B.getAttribute("data-language")||E;if(typeof J!=="number"||J=="NaN"||J<1||J>17){J=3}if(z!==o&&z!==b&&z!==e){z=b}if(x!==g&&x!==m){x=g}var G=B.getElementsByTagName("A")[0],K=null,y=null;if(G){B.innerHTML="<span>"+B.innerHTML+"</span>";K=B.getElementsByTagName("SPAN")[0];if(K){y=K.getElementsByTagName("A")[0];t(K,{color:x,cursor:"default"});t(y,{color:x,display:"inline"},true)}}var D=document.createElement("img"),C=q[L][4]||0,N=(s(J,j)>-1)?820:890,A=document.URL.split("/")[2]||"",H=(document.URL.split("/").pop().indexOf(p)>-1),I="//"+d+n+"/?s="+C+","+J+","+z+","+A;if(H){I+="&"+p}if(!__Cascade.PNG24){I+="&png8"}if(B.className.indexOf(k)>-1){I+="&"+k}t(D);D.src=I;D.onclick=v(h,C,A,N,a,H,E);D.onkeydown=function(O){if((O.keyCode==13)||(O.keyCode==32)){D.click()}};D.setAttribute("alt","DigiCert Seal");D.setAttribute("tabindex","0");var w=document.createElement("div");t(w,{cursor:"default"});w.id=F+"Seal";w.appendChild(D);B.insertBefore(w,K)}},v=function(A,x,z,C,w,y,B){return function(){sp=l.open(A+"?tag="+x+"&url="+z+(y?"&"+p:"")+(B.length>0?"&lang="+B:"")+"&cbr="+new Date().getTime(),"seal","height="+C+",width="+w+",scrollbars=1");if(sp&&sp.focus){sp.focus()}}},t=function(z,y,x){var w=z.style,A=w.cssText||"";w.cssText="";w.color="";w.textDecoration="none";w.textAlign="center";w.display="block";w.verticalAlign="baseline";w.fontSize="100%";w.fontStyle="normal";w.textIndent=0;w.lineHeight=1;w.width="auto";w.margin="0 auto";w.padding=0;w.border=0;w.background="transparent";w.position="relative";w.top=0;w.right=0;w.bottom=0;w.left=0;w.clear="both";w.cssFloat="none";w.styleFloat="none";w.cursor="pointer";if(typeof y==="object"){for(prop in y){w[prop]=y[prop]}}if(typeof x!=="undefined"&&A.length>0){w.cssText=w.cssText+";"+A}},s=function(y,z){if(z.indexOf){return z.indexOf(y)}for(var w=0,x=z.length;w<x;w++){if(z[w]===y){return w}}return -1};return{init:u}}()),f=(function(){var q=false,r=function(){if(!document.body){return setTimeout(r,1)}q=true;if(!__Cascade.Loaded){i.init()}},t=false,s=function(){if(t||__Cascade.Loaded){return}t=true;if(document.readyState==="complete"){return setTimeout(r,1)}if(document.addEventListener){document.addEventListener("DOMContentLoaded",r,false);l.addEventListener("load",r,false)}else{document.attachEvent("onreadystatechange",r);l.attachEvent("onload",r);var v=false;try{v=l.frameElement==null}catch(w){}if(document.documentElement.doScroll&&v){u()}}},u=function(){if(q){return}try{document.documentElement.doScroll("left")}catch(v){setTimeout(u,1);return}r()};return{init:s}}());f.init()}(window));