<template>
    <div>
        <OptionNavBar/>
        <div id="nav">
            <router-link to="/">Home</router-link> |
            <router-link to="/about">About</router-link>
        </div>
        <router-view/>

        <DebugViewer/>
    </div>
</template>

<script>
import OptionNavBar from '@/components/OptionNavBar.vue'
import DebugViewer from '@/components/DebugViewer.vue'

export default {
    name: 'App',
    components: {
        OptionNavBar,
        DebugViewer
    }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
</style>
