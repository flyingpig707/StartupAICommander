import DefaultTheme from 'vitepress/theme'
import StartupHome from './StartupHome.vue'
import './style.css'
export default { extends: DefaultTheme, enhanceApp({ app }) { app.component('StartupHome', StartupHome) } }
