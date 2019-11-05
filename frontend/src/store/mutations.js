export default {
    setApiList(state, payload) {
        state.ApiLists = payload.map(m => m)
    },
    setNewApi(state, payload) {
        state.ApiLists.push(payload)
        state.postData = true
    }
}
