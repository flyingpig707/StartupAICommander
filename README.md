# 创业AI指挥官

**AI九段高手十步问道**  
**张建勇 吴鹏 著**

帮助有专业积累的实践者，把AI能力与商业判断接起来，开展可交付的项目与服务。

v0.1为三章样章，不是全书完稿。全书规划四篇24章，其余章节仍在写作规划中。封面为设计初稿。

- [在线阅读](https://flyingpig707.github.io/StartupAICommander/)
- [全书目录](book/contents.md)
- [第二章·项目导读](book/02-project.md)
- [第六章·智能体高手](book/06-agent.md)
- [第17章·销售策略](book/17-sales.md)

## 一源维护

`book/`是唯一继续维护的Markdown正文源。阅读站直接从正文构建，行动卡也保存在其中，有填写示例与空白模板，可打印保存PDF。`book/public/assets/`保存封面图，`scripts/`保存内容检查，`.github/workflows/`负责自动部署。

## 本地使用

Node.js 22，pnpm 11.25.0：

```bash
pnpm install --frozen-lockfile
pnpm run content:check
pnpm run docs:dev
```

构建：`pnpm run docs:build`；输出：`book/.vitepress/dist`。发布方式见[DEPLOYMENT.md](DEPLOYMENT.md)。

示例培训机构与课程咨询资料整理服务均为教学设计。所有金额、工时、反馈及示意输出均为演练假设，不代表真实成交、经营效果或模型实测。

公开可读不等于整书复制、改编或商业使用授权，本仓库暂未附开放内容许可证。反馈可提Issue，请勿提交保密资料、个人隐私或未经许可的内容。
