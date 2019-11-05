import store from '@/store'
import axios from 'axios'
const apiUrl = '/api'

export default {
    regist(id, pw) {
        const data = JSON.stringify({
            username: id,
            password: pw
        })
        store.state.userData = {username : id}
        return data
    }
}
