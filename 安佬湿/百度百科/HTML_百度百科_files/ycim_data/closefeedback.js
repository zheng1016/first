// ie6 png
if(navigator.userAgent.indexOf('MSIE 6.0')>0){
    var DD_belatedPNG={ns:"DD_belatedPNG",imgSize:{},delay:10,nodesFixed:0,createVmlNameSpace:function(){if(document.namespaces&&!document.namespaces[this.ns]){document.namespaces.add(this.ns,"urn:schemas-microsoft-com:vml")}},createVmlStyleSheet:function(){var b,a;b=document.createElement("style");b.setAttribute("media","screen");document.documentElement.firstChild.insertBefore(b,document.documentElement.firstChild.firstChild);if(b.styleSheet){b=b.styleSheet;b.addRule(this.ns+"\\:*","{behavior:url(#default#VML)}");b.addRule(this.ns+"\\:shape","position:absolute;");b.addRule("img."+this.ns+"_sizeFinder","behavior:none; border:none; position:absolute; z-index:-1; top:-10000px; visibility:hidden;");this.screenStyleSheet=b;a=document.createElement("style");a.setAttribute("media","print");document.documentElement.firstChild.insertBefore(a,document.documentElement.firstChild.firstChild);a=a.styleSheet;a.addRule(this.ns+"\\:*","{display: none !important;}");a.addRule("img."+this.ns+"_sizeFinder","{display: none !important;}")}},readPropertyChange:function(){var b,c,a;b=event.srcElement;if(!b.vmlInitiated){return}if(event.propertyName.search("background")!=-1||event.propertyName.search("border")!=-1){DD_belatedPNG.applyVML(b)}if(event.propertyName=="style.display"){c=(b.currentStyle.display=="none")?"none":"block";for(a in b.vml){if(b.vml.hasOwnProperty(a)){b.vml[a].shape.style.display=c}}}if(event.propertyName.search("filter")!=-1){DD_belatedPNG.vmlOpacity(b)}},vmlOpacity:function(b){if(b.currentStyle.filter.search("lpha")!=-1){var a=b.currentStyle.filter;a=parseInt(a.substring(a.lastIndexOf("=")+1,a.lastIndexOf(")")),10)/100;b.vml.color.shape.style.filter=b.currentStyle.filter;b.vml.image.fill.opacity=a}},handlePseudoHover:function(a){setTimeout(function(){DD_belatedPNG.applyVML(a)},1)},fix:function(a){if(this.screenStyleSheet){var c,b;c=a.split(",");for(b=0;b<c.length;b++){this.screenStyleSheet.addRule(c[b],"behavior:expression(DD_belatedPNG.fixPng(this))")}}},applyVML:function(a){a.runtimeStyle.cssText="";this.vmlFill(a);this.vmlOffsets(a);this.vmlOpacity(a);if(a.isImg){this.copyImageBorders(a)}},attachHandlers:function(i){var d,c,g,e,b,f;d=this;c={resize:"vmlOffsets",move:"vmlOffsets"};if(i.nodeName=="A"){e={mouseleave:"handlePseudoHover",mouseenter:"handlePseudoHover",focus:"handlePseudoHover",blur:"handlePseudoHover"};for(b in e){if(e.hasOwnProperty(b)){c[b]=e[b]}}}for(f in c){if(c.hasOwnProperty(f)){g=function(){d[c[f]](i)};i.attachEvent("on"+f,g)}}i.attachEvent("onpropertychange",this.readPropertyChange)},giveLayout:function(a){a.style.zoom=1;if(a.currentStyle.position=="static"){a.style.position="relative"}},copyImageBorders:function(b){var c,a;c={borderStyle:true,borderWidth:true,borderColor:true};for(a in c){if(c.hasOwnProperty(a)){b.vml.color.shape.style[a]=b.currentStyle[a]}}},vmlFill:function(e){if(!e.currentStyle){return}else{var d,f,g,b,a,c;d=e.currentStyle}for(b in e.vml){if(e.vml.hasOwnProperty(b)){e.vml[b].shape.style.zIndex=d.zIndex}}e.runtimeStyle.backgroundColor="";e.runtimeStyle.backgroundImage="";f=true;if(d.backgroundImage!="none"||e.isImg){if(!e.isImg){e.vmlBg=d.backgroundImage;e.vmlBg=e.vmlBg.substr(5,e.vmlBg.lastIndexOf('")')-5)}else{e.vmlBg=e.src}g=this;if(!g.imgSize[e.vmlBg]){a=document.createElement("img");g.imgSize[e.vmlBg]=a;a.className=g.ns+"_sizeFinder";a.runtimeStyle.cssText="behavior:none; position:absolute; left:-10000px; top:-10000px; border:none; margin:0; padding:0;";c=function(){this.width=this.offsetWidth;this.height=this.offsetHeight;g.vmlOffsets(e)};a.attachEvent("onload",c);a.src=e.vmlBg;a.removeAttribute("width");a.removeAttribute("height");document.body.insertBefore(a,document.body.firstChild)}e.vml.image.fill.src=e.vmlBg;f=false}e.vml.image.fill.on=!f;e.vml.image.fill.color="none";e.vml.color.shape.style.backgroundColor=d.backgroundColor;e.runtimeStyle.backgroundImage="none";e.runtimeStyle.backgroundColor="transparent"},vmlOffsets:function(d){var h,n,a,e,g,m,f,l,j,i,k;h=d.currentStyle;n={W:d.clientWidth+1,H:d.clientHeight+1,w:this.imgSize[d.vmlBg].width,h:this.imgSize[d.vmlBg].height,L:d.offsetLeft,T:d.offsetTop,bLW:d.clientLeft,bTW:d.clientTop};a=(n.L+n.bLW==1)?1:0;e=function(b,p,q,c,s,u){b.coordsize=c+","+s;b.coordorigin=u+","+u;b.path="m0,0l"+c+",0l"+c+","+s+"l0,"+s+" xe";b.style.width=c+"px";b.style.height=s+"px";b.style.left=p+"px";b.style.top=q+"px"};e(d.vml.color.shape,(n.L+(d.isImg?0:n.bLW)),(n.T+(d.isImg?0:n.bTW)),(n.W-1),(n.H-1),0);e(d.vml.image.shape,(n.L+n.bLW),(n.T+n.bTW),(n.W),(n.H),1);g={X:0,Y:0};if(d.isImg){g.X=parseInt(h.paddingLeft,10)+1;g.Y=parseInt(h.paddingTop,10)+1}else{for(j in g){if(g.hasOwnProperty(j)){this.figurePercentage(g,n,j,h["backgroundPosition"+j])}}}d.vml.image.fill.position=(g.X/n.W)+","+(g.Y/n.H);m=h.backgroundRepeat;f={T:1,R:n.W+a,B:n.H,L:1+a};l={X:{b1:"L",b2:"R",d:"W"},Y:{b1:"T",b2:"B",d:"H"}};if(m!="repeat"||d.isImg){i={T:(g.Y),R:(g.X+n.w),B:(g.Y+n.h),L:(g.X)};if(m.search("repeat-")!=-1){k=m.split("repeat-")[1].toUpperCase();i[l[k].b1]=1;i[l[k].b2]=n[l[k].d]}if(i.B>n.H){i.B=n.H}d.vml.image.shape.style.clip="rect("+i.T+"px "+(i.R+a)+"px "+i.B+"px "+(i.L+a)+"px)"}else{d.vml.image.shape.style.clip="rect("+f.T+"px "+f.R+"px "+f.B+"px "+f.L+"px)"}},figurePercentage:function(d,c,f,a){var b,e;e=true;b=(f=="X");switch(a){case"left":case"top":d[f]=0;break;case"center":d[f]=0.5;break;case"right":case"bottom":d[f]=1;break;default:if(a.search("%")!=-1){d[f]=parseInt(a,10)/100}else{e=false}}d[f]=Math.ceil(e?((c[b?"W":"H"]*d[f])-(c[b?"w":"h"]*d[f])):parseInt(a,10));if(d[f]%2===0){d[f]++}return d[f]},fixPng:function(c){c.style.behavior="none";var g,b,f,a,d;if(c.nodeName=="BODY"||c.nodeName=="TD"||c.nodeName=="TR"){return}c.isImg=false;if(c.nodeName=="IMG"){if(c.src.toLowerCase().search(/\.png$/)!=-1){c.isImg=true;c.style.visibility="hidden"}else{return}}else{if(c.currentStyle.backgroundImage.toLowerCase().search(".png")==-1){return}}g=DD_belatedPNG;c.vml={color:{},image:{}};b={shape:{},fill:{}};for(a in c.vml){if(c.vml.hasOwnProperty(a)){for(d in b){if(b.hasOwnProperty(d)){f=g.ns+":"+d;c.vml[a][d]=document.createElement(f)}}c.vml[a].shape.stroked=false;c.vml[a].shape.appendChild(c.vml[a].fill);c.parentNode.insertBefore(c.vml[a].shape,c)}}c.vml.image.shape.fillcolor="none";c.vml.image.fill.type="tile";c.vml.color.fill.on=false;g.attachHandlers(c);g.giveLayout(c);g.giveLayout(c.offsetParent);c.vmlInitiated=true;g.applyVML(c)}};try{document.execCommand("BackgroundImageCache",false,true)}catch(r){}DD_belatedPNG.createVmlNameSpace();DD_belatedPNG.createVmlStyleSheet();
    DD_belatedPNG.fix("img,a,div,.show-cause,#closeBtn,.baidu_logo,.img,#tipWrapper");
}
!function(a){a.baiduCproPage={},function(a){var b=function(a,b){var c=new RegExp("(\\s|^)"+b+"(\\s|$)");return a.className.match(c)};a.dom={find:function(a){return""!==a?document.getElementById(a):void 0},hasClass:b,bind:function(a,b,c){a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent("on"+b,function(){c.call(a)})},getChildElement:function(a){var c,d,b=[];for(c=0,d=a.childNodes.length;d>c;c++)1===a.childNodes[c].nodeType&&b.push(a.childNodes[c]);return b},getByClass:function(a){var b,c,d,e;if(document.getElementsByClassName)return document.getElementsByClassName(a);for(b=[],c=document.getElementsByTagName("*"),d=c.length,e=0;d>e;e++)c[e].className.indexOf(a)>-1&&c[e].className==a&&b.push(c[e]);return b},css:function(a,b){if(a){var c=a.currentStyle?a.currentStyle:window.getComputedStyle(a,null);return c[b]}},addClass:function(a,c){b(a,c)||(a.className+=a.className?" "+c:c)},removeClass:function(a,c){if(b(a,c)){var d=new RegExp("(\\s|^)"+c+"(\\s|$)");a.className=a.className.replace(d," ")}}}}(a.baiduCproPage),function(a){var b=function(a){return a.target||a.srcElement},c=function(a){a.stopPropagation?a.stopPropagation():a.cancelBubble=!0};a.eventUtil={addEvent:function(a,b,c){b=b.replace(/^on/i,"").toLowerCase(),a.addEventListener?a.addEventListener(b,c,!1):a.attachEvent("on"+b,function(){c(window.event)})},removeEvent:function(a,b){eventType=eventType.replace(/^on/i,"").toLowerCase(),a.removeEventListener?a.removeEventListener(eventType,b,!1):a.detachEvent("on"+eventType,b)},hover:function(a,c,d){this.addEvent(a,"mouseover",function(d){for(var e=b(d);e!=a;)e=e.parentNode;c(e)}),this.addEvent(a,"mouseout",function(c){for(var e=b(c);e!=a;)e=e.parentNode;d(e)})},enter:function(a,b){this.addEvent(a,"keydown",function(a){13===a.keyCode&&(b(a),c(a))}),document.onkeydown=function(a){var a=a||window.event;13===a.keyCode&&b(a)}},click:function(a,b){this.addEvent(a,"click",function(a){b(a)})}}}(a.baiduCproPage),function(a){a.html={em:function(a,b,c){var d=new RegExp(b,"ig");return c=c||"red",a=a.replace(d,"<font color="+c+">"+b+"</font>")},loadCss:function(a){var d,e,b=document,c=b.createElement("style");c.setAttribute("type","text/css"),c.styleSheet?c.styleSheet.cssText=a:(d=b.createTextNode(a),c.appendChild(d)),e=b.getElementsByTagName("head"),e.length?e[0].appendChild(c):b.documentElement.appendChild(c)},loadJs:function(a,b){var d,c=document.createElement("script");c.onload=function(){b()},c.onreadystatechange=function(){/loaded|complete/.test(c.readyState)&&b()},c.src=a,d=document.getElementsByTagName("script")[0],d.parentNode.insertBefore(c,d)},getLength:function(a){return a?(a=String(a),a=a.replace(/([^\x00-\xff])/g,"$1 "),a.length/2):""},trim:function(a){return a.replace(/^\s+|\s+$/g,"")},ellipsis:function(a,b){return a?a.length<=b?a:a.substring(0,b-2)+"..":""},cutString:function(a,b,c){return a=String(a),c=c||"",0>b||a.replace(/[^\x00-\xff]/g,"ci").length<=b?a:(a=a.substr(0,b).replace(/([^\x00-\xff])/g,"$1 ").substr(0,b).replace(/[^\x00-\xff]$/,"").replace(/([^\x00-\xff]) /g,"$1"),a+c)},select:function(a,b){var c=b-a+1;return Math.floor(Math.random()*c+a)}}}(a.baiduCproPage)}(window),function(){var b,c,d,e,g,h,i,a=["#closeBtn {z-index: 2147483647; position: absolute; text-align: center; color:#C5C5C7; display:block;overflow:hidden; background: url('http://cpro.baidustatic.com/cpro/ui/noexpire/img/2.0.1/reduce_promotion_oper.png') no-repeat; cursor:pointer; ","text-decoration: none;  font-weight: 100;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,src='http://cpro.baidustatic.com/cpro/ui/noexpire/img/2.0.1/reduce_promotion_oper.png',sizingMethod='crop');_background:0  } ","#closeBtn:hover {background: url('http://cpro.baidustatic.com/cpro/ui/noexpire/img/2.0.1/reduce_promotion_oper.png') no-repeat left top;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,src='http://cpro.baidustatic.com/cpro/ui/noexpire/img/2.0.1/reduce_promotion_oper.png',sizingMethod='crop');_background:0;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,src='http://cpro.baidustatic.com/cpro/ui/noexpire/img/2.0.1/reduce_promotion_oper.png',sizingMethod='crop');}"," #closeWrapper {  position: absolute;  display: inline-block;  zoom:1;  z-index: 2147483648;  }",".closeA ,.closeB{ height:20px;  line-height: 20px;  font-size: 14px;  text-align: center;  color:#000;  margin:0px 0px 1px 0px;  display: block;  width:120px;  position:relative;  text-decoration:none;  background-color:#efefef;  border-bottom: 1px solid #7fccff;  zoom:1;  } ",".closeA:hover, .closeB:hover {  background: #7fccff;  color:#F0F0FB; cursor:pointer;  }",".arr-b {position:absolute;width:11px; height:7px;display: block;right:3px;bottom:-7px;_bottom:-16px;background: url('http://cpro.baidustatic.com/cpro/exp/closead/img/arr_hover.png') no-repeat left top;  } ",".arr-b-hover {  position:absolute;  width:11px;  height:7px;  display: block;  right:3px;  bottom:-7px;  _bottom:-16px;  background: url('http://cpro.baidustatic.com/cpro/exp/closead/img/arr.png') no-repeat left top;  } ","#tipWrapper {position: absolute;  top:0px;  left:0px;  z-index: 2147483648;  text-align:left; background: url('http://cpro.baidustatic.com/cpro/exp/closead/img/bg_rb.png') no-repeat right bottom;  background-color: #fafafa;_background-color: #fafafa;*background-color: #fafafa;_filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(enabled=true,src='http://cpro.baidustatic.com/cpro/exp/closead/img/bg_rb.png',sizingMethod='crop'); }","#tipWrapper .tit {font-size:20px;font-family:microsoft Yahei; color:#333333;line-height: 20px;padding-left:10px; background: url('http://cpro.baidustatic.com/cpro/exp/closead/img/icon_col.png') left top no-repeat;  } ","#tipWrapper .goback ,.btn-blue {font-size: 14px;color:#5ea5fc;cursor:pointer;text-decoration: underline;white-space: nowrap;word-wrap: normal;background-color:#fafafa;}","#tipWrapper .goback {display: inline-block;zoom:1;margin-left:15px; }","#tipWrapper .question_tit .goback {display: inline-block;zoom: 1;margin: 0 15px 0 0; } ","#tipWrapper .baidu_logo{width:59px;height:19px;_width:59px;_height:19px;position:absolute; _position:absolute; right:10px; bottom:10px;_right:10px;_bottom:10px;z-index:9999999999999999999}","#tipWrapper .baidu_logo img {border:0; }","#tipWrapper .question_tit{display:block;text-decoration: none;font-size: 12px; line-height: 25px;margin:5px 0;color:#333;  }","#tipWrapper .question_tittt{display:block;text-decoration: none;font-size: 12px; line-height: 20px;margin:0;color:#333;  }","#tipWrapper .mw1 {max-width: 470px;float:left;}","#tipWrapper .question_choice .choice, #tipWrapper .mw1 span {margin-right: 10px;text-decoration: none;width:120px;overflow:hidden;height:25px;line-height: 25px;  display: inline-block;zoom:1; cursor: pointer;  color:#333;  font-size: 12px;  background: url('http://cpro.baidustatic.com/cpro/exp/closead/img/ico_sel_gray.png') no-repeat left center;  padding-left:20px;  zoom:1;  }","#tipWrapper .question_choice .choice:hover{ background: url('http://cpro.baidustatic.com/cpro/exp/closead/img/ico_sel_blue.png') no-repeat left center; }","#tipWrapper .mw1 span {margin-right: 10px; height:15px; line-height: 15px; display: inline-block; cursor: pointer; color: #666666; font-size: 12px; width: 42%; overflow: hidden; text-overflow: ellipsis; background: url('http://cpro.baidustatic.com/cpro/exp/closead/img/ico_mulsel_gray.png') no-repeat left center; padding-left:20px; zoom: 1;  }","#tipWrapper .mw1 .checked{ background: url('http://cpro.baidustatic.com/cpro/exp/closead/img/ico_mulsel_blue.png') no-repeat left center; }","#tipWrapper.min_90 .question_choice .choice{ height:20px; line-height:20px; }","#tipWrapper.min_90 .question_tit{ line-height:20px; }","#tipWrapper .btn-sub { display: inline-block; zoom:1;width: 80px; height: 25px; line-height: 25px; font-size: 14px; background: none repeat scroll 0% 0% rgb(51, 132, 255); text-align: center; color: rgb(255, 255, 255); float: left; margin-left: 100px; cursor: pointer; }","#tipWrapper.tipWrapper .question_choice .choice{ height:20px; line-height:20px; }","#closePop{ clear:both;padding:10px 10px 0 10px;}","#closeEnd{ padding:10px 0 0 10px;}","#closePop .space{ padding-left:10px; }","#closePop .space .panel-cause{ position: relative; z-index:2; }","#closePop p{ clear:both; font-size:12px;_font-size:11px; color:#333; line-height:30px;_line-height:30px; }","#tipWrapper.tipWrapper #closePop p{ line-height:20px; }","#closePop .btns{ clear:both;*clear:none;font-size:12px; color:#333; line-height:0; }","#closePop .sel-panel{ position:relative; height:20px; display:inline-block; *zoom: 1; cursor:pointer; }","#closePop .sel-panel .ipt-other{ position:absolute;left:0;top:0; z-index:1; padding:0 5px; width:120px;_width:120px; height:20px; line-height:20px; border: 1px solid #d2d2d2;  color:#999; font-family:'microsoft yahei'; font-size:12px;_line-height:20px;_height:20px;  }","#closePop select{ width:131px; height:22px; line-height:20px; border:1px solid #d2d2d2; color:#999; font-size:12px; }","#closePop .causeSelect{ display:none; position:absolute; left:0; top:21px; z-index:99; width:129px; border:1px solid #d2d2d2; color:#999; font-size:12px; background-color:#fff; }","#closePop .causeSelect li{ padding: 0 5px; height:24px; line-height:24px; position:relative; z-index:99; }","#closePop .show-cause{ position:absolute; left:0; top:0; padding: 0 5px; width:119px; height:20px; line-height:20px; border:1px solid #d2d2d2; color:#999; font-size:12px; display:inline-block; zoom:1; background: #fff url('http://cpro.baidustatic.com/cpro/ui/noexpire/img/2.0.0/radio_btn.png') no-repeat right -85px; }","#closePop .sel-panel.on .show-cause{ background-position: right -106px; }","#closePop .ok-btn{ _position:absolute; _z-index:-1; width:65px; height:20px;_height:20px;  line-height:20px;_line-height:20px; margin-top:15px; text-align:center; color:#5ea5fc; text-decoration:none; display:inline-block; zoom:1; background:url('http://cpro.baidustatic.com/cpro/ui/noexpire/img/2.0.0/radio_btn.png') no-repeat 0 -43px;_background:url('http://cpro.baidustatic.com/cpro/ui/noexpire/img/2.0.0/radio_btn.png') no-repeat 0 -44px; }","#closePop .ok-btn:hover{ background:url('http://cpro.baidustatic.com/cpro/ui/noexpire/img/2.0.0/radio_btn.png') no-repeat 0 -64px;_background:url('http://cpro.baidustatic.com/cpro/ui/noexpire/img/2.0.0/radio_btn.png') no-repeat 0 -65px; color:#fff; }","#tipWrapper.wrapper_small .question_choice .choice{ height:18px; line-height:18px; }","#tipWrapper.wrapper_small #closePop p{ line-height:20px; }","#tipWrapper.wrapper_small #closePop .space{ padding-left:0; }","#tipWrapper.wrapper_small #closePop .i-email{ width:89px;float:left; }","#tipWrapper.wrapper_small #closePop .sel-panel .ipt-other{ width:89px; }","#tipWrapper.wrapper_small #closePop .show-cause{ width:89px; }","#tipWrapper.wrapper_small #closePop .causeSelect{ width:99px; }","#tipWrapper.wrapper_small .question_tit{ line-height:20px; }","#tipWrapper.min_hei .question_choice .choice{ width: auto; }","#tipWrapper.wrapper_panel #closePop .space .panel{ float:left; _width:132px; }","#tipWrapper.min_90 #closePop .causeSelect{ top:-61px }","#tipWrapper.min_90 #closePop .causeSelect li{ height:15px; line-height:15px; }","#tipWrapper.wrapper_panel #closePop .panel-email{ margin-left:20px; }","#tipWrapper.wrapper_panel #closePop .btns{ float:left;position:relative; top:16px;left: 20px; }","#tipWrapper.min_90 .complaint,#tipWrapper.min_90 .question_choice{ float:left; }","#closePop .i-email{ width:119px; height:20px; line-height:20px; padding: 0 5px; border: 1px solid #d2d2d2; font-size:12px; color:#666; font-family:'microsoft yahei' }"].join("");for(baiduCproPage.html.loadCss(a),b=[],c=[],d=[],e=0;e<bdUserPreferenceReason.length;e++)"0"==bdUserPreferenceReason[e]["type"]?b.push(bdUserPreferenceReason[e]):c.push(bdUserPreferenceReason[e]);g=function(){var c,d,e,a={},b=location.href.split("?")[1];if(b&&b.length){for(c=b.split("&"),d=0;d<c.length;d++)e=c[d].split("="),a[e[0]]=e[1];return a}}(),"undefined"==typeof config&&(config=g),h=function(a){var d,e,b="http://eclick.baidu.com/close_feedback.jpg?",c=[];for(d in a)c.push(d+"="+a[d]);e=new Image,e.src=b+c.join("&")+"&_="+(new Date).getTime()},i={init:function(){this.getLogo()},hoverTimer:null,elems:{},snippet:{},counter:0,getLogo:function(){var a=this,b=baiduCproPage.dom.find("logo")||baiduCproPage.dom.getByClass("logo")[0]||baiduCproPage.dom.getByClass("bd-logo")[0]||baiduCproPage.dom.getByClass("bd-logo2")[0]||baiduCproPage.dom.getByClass("bd-logo3")[0]||baiduCproPage.dom.getByClass("bd-logo4")[0];!b&&this.counter++<3?setTimeout(function(){a.getLogo()},50):a.draw(b)},draw:function(a){var e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t;if(a){for(e=this,e.coverFlag=!1,f={w:baiduCproPage.dom.css(a,"width"),h:baiduCproPage.dom.css(a,"height"),b:baiduCproPage.dom.css(a,"bottom"),r:baiduCproPage.dom.css(a,"right")},a.style.backgroundPosition=0,g=document.createElement("a"),h=document.createElement("div"),i=document.createElement("div"),a.style.right="29px",a.style.height=a.style.width="14px",a.style.bottom="0px",bdJinglianExpFlag>0?(a.onclick=function(){return!1},a.title=bdJinglianHoverTitle):a.href="http://wangmeng.baidu.com/",a.style.zIndex=2147483647,g.id="closeBtn",g.style.display="block",g.style.lineHeight=g.style.height=f.h="14px",g.style.width="28px",g.style.height="14px",g.style.right="0px",g.style.bottom="0px",a.parentNode.appendChild(g),titleFontSize=baiduCproPage.html.select(14,20),e.coverFlag?(a.parentNode.appendChild(h),h.id="closeWrapper",h.style.right=parseInt(f.r)+2+"px",h.style.display="none",h.style.bottom=parseInt(f.b)+parseInt(f.h)+7+"px",h.innerHTML='<a class="closeB" href="javascript:;">不想看此推广内容</a><a class="closeA" href="javascript:;">关闭此推广位显示<span class="arr-b"></span></a>'):(g.title="关闭此推广位显示",g.title.fontSize=titleFontSize),i.id="tipWrapper",i.style.display="none",i.style.width=parseInt(config.rsi0)+"px",i.style.height=parseInt(config.rsi1)+"px",j=a.parentNode,k=14,l=j.offsetWidth||j.clientWidth,m=j.offsetHeight||j.clientHeight,l>=120&&(240>=m&&(k=14,90>=m&&(k=16,i.className+="min_90 ")),l>=160&&250>l?k=15:l>=250&&300>=l?k=16:l>300&&(k=20,90>=m&&(k=14))),150>=l&&600>=m&&(i.className+="wrapper_small "),(120>=m||230>=m)&&(i.className+="min_hei "),160>=m&&(i.className+="wrapper_panel "),n="将为您关闭此次推广展示",o="此推广有什么问题？",p=[],q="",r="",s="",t=0;t<c.length;t++)q+=['<a index="',t,'" href="javascript:;" class="choice" id="',c[t]["id"],'">',c[t]["name"],"</a>"].join("");for(t=0;t<b.length;t++)r+=['<a index="',t,'" href="javascript:;" class="choice" id="',b[t]["id"],'">',b[t]["name"],"</a>"].join("");for(q&&(q='<p class="question_tit">您屏蔽此推广内容是因为？</p><p class="question_choice">'+q+"</p>"),r&&(r='<p class="question_tit">'+o+'</p><div class="question_choice">'+r+"</div>"),t=0;t<d.length;t++)s+=['<option value="'+d[t].option+'">'+d[t].name+"</option>"].join("");for(t=0;t<d.length;t++)s+=['<li class="opts" data-value="'+d[t].option+'">'+d[t].name+"</li>"].join("");p.push(['<div id="closeEnd" style="display:none">','<div class="tit" style="font-size:'+k+'px;">感谢您的反馈！</div>','<p class="question_tit"><span class="goback toAd">返回</span><a class="btn-blue" href="http://yingxiao.baidu.com/zhichi/knowledge/detail.action?channelId=3&classId=10845&knowledgeId=14394" target="_blank">了解详情</a></p>','<p class="question_tit">我们已记录您对此推广内容的反馈，以便改善您今后的浏览体验。</p>',"</div>"].join("")),p.push(['<div id="closeChoice"><div class="tit" style="width:auto;font-size:'+k+'px;">'+n+'<span class="goback">撤销</span></div>',r,"</div>",'<a href="http://www.baidu.com" target="_blank" class="baidu_logo">','<img src="http://cpro.baidustatic.com/cpro/exp/closead/img/bd_logo.png" width="59" height="19">',"</a>"].join("")),p.push(['<div id="closePop" style="display:none"><div class="tit" style="width:auto;font-size:'+k+'px;">'+n+'<span class="goback">撤销</span></div>','<div class="space">','<div class="panel panel-cause">','<p style="margin:0;">该推广还需要改进的有：</p>','<div class="sel-panel">','<input class="ipt-other" id="iptOther" type="text" value="请输入..." style="display:block;" />','<ul class="causeSelect" id="causeSelect">',s,"</ul>","</div>","</div>",'<div class="panel panel-email">','<p style="margin:0;">常用邮箱(选填)：</p>','<div class="sel-panel"><input class="i-email" id="iptEmail" type="text" /></div>',"</div>",'<div class="panel">','<p class="btns" style="margin-top:0;*margin-top:0;"><a id="affirmBtn" class="ok-btn" href="javascript:;">确认</a></p>',"</div>","</div>","</div>","</a>"].join("")),e.coverFlag&&(p.push(['<div id="coverEnd" style="display:none">','<div class="tit" style="font-size:'+k+'px;">感谢您的反馈！</div>','<p class="question_tit"><span class="goback toAd">返回</span><a class="btn-blue" href="http://yingxiao.baidu.com/zhichi/knowledge/detail.action?channelId=3&classId=10845&knowledgeId=14394" target="_blank">了解详情</a></p>','<p class="question_tit">我们已记录您对此推广内容的反馈，以便改善您今后的浏览体验。</p>',"</div>"].join("")),p.push(['<div id="coverChoice"><div class="tit" style="font-size:'+k+'px;">将为您屏蔽此推广展示<span class="goback">撤销</span></div>',q,"</div>",'<a href="http://www.baidu.com" target="_blank" class="baidu_logo">','<img src="http://cpro.baidustatic.com/cpro/exp/closead/img/bd_logo.png" width="59" height="19">',"</a>"].join(""))),i.innerHTML=p.join(""),j.appendChild(i),e.elems={logo:a,closeBtn:g,tipWrapper:i,closeChoice:baiduCproPage.dom.find("closeChoice"),closeEnd:baiduCproPage.dom.find("closeEnd"),closePop:baiduCproPage.dom.find("closePop"),causeSelect:baiduCproPage.dom.find("causeSelect"),iptOther:baiduCproPage.dom.find("iptOther"),oEmail:baiduCproPage.dom.find("iptEmail"),showCause:baiduCproPage.dom.find("showCause"),inputText:"请输入..."},e.coverFlag&&(e.elems.closeWrapper=h,e.elems.coverChoice=baiduCproPage.dom.find("coverChoice"),e.elems.coverEnd=baiduCproPage.dom.find("coverEnd")),closeChoice.style.width=parseInt(config.rsi0)-40+"px",closeChoice.style.height=parseInt(config.rsi1)-10+"px",closeChoice.style.padding="10px 10px 0 0",e.events()}},events:function(){var a=this,b=baiduCproPage.dom.hasClass;a.coverFlag?(baiduCproPage.eventUtil.hover(a.elems.closeBtn,function(){clearTimeout(a.hoverTimer),a.elems.closeWrapper.style.display="block"},function(){a.hoverTimer=setTimeout(function(){a.elems.closeWrapper.style.display="none"},200)}),baiduCproPage.eventUtil.hover(a.elems.closeWrapper,function(){clearTimeout(a.hoverTimer)},function(){a.hoverTimer=setTimeout(function(){a.elems.closeWrapper.style.display="none"},200)}),baiduCproPage.eventUtil.addEvent(a.elems.closeWrapper,"mouseover",function(a){var b=a.target||a.srcElement;"closeA"==b.className&&(b.getElementsByTagName("span")[0].style.backgroundImage="url(http://cpro.baidustatic.com/cpro/exp/closead/img/arr.png)"),"span"==b.tagName.toLowerCase()&&(b.style.backgroundImage="url(http://cpro.baidustatic.com/cpro/exp/closead/img/arr.png)")}),baiduCproPage.eventUtil.addEvent(a.elems.closeWrapper,"mouseout",function(a){var b=a.target||a.srcElement;"closeA"==b.className&&(b.getElementsByTagName("span")[0].style.backgroundImage="url(http://cpro.baidustatic.com/cpro/exp/closead/img/arr_hover.png)"),"span"==b.tagName.toLowerCase()&&(b.style.backgroundImage="url(http://cpro.baidustatic.com/cpro/exp/closead/img/arr_hover.png)")}),baiduCproPage.eventUtil.addEvent(a.elems.closeWrapper,"click",function(b){for(var c=b.target||b.srcElement;"a"!=c.tagName.toLowerCase();)c=c.parentNode;"closeA"==c.className?(a.elems.coverChoice.style.display="none",a.elems.closeChoice.style.display="block",h({type:1,action:1,filter:0,adn:1,list:1,s:preferenceInfo,dspid:4})):(a.elems.coverChoice.style.display="block",a.elems.closeChoice.style.display="none",h({type:2,action:2,filter:0,adn:1,list:6,s:preferenceInfo})),a.elems.tipWrapper.style.display="block"}),baiduCproPage.eventUtil.addEvent(a.elems.closeWrapper,"hover",function(b){for(var c=b.target||b.srcElement;"a"!=c.tagName.toLowerCase();)c=c.parentNode;"closeA"==c.className?(a.elems.coverChoice.style.display="none",a.elems.closeChoice.style.display="block",h({type:1,action:1,filter:0,adn:1,list:1,s:preferenceInfo,dspid:4})):(a.elems.coverChoice.style.display="block",a.elems.closeChoice.style.display="none",h({type:2,action:2,filter:0,adn:1,list:6,s:preferenceInfo,dspid:4})),a.elems.tipWrapper.style.display="block"})):baiduCproPage.eventUtil.addEvent(a.elems.closeBtn,"click",function(b){var d,c=b.target||b.srcElement;"closeBtn"==c.id&&(d=c.id,a.elems.closeChoice.style.display="block",a.elems.closeEnd.style.display="none",h({type:1,action:1,filter:0,adn:1,list:1,s:preferenceInfo,reasonid:d,dspid:4}),a.elems.tipWrapper.style.display="block")}),baiduCproPage.eventUtil.addEvent(a.elems.closeChoice,"click",function(c){var e,d=c.target||c.srcElement;(b(d,"goback")||b(d.parentNode,"goback"))&&(a.elems.tipWrapper.style.display="none",h({type:1,action:5,filter:0,adn:1,list:1,s:preferenceInfo,dspid:4})),b(d,"choice")&&(e=d.id,a.elems.closeChoice.style.display="none",a.elems.closePop.style.display="",h({type:1,action:3,filter:0,adn:1,list:1,s:preferenceInfo,reasonid:e,dspid:4}))}),baiduCproPage.eventUtil.addEvent(a.elems.closeEnd,"click",function(c){var d=c.target||c.srcElement;(b(d,"goback")||b(d.parentNode,"goback"))&&(a.elems.closeChoice.style.display="block",a.elems.closeEnd.style.display="none",h({type:1,action:4,filter:0,adn:1,list:1,s:preferenceInfo,dspid:4}))}),baiduCproPage.eventUtil.addEvent(a.elems.closePop,"click",function(c){var e,f,g,i,j,k,d=c.target||c.srcElement;if((b(d,"goback")||b(d.parentNode,"goback"))&&(a.elems.closeChoice.style.display="block",a.elems.closePop.style.display="none",h({type:1,action:12,filter:0,adn:1,list:1,s:preferenceInfo,dspid:4})),b(d,"ok-btn")){if(e=a.elems.oEmail.value,f="none"==a.elems.iptOther.style.display?a.elems.showCause.innerHTML:a.elems.iptOther.value,"none"!=a.elems.iptOther.style.display&&a.elems.iptOther.value==a.elems.inputText||""==a.elems.iptOther.value)return alert("请输入投诉该推广的原因!"),void 0;if(""!=a.elems.oEmail.value&&(g=/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/,!g.test(a.elems.oEmail.value)))return alert("邮箱地址不正确!"),void 0;h({type:1,action:10,filter:0,adn:1,list:0,s:preferenceInfo,email:e,report_reason:f,dspid:4}),a.elems.closePop.style.display="none",a.elems.closeChoice.style.display="none",a.elems.closeEnd.style.display="block"}if(b(d,"show-cause")){for(i=baiduCproPage.dom.getChildElement(d.parentNode),k=0;k<i.length;k++)"causeSelect"==i[k].className&&(j=i[k]);"none"==j.style.display?(baiduCproPage.dom.removeClass(d.parentNode,"on"),baiduCproPage.dom.addClass(d.parentNode,"on"),j.style.display="block"):(baiduCproPage.dom.removeClass(d.parentNode,"on"),j.style.display="none"),c.stopPropagation?c.stopPropagation():c.cancelBubble=!0}b(d,"opts")&&(a.elems.showCause.innerHTML=d.innerHTML,d.parentNode.style.display="none",d.parentNode.parentNode.className="sel-panel",a.elems.showCause.innerHTML==a.elems.inputText?(a.elems.iptOther.style.display="block",a.elems.iptOther.focus(),a.elems.iptOther.value=""):a.elems.iptOther.style.display="none")}),baiduCproPage.eventUtil.addEvent(a.elems.iptOther,"click",function(b){this.value==a.elems.inputText&&(this.value=""),b.stopPropagation?b.stopPropagation():b.cancelBubble=!0}),baiduCproPage.eventUtil.addEvent(a.elems.iptOther,"blur",function(){""==this.value&&(this.value=a.elems.inputText)}),baiduCproPage.eventUtil.addEvent(a.elems.closePop,"mouseover",function(a){var d,e,c=a.target||a.srcElement;if(b(c,"opts")){for(d=baiduCproPage.dom.getChildElement(c.parentNode),e=0;e<d.length;e++)d[e].style.backgroundColor="";c.style.backgroundColor="#f5f5f5"}}),baiduCproPage.eventUtil.addEvent(a.elems.closePop,"mouseout",function(a){var c=a.target||a.srcElement;b(c,"opts")&&(c.style.backgroundColor="")}),baiduCproPage.eventUtil.addEvent(document,"click",function(a){var b=a.target||a.srcElement;"causeSelect"!=b.className&&(baiduCproPage.dom.getByClass("causeSelect")[0].style.display="none",baiduCproPage.dom.removeClass(baiduCproPage.dom.getByClass("causeSelect")[0].parentNode,"on"))}),a.coverFlag&&(baiduCproPage.eventUtil.addEvent(a.elems.coverChoice,"click",function(c){var e,d=c.target||c.srcElement;(b(d,"goback")||b(d.parentNode,"goback"))&&(a.elems.tipWrapper.style.display="none",h({type:2,action:5,filter:0,adn:1,list:6,s:preferenceInfo,dspid:4})),b(d,"choice")&&(e=d.id,a.elems.coverChoice.style.display="none",a.elems.coverEnd.style.display="block",a.elems.closePop.style.display="none",h({type:2,action:3,filter:1,adn:1,list:1,s:preferenceInfo,reasonid:e,dspid:4}))}),baiduCproPage.eventUtil.addEvent(a.elems.coverEnd,"click",function(c){var d=c.target||c.srcElement;(b(d,"goback")||b(d.parentNode,"goback"))&&(a.elems.coverChoice.style.display="block",a.elems.coverEnd.style.display="none",a.elems.closePop.style.display="none",h({type:2,action:4,filter:2,adn:1,list:6,s:preferenceInfo,dspid:4}))}))}},i.init()}();