<template>
    <div>
        <el-input v-model="inputValue" :placeholder="placeholder" show-password>
        </el-input>
    </div>
</template>

<script>
    export default {
        name: "Input",
        props:{
            inputValue:{
                default: ''
            },
            placeholder:{
                default: '请输入内容'
            },
        }
    };
</script>

<style scoped>

</style>