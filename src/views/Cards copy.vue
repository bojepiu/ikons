<template>
  <v-container>
        <v-row class="pt-0">
        <v-col cols="12" sm="6" class="pt-0">
            <v-row class="pt-0">
                <h3 class="pt-6">Cards</h3>
            </v-row>
            <v-row class="pt-0 mt-0">
                <span class="mt-6 ml-3">Topic<span style="color:red">*</span>:</span>
                <v-col cols="6" sm="6" class="pt-0">
                <v-combobox class="pl-4   " :items="itemsT" @change="select_topic"></v-combobox>
                </v-col>
            </v-row>
            <v-row class="pt-0 mt-0">
                <span class="mt-6 ml-5">Text<span style="color:red">*</span>: </span>
                <v-col cols="6" sm="6" class="pt-0 mt-0">
                <v-text-field class="pl-4" v-model="description"></v-text-field>
                </v-col>
            </v-row>
            <v-row class="pt-0 mt-0">
                <span class="mt-6 ml-2">Image<span style="color:red">*</span>: </span>
                <v-col cols="6" sm="6" class="pt-0">
                <v-file-input append-icon="mdi-file-image" @change="preview_image" v-model="image_card" clearable:true dark:true></v-file-input>
                </v-col>
            </v-row>
            <v-row class="pt-0 mt-0">
                <span class="mt-6 ml-5">Audio:</span>
                <v-col cols="6" sm="6" class="pt-0">
                <v-file-input @change="load_audio" append-icon="mdi-volume-high" clearable:true dark:true v-model="audio_url"></v-file-input>
                </v-col>
            </v-row>
            <v-row class="pt-0 mt-0">
                <span class="mt-6 ml-5">Video:</span>
                <v-col cols="6" sm="6" class="pt-0">
                <v-file-input append-icon="mdi-video-box" clearable:true dark:true></v-file-input>
                </v-col>
            </v-row>
            <v-row class="pt-0 mt-0">
                <span class="mt-6">Meaning:</span>
                <v-col cols="6" sm="6" class="pt-0">
                <v-file-input append-icon="mdi-file-pdf-box" clearable:true dark:true></v-file-input>
                </v-col>
            </v-row>
            <v-row class="d-flex justify-center">
            <v-btn depressed color="primary" class="pa-4 mt-3">Save</v-btn>
            </v-row>
        </v-col>
        <v-col cols="12" sm="6">
            <v-row class="pt-3">
                <h3>Preview</h3>
            </v-row>
            <v-row class="d-flex justify-center ">
                <v-card elevation="2" width="300" height="370">
                    <v-card-title class="justify-center">{{title}}</v-card-title>
                    <v-card-text class="justify-center">
                        <v-row>
                        <v-img
                        contain
                        max-height="180"
                        max-width="260"
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
        </v-col>
        </v-row>
        <v-row>
        </v-row>
    </v-container>
</template>

<script>

var audio=new Audio()
var title="Topic"
var description=""
export default {
 data: () => ({
      itemsT:['Colours','Pronoums','Verbs','Numbers','Membership','Colours2','Pronoums2','Verbs2','Numbers2','Membership3','Colours4','Pronoums4','Verbs4','Numbers4','Membership4'],
      description:description,
      title:title,
      image_card:null,
      image_url:"404notfoundimage.png",
      track_url:"",
      audio_url:""
    }),
    watch:{
        select(val){
        this.items.push(val);
        }
    },
    methods:{
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

<style>

</style>