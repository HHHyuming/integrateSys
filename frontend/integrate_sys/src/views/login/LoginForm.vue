<template>
    <div class="login-form-style">
        <el-row class="row-one">
            <el-col :span="24" type="flex">
                <div class="title" >
                    <span class="span-title">FEBS 系统登录</span>
                    <i class="iconfont el-zhongyingwenqiehuan"></i>
                </div>
            </el-col>
        </el-row>

        <el-row class="row-two">
            <el-col :span="24" type="flex">
                <el-input prefix-icon="el-icon-user" placeholder="账号" v-model="username">
                </el-input>
            </el-col>
        </el-row>

        <el-row class="row-three">
            <el-col :span="24" type="flex">
                <el-input prefix-icon="pb-icon_password" placeholder="密码" v-model="password"></el-input>
            </el-col>
        </el-row>

        <el-row class="row-four">
            <el-col :span="12" type="flex">
                <el-input prefix-icon="pb-icon_password" placeholder="验证码"></el-input>
            </el-col>
            <el-col :span="8" :offset="2">
            <div class="code-image"></div>
            </el-col>

        </el-row>

        <el-row class="submit-login">
            <el-col :span="24" type="flex">
                <el-button type="primary">立即登录</el-button>
            </el-col>
        </el-row>

        <el-row class="other-login-way">
            <el-col :span="10" type="flex" :offset="18">
                其他登录方式
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "LoginForm",
        data(){
            return{
                username:'',
                password:''
            }
        }
    };
</script>

<style scoped lang="scss">
    @import "../../style/login/loginForm";

</style>