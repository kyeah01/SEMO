import axios from 'axios'
import auth from './modules/auth'

const apiUrl = '/api'

export default{
    regist(id, pw) {
        return auth.regist(id, pw)
    }
}
