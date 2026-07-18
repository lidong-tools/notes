---
title: "挖到一个好东西，claude-seo Skills，25 个子技能 | Web.Cafe"
source: "https://new.web.cafe/topic/ijs583drxq"
archived_at: 2026-07-18T07:26:40.563Z
---

# 挖到一个好东西，claude-seo Skills，25 个子技能

兄弟们，最近挖到一个好东西，必须分享出来。

还没用上的兄弟们可以试试看。

claude-seo 是一套给 Claude Code（也支持 Cursor / Codex CLI 等）用的 SEO 分析工具集，MIT 开源，完全免费。作者 Agrici Daniel 一个人肝出来的，质量和社区维护都很在线。

## 它有什么？

25 个子技能，基本覆盖 SEO 全链路：

| 命令 | 干啥的 |
|---|---|
| `/seo audit ` | 全站审计，15 个并行 agent 同时跑，十几分钟出报告 |
| `/seo page ` | 单页深度分析 |
| `/seo technical ` | 技术 SEO（9 个维度：可爬性、可索引、安全性、CWV 等） |
| `/seo content ` | E-E-A-T 内容质量分析 |
| `/seo schema ` | Schema.org 检测 / 生成 / 验证 |
| `/seo geo ` | AI 搜索优化（AI Overviews / GEO） |
| `/seo local ` | 本地 SEO（GBP、NAP、引用、评论） |
| `/seo maps ...` | 地图情报（geo-grid 排名追踪、竞品半径） |
| `/seo backlinks ` | 外链分析（Moz / Bing / Common Crawl） |
| `/seo cluster <关键词>` | 语义主题聚类，出内容架构图 |
| `/seo sxo ` | 搜索体验优化（页面类型匹配、用户故事） |
| `/seo drift baseline/comapre ` | SEO 漂移监控（SQLite 快照比对） |
| `/seo ecommerce ` | 电商 SEO（商品 schema、市场情报） |
| `/seo hreflang ` | 多语言 SEO 审计 |
| `/seo plan <行业>` | 按行业出 SEO 策略规划 |
| `/seo sitemap ` | sitemap 分析 / 生成 |
| `/seo images ` | 图片优化分析 |
| `/seo programmatic` | 程序化 SEO |
| `/seo competitor-pages` | 竞品对比页面生成 |

还有 8 个可选扩展（DataForSEO、Ahrefs、Firecrawl、SE Ranking、Profound、Bing、Unlighthouse、AI 图片生成），需要自己配账号。

## 我觉得最牛的几个点

1. 每条建议都可证伪

这一点直接吊打所有商业工具。每个推荐都附带：

- 基于什么一阶观察得出的结论
- 依赖哪些其他建议
- "怎么判断这条建议失败了" 的验证方式
- 领先指标

不是那种"建议优化内容"的废话，而是可执行、可验证的。

2. AI 搜索优化非常硬核

紧跟 Google AI Optimization Guide，不跟风搞什么 llms.txt 玄学、内容分块之类的伪概念。实打实评分段落可引用性（134-167 词自包含回答块）、问题式标题层级、引用密度、实体覆盖。

3. 全站并行审计 15 分钟出报告

比起 Agency 等 1-3 周，或者 Screaming Frog 先 crawl 半小时再说，claude-seo 直接并行 15 个 agent，十几分钟出一份带 0-100 分的优先行动清单。

4. 完全本地运行

数据不出机器，没有订阅费，没有按域名计费，没有遥测。Google API 是可选增强（免费额度），不用也行。

5. 生态联动

可以跟 Claude Blog 联动：审计出内容缺口 -&gt; 直接写优化过的博客 -&gt; 生成 OG 图。一条龙。

## 谁适合用？

- SEO Agency ：每天跑一遍客户审计，周报变日报
- In-house SEO ：季度复盘前跑一轮，堵住 CMO 的嘴
- Freelance 顾问 ：第一次沟通直接跑审计，用 0-100 分和 3 条关键问题锚定 engagement
- 独立站站长/创业者 ：零成本 get 专业级 SEO 诊断

### 安装

```bash
# Claude Code 插件安装（1.0.33+）
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo

# 或者手动
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/install.sh
```

然后开箱即用：

```javascript
/seo audit https://你的网站.com
```

### 缺点也要说

- 重度 SPA 的 hydration edge case 还有噪音（比如滚动触发的内容加载）
- 不用 Google API 的话 CWV 只有 lab 数据

但这些都是可接受的 trade-off，考虑到它是 MIT 开源且免费。

总的来说，这可能是目前市面上 性价比最高 的 SEO 审计方案。

没有之一。

👉 GitHub： github.com/AgriciDaniel/claude-seo

- 感谢分享！！！👍👍👍
- 谢谢分享 很好的东西。
- 感谢分享！！！👍👍👍 很好的东西。
