<template>
    <div class="nav-menu">
        导航栏
    </div>
</template>

<script>
    export default {
        name: "NavMenu",
        data(){
            return{
                renderPath:[
                    {
                        name:'系统管理',
                        icon: '',
                        path: '',
                        children:[]
                    }
                ]
            }
        }

    };
</script>

<style scoped>

</style>