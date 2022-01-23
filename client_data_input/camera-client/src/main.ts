import {io} from 'socket.io-client';

import Vue from 'vue';
import {createApp} from 'vue';
import App from './App.vue';
import router from './router';

// const socket = io('http://localhost:54000')
// Vue.prototype.$socket = socket
createApp(App).use(router).mount('#app');