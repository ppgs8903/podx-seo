# Podxero — 企业级 GEO / AI 搜索智能平台

纯静态 HTML 站点，无构建依赖、无框架。GitHub Pages 自动部署。

## 站点结构

| 路径 | 页面 | 来源设计稿 |
| --- | --- | --- |
| `site/index.html` | 首页 | `podxero_geo_ai_1/code.html` |
| `site/solutions.html` | 解决方案 | `podxero_geo_ai_2/code.html` |
| `site/platform.html` | 智能平台 | `podxero/code.html` |
| `site/benchmarks.html` | 基准与洞察 | `podxero_geo/code.html` |
| `site/comparison.html` | 方案对比（SEO vs GEO） | `podxero_seo_vs_podxero_geo/code.html` |
| `site/diagnostic.html` | 免费 GEO 诊断 | `src/diagnostic.html`（手写） |
| `site/404.html` | 404 页 | `src/404.html`（手写） |

## 目录约定

- `podxero*/` — 原始设计稿（`code.html` + `screen.png`），只作设计源，不直接发布
- `src/` — 非设计稿衍生的手写页面
- `site/` — 构建产物，由 `tools/build_site.py` 生成，**不要手改**
- `tools/build_site.py` — 把设计稿里的 `data-path` + `href="#"` 重写成真实相对链接，并注入带当前页高亮的导航

## 本地开发

```bash
python3 tools/build_site.py
cd site && python3 -m http.server 8899
# 打开 http://127.0.0.1:8899/index.html
```

## 部署

推送到 `main` 后 `.github/workflows/deploy-pages.yml` 自动构建并发布到 GitHub Pages。

Pages 源设置为 **GitHub Actions**（首次需要仓库 Settings → Pages → Source 选择 GitHub Actions；workflow 内含 `enablement: true` 会自动开启）。

## 路由约定

所有页面用 `.html` 相对链接，避免依赖服务器 rewrite 规则。
