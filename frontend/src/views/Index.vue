<template>
  <div class="container_">
    <div class="tool">
      <div class="time">
        12:00
      </div>
      <div class="add" v-on:click="add">
        <span class="icon iconfont">&#xe6b9;</span>
      </div>
    </div>

    <div class="event_box">
      <div class="event" v-for="item in data" v-bind:key="item.id">
        <div class="event_title">{{item.title}}</div>
        <div v-if="item.type==1" class="event_type">
          <div class="type">定时 :</div>
          <div class="quant">{{item.time}}</div>
        </div>
        <div v-else-if="item.type==2" class="event_type">
          <div class="type">频率 :</div>
          <div class="quant">{{item.frequency}}</div>
        </div>
        <div v-else class="event_type">
          <div class="type">计量 :</div>
          <div class="quant">{{item.amount}}</div>
        </div>
        <div class="grow"></div>
        <div class="button_log" v-on:click="show(item.id,item.type)">log</div>
      </div>
    </div>
    <div class="dialog" v-if="show_dialog" v-on:click="close_dialog">
      <div class="dialog_box" v-on:click.stop="">
        <div class="close_dialog">
          <div class="close_button"></div>
          <div class="close_button" v-on:click="close_dialog"><span class="icon iconfont">&#xe69a;</span></div>
        </div>
        <div class="row" v-if="log_data.type!=1">
          <div class="tips">数量</div>
          <input class="input" v-model="log_data.amount" />
        </div>
        <div class="row">
          <div class="tips">备注</div>
          <input class="input" v-model="log_data.note" />
        </div>
        <div class="button" v-on:click="log">Log</div>
      </div>
    </div>
  </div>
  
</template>

<script>
import http from '../http/http';

export default {
  name: 'index',
  data(){
    return {
      data:[],
      log_data:{
        event_id:'',
        type:'',
        amount:'',
        note:''
      },
      show_dialog:false
    }
  },
  mounted(){
    http.eventList().then(res=>{
      console.log(res)
      this.data = res.data
    }).catch(err=>{
      console.log(err)
    })
  },
  methods: {
    show(event_id,type){
      console.log(event_id,type)
      this.log_data.event_id = event_id
      this.log_data.type = type
      this.show_dialog = true

    },
    add(){
      this.$router.push({
        name: 'addevent'
      })
    },
    close_dialog(){
      this.show_dialog = false
    },
    log(){
      if (this.log_data.type === 3){
        if (!this.log_data.amount){
          this.$message.error('请输入数值');
        }
        return
      }
      http.addLog(this.log_data).then((res)=>{
        console.log(res)
        if (res.status == 201){
          this.$message({
            message: '添加成功',
            type: 'success'
          })
          this.show_dialog = false
          this.log_data.note = ''
          this.log_data.amount = ''
        }else{
          this.$message.error(res.data);
        }

      }).catch(err=>{
        console.log(err)
        this.$message.error('记录失败');
      })
    }
  }
}

</script>

<style lang="scss">
.container_{
  
  .dialog{
    position: fixed;
    width: 100%;
    height: 100%;
    background-color: rgba($color: #000000, $alpha: 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    .dialog_box{
      border-radius: 15px;
      background-color: white;
      width: 80%;
      .close_dialog{
        width: 100%;
        height: 20px;
        display: flex;
        justify-content: space-between;
        .close_button{
          font-size: 20px;
          margin: 15px;
          span{
            font-size: 20px;
          }
        }
      }
      // height: 220px;
      .row{
        margin: 30px 10px;
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
      }
      .button{
        font-size: 24px;
        height: 60px;
        line-height: 60px;
        width: 100%;
        background-color: #5fb2dc;
        color: white;
        border-radius: 0 0 15px 15px;
        align-self:flex-end;
      }
    }
  }

  display: flex;
  flex-direction: column;
  width: 100%;
  background-color: rgb(240,240,240);
  min-height: 100%;
  .tool{
    padding: 20px 20px 0 20px;
    display: flex;
    justify-content: space-between;
    .time{
      flex-grow: 1;
      color:#5fb2dc;
      font-size: 40px;
      line-height: 50px;
      // width: 200px;
      text-align: center;
      font-family:Comic Sans
    }
    .add{
      width: 50px;
      height: 50px;
      border-radius: 15px;
      background-color: white;
      color: #5fb2dc;

      box-shadow: 3px 3px 3px #888888;

      span{
        font-weight: 600;
        line-height: 50px;
        text-align: center;
        font-size: 40px;
        color: #5fb2dc;
      }
    }
  }
  .event_box{
    padding:0 20px;
    .event{
      display: flex;
      // justify-content: space-between;
      // border:1px solid black;
      background-color: white;
      border-radius: 15px;
      box-shadow: 4px 4px 4px #888888;
      height: 80px;
      margin: 20px 0;
      .event_title{
        margin: 0 10px;
        font-size: 22px;
        font-weight: 600;
        padding:0 20px;
        line-height: 80px;
        height: 100%;
      }
      .event_type{
        margin-left: 10px;
        height: 80px;
        line-height: 80px;
        display: flex;
        justify-content: center;
        .type{
          margin:0 10px;
        }
        .quant{

        }
      }
      .grow{
        flex-grow: 2
      }
      .button_log{
        background-color: rgba(141, 211, 247, 0.849);
        width: 80px;
        height: 100%;
        line-height: 80px;
        border-radius: 15px ;
        align-self: flex-end;
        color: white;
        font-size: 22px;
        font-weight: 600
      }

    }
  }
}
</style>
