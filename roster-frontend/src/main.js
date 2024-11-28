import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App)
  .use(router)   // If you're using Vue Router
  .mount('#app')

