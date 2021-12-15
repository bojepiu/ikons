<template>
  <v-container>
    <div class="d-flex justify-center" style="top:0; left:0; width:100vw;position:absolute;">
    <v-alert :value="alert_visible==true" :type="alert_type" dark  
    transition="scale-transition" dismissible v-on:click="alert_visible=false">{{alert_text}}</v-alert>
    </div>
    <v-expand-transition>
      <div v-show="expand">
        <v-row class="pt-5">
            <h4>Create a new Card</h4>
        </v-row>
        <v-row>
          <v-col sm=8 class="ml-0">
            <v-row>
              <v-col sm="1" class="mt-8 d-flex justify-start">
                <span>Topic<span style="color:red">*</span>:</span>
              </v-col>
              <v-col sm="4">
                <v-select  v-model="selected" :items="list_all_topics" item-value="cveTopic" item-text="topicName" @change="select_topic"></v-select>
              </v-col>
              <v-col sm="1" class="mt-8 ml-2  d-flex justify-end">
                <span class="">Text<span style="color:red">*</span>:</span>
              </v-col>
              <v-col sm="4" class="ml-3">
                <v-text-field v-model="preview_card.text"></v-text-field>
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
                <v-btn depressed color="primary" class="pa-4 mt-3" @click="saveRegistry($event)">Save</v-btn>
              </v-col>
              <v-col sm="3" class="d-flex justify-start">
                <v-btn depressed color="secondary" class="pa-4 mt-3" @click="showForm();">Cancel</v-btn>  
              </v-col>
              </v-row>
          </v-col>
          <v-col sm="4">
                <v-card elevation="2" width="200" height="255">
                    <v-card-title class="justify-center">{{preview_card.topic_text}}</v-card-title>
                    <v-card-text class="justify-center">
                        <v-row>
                        <v-img
                        contain
                        max-height="90"
                        max-width="170"
                        :src="image_url"
                        class="ml-4"
                        ></v-img>
                        </v-row>
                        <v-row>
                            <v-text-field readonly v-model="preview_card.text"></v-text-field>
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
            <td>{{row.item.id}}</td>
            <td>{{row.item.topic_text}}</td>
            <td>{{row.item.text}}</td>
            <td>
              <span v-if="row.item.image" @click="show_dialog_image(row.item.image)"><v-icon border>mdi-image-album</v-icon> </span>
              <span v-if="row.item.audio"><v-icon  border>mdi-volume-high</v-icon> </span>
              <span v-if="row.item.video" @click="show_dialog_video(row.item.video)"><v-icon  border>mdi-video-box</v-icon> </span>
              <span v-if="row.item.meaning" @click="show_dialog_meaning(row.item.meaning)"><v-icon border>mdi-file-pdf-box</v-icon></span>
            </td>            
            <td>
              <v-icon medium border @click="edit_registry(row.item.id)">mdi-pencil-outline</v-icon> 
              <v-icon medium border @click="delete_registry(row.item.id)">mdi-trash-can-outline</v-icon> 
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

var P=process.env
var audio=new Audio()

export default {
  components: { DialogMeaning,DialogImage,DialogVideo },
  data(){
  return{
    expand: false,
    selected:{},
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
      return await axios.get(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      P.VUE_APP_ROUTE_GET_ALL_TOPIC).then(response=>{
        return response.data
      }).catch(error=>{
        this.show_alert("Error: "+error,"error")
      })
    },
    async saveRegistry(e){
      e.preventDefault()
      if(this.preview_card.topic_text==""){
        this.show_alert("Topic not found in card","warning")
        return
      }
      if(this.preview_card.text==""){
        this.show_alert("Text not found in card","warning")
        return
      }
      if(this.preview_card.image==""){
        this.show_alert("Image not found in card","warning")
        return
      }
      
      if(this.preview_card.image=="IMAGE PENDING UPLOAD"){
        let img=await this.upload_file(this.input_image_value,'images')
        if(!img){return}
        else{this.preview_card.image=img.path}  
      }
      if(this.input_audio_value!='' && this.input_audio_value!=null){
        if(this.preview_card.audio==""){
          let mp3=await this.upload_file(this.input_audio_value,'audio')
          if(!mp3){return}
          else{this.preview_card.audio=mp3.path} 
        }
      }else{
        this.preview_card.audio=""
      }
      if(this.input_video_value!='' && this.input_video_value!=null){
        if(this.preview_card.video==""){
          let mp4=await this.upload_file(this.input_video_value,'video')
          if(!mp4){return}
          else{this.preview_card.video=mp4.path} 
        }
      }else{
        this.preview_card.video=""
      }
      if(this.input_meaning_value!='' && this.input_meaning_value!=null){
        if(this.preview_card.meaning==""){
          let pdf=await this.upload_file(this.input_meaning_value,'pdf')
          if(!pdf){return}
          else{this.preview_card.meaning=pdf.path} 
        }
      }else{
        this.preview_card.meaning=""
      }
      this.show_alert("Card saved successfully","success")
      alert(JSON.stringify(this.preview_card))
      this.table_data_cards.push(this.preview_card)
      let a=this.preview_card.topic_id
      let b=this.preview_card.topic_text
      this.preview_card=new Card()
      this.preview_card.topic_id=a
      this.preview_card.topic_text=b
      this.image_url="404notfoundimage.png"
      this.input_image_value=[]
      this.input_audio_value=[]
      this.input_video_value=[]
      this.input_meaning_value=[]
      return
    },
    select_topic(e){
      this.preview_card.topic_id=e
      this.list_all_topics.forEach(element => {
        if(element.cveTopic==e){
          this.preview_card.topic_text=element.topicName
        }
      })
    },
    load_image(e){    
      if(e==null || e==undefined){
        this.preview_card.image=""
        this.image_url="404notfoundimage.png"
        return
      }    
      if(e.type !== 'image/jpeg'&& e.type !== 'image/png' && e.type !== 'image/jpg' && e.type !== 'image/gif'){
        this.show_alert("Image not valid","warning")
        this.input_image_value=[] 
      }
      else{
        this.preview_card.image="IMAGE PENDING UPLOAD"
        this.image_url= URL.createObjectURL(this.input_image_value)
      }
    },
    play_audio(){
      audio =new Audio(this.audio_url)
      audio.play()
    },
    show_dialog_image(url_dialog_image){
      console.log(url_dialog_image)
      this.dialog_image_visible=true
      this.dialog_image_url=url_dialog_image
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
            src: url_dialog_video
          }]
      },
      this.dialog_video_visible=true
    },
    async show_alert(s,type_msg){
      this.alert_visible=true
      this.alert_type=type_msg
      this.alert_text=s      
      this.timeout(3000).then(()=>{
        this.alert_visible=false
      })
    },
    upload_file(file,type){
      try {
      let formData = new FormData()
      formData.append('files',file)
      return axios.post(P.VUE_APP_SERVER_HOST+":"+P.VUE_APP_SERVER_PORT+
      P.VUE_APP_ROUTE_UPLOAD_FILE,
      formData,
      {
        headers: {
            'Content-Type': 'multipart/form-data',
            'X-Type': type
        },
      }
      ).then(function(res){
        if(res.data.status==200){
          console.log(res.data.path)
          return res.data
        }
        else{
          this.show_alert("Error to upload file, try again.","error")
          return false
        }
      })
      .catch(function(){
        this.show_alert("Error uploading file","error")
        return false
      });  
      } catch (error) {
        this.show_alert("Error uploading file","error")
        return false
      }
    },
    timeout(ms) { //pass a time in milliseconds to this function
    return new Promise(resolve => setTimeout(resolve, ms));
    },
    show_dialog_meaning(url_dialog_meaning){
      this.dialog_meaning_visible=true
      this.dialog_meaning_url=url_dialog_meaning
    },
    edit_registry(id){
      document.body.scrollTop = document.documentElement.scrollTop = 0;
      this.table_data_cards.forEach(element => {
        if(element.id==id){
          this.input_image_value=[]
          this.input_audio_value=[]
          this.input_video_value=[]
          this.input_meaning_value=[]
          this.preview_card=element
          this.selected={cveTopic:element.topic_id,topicName:element.topic_text}
          this.image_url=element.image
          this.input_image_value=new File([element.image],element.image.split('/').pop())
          if(element.audio!=''){
            this.input_audio_value=new File([element.audio],element.audio.split('/').pop())
          }
          if(element.video!='')
          this.input_video_value=new File([element.video],element.video.split('/').pop())
          if(element.meaning!='')
          this.input_meaning_value=new File([element.meaning],element.meaning.split('/').pop())
          if(!this.expand)this.showForm()
          return 
        }
      });
    },
    delete_registry(id){
      alert('se elimina '+id)
    },
  },
  //First function to run
  async created(){
    this.preview_card.topic_text="Select Topic"
    //Get all topics
    this.list_all_topics=await this.get_all_topics()
    //Get data table
    this.show_alert("Loading data, please wait...","info")
    await this.timeout(2000)
    this.show_alert("Data loaded successfully","success")
    this.table_data_cards=[
      {id:1,topic_id:1,topic_text:"PRONOMS",text:"YOU",description:"Module init",image:"https://www.gettyimages.com.mx/gi-resources/images/500px/983794168.jpg",audio:"https://www.loquesea/asd.mp3",video:"video/hello_video.mp4",meaning:""},
      {id:2,topic_id:2,topic_text:"COLORS",text:"ORANGE",description:"Second Module",image:"https://cdn.pixabay.com/photo/2021/08/25/20/42/field-6574455__340.jpg",audio:"https://www.loquesea/asd.mp3",video:"http://www.loquesea/asd",meaning:"https://fondosmil.com/fondo/11764.jpg"},
      {id:3,topic_id:2,topic_text:"COLORS",text:"PURPLE",description:"Otrher Module",image:"https://www.gettyimages.es/gi-resources/images/frontdoor/editorial/Velo/GettyImages-Velo-1088643550.jpg",audio:"https://www.loquesea/asd.mp3",video:"https://www.w3school.com.cn/example/html5/mov_bbb.mp4",meaning:"http://qnimate.com/wp-content/uploads/2014/03/images2.jpg"},
      {id:4,topic_id:2,topic_text:"COLORS",text:"BLACK",description:"Otrher Module",image:"https://www.gettyimages.es/gi-resources/images/frontdoor/editorial/Velo/GettyImages-Velo-1088643550.jpg",audio:"",video:"https://www.w3school.com.cn/example/html5/mov_bbb.mp4",meaning:"http://qnimate.com/wp-content/uploads/2014/03/images2.jpg"},
      {id:5,topic_id:2,topic_text:"COLORS",text:"WHITE",description:"Otrher Module",image:"https://www.gettyimages.es/gi-resources/images/frontdoor/editorial/Velo/GettyImages-Velo-1088643550.jpg",audio:"",video:"https://www.w3school.com.cn/example/html5/mov_bbb.mp4",meaning:"http://qnimate.com/wp-content/uploads/2014/03/images2.jpg"},
      {id:6,topic_id:2,topic_text:"COLORS",text:"BLUE",description:"Otrher Module",image:"https://www.gettyimages.es/gi-resources/images/frontdoor/editorial/Velo/GettyImages-Velo-1088643550.jpg",audio:"",video:"https://www.w3school.com.cn/example/html5/mov_bbb.mp4",meaning:"http://qnimate.com/wp-content/uploads/2014/03/images2.jpg"},
      {id:7,topic_id:2,topic_text:"COLORS",text:"YELLOW",description:"Otrher Module",image:"https://www.gettyimages.es/gi-resources/images/frontdoor/editorial/Velo/GettyImages-Velo-1088643550.jpg",audio:"",video:"https://www.w3school.com.cn/example/html5/mov_bbb.mp4",meaning:"http://qnimate.com/wp-content/uploads/2014/03/images2.jpg"},
    ]    
  },
  computed: {
    filteredItems () {
      return this.table_data_cards.filter(item => {
         return (item.text.toLowerCase().indexOf(this.search.toLowerCase()) > -1 ||
         item.id.toString().indexOf(this.search.toLowerCase()) > -1 ||
         item.topic_text.toLowerCase().indexOf(this.search.toLowerCase()) > -1 )
      })
    }
  }
}
</script>
