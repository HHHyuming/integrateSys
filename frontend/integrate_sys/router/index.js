import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

export default new VueRouter({
    routes :[
        {
            path: '*',
            component: () => import('@/views/login/Login')
        },
        {
            path: '/login',
            component: () => import('@/views/login/Login')
        },
        {
            path: '/test',
            component: () => import('@/components/base/Input')
        }
    ]
})
