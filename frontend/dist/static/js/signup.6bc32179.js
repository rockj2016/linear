(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["signup"],{"34c3":function(s,a,t){"use strict";t.r(a);var e=function(){var s=this,a=s.$createElement,t=s._self._c||a;return t("div",{staticClass:"container"},[t("div",{staticClass:"logo"},[s._v("Linear")]),t("div",{staticClass:"box"},[t("div",{staticClass:"title"}),t("div",{staticClass:"form"},[t("div",{staticClass:"row-border"},[t("div",{staticClass:"row"},[t("span",{staticClass:"icon iconfont"},[s._v("")]),t("input",{directives:[{name:"model",rawName:"v-model",value:s.username,expression:"username"}],attrs:{placeholder:"Username"},domProps:{value:s.username},on:{input:function(a){a.target.composing||(s.username=a.target.value)}}})])]),t("div",{staticClass:"row-border"},[t("div",{staticClass:"row"},[t("span",{staticClass:"icon iconfont"},[s._v("")]),t("input",{directives:[{name:"model",rawName:"v-model",value:s.password,expression:"password"}],attrs:{placeholder:"Password",type:"password"},domProps:{value:s.password},on:{input:function(a){a.target.composing||(s.password=a.target.value)}}})])]),t("div",{staticClass:"row-border"},[t("div",{staticClass:"row"},[t("span",{staticClass:"icon iconfont"},[s._v("")]),t("input",{directives:[{name:"model",rawName:"v-model",value:s.email,expression:"email"}],attrs:{placeholder:"Email"},domProps:{value:s.email},on:{input:function(a){a.target.composing||(s.email=a.target.value)}}})])]),t("div",{staticClass:"submit",on:{click:s.signup}},[s._v("Sign Up")])])]),t("div",{staticClass:"other-button"},[t("div",{staticClass:"button",on:{click:s.reset}},[s._v("Reset Password")]),t("div",{staticClass:"button",on:{click:s.login}},[s._v("Login")])])])},i=[],n=(t("a481"),t("1c03")),o={name:"signup",data:function(){return{username:"",password:"",email:""}},methods:{signup:function(){var s=this;this.username&&this.password&&this.email&&n["a"].signup(this.username,this.password,this.email).then(function(a){200===a.status?s.$message({message:"注册成功",type:"success"}):s.$message.error(a.data)}).catch(function(a){s.$message.error("注册失败")})},reset:function(){this.$router.replace({name:"reset"})},login:function(){this.$router.replace({name:"login"})}}},r=o,l=t("2877"),c=Object(l["a"])(r,e,i,!1,null,null,null);a["default"]=c.exports}}]);
//# sourceMappingURL=signup.6bc32179.js.map