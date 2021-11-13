<template>
  <v-container>
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
                <v-combobox :items="list_all_topics" item-value="cveTopic" item-text="topicName" @change="select_topic"></v-combobox>
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
                <v-file-input id="inputImage" v-model="input_image_value" append-icon="mdi-file-image" @change="load_image" dark:true></v-file-input>
              </v-col>
              <v-col sm="1" class="ml-3 mt-3 d-flex justify-start">
                <span class="">Audio:</span>
              </v-col>
              <v-col sm="4" class="pt-0">
                <v-file-input append-icon="mdi-volume-high" @change="load_audio" dark:true v-model="preview_card.audio"></v-file-input>
              </v-col>
            </v-row>
            <v-row>
              <v-row>
                <v-col sm="1" class="mt-2 d-flex justify-start ml-3">
                    <span class="ml-3">Video:</span>
                </v-col>
                <v-col sm="4" class="pt-0">
                  <v-file-input append-icon="mdi-video-box" dark:true v-model="preview_card.video"></v-file-input>
                </v-col>
                <v-col sm="1" class="mt-4 d-flex justify-end">
                  <span class="">Meaning:</span>
                </v-col>
                <v-col sm="4" class="pt-0">
                  <v-file-input append-icon="mdi-file-pdf-box" dark:true v-model="preview_card.meaning"></v-file-input>
                </v-col>
              </v-row>      
            </v-row>
            <v-row>
              <v-col sm="8" class="d-flex justify-end ml-8">
                <v-btn depressed color="primary" class="pa-4 mt-3" @click="saveRegistry()">Save</v-btn>
              </v-col>
              <v-col sm="3" class="d-flex justify-start">
                <v-btn depressed color="secondary" class="pa-4 mt-3" @click="showForm();">Cancel</v-btn>  
              </v-col>
              </v-row>
          </v-col>
          <v-col sm="4">
                <v-card elevation="2" width="200" height="255">
                    <v-card-title class="justify-center">{{preview_card.topic}}</v-card-title>
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
                            <v-icon large border @click="play_audio">mdi-volume-high</v-icon> 
                            <v-icon large border>mdi-video-box</v-icon> 
                            <v-icon large border>mdi-file-pdf-box</v-icon> 
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
          <v-text-field type="text" placeholder="Search Card" append-icon="mdi-magnify" class="ml-4"></v-text-field>
        </div>
        <div style="width:50%" class="d-flex justify-start ml-6">
          <v-btn class="mt-3" title="New Topic" fab dark color="indigo" small @click="showForm()"> 
            <v-icon id="icon_new" dark>{{icon_new}}</v-icon>
          </v-btn>
        </div>
      </v-row>    
    <v-data-table :headers="headers" :items="table_data_cards" :items-per-page="10" class="elevation-2">
      <template v-slot:item="row">
          <tr>
            <td>{{row.item.id}}</td>
            <td>{{row.item.text}}</td>
            <td>
              <span v-if="row.item.image" @click="show_dialog_image(row.item.image)"><v-icon border>mdi-image-album</v-icon> </span>
              <span v-if="row.item.audio"><v-icon  border>mdi-volume-high</v-icon> </span>
              <span v-if="row.item.video" @click="show_dialog_video(row.item.video)"><v-icon  border>mdi-video-box</v-icon> </span>
              <span v-if="row.item.meaning" @click="show_dialog_meaning(row.item.meaning)"><v-icon border>mdi-file-pdf-box</v-icon></span>
            </td>
            
            <td>
              <v-icon medium border>mdi-pencil-outline</v-icon> 
              <v-icon medium border>mdi-trash-can-outline</v-icon> 
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

var audio=new Audio()

// var new_card={id:0,text:"",image:"",audio:"",video:"",meaning:""}

export default {
  components: { DialogMeaning,DialogImage,DialogVideo },
  //Validar como funciona al montar para validar sesion valida 
  data(){
  return{
    expand: false,
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
    preview_card:{id:0,topic:"",text:"",image:undefined,audio:undefined,video:undefined,meaning:undefined},
    input_image_value:[],
    input_audio_value:[],
    input_video_value:[],
    input_meaning_value:[],
    image_url:"404notfoundimage.png",
    audio_url:"",
    video_url:"",
    meaning_url:"",
  }
  },
  methods:{
    async get_all_topics(){
      return await axios.get('http://localhost:5000/ikon/v1/topic/getall').then(response=>{
        return response.data
      })
    },
    showForm() {
      this.expand = !this.expand
      if(this.expand){this.icon_new='mdi-minus'}
      else{this.icon_new='mdi-plus'}
    },
    saveRegistry(id=0){
      if(this.preview_card.topic==""){
        console.log("No se ha seleccionado un tema")
      }
      if(this.preview_card.text==""){
        console.log("Faltan datos por llenar")
        return
      }
      if(this.preview_card.image==""){
        console.log("Faltan datos por llenar")
      }
        console.log(id)
    },
    select_topic(e){
      if(e.cveTopic==undefined){
        alert(0)
      }
      console.log(e.cveTopic)
      this.preview_card.topic=e.topicName
    },
    load_image(e){    
      if(e==null){
        this.preview_card.image=undefined
        this.image_url="404notfoundimage.png"
        return
      }    
      if(e.type !== 'image/jpeg'&& e.type !== 'image/png' && e.type !== 'image/jpg'){
        alert("Solo se permiten imagenes")
        this.input_image_value=[] 
      }
      else{
        this.image_url= URL.createObjectURL(this.input_image_value)
      }
    },
    load_audio(){
      this.audio_url=URL.createObjectURL(this.preview_card.audio)    
    },
    play_audio(){
      audio =new Audio(this.audio_url)
      audio.play()
    },
    load_video(){
      return 
    },
    play_video(){
      return
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
          // videojs options
          width: '400px',
          height: '400px',
          muted: false,
          language: 'en',
          playbackRates: [0.7, 1.0, 1.5, 2.0],
          sources: [{
            type: "video/mp4",
            src: url_dialog_video
          }]
      }
      this.dialog_video_visible=true
    },
    show_dialog_meaning(url_dialog_meaning){
      this.dialog_meaning_visible=true
      this.dialog_meaning_url=url_dialog_meaning
    },
  },
  //First function to run
  async created(){
    //Get all topics
    this.list_all_topics=await this.get_all_topics()
    //Get data table
    this.table_data_cards=[
      {id:1,id_topic:"",topic_text:"asd",text:"Module One",description:"Module init",image:"https://www.gettyimages.com.mx/gi-resources/images/500px/983794168.jpg",audio:"asd",video:"video/hello_video.mp4",meaning:""},
      {id:2,text:"Module Two",description:"Second Module",image:"https://cdn.pixabay.com/photo/2021/08/25/20/42/field-6574455__340.jpg",audio:"asd",video:"asd",meaning:"https://fondosmil.com/fondo/11764.jpg"},
      {id:3,text:"Module Three",description:"Otrher Module",image:"https://www.gettyimages.es/gi-resources/images/frontdoor/editorial/Velo/GettyImages-Velo-1088643550.jpg",audio:"",video:"https://www.w3school.com.cn/example/html5/mov_bbb.mp4",meaning:"http://qnimate.com/wp-content/uploads/2014/03/images2.jpg"},
    ]    
    
    

  }
}
</script>
