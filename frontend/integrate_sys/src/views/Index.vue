<template>
    <div class="index-page">
        <el-container>
            <el-aside class="aside">
                <div class="title">
                    <div class="logo"></div>
                    <span>ITG管理系统</span>
                </div>
                <NavMenu></NavMenu>
            </el-aside>
            <el-container>
                <el-header>Header</el-header>
                <el-main>
                    <router-view></router-view>
                </el-main>
            </el-container>
        </el-container>

    </div>
</template>

<script>
    import NavMenu from "../components/NavMenu";
    export default {
        name: "Index",
        components:{
            NavMenu
        }
    };
</script>

<style  lang="scss">
@import "@/style/index.scss";
</style>