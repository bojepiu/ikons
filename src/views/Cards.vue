<template>
  <v-container>
    <!-- REVISAR QUE ONDA CON EL MESSAGE UNDEFINED -->
    <div class="d-flex justify-center" style="top:0; left:0; width:100vw;position:absolute;">
    <v-alert :value="alert_visible==true" :type="alert_type" dark  
    transition="scale-transition" dismissible v-on:click="alert_visible=false">{{alert_text}}</v-alert>
    </div>
    <v-expand-transition>
      <div v-show="expand">
        <v-row class="pt-5">
            <h4>Create new Card</h4>
        </v-row>
        <v-row>
          <v-col sm=8 class="ml-0">
            <v-row>
              <v-col sm="1" class="mt-8 d-flex justify-start">
                <span>Topic<span style="color:red">*</span>:</span>
              </v-col>
              <v-col sm="4">
                <v-combobox v-model="selected.topicName" :items="list_all_topics" item-value="cveTopic" item-text="topicName" @change="select_topic"></v-combobox>
              </v-col>
              <v-col sm="1" class="mt-8 ml-2  d-flex justify-end">
                <span class="">Text<span style="color:red">*</span>:</span>
              </v-col>
              <v-col sm="4" class="ml-3">
                <v-text-field v-model="preview_card.cardText"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col sm="1" class="mt-3 d-flex justify-start" >
                <span class="">Image<span style="color:red">*</span>: </span>
              </v-col>
              <v-col sm="4" class=" pt-0">
                <v-file-input v-model="input_image_value" append-icon="mdi-file-image" @change="load_image" dark:true></v-file-input>
              </v-col>
              <v-col sm="1" class="ml-3 mt-3 d-flex justify-start">
                <span class="">Audio:</span>
              </v-col>
              <v-col sm="4" class="pt-0">
                <v-file-input v-model="input_audio_value" append-icon="mdi-volume-high" dark:true ></v-file-input>
              </v-col>
            </v-row>
            <v-row>
              <v-row>
                <v-col sm="1" class="mt-2 d-flex justify-start ml-3">
                    <span class="ml-3">Video:</span>
                </v-col>
                <v-col sm="4" class="pt-0">
                  <v-file-input v-model="input_video_value" append-icon="mdi-video-box" dark:true></v-file-input>
                </v-col>
                <v-col sm="1" class="mt-4 d-flex justify-end">
                  <span class="">Meaning:</span>
                </v-col>
                <v-col sm="4" class="pt-0">
                  <v-file-input v-model="input_meaning_value" id="inputMeaning" append-icon="mdi-file-pdf-box" dark:true></v-file-input>
                </v-col>
              </v-row>      
            </v-row>
            <v-row>
              <v-col sm="8" class="d-flex justify-end ml-8">
                <v-btn depressed color="primary" class="pa-4 mt-3" @click="saveRegistry($event)">{{text_btn_save}}</v-btn>
              </v-col>
              <v-col sm="3" class="d-flex justify-start">
                <v-btn depressed color="secondary" class="pa-4 mt-3" @click="cancelRegistry()">Cancel</v-btn>  
              </v-col>
              </v-row>
          </v-col>
          <v-col sm="4">
                <v-card elevation="2" max-width="300" height="280">
                    <v-card-title class="justify-center">{{preview_card.topicName}}</v-card-title>
                    <v-card-text class="justify-center">
                        <v-img
                        contain
                        max-height="120"
                        max-width="200"
                        :src="image_url"
                        class="mx-auto"
                        ></v-img>
                        <v-row>
                            <v-text-field readonly v-model="preview_card.cardText"></v-text-field>
                        </v-row>
                        <v-row class="d-flex justify-center">
                            <v-icon v-if="input_audio_value!='' && input_audio_value!=null" medium border >mdi-volume-high</v-icon> 
                            <v-icon v-if="input_video_value!='' && input_video_value!=null" medium border >mdi-video-box</v-icon> 
                            <v-icon v-if="input_meaning_value!='' && input_meaning_value!=null" medium border>mdi-file-pdf-box</v-icon> 
                        </v-row>
                    </v-card-text>
                </v-card>
          </v-col> 
        </v-row>
        <v-row>
            <v-col sm="12" >
              
            </v-col>
        </v-row>
      </div>
    </v-expand-transition>
      <v-row>
        <div style="width:30%">
          <v-text-field type="text" v-model="search" placeholder="Search Card" append-icon="mdi-magnify" class="ml-4"></v-text-field>
        </div>
        <div style="width:50%" class="d-flex justify-start ml-6">
          <v-btn class="mt-3" title="New Topic" fab dark color="indigo" small @click="showForm()"> 
            <v-icon id="icon_new" dark>{{icon_new}}</v-icon>
          </v-btn>
        </div>
      </v-row>    
    <v-data-table :headers="headers" :items="filteredItems" :items-per-page="10" class="elevation-2">
      <template v-slot:item="row">
          <tr>
            <td>{{row.item.cveCard}}</td>
            <td>{{row.item.topicName}}</td>
            <td>{{row.item.cardText}}</td>
            <td>
              <span v-if="row.item.pathImage" @click="show_dialog_image(row.item.pathImage)"><v-icon border>mdi-image-album</v-icon> </span>
              <span v-if="row.item.pathSound"><v-icon  border>mdi-volume-high</v-icon> </span>
              <span v-if="row.item.pathVideo" @click="show_dialog_video(row.item.pathVideo)"><v-icon  border>mdi-video-box</v-icon> </span>
              <span v-if="row.item.pathMeaning" @click="show_dialog_meaning(row.item.pathMeaning)"><v-icon border>mdi-file-pdf-box</v-icon></span>
            </td>            
            <td>
              <v-icon medium border @click="edit_registry(row.item.cveCard)">mdi-pencil-outline</v-icon> 
              <v-icon medium border @click="delete_registry(row.item.cveCard)">mdi-trash-can-outline</v-icon> 
            </td>
          </tr>
      </template>
    </v-data-table>
    <DialogMeaning :dialog.sync="dialog_meaning_visible" :image_url.sync="dialog_meaning_url"/>
    <DialogImage :dialog.sync="dialog_image_visible" :image_url.sync="dialog_image_url"/>
    <DialogVideo :dialog.sync="dialog_video_visible" :playerOptions.sync="dialog_video_options"/>
  </v-container>
</template>
<script>
import axios from 'axios'
import DialogMeaning from '../components/DialogMeaning.vue'
import DialogImage from '../components/DialogImage.vue'
import DialogVideo from '../components/DialogVideo.vue'
import Card from '../Class/Card.js'

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';


var P=process.env
var audio=new Audio()

export default {
  components: { DialogMeaning,DialogImage,DialogVideo },
  data(){
  return{
    expand: false,
    selected:{},
    text_btn_save:'Save',
    icon_new:'mdi-plus',
    //DIALOGS SECTION
    dialog_image_visible:false,
    dialog_image_url:"",
    dialog_audio_visible:false,
    dialog_audio_url:"",
    dialog_video_visible:false,
    dialog_video_options:{},
    dialog_meaning_visible:false,
    dialog_meaning_url:"",
    //TABLE SECTION
    search:'',
    headers:[
      {text:"ID",align:'start',sortable:true,value:"id"},
      {text:"Topic",align:'start',sortable:true,value:"topic_text"},
      {text:"Text",align:'start',sortable:true,value:"text"},
      {text:"Help",align:'start',value:"description"},
      {text:"Actions",align:'start',value:"actions"}
    ],
    table_data_cards:[],
    //FORM SECTION
    list_all_topics:[],
    preview_card:new Card(),
    input_image_value:[],
    input_audio_value:[],
    input_video_value:[],
    input_meaning_value:[],
    //ALERT
    alert_visible:false,
    alert_type:"success",
    alert_text:"",
    image_url:"404notfoundimage.png",
  }
  },
  methods:{
    showForm() {
      this.expand = !this.expand
      if(this.expand){this.icon_new='mdi-minus'}
      else{this.icon_new='mdi-plus'}
    },
    async get_all_topics(){
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_GET_ALL_TOPICS)
      return await axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      P.VUE_APP_GET_ALL_TOPICS).then(response=>{
        return response.data
      }).catch(error=>{
        this.show_alert("Error: "+error,"error")
      })
    },
    async saveRegistry(e){
      e.preventDefault()
      if(this.preview_card.topicName=="" || this.preview_card.topicName=="Select Topic"){
        this.show_alert("Topic not found in card","warning")
        return
      }
      console.log('topic')
      if(this.preview_card.cardText==""){
        this.show_alert("Text not found in card","warning")
        return
      }
      console.log('text')
      if(this.preview_card.pathImage==""){
        this.show_alert("Image not found in card","warning")
        return
      }
      console.log('image')
      if(this.preview_card.pathImage=="IMAGE PENDING UPLOAD"){
        let img=await this.upload_file(this.input_image_value,'images')
        if(!img){return}
        else{this.preview_card.pathImage=img.path}  
      }
      console.log('image_uploaded')
      if(this.input_audio_value!='' && this.input_audio_value!=null){
        if(this.preview_card.pathSound==""){
          let mp3=await this.upload_file(this.input_audio_value,'audio')
          if(!mp3){return}
          else{this.preview_card.pathSound=mp3.path} 
        }
      }else{
        this.preview_card.pathSound=""
      }
      console.log('audio_uploaded')
      if(this.input_video_value!='' && this.input_video_value!=null){
        if(this.preview_card.pathVideo==""){
          let mp4=await this.upload_file(this.input_video_value,'video')
          if(!mp4){return}
          else{this.preview_card.pathVideo=mp4.path} 
        }
      }else{
        this.preview_card.pathVideo=""
      }
      console.log('video_uploaded')
      if(this.input_meaning_value!='' && this.input_meaning_value!=null){
        console.log('meaning_validation')
        if(this.preview_card.pathMeaning==""){
          let pdf=await this.upload_file(this.input_meaning_value,'meaning')
          if(!pdf){return}
          else{this.preview_card.pathMeaning=pdf.path} 
        }
      }else{
        this.preview_card.pathMeaning=""
      }
      console.log('meaning_uploaded')
      alert(JSON.stringify(this.preview_card))
      axios.post(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_INSERT_TOPIC_CARD,this.preview_card).then(response=>{
        console.log(response)
        this.show_alert("Card saved successfully","success")
        
      }).catch(error=>{
        this.show_alert("Error: "+error,"error")
      })
      if(this.preview_card.cveTopic==0){
        await this.load_topics()
      }

      this.show_alert("Card saved successfully","success")
      
      // this.table_data_cards.push(this.preview_card)
      let a=this.preview_card.cveTopic
      let b=this.preview_card.topicName
      this.preview_card=new Card()
      if(a!=0){
        this.preview_card.cveTopic=a
        this.preview_card.topicName=b
      }else{
        this.list_all_topics.forEach(element => {
          if(element.topicName==b){
            this.preview_card.cveTopic=element.cveTopic
            this.preview_card.topicName=element.topicName
          }
        });
      }
      this.image_url="404notfoundimage.png"
      this.input_image_value=[]
      this.input_audio_value=[]
      this.input_video_value=[]
      this.input_meaning_value=[]
      this.text_btn_save='Save'
      return
    },
    cancelRegistry(){
      this.preview_card=new Card()
      this.selected={}
      this.preview_card.topicName="Select Topic"
      this.image_url="404notfoundimage.png"
      this.input_image_value=[]
      this.input_audio_value=[]
      this.input_video_value=[]
      this.input_meaning_value=[]
      this.text_btn_save='Save'
      this.showForm()
    },
    select_topic(e){
      if(e.cveTopic==undefined){
        this.preview_card.cveTopic=0
        this.preview_card.topicName=e
        return
      }
      this.preview_card.cveTopic=e.cveTopic
      this.preview_card.topicName=e.topicName
    },
    load_image(e){    
      if(e==null || e==undefined){
        this.preview_card.pathImage=""
        this.image_url="404notfoundimage.png"
        return
      }    
      if(e.type !== 'image/jpeg'&& e.type !== 'image/png' && e.type !== 'image/jpg' && e.type !== 'image/gif'){
        this.show_alert("Image not valid","warning")
        this.input_image_value=[] 
      }
      else{
        this.preview_card.pathImage="IMAGE PENDING UPLOAD"
        this.image_url= URL.createObjectURL(this.input_image_value)
      }
    },
    play_audio(){
      audio =new Audio(this.audio_url)
      audio.play()
    },
    show_dialog_image(url_dialog_image){
      let urlsrc=url_dialog_image.includes("http")?url_dialog_image:P.VUE_APP_URL_FILES_TEMP+url_dialog_image
      console.log(urlsrc)
      console.log(url_dialog_image)
      this.dialog_image_visible=true
      
      this.dialog_image_url=urlsrc
    },
    show_dialog_audio(url_dialog_audio){
      this.dialog_audio_visible=true
      this.dialog_audio_url=url_dialog_audio
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
    show_alert(s="vacio",type_msg="info"){
      this.alert_visible=true
      this.alert_type=type_msg
      this.alert_text=s      
      // this.timeout(3000).then(()=>{
      //   this.alert_visible=false
      // })
    },
    async load_topics(){
      this.list_all_topics=await this.get_all_topics()
    },
    getBase64(file) {
      var reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = function () {
        console.log(reader.result)
        return reader.result;
      };
      reader.onerror = function (error) {
        console.log('Error: ', error);
        return "ERROR"
      }
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
    timeout(ms) { //pass a time in milliseconds to this function
    return new Promise(resolve => setTimeout(resolve, ms));
    },
    show_dialog_meaning(url_dialog_meaning){
      this.dialog_meaning_visible=true
      this.dialog_meaning_url=url_dialog_meaning.includes("http")?url_dialog_meaning:P.VUE_APP_URL_FILES_TEMP+url_dialog_meaning
    },
    edit_registry(id){
      document.body.scrollTop = document.documentElement.scrollTop = 0;
      this.table_data_cards.forEach(element => {
        if(element.cveCard==id){
          this.text_btn_save="Update"
          this.input_image_value=[]
          this.input_audio_value=[]
          this.input_video_value=[]
          this.input_meaning_value=[]
          this.preview_card=element
          this.selected={cveTopic:element.cveTopic,topicName:element.topicName}
          this.image_url=element.pathImage.includes("http")?element.pathImage:P.VUE_APP_URL_FILES_TEMP+element.pathImage
          this.input_image_value=new File([element.pathImage],element.pathImage.split('/').pop())
          if(element.pathSound!=''){
            this.input_audio_value=new File([element.pathSound],element.pathSound.split('/').pop())
          }
          if(element.pathVideo!='')
          this.input_video_value=new File([element.pathVideo],element.pathVideo.split('/').pop())
          if(element.pathMeaning!='')
          this.input_meaning_value=new File([element.pathMeaning],element.pathMeaning.split('/').pop())
          if(!this.expand)this.showForm()
          return 
        }
      });
    },
    delete_registry(id){
      console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_DELETE_CARD+"?cveCard="+id)
      axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_DELETE_CARD,{ params: { cveCard:id } }).then(function(res){
        if(res.status==200){
          this.show_alert("Deleted","info")
          this.load_cards() //Resolver en local
        }
        else{
          this.show_alert("Error to delete card, try again.","error")
        }
      }).catch(function(error){
        console.log(error)
        this.show_alert("Error to delete card, try again.","error")
      })
    },
  },
  //First function to run
  async created(){
    this.preview_card.topicName="Select Topic"
    //Get all topics
    this.load_topics()
    //Get data table
    this.show_alert("Loading data, please wait...","info")
    console.log(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_GET_ALL_CARDS)
    this.table_data_cards=await axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+P.VUE_APP_GET_ALL_CARDS).then(function(res){
      console.log(res)
      if(res.status==200){
        return res.data
      }
      else{
        this.show_alert("Error to load data, try again.","error")
        return []
      }
    }).catch(function(error){
      console.log(error)
      this.show_alert("Error to load data, try again.","error")
      return []
    })
    
  },
  computed: {
    filteredItems () {
      return this.table_data_cards.filter(item => {
         return (item.cardText.toLowerCase().indexOf(this.search.toLowerCase()) > -1 ||
         item.cveCard.toString().indexOf(this.search.toLowerCase()) > -1 ||
         item.topicName.toLowerCase().indexOf(this.search.toLowerCase()) > -1 )
      })
    }
  }
}
</script>
