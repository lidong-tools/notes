---
title: "给美国怀俄明州 LLC 报税的全过程记录 | Web.Cafe"
source: "https://new.web.cafe/topic/9jvooth0z2"
archived_at: 2026-07-18T08:57:12.552Z
---

# 给美国怀俄明州 LLC 报税的全过程记录

先提醒一句：美国公司 Form 5472 + pro forma Form 1120 的 2026 年截止日是 2026 年 4 月 15 日。 如果没有按时提交、没有按要求提交，或者表格填写不完整，Form 5472 的基础罚款就是每次 25,000 美元。更麻烦的是，如果 IRS 发了 notice 之后，你在 90 天内仍未补交，后面还可能按每 30 天继续追加 25,000 美元罚款，而且理论上没有最高上限。

有美国公司的朋友，这件事别拖别忘了交。

去年我注册了美国怀俄明州公司，见 https://new.web.cafe/topic/qrire7ds6n 这篇文章，今年第一次正式处理美国公司的报税和州年报。

实际走完后发现，对于像我这种规模很小、结构也比较简单的 nonresident alien 单人 LLC，真正要做的事情并没有想象中那么复杂，核心只有两件事：

第一件是联邦层面的 Form 5472 + pro forma Form 1120

第二件是怀俄明州 annual report

下面是报税的完整操作过程，希望对你有所帮助

第一条线是联邦报税，我这次是 Form 5472 + pro forma Form 1120，然后通过传真提交给 IRS。

第二条线是州层面的年报，在怀俄明州官网完成填写和支付 61.44\$。

整个流程可以概括成四步：

- 导出 Mercury 和 Stripe 的记录，先把原始证据留好
- 下载 Form 5472 和 Form 1120 的 PDF
- 把 5472 + 1120 填好，确认后传真给 IRS
- 再去怀俄明州官网完成 annual report

第一步：先把银行和 Stripe 的原始记录全部导出来

进入 https://app.mercury.com/dashboard 然后在左侧找到 Transactions 点击导出

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%BB%99%E7%BE%8E%E5%9B%BD%E6%80%80%E4%BF%84%E6%98%8E%E5%B7%9E%20LLC%20%E6%8A%A5%E7%A8%8E%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B%E8%AE%B0%E5%BD%95%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2016%EF%BC%9A56%EF%BC%9A59).assets/image-002.png)

首先选择 Last year ，然后点击 Export filtered 导出 csv 文件

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%BB%99%E7%BE%8E%E5%9B%BD%E6%80%80%E4%BF%84%E6%98%8E%E5%B7%9E%20LLC%20%E6%8A%A5%E7%A8%8E%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B%E8%AE%B0%E5%BD%95%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2016%EF%BC%9A56%EF%BC%9A59).assets/image-003.png)

按照下图找 Accounts &gt; Checking &gt; Documents &gt; Statements 点进去

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%BB%99%E7%BE%8E%E5%9B%BD%E6%80%80%E4%BF%84%E6%98%8E%E5%B7%9E%20LLC%20%E6%8A%A5%E7%A8%8E%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B%E8%AE%B0%E5%BD%95%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2016%EF%BC%9A56%EF%BC%9A59).assets/image-004.png)

年份改到 2025 然后把所有 Checking 和 Saving 的所有 statement 都下载下来

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%BB%99%E7%BE%8E%E5%9B%BD%E6%80%80%E4%BF%84%E6%98%8E%E5%B7%9E%20LLC%20%E6%8A%A5%E7%A8%8E%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B%E8%AE%B0%E5%BD%95%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2016%EF%BC%9A56%EF%BC%9A59).assets/image-005.png)

进入美国 stripe，导出五份 csv 文件

左侧菜单找到 Transactions &gt; Export 然后选择 2025-01-01 ~ 2025-12-31 导出

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%BB%99%E7%BE%8E%E5%9B%BD%E6%80%80%E4%BF%84%E6%98%8E%E5%B7%9E%20LLC%20%E6%8A%A5%E7%A8%8E%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B%E8%AE%B0%E5%BD%95%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2016%EF%BC%9A56%EF%BC%9A59).assets/image-006.png)

左侧菜单找到 Billing &gt; Invoices 然后选择 2025-01-01 ~ 2025-12-31 导出

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%BB%99%E7%BE%8E%E5%9B%BD%E6%80%80%E4%BF%84%E6%98%8E%E5%B7%9E%20LLC%20%E6%8A%A5%E7%A8%8E%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B%E8%AE%B0%E5%BD%95%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2016%EF%BC%9A56%EF%BC%9A59).assets/image-007.png)

左侧菜单找到 Reporting &gt; Reports &gt; Balance summary

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%BB%99%E7%BE%8E%E5%9B%BD%E6%80%80%E4%BF%84%E6%98%8E%E5%B7%9E%20LLC%20%E6%8A%A5%E7%A8%8E%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B%E8%AE%B0%E5%BD%95%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2016%EF%BC%9A56%EF%BC%9A59).assets/image-008.png)

接着将日期改为 stripe 注册日期到 2025-12-31，然后点击下面三个导出

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%BB%99%E7%BE%8E%E5%9B%BD%E6%80%80%E4%BF%84%E6%98%8E%E5%B7%9E%20LLC%20%E6%8A%A5%E7%A8%8E%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B%E8%AE%B0%E5%BD%95%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2016%EF%BC%9A56%EF%BC%9A59).assets/image-009.png)

到这里我们获得了 水星银行的交易记录 csv、水星银行的 checking 和 statement、stripe 的五份 csv，将这些文件在本地保存好，未来 IRS 要查账这些要作为证据提交给他，2025 年的公司设立费简化处理，不记录进税表，这样可以简化税务计算和证据收集，接下来就开始准备填写表格

下载 Form 5472 和 Form 1120 的 pdf

- Form 5472 PDF 下载地址
  - https://www.irs.gov/pub/irs-pdf/f5472.pdf
- Form 1120 PDF 下载地址
  - https://www.irs.gov/pub/irs-pdf/f1120.pdf

下面两份文档是这两个表格的填写说明书

- Instructions for Form 5472 PDF 表格说明书
  - https://www.irs.gov/pub/irs-pdf/i5472.pdf
- Instructions for Form 1120 表格说明书
  - https://www.irs.gov/instructions/i1120

接下来通过和 GPT 对话将 5472 + 1120 两张税表填好，填好后将税表发给 GPT 获得 GPT 点头后将税表传真到 +1 855-887-7737 这个号码，报税到这里就结束了

发送传真可以使用下面的邀请链接，你会获得 5 页的免费额度 https://app.hellofax.com?ref=b67727ed&s=F&utm_medium=social&utm_source=facebooktwitter&utm_campaign=hellofax-incentivized-post&utm_content=hf

接下来要处理怀俄明的年报，打开 https://wyobiz.wyo.gov/Business/ARWizard.aspx，然后在里面输入 Filing ID，跟着 AI 填好信息，页面会计算好要交的税，然后进行支付

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%BB%99%E7%BE%8E%E5%9B%BD%E6%80%80%E4%BF%84%E6%98%8E%E5%B7%9E%20LLC%20%E6%8A%A5%E7%A8%8E%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B%E8%AE%B0%E5%BD%95%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2016%EF%BC%9A56%EF%BC%9A59).assets/image-010.png)

支付完成后会提示以下信息，报税完成

![image.png](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E7%BB%99%E7%BE%8E%E5%9B%BD%E6%80%80%E4%BF%84%E6%98%8E%E5%B7%9E%20LLC%20%E6%8A%A5%E7%A8%8E%E7%9A%84%E5%85%A8%E8%BF%87%E7%A8%8B%E8%AE%B0%E5%BD%95%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2016%EF%BC%9A56%EF%BC%9A59).assets/image-011.png)

- 我想问下，如果还没开单，这里的 stripe 账单之类的还要准备吗。流程有什么区别吗
没开单那就不用了，你没有流水，直接和 gpt 说没有流水，然后让他帮你填表就行了
好的，感谢分享。去年也是看你的文档开通的美司
- 感谢
- 对c corp的报税差不多吗。有大佬知道的吗
c corp 没研究，需要你探索一下
- 传真的话，自己的吗，还是闲鱼之类的
上面有发传真的平台链接，准备好 pdf 然后上平台发就行了
- 请问您是多久收到 IRS 回执的呢？ 我用的 DHL 发了快递过去，大半个月了都没有收到回执。
- 你自己搞得，太牛了吧...我还想要找CPA啥的呢...
- +1 855-887-7737 这个号码的来源是什么，为什么我的gpt告诉我不要传到这里，叫我邮寄
说明里面有这个号码的，你要给 gpt 说清楚你是非美国的单人 LLC，让他阅读说明
- 水星银行这里的地址证明 资金来源证明怎么搞得啊，
