<template>
  <v-container>
    <v-expand-transition>
      <v-row v-show="expand">
        <v-col cols="12" sm="4">
          <v-text-field placeholder="Text"></v-text-field>
        </v-col>
        <v-col cols="12" sm="4">
          <v-select :items="itemsT" class="mt-3" placeholder="Select topic" @change="loadTopic"></v-select> 
        </v-col>
        <v-col cols="12" sm="4">
            <v-select :items="itemsP" class="mt-3" placeholder="Select card" @change="select_sentence"></v-select>
        </v-col>
        <v-col cols="12" sm="4">
          <v-text-field rows="1" readonly placeholder="Sentence" filled v-model="list_sentences"></v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-file-input append-icon="mdi-file-image" clearable dark></v-file-input>
          
        </v-col>
        <v-col cols="12" sm="2">
            <v-file-input append-icon="mdi-volume-high" clearable dark></v-file-input>  
        </v-col>
        <v-col cols="12" sm="2">
            <v-file-input append-icon="mdi-file-pdf-box" clearable dark></v-file-input>
        </v-col>
        <v-col cols="12" sm="2">
          <v-btn depressed color="primary" class="mt-3 text-none" @click="saveRegistry()">Save</v-btn>
          <v-btn depressed color="secondary" class="ml-3 mt-3 text-none" @click="showForm();">Cancel</v-btn>    
        </v-col>
      </v-row>
      
    </v-expand-transition>
      
      <v-row>
        <div style="width:30%">
          <v-text-field type="text" placeholder="Search Sentence" append-icon="mdi-magnify" class="ml-4"></v-text-field>
        </div>
        <div style="width:50%" class="d-flex justify-start ml-6">
          <v-btn class="mt-3" title="New Module" fab dark color="indigo" small @click="showForm()"> 
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
            <td>{{row.item.sentences}}</td>
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

export default {
  //Validar como funciona al motar para validar sesion valida
  data(){
  return{
    expand: false,
    icon_new:'mdi-plus',
    list_sentences:"",
    itemsT:['Pronoums','Verbs','Verbs2','Lo que sea'],
    itemsP:[],
    headers:[
      {text:"ID",align:'start',sortable:true,value:"id"},
      {text:"Name",align:'start',sortable:true,value:"name"},
      {text:"Description",align:'start',value:"description"},
      {text:"Sentences",align:'start',value:"sentences"},
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

    }
  }
}
</script>
