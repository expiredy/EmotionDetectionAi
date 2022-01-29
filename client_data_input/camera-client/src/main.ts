import {io} from 'socket.io-client';
import {createApp} from 'vue';
import App from './App.vue';
import router from './router';
import initializeSocket from '@/compositions/useWebSocket';

initializeSocket();
createApp(App).use(router).mount('#app');