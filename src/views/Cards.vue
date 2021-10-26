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
                <v-combobox :items="itemsT" @change="select_topic"></v-combobox>
              </v-col>
              <v-col sm="1" class="mt-8 ml-2  d-flex justify-end">
                <span class="">Text<span style="color:red">*</span>:</span>
              </v-col>
              <v-col sm="4" class="ml-3">
                <v-text-field v-model="description"></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col sm="1" class="mt-3 d-flex justify-start" >
                <span class="">Image<span style="color:red">*</span>: </span>
              </v-col>
              <v-col sm="4" class=" pt-0">
                <v-file-input append-icon="mdi-file-image" @change="preview_image" dark:true v-model="image_card"></v-file-input>
              </v-col>
              <v-col sm="1" class="ml-3 mt-3 d-flex justify-start">
                <span class="">Audio:</span>
              </v-col>
              <v-col sm="4" class="pt-0">
                <v-file-input append-icon="mdi-volume-high" @change="load_audio" dark:true v-model="audio_url"></v-file-input>
              </v-col>
            </v-row>
            <v-row>
              <v-row>
                <v-col sm="1" class="mt-2 d-flex justify-start ml-3">
                    <span class="ml-3">Video:</span>
                </v-col>
                <v-col sm="4" class="pt-0">
                  <v-file-input append-icon="mdi-video-box" dark:true v-model="video_url"></v-file-input>
                </v-col>
                <v-col sm="1" class="mt-4 d-flex justify-end">
                  <span class="">Meaning:</span>
                </v-col>
                <v-col sm="4" class="pt-0">
                  <v-file-input append-icon="mdi-file-pdf-box" dark:true v-model="meaning_url"></v-file-input>
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
                    <v-card-title class="justify-center">{{title}}</v-card-title>
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
                            <v-text-field readonly v-model="description"></v-text-field>
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
            <v-col  sm="12" >
              
            </v-col>
        </v-row>
      </div>
    </v-expand-transition>
      <v-row>
        <div style="width:30%">
          <v-text-field type="text" placeholder="Search Sentence" append-icon="mdi-magnify" class="ml-4"></v-text-field>
        </div>
        <div style="width:50%" class="d-flex justify-start ml-6">
          <v-btn class="mt-3" title="New Topic" fab dark color="indigo" small @click="showForm()"> 
            <v-icon id="icon_new" dark>{{icon_new}}</v-icon>
          </v-btn>
        </div>
      </v-row>    
    <v-data-table :headers="headers" :items="desserts" :items-per-page="10" class="elevation-2">
      <template v-slot:item="row">
          <tr>
            <td>{{row.item.id}}</td>
            <td>{{row.item.text}}</td>
            <td>
              <span v-if="row.item.image"><v-icon border>mdi-image-album</v-icon> </span>
              <span v-if="row.item.audio"><v-icon  border>mdi-volume-high</v-icon> </span>
              <span v-if="row.item.video"><v-icon  border>mdi-video-box</v-icon> </span>
              <span v-if="row.item.meaning"><v-icon border>mdi-file-pdf-box</v-icon> </span>
            </td>
            
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
var audio=new Audio()
var title="Topic"
var description=""

export default {
  //Validar como funciona al motar para validar sesion valida
  data(){
  return{
    expand: false,
    icon_new:'mdi-plus',
    list_sentences:"",
    itemsT:['Colours','Pronoums','Verbs','Numbers','Membership','Colours2','Pronoums2','Verbs2','Numbers2','Membership3','Colours4','Pronoums4','Verbs4','Numbers4','Membership4'],
    description:description,
    title:title,
    image_card:null,
    image_url:"404notfoundimage.png",
    track_url:"",
    audio_url:null,
    itemsP:[],
    headers:[
      {text:"ID",align:'start',sortable:true,value:"id"},
      {text:"Text",align:'start',sortable:true,value:"text"},
      {text:"Help",align:'start',value:"description"},
      {text:"Actions",align:'start',value:"actions"}
    ],
    desserts:[
      {id:1,text:"Module One",description:"Module init",image:"url",audio:"asd",video:"",meaning:""},
      {id:2,text:"Module Two",description:"Second Module",image:"xd",audio:"asd",video:"asd",meaning:""},
      {id:3,text:"Module Three",description:"Otrher Module",image:"as",audio:"",video:"asd",meaning:"asd"},
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
    select_sentence(e){
            this.list_sentences+=','+e
            if(this.list_sentences.substr(0,1)==','){
              this.list_sentences=this.list_sentences.substring(1,this.list_sentences.length)
            }
            this.itemsT=this.itemsT.filter(session=>e!=session)


    },
    saveRegistry(){

    },
            select_module(e){
            this.title=e
        },
        select_topic(e){
            this.title=e
        },
        preview_image(){
            this.image_url= URL.createObjectURL(this.image_card)
        },
        load_audio(){
            this.track_url=URL.createObjectURL(this.audio_url)
            
        },
        play_audio(){
            audio =new Audio(this.track_url)
            audio.play()
        },
        load_video(){
            alert('xd')
        },
        play_video(){
            alert('xd3')
        }
  }
}
</script>
