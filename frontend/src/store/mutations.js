export default {
    setApiList(state, payload) {
        state.ApiLists = payload.map(m => m)
    }
}
