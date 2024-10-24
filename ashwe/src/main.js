import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min';

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios';

const app = createApp(App)
axios.defaults.baseURL = "https://ashwe.pythonanywhere.com/"
app.use(createPinia())
app.use(router)

app.mount('#app')
