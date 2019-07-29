<template>
  <div class="container_">
    <div class="form">
      <div class="row">
        <div class="tips">标题</div>
        <input class="input" v-model=event.title />
      </div>
      <div class="row">
        <div class="tips">类型</div>
        <div class="radio_box">
          <input class="radio_input" type="radio" value="1" v-model="event.type">
          <label >时间</label>
          <input class="radio_input" type="radio" value="2" v-model="event.type">
          <label >频率</label>
          <input class="radio_input" type="radio" value="3" v-model="event.type">
          <label >计量</label>
        </div>
      </div>
      <div class="row" v-if="event.type==1">
        <div class="tips">时间</div>
        <input class="input" placeholder="HH:MM" v-model="event.time" />
      </div>
      <div class="row" v-if="event.type==2">
        <div class="tips">频率</div>
        <input class="input" v-model="event.frequency"/>
      </div>
      <div class="row" v-if="event.type==3">
        <div class="tips">数量</div>
        <input class="input" v-model="event.amount" />
      </div>
      <div class="row">
        <div class="tips">描述</div>
        <input class="input" v-model="event.desc" />
      </div>
      <div class="button_submit" v-on:click="submit">提交</div>
    </div>
  </div>
</template>

<script>
import Http from '../http/http.js'
export default {
  name: 'addevent',
  data(){
    return {
      event:{
        title:'',
        type:1,
        time:'',
        frequency:'',
        amount:'',
        desc:''
      }
    }
  },
  mounted(){
  },
  methods: {
    submit(){
      let data = this.event
      if (!data.title){
        this.$message.error('请输入标题');
        return
      }
      if (data.type===1 && !data.time){
        this.$message.error('请输入时间');
        return
      }
      if (data.type===2 && !data.frequency){
        this.$message.error('请输入频率');
        return
      }
      Http.addEvent(data).then(res=>{
        this.$message({
          message: '添加成功',
          type: 'success'
        });
        this.$router.go(-1)
      }).catch(err=>{
        this.$message.error('添加失败')
      })
    }
  }
}

</script>

<style lang="scss">
.container_{
  display: flex;
  flex-direction: column;
  width: 100%;
  background-color: rgb(240,240,240);
  min-height: 100%;
  .form{
    padding: 20px;
    margin: 20px;
    border-radius: 10px;
    background-color: white;
    display: flex;
    flex-direction: column;
    .row{
      margin: 10px;
      display: flex;
      height: 50px;
      line-height: 50px;
      .tips{
        width:60px;
        font-size: 24px;
      }
      .input{
        background-color: rgb(240,240,240);
        outline:0;
        border:0;
        height: 40px;
        margin: auto;
        text-align: center;
        width: 200px;
        border-radius: 10px;
        font-size: 20px;
        line-height: 40px;
      }
      .radio_box{
        margin: auto;
        width: 200px;
        height: 50px;
        line-height: 50px;;
      }
      .radio_input{

      }
    }
    .button_submit{
      background-color: #5fb2dc;
      color: white;
      width: 80px;
      height: 40px;
      line-height: 40px;
      margin: 30px auto;
      border-radius: 10px;
    }
  }
}
</style>
