<template>
  <div class="container">
    <div class="logo">Linear</div>
    <div class="box">
      <div class="title"></div>
      <div class="form">
        <div class="row-border">
          <div class="row">
            <span class="icon iconfont">&#xe6b8;</span>
            <input v-model="username" placeholder="Username"/>
          </div>
        </div>
        <div class="row-border">
          <div class="row">
            <span class="icon iconfont">&#xe82b;</span>
            <input v-model="password" placeholder="Password" type="password"/>
          </div>
        </div>
        <div class="submit" @click="login">Login</div>
      </div>
    </div>
    <div class="other-button">
      <div class="button" @click="reset">Reset Password</div>
      <div class="button" @click="signup">Sign Up</div>
    </div>
  </div>
</template>

<script>
import Http from '../http/http.js'
export default {
  name: 'login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  mounted(){
    if (this.$store.state.is_login){
      this.$router.push({ name: 'index',})
    }else{
      this.check()
    }
  },
  methods: {
    async check(){
      //检查session 是否有效
      try{
        let res = await Http.checkSession()
        console.log('check_session',res)
        if (res.status == 200){
          this.$store.commit('login', res.username)
          this.$router.push({name: 'index',})
        }
      }catch (err){
        console.log(err)
        this.$message.error('网络错误');
      }
    },

    login () {
      if ( !this.username ) {
        return 
      }
      if ( !this.password ) {
        return 
      }
      Http.login(this.username, this.password).then((res)=>{
        if (res.status == 200){
          res = res.data
          let username = res.username
          this.$store.commit('login', username)
          this.$router.push({
              name: 'index',
          })
        }else{
          this.$message.error(res.data)
          console.log(res)
        }
      }).catch((err)=>{
        console.log(err)
        this.$message.error('登录失败')
      })
    },
    reset () {
      this.$router.replace({ name: 'reset' })
    },
    signup () {
      this.$router.replace({ name: 'signup' })
    }
  }
}
</script>

<style lang="scss">
.container{
  height: 100%;
  width: 100%;
  background-image: url('../assets/bg.jpg');
  background-repeat:no-repeat;
  background-size:100% 100%;
  -moz-background-size:100% 100%;
}
.logo{
  color: #5fb2dc;
  font-size: 50px;
  padding: 60px 0;
}
.box{
  width:60%;
  margin: auto;
  margin-top: 120px;
  padding: 20px;
  .title{
    height: 30px;
    line-height: 30px;
    font-weight: 500;
    color: #dedede;
    font-size: 30px;
  }
}
.form{
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  .row-border{
    margin-top: 20px;
    height: 40px;
    border:1px solid #dedede;
    border-radius: 20px;
    .row{
      padding: 0 20px;
      display: flex;
      justify-content: center;
    }
    span{
      color:#dedede;
      font-size: 26px;
      line-height: 40px;
      margin-right: 10px;
    }
    input{
      margin: auto;
      width: 100%;
      flex-shrink: 1;
      color:#dedede;
      font-size: 22px;
      outline:0;
      padding: 0;
      height: 40px;
      line-height: 40px;
      border: 0;
      background-color: transparent!important;

    }
    input::placeholder{
      color: #dedede;
      font-size: 22px;
      line-height: 40px;
      height: 40px;
      text-align: center;
      background-color: transparent!important;
    }
  }
  .submit{
    font-size: 24px;
    margin: auto;
    width: 80%;
    margin-top: 30px;
    background-color:rgba(#dedede,0.6);
    color:white;
    height: 50px;
    line-height: 50px;
    border-radius: 25px;
  }
}
.form-button{
  margin-top: 30px;
  display: flex;
  justify-content: space-between
}
.other-button{
  position: fixed;
  bottom: 0;
  display: flex;
  width: 100%;
  padding-bottom: 20px;
  color:#ededed;
  justify-content: space-around;
  .button{
    font-size: 18px;
    font-weight: 100;
    border-bottom: 1px solid #dedede
  }
}
</style>
