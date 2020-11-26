<template>
    <div>
        <el-input v-model="value">

        </el-input>
    </div>
</template>

<script>
    export default {
        name: "Input",
        props:{
            value:{
                default: ''
            }
        }
    };
</script>

<style scoped>

</style>