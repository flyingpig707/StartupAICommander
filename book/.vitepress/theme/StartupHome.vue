<script setup>
import { withBase } from 'vitepress'
const samples = [
 { n: '02', tag: '起点', title: '先带着一个项目进来', text: '把模糊请求变成任务，填好第一张项目起点卡。', href: '/02-project' },
 { n: '06', tag: '九段高手 · 四段', title: '让一个助手把一件事做稳', text: '给出完整资料与职责，经历失败、修订和复测。', href: '/06-agent' },
 { n: '17', tag: '十步问道 · 第六步', title: '把作品变成可交付的服务', text: '写清范围、成本与报价，从拒绝中调整方案。', href: '/17-sales' },
]
</script>
<template>
  <main class="book-home">
    <section class="book-hero" aria-labelledby="book-title">
      <div class="hero-copy">
        <p class="eyebrow">AI指挥官丛书 <span>实践指南</span></p>
        <h1 id="book-title">创业<br><span>AI指挥官</span></h1>
        <p class="book-subtitle">AI九段高手十步问道</p>
        <p class="authors">张建勇 <span>吴鹏</span> 著</p>
        <p class="hero-description">带着一个真实项目，<br>把专业积累做成能交付的服务。</p>
        <div class="hero-actions">
          <a class="primary-action" :href="withBase('/02-project')">开始读样章 <span aria-hidden="true">↗</span></a>
          <a class="secondary-action" :href="withBase('/contents')">看全书目录 →</a>
        </div>
        <p class="edition"><span class="edition-dot"></span> v0.1 · 三章样章开放阅读 · 全书写作中</p>
      </div>
      <div class="cover-stage">
        <div class="cover-caption">COVER STUDY / 01</div>
        <img class="cover-image" :src="withBase('/assets/cover.png')" alt="《创业AI指挥官》封面设计初稿，副标题AI九段高手十步问道，张建勇、吴鹏著" width="1024" height="1536" />
        <p class="cover-footnote">封面设计初稿 · 非正式出版封面</p>
      </div>
    </section>
    <section class="reading-section" aria-labelledby="reading-title">
      <div class="section-header"><div><p class="eyebrow">先从这三章开始</p><h2 id="reading-title">一条项目线，三次动手。</h2></div><p class="section-aside">定义任务 → 组织AI → 验证服务</p></div>
      <div class="sample-grid">
        <a v-for="sample in samples" :key="sample.n" class="sample-card" :href="withBase(sample.href)">
          <div class="sample-meta"><span>{{ sample.tag }}</span><span>{{ sample.n }}</span></div>
          <h3>{{ sample.title }}</h3><p>{{ sample.text }}</p><span class="read-label">阅读样章 <span aria-hidden="true">↗</span></span>
        </a>
      </div>
    </section>
    <section class="tools-section">
      <div><p class="eyebrow">读完就做</p><h2>把方法留在你的项目里。</h2><p>每张行动卡都有填写示例与空白模板，可以打印或保存PDF。示例为教学演练，实际验证由你完成。</p></div>
      <div class="tool-links">
        <a :href="withBase('/toolkit-project')"><span>01</span> 项目起点卡 <span aria-hidden="true">↗</span></a>
        <a :href="withBase('/toolkit-agent')"><span>02</span> 助手职责与测试卡 <span aria-hidden="true">↗</span></a>
        <a :href="withBase('/toolkit-sales')"><span>03</span> 报价与销售反馈卡 <span aria-hidden="true">↗</span></a>
      </div>
    </section>
    <section class="book-note"><p>关于这本书</p><h2>九段建立能力，十步检验选择。</h2><p>从《AIOPC》上册的两个核心章节出发，把方法展开成操作、示范、纠错与验收。围绕同一个演练项目，先学会把事情做清楚，再去真实世界检验它是否值得做。</p><a :href="withBase('/about')">了解本书与版本说明 →</a></section>
  </main>
</template>
