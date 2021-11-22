<template>
    <v-container>
        <div id="header" v-if="!showBody">
            <v-row>
                <v-col sm="12" md="4" lg="3">
                    <v-select :items="itemsModules" :disabled="showBody" item-value="cveModule" item-text="moduleName"  class="mt-3" placeholder="Select Module" @change="load_sessions"></v-select>
                </v-col>
                <v-col sm="12" md="4" lg="3">
                    <v-select ref="select_session" :disabled="selectSessionDisabled || showBody" :items="itemsSession" item-value="cveSession" item-text="sessionName" class="mt-3" @change="select_session" ></v-select>
                </v-col>
                <v-col sm="6" md="4" lg="3">
                    <v-btn :disabled="!testSelected || showBody" id="btnInitTest"  depressed color="primary" class="mt-3 text-none" @click="initTest()">Init Session</v-btn>
                </v-col>
            </v-row>
        </div>
        <div id="body" v-if="showBody">
            <Skeleton v-if="showSkeleton"/>    
            <div id="bodytest" v-if="showTest">
                <v-row>
                    <v-col sm="12" md="6" lg="3"><Card v-bind:title="sentence[0].text[0]"/></v-col>
                    <v-col sm="12" md="6" lg="3"><Card v-bind:title="sentence[0].text[1]"/></v-col>
                    <v-col sm="12" md="6" lg="3"><Card v-bind:title="sentence[0].text[2]"/></v-col>
                    <v-col sm="12" md="6" lg="3"><Card v-bind:title="sentence[0].text[3]"/></v-col>    
                </v-row>
            </div>
            <v-footer style="margin-top:140px">
                <ControlPanel/>
            </v-footer>
        </div>
    </v-container>
</template>

<script>
import Card from '../components/TestCard.vue'
import ControlPanel from '../components/ControlPanel.vue'
import Skeleton from '../components/Skeleton.vue'

export default {
 data: () => {
    return{
        sentence:[{text:["title1","title2","title3","title4"]}],
        selectSessionDisabled:true,
        testSelected:false,
        showBody:false,
        showTest:false,
        showSkeleton:true,
        itemsModules:[{cveModule:1,moduleName:'Module One'},{cveModule:2,moduleName:'Module Two'},
        {cveModule:3,moduleName:'Module Three'},{cveModule:4,moduleName:'Module Four'}],
        itemsSession:[]
    }
 },
components:{
    Card,
    ControlPanel,
    Skeleton
    },
 methods:{
     load_sessions(e){
         this.selectSessionDisabled=true
         this.testSelected=false
         this.$refs["select_session"].reset()
         this.itemsSession=[]
         if(e!=undefined){
             this.currentTest=0
             console.log("Load Sessions")
             this.itemsSession=[{cveSession:1,sessionName:'Module '+e+'Session 1'},{cveSession:2,sessionName:'Module '+e+'Session 2'}]
             this.selectSessionDisabled=false
         }
     },
     select_session(e){
         if(e!=undefined){
            this.testSelected=true
            this.currentTest=e
         }
         
     },
    loadTest(){
        this.showBody=true
        this.showSkeleton=true
        this.activate()
    },
    activate() {
         setTimeout(() => {this.showSkeleton = false; this.showTest=true}, 100);
    },
    initTest(){
        if(this.currentTest!=0){
            this.loadTest()
            console.log("Test a mostrar"+this.currentTest)
        }
    }
 }
}
</script>

<style>

</style>