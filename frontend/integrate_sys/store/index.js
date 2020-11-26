import Vue from 'vue'
import vuex from 'vuex'

import actions from './actions'
import mutations from './mutations'
import modules from './modules'
Vue.use(vuex)

export default new vuex.Store({
    state:{

    },
    modules,
    actions,
    mutations
})