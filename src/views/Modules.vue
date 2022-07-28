<template>
  <v-container>
    <!--ALERT-->
    <div v-if="alert_visible" class="d-flex justify-center" style="top:0; left:0; width:100vw;position:absolute;">
    <v-alert  :type="alert_type"
      transition="scale-transition" dismissible v-on:click="alert_visible=false">{{alert_text}}</v-alert>
    </div>
     <!--SESSION FORM-->
    <v-expand-transition>
      <div v-show="expand">
        <v-row>
          <v-col sm=12 md=4 lg=6>
            <v-text-field v-model="module.moduleName" placeholder="Name"></v-text-field>
          </v-col>
          <v-col sm=12 md=4 lg=6>
            <v-text-field v-model="module.moduleDesc" placeholder="Description" class="pl-3"></v-text-field>
          </v-col>
        </v-row>
          <v-row>
            <v-col sm=12 md=4 lg=4>
            <v-select id="select_sessions" :items="data_sessions" item-text="sessionName" item-value="cveSession" class="mt-3" placeholder="Select sessions" @change="select_session"></v-select>
          </v-col>
          <v-col sm=12 md=8 lg=8>
            <v-chip-group>
              <v-chip close v-for="(item) in module_items" :key="item.key" :value="item.text" @click:close="delete_session(item)">{{item.text}}
              </v-chip>
            </v-chip-group>
          </v-col>
        </v-row>
        <v-row>
          <v-col sm=6 md=6 lg=6 class="d-flex justify-end">
            <v-btn depressed color="primary" class="mt-3 text-none" @click="saveRegistry()">{{txt_btn_save}}</v-btn>
          </v-col>
          <v-col sm=6 md=6 lg=6 class="d-flex justify-start">
            <v-btn depressed color="secondary" class="ml-3 mt-3 text-none" @click="cancelRegistry();">Cancel</v-btn>    
          </v-col>
        </v-row>
      </div>
    </v-expand-transition>
    <v-row>
      <div style="width:30%">
        <v-text-field
          type="text"
          placeholder="Search Module"
          append-icon="mdi-magnify"
          v-model="search"
          class="ml-4"
        ></v-text-field>
      </div>
      <div style="width:50%" class="d-flex justify-start ml-6">
        <v-btn
          class="mt-3"
          title="New Module"
          fab
          dark
          color="indigo"
          small
          @click="showForm()"
        >
          <v-icon id="icon_new" dark>{{ icon_new }}</v-icon>
        </v-btn>
      </div>
    </v-row>
    <v-data-table :headers="headers" :items="filteredItems" :items-per-page="10" class="elevation-2">
      <template v-slot:item="row">
          <tr>
            <td>{{row.item.cveModule}}</td>
            <td>{{row.item.moduleName}}</td>
            <td>{{row.item.moduleDesc}}</td>
            <td>{{row.item.sessione.length}}</td>
            <!-- <td>{{row.item.sentences}}</td> -->
            <td>
              <v-icon medium border @click="edit_session_registry(row.item)">mdi-pencil-outline</v-icon> 
              <v-icon medium border  @click="delete_session_registry(row.item.cveSession)">mdi-trash-can-outline</v-icon> 
            </td>
          </tr>
      </template>
    </v-data-table>
  </v-container>
</template>
<script>
import axios from 'axios'
import Module from '../Class/Module'
var P=process.env

export default {
  //Validar como funciona al montar para validar sesion valida
  data(){
  return{
    dialog:false,
    expand: false,
    txt_btn_save:'Save',
    icon_new:'mdi-plus',
    alert_visible:false,
    alert_type:"info",
    alert_text:"",
    search:"",
    list_sessions:"",
    data_sessions:"",
    module_items:[],
    module:new Module(),
    table_data_modules:[],
    itemsT:[],
    headers:[
      {text:"ID",align:'start',sortable:true,value:"cveModule"},
      {text:"Name",align:'start',sortable:true,value:"moduleName"},
      {text:"Description",align:'start',sortable:true,value:"moduleDesc"},
      {text:"Sentences",align:'start',value:"sessione"},
      {text:"Actions",align:'start',value:"actions"}
    ],
    desserts:[]
  }
  },
  methods:{
    showForm() {
      this.expand = !this.expand
      if(this.expand){this.icon_new='mdi-minus'}
      else{this.icon_new='mdi-plus'}
    },
    select_session(e){
      var sessionName=""
      this.data_sessions.forEach(el=>{
        if(el.cveSession==e){
          sessionName=el.sessionName
          return
        }
      })
      this.module_items.push({key:e,text:sessionName})
      this.data_sessions=this.data_sessions.filter(session=>e!=session.cveSession)
      console.log(this.module_items)
    },
    delete_session(e){
      this.module_items=this.module_items.filter(item=>item.key!=e.key)
      this.data_sessions.push({cveSession:e.key,sessionName:e.text})
    },
    saveRegistry(){
      this.show_alert('Saving module, please wait!','info')
      if(this.module.moduleName=="" || this.module.moduleName.length<3){
        this.show_alert("Name is required at least 4 chars",'error')
        return
      }
      if(this.module_items.length<1){
        this.show_alert("At least one sentece is required to create a session",'error')
        return
      }
      this.module_items.forEach(e=>{
        this.module.sesiones.push({cveSesion:e.key})
      })
      console.log({cveModule:this.module.cveModule,moduleName:this.module.moduleName,
      moduleDesc:this.module.moduleDesc,sesiones:this.module.sesiones})
      axios.post(P.VUE_APP_SERVER_HOST+':'+P.VUE_APP_SERVER_PORT+P.VUE_APP_INSERT_MODULE,{cveModule:this.module.cveModule,moduleName:this.module.moduleName,
      moduleDesc:this.module.moduleDesc,sesiones:this.module.sesiones}).then(res=>{
        console.log(res.status_code)
        this.module = new Module()
        this.module_items=[]
        this.data_sessions=[]
        this.getSessions()
        this.show_alert("Module saved!","success")
        this.getAllModules()
      }).catch(err=>{
        this.txt_btn_save="Save"
        if(err.response.status==400){
          alert(err.response.data)
          console.log(err.response)
        }else{
          alert("Error al registrar, intente nuevamente si el error persiste comuniquese con IPSRA")
        }
      })
      this.txt_btn_save="Save"
      this.show_alert('Module saved!','success')
    },
    cancelRegistry(){
      this.module = new Module()
      this.txt_btn_save="Save"
      this.module_items=[]
      this.data_sessions=[]
      this.getAllSessions()
      this.showForm()
    },
    timeout(ms) { //pass a time in milliseconds to this function
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    show_alert(s="vacio",type_msg="info"){
      this.alert_visible=true
      this.alert_type=type_msg
      this.alert_text=s      
      this.timeout(3000).then(()=>{
        this.alert_visible=false
      })
    },
    getAllSessions(){
      this.data_sessions=[]
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_GET_ALL_SESSIONS)
      return axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      P.VUE_APP_GET_ALL_SESSIONS).then(response=>{
        console.log(response)
        if(response.status==204){
          console.log("No data")
          this.data_sessions=[]
          return
        }
        if(response.data!=undefined && response.data.length>0){
          response.data.forEach(element => {
            this.data_sessions.push(element)
          });
        }
        else
        this.data_sessions=[]
        this.show_alert("Data loaded","success")
      }).catch(error=>{
        console.log(error)
        this.show_alert("Error: "+error,"error")
      })
    },
    getAllModules(){
      this.show_alert("Loading data, please wait","info")
      this.table_data_modules=[]
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_GET_ALL_MODULES)
      return axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      P.VUE_APP_GET_ALL_MODULES).then(response=>{
        if(response.status==204){
          console.log("No data")
          this.table_data_modules=[]
          this.show_alert("Data loaded","success")
          return
        }
        if(response.data!=undefined && response.data.length>0){
          console.log(response.data)
          response.data.forEach(element => {
            this.table_data_modules.push(element)
          });
        }
        this.show_alert("Data loaded","success")
      }).catch(error=>{
        console.log(error)
        this.show_alert("Error: "+error,"error")
      })
    }
  },
  async created(){
    await this.getAllSessions()
    await this.getAllModules()
  },
  computed: {
    filteredItems () {
      // return this.table_data_modules
      return this.table_data_modules.filter(item => {
        console.log(item)
         return (item.moduleName.toString().toLowerCase().indexOf(this.search.toLowerCase()) > -1 ||
         item.cveModule.toString().indexOf(this.search.toLowerCase()) > -1)
      })
    }
  }
}
</script>
