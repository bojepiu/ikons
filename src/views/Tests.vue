<template>
    <v-container>
        <div id="header" v-if="!showTest">
            <v-row>
                <v-col sm="12" md="4" lg="3">
                    <v-select :items="itemsModules" item-value="cveModule" item-text="moduleName"  class="mt-3" placeholder="Select Module" @change="load_sessions"></v-select>
                </v-col>
                <v-col sm="12" md="4" lg="3">
                    <v-select ref="select_session" :disabled="selectSessionDisabled" :items="itemsSession" item-value="cveSession" item-text="sessionName" class="mt-3" @change="select_session" ></v-select>
                </v-col>
                <v-col sm="6" md="4" lg="3">
                    <v-btn :disabled="!testSelected" id="btnInitTest"  depressed color="primary" class="mt-3 text-none" @click="initTest()">Init Session</v-btn>
                </v-col>
            </v-row>
        </div>
        <div id="body" v-if="showTest">
            HOLA PIANOLA
        </div>
        <div id="control">
        </div>
    </v-container>
</template>

<script>

export default {
 data: () => {
    return{
        selectSessionDisabled:true,
        testSelected:false,
        showTest:false,
        itemsModules:[{cveModule:1,moduleName:'Module One'},{cveModule:2,moduleName:'Module Two'},
        {cveModule:3,moduleName:'Module Three'},{cveModule:4,moduleName:'Module Four'}],
        itemsSession:[]
    }
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
     initTest(){
         if(this.currentTest!=0){
             console.log("Test a mostrar"+this.currentTest)
             this.showTest=true
         }
     }
 }
}
</script>

<style>

</style>