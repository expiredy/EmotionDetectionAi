<template>
    <div class="option-section">
        <h1>Fuck you!</h1>
        <HamburgerMenu />
    </div>
</template>

<script>
import HamburgerMenu from './HamburgerMenu.vue'

export default {
    name: 'OptionNavBar',
    components: {
        HamburgerMenu
    },
    props: {}
}
</script>

<style>
.option-section{
    padding: 0;
    border: 0;
    margin: 0;
    z-index: 10;
    position: flex;
    background-color: rgb(233, 233, 233);
    -webkit-filter: drop-shadow( 25px 25px 7px #000000b3);
    filter: drop-shadow( 0px 0px 50px rgba(0, 0, 0, .7));
}
</style>
