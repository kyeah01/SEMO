import axios from 'axios'
const apiUrl = '/api'

export default {
    regist(id, pw) {
        const data = JSON.stringify({
            username: id,
            password: pw
        })
        return data
    }
}
