<template>
  <v-container>
    
    <v-expand-transition>
      <v-row v-show="expand">
        <v-col cols="12" sm="4">
          <v-text-field placeholder="Name"></v-text-field>
        </v-col>
        <v-col cols="12" sm="8">
          <v-text-field placeholder="Description" class="pl-3"></v-text-field>
        </v-col>
        <v-col cols="12" sm="4">
          <v-select :items="itemsT" class="mt-3" placeholder="Select sessions" @change="select_session"></v-select>
        </v-col>
        <v-col cols="12" sm="6">
          <v-textarea rows="1" readonly filled v-model="list_sessions"></v-textarea>
        </v-col>
        <v-col cols="12" sm="2">
          <v-btn depressed color="primary" class="mt-3 text-none" @click="saveRegistry()">Save</v-btn>
          <v-btn depressed color="secondary" class="ml-3 mt-3 text-none" @click="showForm();">Cancel</v-btn>    
        </v-col>
      </v-row>
      
    </v-expand-transition>
      
      <v-row>
        <div style="width:30%">
          <v-text-field type="text" placeholder="Search Module" append-icon="mdi-magnify" class="ml-4"></v-text-field>
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
            <td>{{row.item.sessions}}</td>
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
  //Validar como funciona al montar para validar sesion valida
  data(){
  return{
    dialog:false,
    expand: false,
    icon_new:'mdi-plus',
    list_sessions:"",
    itemsT:['Pronoums','Verbs','Numbers','Membership'],
    headers:[
      {text:"ID",align:'start',sortable:true,value:"id"},
      {text:"Name",align:'start',sortable:true,value:"name"},
      {text:"Description",align:'start',value:"description"},
      {text:"Sessions",align:'start',value:"sessions"},
      {text:"Actions",align:'start',value:"actions"}
    ],
    desserts:[
      {id:1,name:"Module One",description:"Module init",sessions:5},
      {id:2,name:"Module Two",description:"Second Module",sessions:1},
      {id:3,name:"Module Three",description:"Otrher Module",sessions:3},
    ]
  }
  },
  methods:{
    showForm() {
      this.expand = !this.expand
      if(this.expand){this.icon_new='mdi-minus'}
      else{this.icon_new='mdi-plus'}
    },
    select_session(e){
            this.list_sessions+=','+e
            if(this.list_sessions.substr(0,1)==','){
              this.list_sessions=this.list_sessions.substring(1,this.list_sessions.length)
            }
            this.itemsT=this.itemsT.filter(session=>e!=session)


    },
    saveRegistry(){

    }
  }
}
</script>
