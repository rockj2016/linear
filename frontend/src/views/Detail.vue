<template>
  <div class="container_detail">
    <div>{{event.title}} </div>
    <div v-for="log in log_list"  v-bind:key="log.id">
      <div>
        {{log.datetime}}  {{log.note}}  {{log.amount}}
      </div>
    </div>
  </div>
</template>

<script>
import http from '../http/http';

export default {
  name: 'detail',
  data(){
    return {
      event:{},
      log_list:[]
    }
  },
  mounted(){
    let params = this.$route.params
    let data = {
      event_id: params.id
    }
    http.eventDetail(data).then(res=>{
      console.log(res)
      this.event = res.data.event
      this.log_list = res.data.log_list
    }).catch(err=>{
      console.log(err)
    })
  },
  methods: {
  }
}

</script>

<style lang="scss">
.container_detail{
  display: flex;
  flex-direction: column;
  width: 100%;
  background-color: rgb(240,240,240);
  min-height: 100%;
}
</style>
