import { defineConfig } from 'vitepress'
const base = process.env.SITE_BASE || '/StartupAICommander/'
export default defineConfig({
  lang: 'zh-CN',
  title: '创业AI指挥官',
  titleTemplate: ':title｜AI九段高手十步问道',
  description: '张建勇、吴鹏 著。把AI能力与创业判断接起来，从专业积累走向真实交付。当前开放三章样章与三张行动卡。',
  base,
  cleanUrls: true,
  lastUpdated: true,
  sitemap: { hostname: 'https://flyingpig707.github.io/StartupAICommander/' },
  head: [
    ['meta', { name: 'theme-color', content: '#b9402e' }],
    ['meta', { property: 'og:type', content: 'book' }],
    ['meta', { property: 'og:title', content: '创业AI指挥官｜AI九段高手十步问道' }],
    ['meta', { property: 'og:description', content: '张建勇 吴鹏 著 · 三章样章开放阅读' }],
    ['meta', { property: 'og:image', content: 'https://flyingpig707.github.io/StartupAICommander/assets/cover-compass-v2.png' }],
    ['link', { rel: 'icon', type: 'image/svg+xml', href: `${base}favicon.svg` }],
  ],
  themeConfig: {
    siteTitle: '创业AI指挥官',
    nav: [
      { text: '读样章', link: '/02-project' },
      { text: '全书目录', link: '/contents' },
      { text: '行动工具', link: '/toolkit-project' },
      { text: '关于本书', link: '/about' },
    ],
    sidebar: [
      { text: '阅读导引', items: [{ text: '全书目录与写作进度', link: '/contents' }, { text: '关于本书与版本', link: '/about' }] },
      { text: '三章样章 · v0.1', items: [
        { text: '02 带着一个项目，读懂九段与十步', link: '/02-project' },
        { text: '06 四段·智能体高手', link: '/06-agent' },
        { text: '17 第六步·销售策略', link: '/17-sales' },
      ] },
      { text: '可打印行动卡', items: [
        { text: '项目起点卡', link: '/toolkit-project' },
        { text: '演练资料与15条FAQ', link: '/exercise' },
        { text: '内部助手职责与测试卡', link: '/toolkit-agent' },
        { text: '报价与销售反馈卡', link: '/toolkit-sales' },
      ] },
    ],
    outline: { level: [2, 3], label: '本章目录' },
    search: { provider: 'local', options: { locales: { root: { translations: { button: { buttonText: '搜索样章', buttonAriaLabel: '搜索样章与工具' }, modal: { noResultsText: '未找到相关内容', resetButtonTitle: '清除', footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' } } } } } } },
    socialLinks: [{ icon: 'github', link: 'https://github.com/flyingpig707/StartupAICommander' }],
    docFooter: { prev: '上一篇', next: '下一篇' },
    lastUpdated: { text: '最后更新' },
    footer: { message: '样章 v0.1 · 全书写作中', copyright: '张建勇 吴鹏 著 · 公开可读，其他使用请确认授权' },
  },
})
