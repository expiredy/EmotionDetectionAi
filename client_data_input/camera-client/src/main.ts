import {io} from 'socket.io-client';

import Vue from 'vue';
import {createApp} from 'vue';
import App from './App.vue';
import router from './router';

createApp(App).use(router).mount('#app');
