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
            <v-text-field v-model="session.sessionName" placeholder="Name"></v-text-field>
          </v-col>
          <v-col sm=12 md=4 lg=6>
            <v-text-field v-model="session.sesionDesc" placeholder="Description" class="pl-3"></v-text-field>
          </v-col>
        </v-row>
          <v-row>
            <v-col sm=12 md=4 lg=4>
            <v-select id="select_sentences" :items="data_sentences" item-text="sentenceName" item-value="cveSentence" class="mt-3" placeholder="Select sentences" @change="select_sentence"></v-select>
          </v-col>
          <v-col sm=12 md=8 lg=8>
            <v-chip-group>
              <v-chip close v-for="(item) in session_items" :key="item.key" :value="item.text" @click:close="delete_sentence(item)">{{item.text}}
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
    <!--SEARCH-->
    <v-row>
      <div style="width:30%">
        <v-text-field  v-model="search" type="text" placeholder="Search Session" append-icon="mdi-magnify" class="ml-4"></v-text-field>
      </div>
      <div style="width:50%" class="d-flex justify-start ml-6">
        <v-btn class="mt-3" title="New Module" fab dark color="indigo" small @click="showForm()"> 
          <v-icon id="icon_new" dark>{{icon_new}}</v-icon>
        </v-btn>
      </div>
    </v-row>    
    <v-data-table :headers="headers" :items="filteredItems" :items-per-page="10" class="elevation-2">
      <template v-slot:item="row">
          <tr>
            <td>{{row.item.cveSession}}</td>
            <td>{{row.item.sessionName}}</td>
            <td>{{row.item.sesionDesc}}</td>
            <td>{{row.item.sentences.length}}</td>
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
import Session from '../Class/Session'
var P=process.env

export default {
  //Validar como funciona al motar para validar sesion valida
  data(){
  return{
    expand: false,
    icon_new:'mdi-plus',
    alert_visible:false,
    session: new Session(),
    session_items:[],
    search:"",
    txt_btn_save:"Save",
    data_sentences:[],
    table_data_sessions:[],
    itemsT:['This is a sentence','Composed with multiple cards','Not in order','Are you ready'],
    headers:[
      {text:"ID",align:'start',sortable:true,value:"cveSession"},
      {text:"Name",align:'start',sortable:true,value:"sessionName"},
      {text:"Description",align:'start',sortable:true,value:"sesionDesc"},
      {text:"Sentences",align:'start',value:"sentences"},
      {text:"Actions",align:'start',value:"actions"}
    ],
    desserts:[
      {id:1,name:"Session Pronoums",description:"Session Pronoums",sentences:5},
      {id:2,name:"Session Verbs",description:"Session verbs",sentences:1},
      {id:3,name:"Session Present",description:"Session present continuos",sentences:3},
    ]
  }
  },
  methods:{
    showForm() {
      this.expand = !this.expand
      if(this.expand){this.icon_new='mdi-minus'}
      else{this.icon_new='mdi-plus'}
    },
    select_sentence(e){
      var sentenceName=""
      this.data_sentences.forEach(el=>{
        if(el.cveSentence==e){
          sentenceName=el.sentenceName
          return
        }
      })
      this.session_items.push({key:e,text:sentenceName})
      this.data_sentences=this.data_sentences.filter(sentence=>e!=sentence.cveSentence)
    },
    delete_sentence(e){
      this.session_items=this.session_items.filter(item=>item.key!=e.key)
      this.data_sentences.push({cveSentence:e.key,sentenceName:e.text})
    },
    cancelRegistry(){
      this.session = new Session()
      this.txt_btn_save="Save"
      this.session_items=[]
      this.data_sentences=[]
      this.getSessionsWithoutAssign()
      this.showForm()
    },
    saveRegistry(){
      this.show_alert('Saving session, please wait!','info')
      if(this.session.sessionName=="" || this.session.sessionName.length<3){
        this.show_alert("Name is required at least 4 chars",'error')
        return
      }
      if(this.session_items.length<1){
        this.show_alert("At least one sentece is required to create a session",'error')
        return
      }
      this.session_items.forEach(e=>{
        this.session.sentences.push({cveSentence:e.key})
      })
      console.log(this.session.sentences)
      axios.post(P.VUE_APP_SERVER_HOST+':'+P.VUE_APP_SERVER_PORT+P.VUE_APP_INSERT_SESSION,{cveSession:this.session.cveSession,sessionName:this.session.sessionName,
      sessionDesc:this.session.sesionDesc,sentences:this.session.sentences}).then(res=>{
        console.log(res.status_code)
        this.session = new Session()
        this.session_items=[]
        this.data_sentences=[]
        this.getSessionsWithoutAssign()
        this.show_alert("Session saved!","success")
        this.getAllSessions()
        this.getSessionsWithoutAssign()
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
      this.show_alert('Session saved!','success')
    },
    edit_session_registry(session){
      this.expand=true
      this.session.cveSession=session.cveSession
      this.session.sessionName=session.sessionName
      this.session.sesionDesc=session.sesionDesc
      this.session_items=[]
      session.sentences.forEach(sentence=>{    
        this.session_items.push({key:sentence.cveSentence,text:sentence.sentenceName})
      })
     
      this.txt_btn_save="Update"
    },
    delete_session_registry(id){
      console.log(id)
      let x=confirm("Are you sure delete this session?")
      if(x){
        try {
          axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_DELETE_SESSION+"?cveSession="+id).then(()=>{
            this.getSessionsWithoutAssign()
            this.getAllSessions()
            this.show_alert("Session deleted!","success")
          }).catch((error)=>{
            console.log(error)
            this.show_alert("Error in server to delete id:"+id,"error")  
          })
        } catch (error) {
          console.log(error)
          this.show_alert("Error in server to delete id:"+id,"error")
        }
        
        
      }
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
    //De momento get_all_sessions
    getSessionsWithoutAssign(){
      this.data_sentences=[]
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+'/ikon/v1/sentence/notassociated/')
      return axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      '/ikon/v1/sentence/notassociated/').then(response=>{
        if(response.status==204){
          console.log("No data")
          this.data_sentences=[]
          return
        }
        if(response.data!=undefined && response.data.length>0){
          response.data.forEach(element => {
            this.data_sentences.push(element)
          });
        }
        else
        this.data_sentences=[]
        this.show_alert("Data loaded","success")
      }).catch(error=>{
        console.log(error)
        this.show_alert("Error: "+error,"error")
      })
    },
    getAllSessions(){
      this.show_alert("Loading data, please wait","info")
      this.table_data_sessions=[]
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_GET_ALL_SESSIONS)
      return axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      P.VUE_APP_GET_ALL_SESSIONS).then(response=>{
        if(response.status==204){
          console.log("No data")
          this.table_data_sessions=[]
          this.show_alert("Data loaded","success")
          return
        }
        if(response.data!=undefined && response.data.length>0){
          console.log(response.data)
          response.data.forEach(element => {
            this.table_data_sessions.push(element)
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
      await this.getSessionsWithoutAssign()
      await this.getAllSessions()
  },
  computed: {
    filteredItems () {
      // return this.table_data_sessions
      return this.table_data_sessions.filter(item => {
         return (item.sessionName.toString().toLowerCase().indexOf(this.search.toLowerCase()) > -1 ||
         item.cveSession.toString().indexOf(this.search.toLowerCase()) > -1)
      })
    }
  }
}
</script>
<!--PARA EL BUEN ISRA, NO SE PUEDE ELIMINAR SESSION, LISTAR SENTENCIAS SIN ASIGNACION, UPDATE_ERROR-->