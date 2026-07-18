---
title: "用 Claude SEO Skill 做一次全站审计，比我预期的要细 | Web.Cafe"
source: "https://new.web.cafe/topic/t9vpt7evaq"
archived_at: 2026-07-18T07:13:05.369Z
---

# 用 Claude SEO Skill 做一次全站审计，比我预期的要细

最近试了一下 AgriciDaniel 做的 Claude SEO Skill。

地址在这里： https://github.com/AgriciDaniel/claude-seo

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%94%A8%20Claude%20SEO%20Skill%20%E5%81%9A%E4%B8%80%E6%AC%A1%E5%85%A8%E7%AB%99%E5%AE%A1%E8%AE%A1%EF%BC%8C%E6%AF%94%E6%88%91%E9%A2%84%E6%9C%9F%E7%9A%84%E8%A6%81%E7%BB%86%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2015%EF%BC%9A12%EF%BC%9A57).assets/image-003.png)

如果你用的是 Codex，他也有配套版本： https://github.com/AgriciDaniel/codex-seo

## 上手比我想的还简单

按文档说明，直接对目标站点跑这条命令就行：

```javascript
/seo audit <url>
```

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%94%A8%20Claude%20SEO%20Skill%20%E5%81%9A%E4%B8%80%E6%AC%A1%E5%85%A8%E7%AB%99%E5%AE%A1%E8%AE%A1%EF%BC%8C%E6%AF%94%E6%88%91%E9%A2%84%E6%9C%9F%E7%9A%84%E8%A6%81%E7%BB%86%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2015%EF%BC%9A12%EF%BC%9A57).assets/image-004.png)

我直接用了自己的站点做测试。

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%94%A8%20Claude%20SEO%20Skill%20%E5%81%9A%E4%B8%80%E6%AC%A1%E5%85%A8%E7%AB%99%E5%AE%A1%E8%AE%A1%EF%BC%8C%E6%AF%94%E6%88%91%E9%A2%84%E6%9C%9F%E7%9A%84%E8%A6%81%E7%BB%86%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2015%EF%BC%9A12%EF%BC%9A57).assets/image-005.png)

整个过程大概跑了 10 分钟。页面多的话，时间会再长一点。

跑完之后，会先出一个概览。里面有总体评分、最关键的问题，还有一些「改了就能见效」的快速收益项。

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%94%A8%20Claude%20SEO%20Skill%20%E5%81%9A%E4%B8%80%E6%AC%A1%E5%85%A8%E7%AB%99%E5%AE%A1%E8%AE%A1%EF%BC%8C%E6%AF%94%E6%88%91%E9%A2%84%E6%9C%9F%E7%9A%84%E8%A6%81%E7%BB%86%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2015%EF%BC%9A12%EF%BC%9A57).assets/image-006.png)

## 它到底输出了什么

最实用的有三个文件：

1. 完整审计报告
2. 行动计划
3. 可以生成 PDF 的结构化数据

报告和行动计划默认是英文的。我直接让 AI 翻成了中文，能看懂。

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%94%A8%20Claude%20SEO%20Skill%20%E5%81%9A%E4%B8%80%E6%AC%A1%E5%85%A8%E7%AB%99%E5%AE%A1%E8%AE%A1%EF%BC%8C%E6%AF%94%E6%88%91%E9%A2%84%E6%9C%9F%E7%9A%84%E8%A6%81%E7%BB%86%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2015%EF%BC%9A12%EF%BC%9A57).assets/image-007.png)

报告的内容非常细。技术、内容、页面 SEO、schema、性能、AI 搜索、图片优化，全都有。

而且每个问题都按紧急程度排了序。Critical 到 Low，一眼就能看出来优先级。

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%94%A8%20Claude%20SEO%20Skill%20%E5%81%9A%E4%B8%80%E6%AC%A1%E5%85%A8%E7%AB%99%E5%AE%A1%E8%AE%A1%EF%BC%8C%E6%AF%94%E6%88%91%E9%A2%84%E6%9C%9F%E7%9A%84%E8%A6%81%E7%BB%86%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2015%EF%BC%9A12%EF%BC%9A57).assets/image-008.png)

## 我是怎么修复的

我没有直接让 AI 全部自动改完。

而是打开行动计划，把里面每一条分别复制到 Codex 里，逐条讨论怎么修。

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%94%A8%20Claude%20SEO%20Skill%20%E5%81%9A%E4%B8%80%E6%AC%A1%E5%85%A8%E7%AB%99%E5%AE%A1%E8%AE%A1%EF%BC%8C%E6%AF%94%E6%88%91%E9%A2%84%E6%9C%9F%E7%9A%84%E8%A6%81%E7%BB%86%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2015%EF%BC%9A12%EF%BC%9A57).assets/image-009.png)

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%94%A8%20Claude%20SEO%20Skill%20%E5%81%9A%E4%B8%80%E6%AC%A1%E5%85%A8%E7%AB%99%E5%AE%A1%E8%AE%A1%EF%BC%8C%E6%AF%94%E6%88%91%E9%A2%84%E6%9C%9F%E7%9A%84%E8%A6%81%E7%BB%86%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2015%EF%BC%9A12%EF%BC%9A57).assets/image-010.png)

这里我强烈建议一个问题开一个新聊天框处理。问题多的时候尤其要这样。混在一起很容易漏掉细节，上下文也容易乱。

## 修完怎么验证

修复之后，我启动了本地开发服务器。然后用 `/seo-page` 审计单个页面，看修复结果是否过关。

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%94%A8%20Claude%20SEO%20Skill%20%E5%81%9A%E4%B8%80%E6%AC%A1%E5%85%A8%E7%AB%99%E5%AE%A1%E8%AE%A1%EF%BC%8C%E6%AF%94%E6%88%91%E9%A2%84%E6%9C%9F%E7%9A%84%E8%A6%81%E7%BB%86%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2015%EF%BC%9A12%EF%BC%9A57).assets/image-011.png)

结果没有问题。

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%94%A8%20Claude%20SEO%20Skill%20%E5%81%9A%E4%B8%80%E6%AC%A1%E5%85%A8%E7%AB%99%E5%AE%A1%E8%AE%A1%EF%BC%8C%E6%AF%94%E6%88%91%E9%A2%84%E6%9C%9F%E7%9A%84%E8%A6%81%E7%BB%86%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2015%EF%BC%9A12%EF%BC%9A57).assets/image-012.png)

整体用下来，这个 Skill 确实极大方便了 SEO 工作

- 谢谢分享！
- 为什么你的可以自动生成报告，我的不行，执行了/seo-audit URL 命令
是Claude的问题，我后面又执行了一遍，生成了
- mark
