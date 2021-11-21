<template>
  <v-container class="d-flex">
    <v-card elevation="2" width="100%" height="350px">
        <v-card-title class="justify-center">{{title}}</v-card-title>
        <hr>
        <v-card-text class="justify-center">
            <v-row>
                <v-img
                contain
                max-width="95%"
                :src="image_url"
                ></v-img>
            </v-row>
            
        </v-card-text>
        <hr>
        <br>
        <v-card-actions class="pt-0">
            <v-row class="d-flex justify-center">
                <v-icon medium class="ml-0">mdi-arrow-left-circle</v-icon>
                <v-icon medium class="p-0">mdi-arrow-right-circle</v-icon>
                <v-icon medium class="pl-4">mdi-volume-high</v-icon> 
                <v-icon medium class="">mdi-video-box</v-icon> 
                <v-icon medium class="">mdi-file-pdf-box</v-icon> 
                <v-icon medium class="ml-4" @click="change_mark">mdi-pound</v-icon>
                <v-icon medium @click="clear_mark">mdi-backspace</v-icon>
            </v-row>
        </v-card-actions>
    </v-card>
    <v-img
        v-if="image_url_mark"
        contain
        max-width="60px"
        :style="image_margin_top"
        :src="image_url_mark"
        class="img_marker"
    ></v-img>
  </v-container>
</template>

<script>
export default {
    //add properties
    
    name: 'Contact-Component',
    props: {'title':String},
    data(){
        return{
            image_card:null,
            image_url:"404notfoundimage.png",
            image_url_mark:null,
            track_url:"",
            audio_url:null,
            index_mark_items:0,
            image_margin_top:"0px",
            marks_items:[
                {mt:"margin-top:0px",src:"/images/questionmark.png"},
                {mt:"margin-top:0px",src:"/images/exclamation.png"},
                {mt:"margin-top:150px",src:"/images/comma.png"},
                {mt:"margin-top:-120px",src:"/images/comilla.png"}]
        }
    },
    methods:{
        change_mark(){
            this.image_url_mark=this.marks_items[this.index_mark_items].src;
            this.image_margin_top=this.marks_items[this.index_mark_items].mt;
            this.index_mark_items = (this.index_mark_items + 1) % this.marks_items.length;
        },
        clear_mark(){
            this.image_url_mark="";
        }
    }
}
</script>

<style>
#img_marker {
    top: 150px;
    left: 10px;
}
</style>