const axios =require('axios');
const dotenv = require('dotenv');
dotenv.config('../../.env');
const env=process.env;
//Return status 200 in other case ERROR
const insert_update_topic_card=async (card)=>{
    try {
        return axios.post(`${env.INSERT_TOPIC_CARD}`,card).catch(err=>{
            return {status:err.response.status};
        })
    } catch (error) {
        return {"status":500,"message":"INTERNAL SERVER ERROR",error}
    }
}

//Section cards
//Return all cards with STATUS 200 in other case ERROR
const get_all_cards=async ()=>{
    try {
        return axios.get(`${env.GET_ALL_CARDS}`).catch(err=>{
            return {status:err.response.status};
        })
    } catch (error) {
        return {"status":500,"message":"INTERNAL SERVER ERROR",error}
    }
}

const get_all_topics=async ()=>{
    try {
        return axios.get(`${env.GET_ALL_TOPICS}`).catch(err=>{
            return {status:err.response.status};
        })
    } catch (error) {
        return {"status":500,"message":"INTERNAL SERVER ERROR",error}
    }
}

//Return all cards of the topic with STATUS 200 in other case ERROR
const get_all_cards_by_topic=async (cveTopic)=>{
    try {
        return axios.get(`${env.GET_ALL_CARDS_BY_TOPIC}?cveTopic=${cveTopic}`).catch(err=>{
            return {status:err.response.status};
        })
    } catch (error) {
        return {"status":500,"message":"INTERNAL SERVER ERROR",error}
    }
}

//Return status 200 in other case ERROR
const delete_card=async (cveCard)=>{
    try {
        return axios.delete(`${env.DELETE_CARD}?cveCard=${cveCard}`).catch(err=>{
            return {status:err.response.status};
        })
    } catch (error) {
        return {"status":500,"message":"INTERNAL SERVER ERROR",error}
    }
}

//Return card with STATUS 200 in other case ERROR
const get_card_by_id=async (cveCard)=>{
    try {
        return axios.get(`${env.GET_CARD}?cveCard=${cveCard}`).catch(err=>{
            return {status:err.response.status};
        })
    } catch (error) {
        return {"status":500,"message":"INTERNAL SERVER ERROR",error}
    }
}


    ////SENTENCES////

//Return sentences with STATUS 200 in other case ERROR
const insert_update_sentences=async (sentence)=>{
    try {
        return axios.get(`${env.INSERT_UPDATE_SENTENCE}`).catch(err=>{
            return {status:err.response.status};
        })
    } catch (error) {
        return {"status":500,"message":"INTERNAL SERVER ERROR",error}
    }
}

//Return sentences with STATUS 200 in other case ERROR
const get_all_sentences=async ()=>{
    try {
        return axios.get(`${env.GET_ALL_SENTENCES}`).catch(err=>{
            return {status:err.response.status};
        })
    } catch (error) {
        return {"status":500,"message":"INTERNAL SERVER ERROR",error}
    }
}

const delete_sentence=async (cveSentence)=>{
    try {
        return axios.get(`${env.DELETE_SENTENCE}?cveSentence=${cveSentence}`).catch(err=>{
            return {status:err.response.status};
        })
    } catch (error) {
        return {"status":500,"message":"INTERNAL SERVER ERROR",error}
    }
}

////SESSIONS////
//Insert update session with STATUS 200 in other case ERROR


///////PENDIENTE////////////
//Return all cards of the session with STATUS 200 in other case ERROR
const get_all_cards_by_session=async (cveSession)=>{
    try {
        return axios.get(`${env.GET_ALL_CARDS_BY_SESSION}/${cveSession}`).catch(err=>{
            return {status:err.response.status};
        })
    } catch (error) {
        return {"status":500,"message":"INTERNAL SERVER ERROR",error}}
}

