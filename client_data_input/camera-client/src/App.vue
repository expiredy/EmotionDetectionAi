<template>
    <div>
        <OptionNavBar/>
        <DebugViewer/>
    </div>
</template>

<script>
import OptionNavBar from './components/OptionNavBar.vue'
import DebugViewer from './components/DebugViewer.vue'

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
