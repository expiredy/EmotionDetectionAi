<template>
    <div>
        <OptionNavBar/>
    </div>
</template>

<script>
import OptionNavBar from "./components/OptionNavBar.vue"

export default {
  name: 'App',
  components: {
    OptionNavBar
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
  margin-top: 60px;
}
</style>
