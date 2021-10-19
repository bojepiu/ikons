<template>
  <v-container>
    <v-expand-transition>
      <div v-show="expand">
        <v-row class="pt-5">
            <h4>Create a new Card</h4>
        </v-row>
        <v-row>
            <v-col sm="1" class="pt-10">
                <span>Topic<span style="color:red">*</span>:</span>
            </v-col>
            <v-col sm="4">
                <v-combobox :items="itemsT" @change="select_topic"></v-combobox>
            </v-col>
            <v-col sm="1" class="pt-10 ml-0">
                <span class="mt-6">Text<span style="color:red">*</span>: </span>
            </v-col>
            <v-col sm="4" class="pt-3 ml-0">
                <v-text-field v-model="description"></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col sm="1" class="pt-6 ml-0">
                <span class="pt-6 ml-2">Image<span style="color:red">*</span>: </span>
            </v-col>
            <v-col sm="4" class="pt-0">
                <v-file-input append-icon="mdi-file-image" @change="preview_image" dark:true v-model="image_card"></v-file-input>
            </v-col>
            <v-col sm="1" class="mt-4">
                <span class="mt-6">Audio:</span>
            </v-col>
            <v-col sm="4" class="pt-0">
                <v-file-input append-icon="mdi-volume-high" @change="load_audio" dark:true v-model="audio_url"></v-file-input>
            </v-col>
        </v-row>
        <v-row>
            <v-col sm="1" class="pt-6 ml-0">
                <span class="pt-6 ml-2">Video: </span>
            </v-col>
            <v-col sm="4" class="pt-0">
                <v-file-input append-icon="mdi-video-box" dark:true v-model="image_card"></v-file-input>
            </v-col>
            <v-col sm="1" class="mt-4">
                <span class="mt-6">Meaning:</span>
            </v-col>
            <v-col sm="4" class="pt-0">
                <v-file-input append-icon="mdi-file-pdf-box" dark:true v-model="audio_url"></v-file-input>
            </v-col>
        </v-row>
        <v-row>
            <v-row>
                <v-card elevation="2" width="150" height="165">
                    <v-card-title class="justify-center">{{title}}</v-card-title>
                    <v-card-text class="justify-center">
                        <v-row>
                        <v-img
                        contain
                        max-height="90"
                        max-width="160"
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
            </v-row>
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
            <td>{{row.item.name}}</td>
            <td>{{row.item.description}}</td>
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
      {text:"Name",align:'start',sortable:true,value:"name"},
      {text:"Description",align:'start',value:"description"},
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
