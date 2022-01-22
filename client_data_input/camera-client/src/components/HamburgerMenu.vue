<template>
    <div class="main-menu-activator">
        <button class="hamburger-button" v-on:click="OpenMenu">
            <div class="col">
               <div class="special-con">
                  <div class="bar arrow-top-fall"></div>
                  <div class="bar arrow-middle-fall"></div>
                  <div class="bar arrow-bottom-fall"></div>
               </div>
            </div>
        </button>
    </div>
</template>

<script>
export default {
    name: 'HamburgerMenu',
    props: { },
    methods: {
         OpenMenu: function (event) {
            if (event) {
            console.log('Sheeesh')
            }
         }
      }
}

</script>

<style>
.special-con {
   cursor: pointer;
   display: inline-block;
}
.bar {
   display: block;
   height: 5px;
   width: 50px;
   background: #df0000;
   margin: 10px auto;
 }

.special-con:hover .bar {
  background-color: #048300;
}

.col {
   display: inline-block;
   text-align: center;
   height: auto;
   position: relative;
   z-index: 100;
}

.middle {
   margin: 0 auto;
}

.hamburger-button{
   border: none;
   outline: none;
   background-color: rgba(0,0,0,0);
}

.bar {
   -webkit-transition: all .7s ease;
   -moz-transition: all .7s ease;
   -ms-transition: all .7s ease;
   -o-transition: all .7s ease;
   transition: all .7s ease;
}

.special-con {
   margin: 0 auto;
   -webkit-transition: all .7s ease;
   -moz-transition: all .7s ease;
   -ms-transition: all .7s ease;
   -o-transition: all .7s ease;
   transition: all .7s ease;
}

.special-con:hover .arrow-top-fall {
   -webkit-transition: all .7s ease-in-out;
   -moz-transition: all .7s ease-in-out;
   -ms-transition: all .7s ease-in-out;
   -o-transition: all .7s ease-in-out;
   transition: all .7s ease-in-out;
   -webkit-transform: translateY(15px);
   -moz-transform: translateY(15px);
   -ms-transform: translateY(15px);
   -o-transform: translateY(15px);
   transform: translateY(15px);
}

.arrow-bottom-fall,
.arrow-top-fall {
   -webkit-transition: all .7s ease-in-out;
   -moz-transition: all .7s ease-in-out;
   -ms-transition: all .7s ease-in-out;
   -o-transition: all .7s ease-in-out;
   transition: all .7s ease-in-out;
}

.special-con:hover .arrow-bottom-fall {
   -webkit-transform: translateY(-15px);
   -moz-transform: translateY(-15px);
   -ms-transform: translateY(-15px);
   -o-transform: translateY(-15px);
   transform: translateY(-15px);
   -webkit-transition: all .7s ease-in-out;
   -moz-transition: all .7s ease-in-out;
   -ms-transition: all .7s ease-in-out;
   -o-transition: all .7s ease-in-out;
   transition: all .7s ease-in-out;
}
</style>
