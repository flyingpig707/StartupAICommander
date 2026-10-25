# 阅读站部署

默认发布地址：`https://flyingpig707.github.io/StartupAICommander/`。

## 构建

Node.js 22，pnpm 11.25.0。依次运行：

```bash
pnpm install --frozen-lockfile
pnpm run content:check
pnpm run docs:build
```

产物为 `book/.vitepress/dist`，不提交Git。默认站点前缀 `/StartupAICommander/`；以后迁至独立域名根目录时设置 `SITE_BASE=/` 再构建。

## 自动发布

Pages构建来源为GitHub Actions。`main`推送或手动触发运行 `.github/workflows/pages.yml`：安装锁定依赖、内容检查、构建、上传产物、部署。

工作流成功后再核对线上首页、三个样章、三张工具卡、封面、全文搜索、窄屏导航与打印样式，才记录为完成。

本版不绑定自定义域名。封面是正面概念设计，尚无印刷出血、书脊、封底、ISBN或出版社信息。

`edgeone.json`保留兼容配置，便于以后沿用丛书平台；文件存在不代表EdgeOne已部署。迁移时重新确认域名和SITE_BASE。
