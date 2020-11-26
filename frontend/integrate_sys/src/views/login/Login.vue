<template>
    <div class="login-main">
        <LoginForm></LoginForm>
    </div>
</template>

<script>
    import LoginForm from "./LoginForm";
    export default {
        name: "Login",
        components:{
            LoginForm
        }

    };
</script>

<style scoped lang="scss">
    @import "../../style/login/login";

</style>