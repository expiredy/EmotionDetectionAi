<template>
    <div class="main-menu-activator">
        <div class="col" v-on:onclick="OpenMenu">
            <div class="special-con">
                <div class="bar arrow-top-fall"></div>
                <div class="bar arrow-middle-fall"></div>
                <div class="bar arrow-bottom-fall"></div>
            </div>
         </div>
    </div>
</template>

<script>
export default {
    name: 'HamburgerMenu',
    props: { },
    methods: {
        OpenMenu: function (event) {
            console.log("Sheeesh")
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
   background: #6FFFE9;
   margin: 10px auto;
 }

.special-con:hover .bar {
  background-color: #f92c8c;
}

.col {
   display: inline-block;
   width: 24%;
   text-align: center;
   height: auto;
   position: relative;
}

.middle {
   margin: 0 auto;
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
