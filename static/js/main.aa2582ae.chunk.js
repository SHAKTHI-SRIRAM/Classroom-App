(this.webpackJsonpgui=this.webpackJsonpgui||[]).push([[0],{57:function(e,a,t){e.exports=t(88)},62:function(e,a,t){},63:function(e,a,t){},69:function(e,a,t){},70:function(e,a,t){},88:function(e,a,t){"use strict";t.r(a);var n=t(0),c=t.n(n),s=t(17),l=t.n(s),r=(t(62),t(63),t(108)),o=t(116),m=t(109),i=t(111),u=t(110),h=t(44),E=t.n(h),d=Object(r.a)((function(e){return{root:{flexGrow:1},menuButton:{marginRight:e.spacing(2)},title:{flexGrow:1,fontFamily:"Acme",fontSize:"2.7vw"}}}));function b(){var e=d();return c.a.createElement("div",{className:e.root},c.a.createElement(o.a,{position:"static",className:"navbar"},c.a.createElement(m.a,null,c.a.createElement(u.a,{edge:"start",className:e.menuButton,color:"inherit","aria-label":"menu"},c.a.createElement(E.a,null)),c.a.createElement(i.a,{variant:"h6",className:e.title},"Classroom"))))}var p=t(16),v=t.n(p),f=t(28),N=t(30),g=t(49),O=t(113),S=t(114),w=t(112),j=t(45),x=t.n(j),T=t(47),y=t.n(T),k=t(46),C=t.n(k);t(69);var _=function(){return c.a.createElement("div",{className:"classroom"},c.a.createElement("div",{className:"classroom-top"},c.a.createElement("h1",null,"Computer Science Class 11"),c.a.createElement("div",{className:"teachers"},c.a.createElement("h5",null,"Ms.Shobana")),c.a.createElement("div",{className:"stats"},c.a.createElement("h3",null,"Your Score: 2500"),c.a.createElement("h3",null,"No.of tests: 25"),c.a.createElement("h3",null,"No.of homeworks: 50"))),c.a.createElement("div",{className:"classroom-main"},c.a.createElement("div",{className:"tests"},c.a.createElement("div",{className:"top"},c.a.createElement(x.a,null),c.a.createElement("h1",null,"Tests")),c.a.createElement("div",{className:"tests-desc"},c.a.createElement("div",{className:"box"},c.a.createElement("h4",null,"Binary Addition"),c.a.createElement("p",null,"15th October")),c.a.createElement("div",{className:"box"},c.a.createElement("h4",null,"2's Complement"),c.a.createElement("p",null,"10th October")))),c.a.createElement("div",{className:"hws"},c.a.createElement("div",{className:"top"},c.a.createElement(C.a,null),c.a.createElement("h1",null,"Homeworks")),c.a.createElement("div",{className:"hw-desc"},c.a.createElement("div",{className:"hwbox"},c.a.createElement("h4",null,"Logic Gates"),c.a.createElement("p",null,"15th October")),c.a.createElement("div",{className:"hwbox"},c.a.createElement("h4",null,"Boolean Logic Book Back Questions"),c.a.createElement("p",null,"10th October"))))),c.a.createElement("div",{className:"right"},c.a.createElement("div",{className:"doubtbox"},c.a.createElement("div",{className:"chat-top"},c.a.createElement("h3",null,"Doubt Box")),c.a.createElement("div",{className:"chat-mid"},c.a.createElement("div",{className:"chat-left"},c.a.createElement("p",{className:"name-left"},"Ms.Shobana"),c.a.createElement("span",{className:"message-left"},"Hello")),c.a.createElement("div",{className:"chat-left"},c.a.createElement("p",{className:"name-left"},"Ms.Shobana"),c.a.createElement("span",{className:"message-left"},"Hello")),c.a.createElement("div",{className:"chat-left"},c.a.createElement("p",{className:"name-left"},"Ms.Shobana"),c.a.createElement("span",{className:"message-left"},"In this doubt box you can ask all your doubts.")),c.a.createElement("div",{className:"chat-left"},c.a.createElement("p",{className:"name-right"},"Me"),c.a.createElement("span",{className:"message-right"},"Hello mam")),c.a.createElement("div",{className:"chat-left"},c.a.createElement("p",{className:"name-right"},"Me"),c.a.createElement("span",{className:"message-right"},"I have doubt in Logic gates")),c.a.createElement("div",{className:"chat-left"},c.a.createElement("p",{className:"name-left"},"Ms.Shobana"),c.a.createElement("span",{className:"message-left"},"Ok pa we will discuss about it in today's class"))),c.a.createElement("div",{className:"chat-bottom"},c.a.createElement("input",{type:"text"}),c.a.createElement("button",null,c.a.createElement(y.a,null))))))},M=(t(70),t(48)),R=t.n(M).a.create({baseURL:"http://http://127.0.0.1:8000/api"}),B=Object(n.createContext)(),H=function(e){var a=e.initialState,t=e.reducer,s=e.children;return c.a.createElement(B.Provider,{value:Object(n.useReducer)(t,a)},s)};function I(e){var a=e.children,t=e.value,n=e.index,s=Object(g.a)(e,["children","value","index"]);return c.a.createElement("div",Object.assign({role:"tabpanel",hidden:t!==n,id:"vertical-tabpanel-".concat(n),"aria-labelledby":"vertical-tab-".concat(n)},s),t===n&&c.a.createElement(O.a,null,a))}function A(e){return{id:"vertical-tab-".concat(e),"aria-controls":"vertical-tabpanel-".concat(e)}}var L=Object(r.a)((function(e){return{root:{flexGrow:1,backgroundColor:e.palette.background.paper,display:"flex",height:"89.5vh"},tabs:{borderRight:"1px solid ".concat(e.palette.divider),backgroundColor:"whitesmoke",width:"15vw"}}}));function U(e){var a=Object(n.useContext)(B),t=Object(N.a)(a,2),s=t[0],l=s.user,r=s.is_teacher,o=s.is_student,m=s.classrooms,i=s.tests,u=s.homeworks,h=s.chats,E=t[1];Object(n.useEffect)((function(){function e(){return(e=Object(f.a)(v.a.mark((function e(){var a;return v.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,R.get("http://localhost:8000/api/classrooms/").then((function(e){E({type:"SET_USER",user:e.data.user}),E({type:"SET_TEACHER",teacher:e.data.is_teacher}),E({type:"SET_STUDENT",student:e.data.is_student}),E({type:"SET_CLASSROOMS",classrooms:e.data.classrooms})})).catch((function(e){console.log(e),alert("There was an error in the classroom. Please try again later.")}));case 2:return a=e.sent,e.abrupt("return",a);case 4:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function a(){return(a=Object(f.a)(v.a.mark((function e(){var a;return v.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,R.get("http://localhost:8000/api/tests/").then((function(e){E({type:"SET_TESTS",tests:e.data.tests})})).catch((function(e){console.log(e),alert("There was an error in the classroom. Please try again later.")}));case 2:return a=e.sent,e.abrupt("return",a);case 4:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function t(){return(t=Object(f.a)(v.a.mark((function e(){var a;return v.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,R.get("http://localhost:8000/api/homeworks/").then((function(e){E({type:"SET_HOMEWORKS",homeworks:e.data.homeworks})})).catch((function(e){console.log(e),alert("There was an error in the classroom. Please try again later.")}));case 2:return a=e.sent,e.abrupt("return",a);case 4:case"end":return e.stop()}}),e)})))).apply(this,arguments)}(function(){e.apply(this,arguments)})(),function(){a.apply(this,arguments)}(),function(){t.apply(this,arguments)}()}),[e]);var d=L(),b=c.a.useState(0),p=Object(N.a)(b,2),g=p[0],O=p[1];console.log(l,r,o,m,i,u,h);return c.a.createElement("div",{className:"main ".concat(d.root)},c.a.createElement(S.a,{orientation:"vertical",variant:"scrollable",value:g,onChange:function(e,a){O(a)},"aria-label":"Vertical tabs example",className:"sidebar ".concat(d.tabs)},function(){for(var e="",a=0;a<m.length;a++){var t=m[a];e+="<Tab className='sidebar-comp ' label='".concat(t.classname,"' {...a11yProps(").concat(a,")} />")}return console.log(e),e}(),c.a.createElement(w.a,Object.assign({className:"sidebar-comp ",label:"Computer Science Class 11"},A(0))),c.a.createElement(w.a,Object.assign({className:"sidebar-comp ",label:"Class Two"},A(1))),c.a.createElement(w.a,Object.assign({className:"sidebar-comp ",label:"Class Three"},A(2))),c.a.createElement(w.a,Object.assign({className:"sidebar-comp ",label:"Class Four"},A(3))),c.a.createElement(w.a,Object.assign({className:"sidebar-comp ",label:"Class Five"},A(4))),c.a.createElement(w.a,Object.assign({className:"sidebar-comp ",label:"Class Six"},A(5))),c.a.createElement(w.a,Object.assign({className:"sidebar-comp ",label:"Class Seven"},A(6)))),c.a.createElement(I,{value:g,index:0},c.a.createElement(_,null)),c.a.createElement(I,{value:g,index:1},"Item Two"),c.a.createElement(I,{value:g,index:2},"Item Three"),c.a.createElement(I,{value:g,index:3},"Item Four"),c.a.createElement(I,{value:g,index:4},"Item Five"),c.a.createElement(I,{value:g,index:5},"Item Six"),c.a.createElement(I,{value:g,index:6},"Item Seven"))}var F={fetchClassroom:"/classroom/"};var P=function(){return c.a.createElement("div",{className:"app"},c.a.createElement(b,null),c.a.createElement(U,{fetchUrl:F.fetchClassroom}))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));var G=t(8),W=function(e,a){switch(a.type){case"SET_USER":return Object(G.a)(Object(G.a)({},e),{},{user:a.user});case"SET_CLASSROOMS":return Object(G.a)(Object(G.a)({},e),{},{classrooms:a.classrooms});case"SET_TESTS":return Object(G.a)(Object(G.a)({},e),{},{tests:a.tests});case"SET_HOMEWORKS":return Object(G.a)(Object(G.a)({},e),{},{homeworks:a.homeworks});case"SET_CHATS":return Object(G.a)(Object(G.a)({},e),{},{chats:a.chats});case"SET_TEACHER":return Object(G.a)(Object(G.a)({},e),{},{is_teacher:a.teacher});case"SET_STUDENT":return Object(G.a)(Object(G.a)({},e),{},{is_student:a.student});default:return Object(G.a)({},e)}};l.a.render(c.a.createElement(c.a.StrictMode,null,c.a.createElement(H,{initialState:{user:null,is_teacher:!1,is_student:!1,classrooms:[],tests:[],homeworks:[],chats:[]},reducer:W},c.a.createElement(P,null))),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))}},[[57,1,2]]]);
//# sourceMappingURL=main.aa2582ae.chunk.js.map