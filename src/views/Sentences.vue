<template>
  <v-container>
    <div v-if="alert_visible" class="d-flex justify-center" style="top:0; left:0; width:100vw;position:absolute;">
      <v-alert  :type="alert_type"
        transition="scale-transition" dismissible v-on:click="alert_visible=false">{{alert_text}}</v-alert>
      </div>
    <v-expand-transition>
      <div v-show="expand">
        <v-row class="mt-6">
          <h4>Create new sentence</h4>
        </v-row>
        <v-row>
          <v-col sm=12 md=6 lg=6>
            <v-select v-model="selected_topic" :items="itemsT" item-value="cveTopic" item-text="topicName" placeholder="Select topic" @change="get_cards_by_topic"></v-select> 
          </v-col>
          <v-col sm=12 md=6 lg=6>
            <v-select :items="itemsP" item-value="cveCard" item-text="cardText" placeholder="Select card" @change="select_card"></v-select>
          </v-col>
        </v-row>
        <v-row>
          <v-col sm=6 md=4 lg=4>
            <v-file-input v-model="input_image_value" append-icon="mdi-file-image" @change="verify_image" placeholder="Info image"></v-file-input>
          </v-col>
          <v-col sm=6 md=4 lg=4>
            <v-file-input v-model="input_audio_value" append-icon="mdi-volume-high" @change="verify_audio" placeholder="Info Audio"></v-file-input>
          </v-col>
          <v-col sm=6 md=4 lg=4>
            <v-file-input v-model="input_video_value" append-icon="mdi-video-box" @change="verify_video" placeholder="Info video"></v-file-input>
          </v-col>
        </v-row>
        <v-row>
          <v-col sm=12 md=6 lg=6 class="d-flex justify-center">
            <v-chip-group>
              <v-chip close v-for="(item) in sentence_items" :key="item.key" :value="item.text" @click:close="delete_card(item.key)">{{item.text}}
              </v-chip>
            </v-chip-group>
          </v-col>
          <v-col sm=12 md=6 lg=6 class="d-flex justify-center">
            <v-col md=6><v-btn :disabled="btn_save" depressed color="primary" class="mt-3 text-none" @click="saveRegistry()">{{text_btn_save}}</v-btn></v-col>
            <v-col md=6><v-btn :disabled="btn_save" depressed color="secondary" class="ml-3 mt-3 text-none" @click="cancelRegistry()">Cancel</v-btn>    </v-col>
        </v-col>
        </v-row> 
      </div>
    </v-expand-transition> 
      <v-row>
        <div style="width:30%">
          <v-text-field type="text" v-model="search" placeholder="Search Sentence" append-icon="mdi-magnify" class="ml-4"></v-text-field>
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
            <td>{{row.item.cveSentence}}</td>
            <td>{{row.item.sentenceName}}</td>
            <td>
              <span v-if="row.item.pathInfo" @click="show_dialog_info(row.item.pathInfo)"><v-icon border>mdi-image-album</v-icon> </span>
              <span v-if="row.item.pathSound" @click="show_dialog_audio(row.item.pathSound)"><v-icon  border>mdi-volume-high</v-icon> </span>
              <span v-if="row.item.pathVideo" @click="show_dialog_video(row.item.pathVideo)"><v-icon  border>mdi-video-box</v-icon> </span>
            </td>            
            <td>
              <v-icon medium border @click="edit_registry(row.item.cveSentence)">mdi-pencil-outline</v-icon> 
              <v-icon medium border @click="delete_sentence_registry(row.item.cveSentence)">mdi-trash-can-outline</v-icon>
            </td>
          </tr>
      </template>
    </v-data-table>
    <DialogImage :dialog.sync="dialog_info_visible" :image_url.sync="dialog_info_url"/>
    <DialogVideo :dialog.sync="dialog_video_visible" :playerOptions.sync="dialog_video_options"/>
    <DialogAudio :dialog.sync="dialog_audio_visible" :playerOptions.sync="dialog_audio_options"/>
  </v-container>
</template>
<script>
import axios from 'axios'
import Sentence from '../Class/Sentence.js'
import DialogAudio from '../components/DialogAudio.vue'
import DialogVideo from '../components/DialogVideo.vue'
import DialogImage from '../components/DialogImage.vue'


var P=process.env

export default {
  components: {
    DialogAudio,
    DialogVideo,
    DialogImage
  },
  data(){
  return{
    text_btn_save:'Save',
    select_value:"",
    sentence_items:[],
    sentence_object:new Sentence(),
    expand: false,
    alert_visible:false,
    btn_save:false,
    alert_type:"info",
    alert_text:"",
    selected_topic:"",
    icon_new:'mdi-plus',
    list_sentences:"",
    itemsT:[],
    itemsP:[],
    headers:[
      {text:"ID",align:'start',sortable:true,value:"cveSentence"},
      {text:"Sentence",align:'start',sortable:true,value:"sentenceName"},
      {text:"Help",align:'start',value:"help"},
      {text:"Actions",align:'start',value:"actions"}
    ],
    search:"",
    table_data_sentences:[],
    input_image_value:undefined,
    input_audio_value:undefined,
    input_video_value:undefined,
    dialog_info_visible:false,
    dialog_info_url:"",
    dialog_video_visible:false,
    dialog_video_options:{},
    dialog_audio_visible:false,
    dialog_audio_options:{},
    dialog_audio_url:"",
    }
  },
  methods:{
    showForm() {
      this.expand = !this.expand
      if(this.expand){this.icon_new='mdi-minus'}
      else{this.icon_new='mdi-plus'}
    },
    async get_cards_by_topic(e){
      console.log(e)
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_GET_ALL_CARDS_BY_TOPIC+"?cveTopic="+e)
      return await axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      P.VUE_APP_GET_ALL_CARDS_BY_TOPIC+"?cveTopic="+e).then(response=>{
        if(response.status==204){
          this.itemsP=[]
          return
        }
        this.itemsP= response.data
      }).catch(error=>{
        this.show_alert("Error: "+error,"error")
      })
    },
    verify_image(e){
      if(e==undefined){
        this.sentence_object.pathInfo=""
        return
      }
      if(e.type !== 'image/jpeg'&& e.type !== 'image/png' && e.type !== 'image/jpg' && e.type !== 'image/gif'){
        this.show_alert("Image not valid","warning")
        this.input_image_value=[] 
      }
    },
    verify_audio(e){
      if(e==undefined){
        this.sentence_object.pathSound=""
        return
      }
      if(e.type !== 'audio/mp3' && e.type !== 'audio/mpeg' && e.type !== 'audio/wav'){
        this.show_alert("Audio not valid","warning")
        this.input_audio_value=[] 
      }
    },
    verify_video(e){
      if(e==undefined){
        this.sentence_object.pathVideo=""
        return
      }
      if(e.type !== 'video/mp4' && e.type !== 'video/mpeg' && e.type !== 'video/webm'){
        this.show_alert("Video not valid","warning")
        this.input_video_value=[] 
      }
    },
    select_card(e){
      this.itemsP.forEach(element => {
        if(element.cveCard==e){
          this.sentence_items.forEach(element => {
            if(element.key==e){
              this.sentence_items.splice(this.sentence_items.indexOf(element),1)
            }
          });
          if(this.sentence_items.length>=4){
            this.show_alert("You can only select max 4 cards","error")
            return
          }
          this.sentence_items.push({key:e,text:element.cardText})
        }
      }); 
    },
    delete_card(e){
      this.sentence_items=this.sentence_items.filter(item=>item.key!=e)
    },
    show_alert(s="vacio",type_msg="info"){
      this.alert_visible=true
      this.alert_type=type_msg
      this.alert_text=s      
      this.timeout(3000).then(()=>{
        this.alert_visible=false
      })
    },
    async get_all_topics(){
      this.show_alert("Loading data, please wait","info")
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_GET_ALL_TOPICS)
      return await axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      P.VUE_APP_GET_ALL_TOPICS).then(response=>{
        return response.data
      }).catch(error=>{
        if(error.response.status==204){
          this.show_alert("No topics found","info")
        }
        this.show_alert("Error: "+error,"error")
      })
    },
    async delete_sentence_registry(id){
      let x=confirm("Are you sure you want to delete this sentence?")
      if(!x){return}
      this.show_alert("Deleting sentence, please wait","info")
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_DELETE_SENTENCE+"?cveSentence="+id)
      let result= await axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_DELETE_SENTENCE,{ params: { cveSentence:id } }).then(function(res){
          return res.data
      }).catch(function(error){
        console.log(error)
        this.show_alert("Error to delete sentence, try again.","warning")
        return 'error'
      })
      if(result.code==0){
        this.show_alert("Sentence deleted successfully","success")
        this.getAllSentences()
      }else{
        this.show_alert("Error to delete sentence, try again.","error")
      }
    },
    async saveRegistry(){
        this.btn_save=true
        this.show_alert('Saving sentence, please wait','info')
        let cards=[]
        delete this.sentence_object.card
        this.sentence_object.sentenceName=""
        this.sentence_items.forEach(element => {
          cards.push({"cveCard":element.key})
          this.sentence_object.sentenceName+=element.text+" "
        });
        this.sentence_object.sentenceName=this.sentence_object.sentenceName.trim()
        this.sentence_object.cards=cards
        if(this.sentence_object.cards.length<1){
          this.show_alert("Select at least one card","error")
          return
        }
        
        if(this.input_image_value!=null){
          if(this.input_image_value.name!=undefined)
          if(!this.input_image_value.name.startsWith('...')){
            let path=await this.upload_file(this.input_image_value,"images")
            this.sentence_object.pathInfo=path.path
          }
        }
        else{
          this.sentence_object.pathInfo=""
        }
        if(this.input_audio_value!=null){
          if(this.input_audio_value.name!=undefined)
          if(!this.input_audio_value.name.startsWith('...')){
            let path=await this.upload_file(this.input_audio_value,"audio")
            this.sentence_object.pathSound=path.path
          }
        }
        else{
          this.sentence_object.pathSound=""
        }
        if(this.input_video_value!=null){
          if(this.input_video_value.name!=undefined){
            let path=await this.upload_file(this.input_video_value,"video")
            this.sentence_object.pathVideo=path.path
          }
          
        }
        else{
          this.sentence_object.pathVideo=""
        }
        // let js={cveSentence:0,card:this.sentence_object.card}
        console.log(this.sentence_object)
        axios.post(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
        P.VUE_APP_INSERT_SENTENCE,this.sentence_object).then(response=>{
          this.show_alert("Sentence saved","success")
          this.btn_save=false
          console.log(response.status)
          this.sentence_object=new Sentence()
          this.sentence_items=[]
          this.input_image_value=[]
          this.input_audio_value=[]
          this.input_video_value=[]
          this.text_btn_save="Save"
          this.getAllSentences()
        })
        .catch(error=>{
          console.log(error.response)
          if(error.response.data.code){
            this.show_alert(error.response.data.message,"warning")
          }else{
            console.log(error.stats_code)
            this.show_alert("Error: "+error,"error")
          }
        })
        console.log(this.sentence_object)
    },
    cancelRegistry(){
      this.sentence_object=new Sentence()
      this.text_btn_save="Save"
      this.sentence_items=[]
      this.input_image_value=[]
      this.input_audio_value=[]
      this.input_video_value=[]    
      this.itemsP=[]
      this.select_value=""
      this.showForm()
    },
    edit_registry(e){
      if(!this.expand){
        this.showForm()
      }
      this.sentence_object=new Sentence()
      this.sentence_object.cveSentence=e
      this.text_btn_save="Update"
      this.sentence_object=Object.assign({},this.table_data_sentences.find(item=>item.cveSentence==e))
      this.sentence_items=[]
      this.sentence_object.card.forEach(element => {
        this.sentence_items.push({key:element.cveCard,text:element.cardText})
      });
      console.log(this.sentence_object)
      if(this.sentence_object.pathInfo=="")
        this.input_image_value=undefined
      else
        this.input_image_value=new File([this.sentence_object.pathInfo],'...'+this.sentence_object.pathInfo.split('/').pop())
      if(this.sentence_object.pathSound=="")
        this.input_audio_value=undefined
      else
        this.input_audio_value=new File([this.sentence_object.pathSound],'...'+this.sentence_object.pathSound.split('/').pop())

      if(this.sentence_object.pathVideo=="")
        this.input_video_value=undefined
      else
        this.input_video_value=new File([this.sentence_object.pathVideo],'...'+this.sentence_object.pathVideo.split('/').pop())
    },
    upload_file(file,type){
      try {
      let formData = new FormData()
      formData.append('files',file)
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_FILE_PORT+P.VUE_APP_UPLOAD_FILE)
      return axios.post(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_FILE_PORT+P.VUE_APP_UPLOAD_FILE,formData,{headers: {'Content-Type': 'multipart/form-data','X-Type':type}
      }).then(function(res){
        console.log(res)
        if(res.status==200){
          console.log(res.data)
          return res.data
        }
        else{
          this.show_alert("Error to upload file, try again.","error")
          return false
        }
      })
      .catch(function(error){
        console.log(error)
        this.show_alert("Error uploading file catch es del request","error")
        return false
      });  
      } catch (error) {
        this.show_alert("Error uploading file catch es de la funcion","error")
        return false
      }
    },
    show_dialog_info(url_dialog_info){
      let urlsrc=url_dialog_info.includes("http")?url_dialog_info:P.VUE_APP_URL_FILES_TEMP+url_dialog_info
      console.log(urlsrc)
      console.log(url_dialog_info)
      this.dialog_info_visible=true
      
      this.dialog_info_url=urlsrc
    },
    show_dialog_video(url_dialog_video){
      this.dialog_video_options={
          width: '400px',
          height: '400px',
          muted: false,
          language: 'en',
          playbackRates: [0.7, 1.0, 1.5, 2.0],
          sources: [{
            type: "video/mp4",
            src: url_dialog_video.includes("http")?url_dialog_video:P.VUE_APP_URL_FILES_TEMP+url_dialog_video
          }]
      },
      this.dialog_video_visible=true
    },
    show_dialog_audio(url_dialog_audio){
      console.log(url_dialog_audio)
      this.dialog_audio_options={
          width: '400px',
          height: '50px',
          muted: false,
          language: 'en',
          playbackRates: [0.7, 1.0, 1.5, 2.0],
          sources: [{
            type: "audio/mp3",
            src: url_dialog_audio.includes("http")?url_dialog_audio:P.VUE_APP_URL_FILES_TEMP+url_dialog_audio
          }]
      }
      this.dialog_audio_visible=true
    },
    getAllSentences(){
      this.show_alert("Loading data, please wait","info")
      this.table_data_sentences=[]
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_GET_ALL_SENTENCES)
      return axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      P.VUE_APP_GET_ALL_SENTENCES).then(response=>{
        if(response.status==204){
          console.log("No data")
          this.table_data_sentences=[]
          return
        }
        let i=0
        if(response.data!=undefined && response.data.length>0){
          response.data.forEach(element => {
            this.table_data_sentences.push(element)
            this.table_data_sentences[i].sentenceName=""
            element.card.forEach(e => {
              this.table_data_sentences[i].sentenceName+=e.cardText+" "
            });
            i++
          });
        }
        else
        this.table_data_sentences=[]
        this.show_alert("Data loaded","success")
      }).catch(error=>{
        console.log(error)
        this.show_alert("Error: "+error,"error")
      })
    },
    timeout(ms) { //pass a time in milliseconds to this function
      return new Promise(resolve => setTimeout(resolve, ms));
    },
  },
  async created(){
    let items=await this.get_all_topics()
    await this.getAllSentences()
    this.itemsT=items
  },
  computed: {
    filteredItems () {
      return this.table_data_sentences.filter(item => {
         return (item.sentenceName.toString().toLowerCase().indexOf(this.search.toLowerCase()) > -1 ||
         item.cveSentence.toString().indexOf(this.search.toLowerCase()) > -1)
      })
    }
  }
}
</script>
<!--Corregir el concatenado de sentence name--->