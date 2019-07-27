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
        <div class="row-border">
          <div class="row">
            <span class="icon iconfont">&#xe69f;</span>
            <input v-model="email" placeholder="Email" />
          </div>
        </div>

        <div class="submit" @click="signup">Sign Up</div>
      </div>
    </div>
    <div class="other-button">
      <div class="button" @click="reset">Reset Password</div>
      <div class="button" @click="login">Login</div>
    </div>
  </div>
</template>

<script>
import Http from '../http/http.js'
export default {
  name: 'signup',
  data () {
    return {
      username: '',
      password: '',
      email: ''
    }
  },
  methods: {
    signup () {
      if (!this.username) {
        return 
      }
      if ( !this.password ) {
        return 
      }
      if ( !this.email ) {
        return 
      }
      Http.signup(this.username, this.password, this.email).then((res) => {
        if (res.status === 200) {
          this.$message({
            message:'注册成功',
            type:'success'
          })
        }else {
          this.$message.error(res.data)
        }
      }).catch((err) => {
        this.$message.error('注册失败')
      })
    },
    reset () {
      this.$router.replace({ name: 'reset' })
    },
    login () {
      this.$router.replace({ name: 'login' })
    }
  }
}
</script>
