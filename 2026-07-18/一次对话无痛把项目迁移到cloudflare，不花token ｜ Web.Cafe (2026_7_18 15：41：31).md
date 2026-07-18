---
title: "一次对话无痛把项目迁移到cloudflare，不花token | Web.Cafe"
source: "https://new.web.cafe/topic/t12fmxy9ju"
archived_at: 2026-07-18T07:41:35.782Z
---

# 一次对话无痛把项目迁移到cloudflare，不花token

之前我项目用的mksaas，部署在vps上不太稳定，现在迁移到cf-d1上。以前这个工程会很麻烦，现在我只用一句话就解决了，方法就是用chatgpt 网页端，使用pro进阶思考,比codex牛逼而且不花codex额度。把你的项目打包，连同mksaas cloudflare原始模板的两个zip上传到对话框（或者你用的shipany就传shipany的）

然后输入这个提示词： mksaas-cf.zip 这个是mksaas模板的cloudflare 部署和d1版。myproject.zip项目是mksaas vercel版模板改进后的代码。把这个项目全部搬进cf版里面。让他能够用cf部署并且使用d1 。保留这个项目（myproject.zip）的所有页面、特性、功能和其他所有内容。并安装 pnpm 依赖，反复运行pnpm dev测试、类型检查测试、构建测试，直到它正常工作。同时，还要在各个方面进行改进。反复干活直到成功。

大概会工作几个小时，最后会给你一个代码压缩包。把这个按照cf部署就可以了（这个需要自己研究）。里面会有一些残留的测试脚本什么的，删掉自己测试就行。大概率代码都是能直接跑通的。

- 没想到 ChatGPT 网页端能干这么久的活
- 这个做法太好了，省掉巨大的token
- 骚操作牛逼哈哈
- 同理 也能转成tanstack。我昨天还开个goal干嘛去了。。。
还可以让他用shipany模板的代码优化mksaas，我现在mksaas速度很快了。
- 薅 token 小妙招
- 我去试试 plus 进阶思考，可能也差不多，差一点估计
沙盒里依赖安装和 build 多次受网络/超时影响中断
告诉他使用内部npm 源地址安装
- 感谢大佬的方法。 试了下 plus，只运行了1个多小时就停了，可能和pro时间上不同
