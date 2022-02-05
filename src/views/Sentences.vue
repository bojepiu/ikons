<template>
  <v-container>
    <div class="d-flex justify-center" style="top:0; left:0; width:100vw;position:absolute;">
    <v-alert :value="alert_visible==true" :type="alert_type" dark  
    transition="scale-transition" dismissible v-on:click="alert_visible=false">{{alert_text}}</v-alert>
    </div>
    <v-expand-transition>
      <div v-show="expand">
        <v-row>
          <v-col sm="4">
            <v-select v-model="selected_topic" :items="itemsT" class="mt-3" placeholder="Select topic" @change="loadTopic"></v-select> 
          </v-col>
          <v-col sm="4">
            <v-select :items="itemsP" class="mt-3" placeholder="Select card" @change="select_card"></v-select>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" sm="6">
            <v-text-field rows="1" v-model="sentence_items" chips readonly placeholder="Sentence" filled></v-text-field>
            <v-chip-group>
              <v-chip v-if="chips_visible[0]"  close @click:close="close_chip('id')">asdasd</v-chip>
              <v-chip v-if="chips_visible[0]"  close @click:close="close_chip('id')">asdasd</v-chip>
              <v-chip v-if="chips_visible[0]"  close @click:close="close_chip('id')">asdasd</v-chip>
              <v-chip v-if="chips_visible[0]"  close @click:close="close_chip('id')">asdasd</v-chip>
              
              
            </v-chip-group>
          </v-col>
          <v-col cols="12" sm="2">
          <v-btn depressed color="primary" class="mt-3 text-none" @click="saveRegistry()">Save</v-btn>
          <v-btn depressed color="secondary" class="ml-3 mt-3 text-none" @click="cancelRegistry()">Cancel</v-btn>    
        </v-col>
        </v-row> 
      </div>
    </v-expand-transition> 
      <v-row>
        <div style="width:30%">
          <v-text-field type="text" placeholder="Search Sentence" append-icon="mdi-magnify" class="ml-4"></v-text-field>
        </div>
        <div style="width:50%" class="d-flex justify-start ml-6">
          <v-btn class="mt-3" title="New Module" fab dark color="indigo" small @click="showForm()"> 
            <v-icon id="icon_new" dark>{{icon_new}}</v-icon>
          </v-btn>
        </div>
      </v-row>    
    <v-data-table :headers="headers" :items="desserts" :items-per-page="10" class="elevation-2">
      <template v-slot:item="row">
          <tr>
            <td>{{row.item.id}}</td>
            <td>{{row.item.sentence}}</td>
            <td>{{row.item.session}}</td>
            <td>{{row.item.module}}</td>
            <td>
              <v-icon medium border>mdi-pencil-outline</v-icon> 
              <v-icon medium border>mdi-trash-can-outline</v-icon> 
            </td>
          </tr>
      </template>
    </v-data-table>
  </v-container>
</template>
<script>
import axios from 'axios'
import Sentence from '../Class/Sentence.js'

var P=process.env

export default {
  data(){
  return{
    select_value:"",
    sentence_items:[],
    sentence_object:new Sentence(),
    expand: false,
    alert_visible:false,
    alert_type:"info",
    alert_text:"",
    selected_topic:"",
    icon_new:'mdi-plus',
    list_sentences:"",
    itemsT:['Pronoums','Verbs','Verbs2','Lo que sea'],
    itemsP:[],
    chips_visible:[true,true,true],
    headers:[
      {text:"ID",align:'start',sortable:true,value:"id"},
      {text:"Sentence",align:'start',sortable:true,value:"sentence"},
      {text:"Session",align:'start',value:"session"},
      {text:"Module",align:'start',value:"module"},
      {text:"Actions",align:'start',value:"actions"}
    ],
    desserts:[
      {id:1,sentence:"I miss you",session:"Pronoms",module:"One"},
      {id:2,sentence:"Other sentence",session:"Pronoms",module:"One"},
      {id:3,sentence:"And other sentence",session:"Verbs",module:"Two"},
    ]
  }
  },
  methods:{
    showForm() {
      this.expand = !this.expand
      if(this.expand){this.icon_new='mdi-minus'}
      else{this.icon_new='mdi-plus'}
    },
    loadTopic(e){
        this.itemsP=[e+'1',e+'2',e+'3',e+'4',e+'5']
    },
    select_card(e){
      this.sentence_items.push(e)
      // if(this.list_sentences.substr(0,1)==','){
      //   this.list_sentences=this.list_sentences.substring(1,this.list_sentences.length)
      // }
      this.itemsT=this.itemsT.filter(session=>e!=session)
    },
    async show_alert(s,type_msg){
      this.alert_visible=true
      this.alert_type=type_msg
      this.alert_text=s      
      this.timeout(3000).then(()=>{
        this.alert_visible=false
      })
    },
    async get_all_topics(){
      this.show_alert("Loading data","info")
      return await axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      P.VUE_APP_ROUTE_GET_ALL_TOPIC).then(response=>{
        response.data.forEach(element => {
          this.itemsT.push(element.topicName)
        });  
        this.show_alert("Data loaded","success")
     
      }).catch(error=>{
        this.show_alert("Error: "+error,"error")
      })
    },
    saveRegistry(){
      if(this.sentence_object.id==0){
        this.show_alert("Creamos una nueva sentencia","info")
      }
      else{
        this.show_alert("Actualizamos la sentencia","info")
      }
    },
    cancelRegistry(){
      this.sentence_items=[]
      this.itemsP=[]
      this.select_value=""
      this.showForm()
    },
    editRegistry(){
      this.sentence_object=new Sentence()
      this.sentence_object.id=1
      this.sentence_object.sentence=[1,2,3]
      this.sentence_object.session="Pronoms"
      this.sentence_object.module="One"
    },
    close_chip(e){
      this.chips_visible[e]=false
      
    },
    timeout(ms) { //pass a time in milliseconds to this function
      return new Promise(resolve => setTimeout(resolve, ms));
    },
  },
  async created(){
    this.get_all_topics()
    
  }
}
</script>
