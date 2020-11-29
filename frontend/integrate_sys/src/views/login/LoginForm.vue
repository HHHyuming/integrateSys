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
                <el-input prefix-icon="el-icon-user" placeholder="账号">
                </el-input>
            </el-col>
        </el-row>

        <el-row class="row-three">
            <el-col :span="24" type="flex">
                <el-input prefix-icon="el-icon_password" placeholder="密码"></el-input>
            </el-col>
        </el-row>

        <el-row class="row-four">
            <el-col :span="24" type="flex">
                <el-input prefix-icon="el-icon_password" placeholder="验证码"></el-input>
                <div class="code-image"></div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "LoginForm"
    };
</script>

<style scoped lang="scss">
    @import "../../style/login/loginForm";

</style>