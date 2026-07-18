---
title: "香港Stripe注册教程 | Web.Cafe"
source: "https://new.web.cafe/topic/em8626t5aj"
archived_at: 2026-07-18T03:28:08.519Z
---

# 香港Stripe注册教程

说来惭愧入群估计也快一年了, 因为有本职工作所以一直都在潜水没有怎么具体去实操过, 最近跟着idoubi大佬的B站视频实操了一下建站, 因为集成了支付功能, 所以去香港注册了个人Stripe, 记录下来给大家参考.

## 需要准备的资料

以下是以中国大陆身份申请香港Stripe需要的资料. 提前准备好以下资料会大量节约你的时间.

- 功能完备的网站, 如果网站什么内容都没有, 建议完善以后再来申请, 否则审核大概率不通过.
- 香港手机号
- 中国大陆颁发的护照
- 香港的银行卡号
- 香港银行卡的银行英文名称, 例如汇丰香港的名称是: The Hongkong and Shanghai Banking Corporation Limited
- 香港银行卡的开户分行的英文名和地址, 例如汇丰银行尖沙咀分行的地址是: Tsim Sha Tsui Branch, B/F, LG/F & G/F,HSBC Building Tsim Sha Tsui, 82-84 Nathan Road, Tsim Sha Tsui, Kowloon, HongKong (181). 这家分行比较坑, 在Stripe选择分行的时候会有两个选项, 还有一个是数字491结尾的但是前面地址一样, 咨询客服以后说是同一家, 我就选择了第一个.
- 一个网络信号非常强的地方
- 所在地方光线适中不要太强反光
- iPhone, 或原生Android系统手机. 国产Android手机可能会有问题.
- 提前在手机上下载Microsoft Authenticator, Google Authenticator, Authy 等验证器应用

## 注册步骤

### 注册账号

注册地址: https://dashboard.stripe.com/register , 填写以下信息.

![01.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-002.jpg)

注册后直接进入后台, 这时候会提示你填写网站信息. 也可以跳过后续再设置. 这里我们直接填写信息.

![02.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-003.jpg)

设置后我们就可以看到后台了. 如下所示.

![03.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-004.jpg)

但此时的账号没有任何功能, 我们点击右上角的"获取您的真实账号", 系统提示要进行邮箱验证. 点击邮件中的验证链接即可完成验证.

![04.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-005.jpg)

验证后再次点击右上角的"获取您的真实账号"进行后续操作.

### 验证您的业务

地区选择香港, 商家类型选择个人Individual, 如果不是个人请根据实际情况进行选择.

![05.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-006.jpg)

接下来填写个人信息, 如果不是香港身份, 就按照护照上的信息填写. 可能有隐患的就是家庭住址, 我们都没有真实的香港地址, 看其他分享贴都是填写开户行的地址, 但是如果后期真的触发KYC审核, 要求提供对应地址的水电气账单, 可能就会比较麻烦. 但目前看来还没有人遇到.

![06.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-007.jpg)

接下来填写商家信息. 请根据自己的真实情况进行选择, 避免后期审核出现问题. 产品描述看到很多经验分享贴介绍使用英文, 所以这里建议大家也使用英文, 猜测审核团队可能是使用英文作为工作语言.

![07.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-008.jpg)

接下来填写公开描述详情, 其实就是发送给客户的账单上会显示的一些公司信息.

![08.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-009.jpg)

### 添加您的银行账户

这一步填写您的银行账户, 如果有提前准备开户行的名字和分行信息, 直接选择即可, 否则此时才去查询会比较耗时. 提现计划考虑到新账户前期应该收款较少, 所以就选择自动每月一号提现.

![09.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-010.jpg)

### 保护您的账户

使用提前下载的验证器应用扫描屏幕上的二维码, 点击继续, 然后在输入框中输入验证器上显示的六位数字即可添加成功. 此时系统会弹出一串字符让你保存, 请务必保存好, 因为一旦丢失, 别人可以重置你的账号密码. 以后每次登录Stripe账号, 在输入密码以后, 还要输入验证器生成的随机数字才能进入后台.

![10.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-011.jpg)

添加验证器以后还可以再添加一个验证方式, 避免验证器丢失导致无法登录. 这里我选择通行密钥, 如果是iOS设备就是指可以用Face ID或指纹登录, 如果是Mac设备就是指可以用指纹登录. 其他设备因为我没有所以无法进行测试.

![11.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-012.jpg)

### 添加其他

选择产品收税方式, 请根据实际情况进行选择, 如果不清楚也可以先跳过, 等后面收款金额多的时候咨询专业人士再做选择.

![12.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-013.jpg)

是否进行气候捐款, 请根据实际情况进行选择. 老外很吃这一套, 有了这个标也许能为你的产品提高转化率.

![132.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-014.jpg)

### 审核并提交

此时会让你预览所有填写的信息, 对于错误和不完整的信息可以点击编辑按钮进行重新编辑, 确认无误以后点击最下方的"同意并提交"按钮提交信息.

![14.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-015.jpg)

提交成功后可以看到如下弹窗

![15.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-016.jpg)

### 身份信息验证

注册成功以后, 回到后台首页, 会看到如下提示.

![16.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-017.jpg)

点击右上角的"开始"进行身份验证

![17.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-018.jpg)

在弹窗中点击"同意并继续"

![19.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-019.jpg)

使用iPhone上的 `原生相机` 应用扫描二维码, 会打开验证网页, 在验证网页拍摄护照页, 注意找一个光线适中没有太强反光的地方, 如果实在反光很强就找个书本背包之类的东西遮挡一下, 拍摄以后如果不满意可以重新拍摄, 看到照片比较清晰了再点击提交. `千万不要用微信支付宝扫描这个二维码` 大概率会出问题, 国产安卓手机大概率也是无法用原生相机扫这个二维码, 建议用iPhone, 因为我没有设备所以无法做测试, 但是以我做跨境的经验来说, 出问题的概率很高.

验证完成后会有以下提示:

![20.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-020.jpg)

### 关注审核状态

提交护照信息后可以在如下位置查看审核状态

![21.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-021.jpg)

刚刚提交的时候已激活下可以看到审核中的信息, 我的大概过了几分钟就完成审核了, 再去点击已激活就可以看到没有审核中的信息了.

![22.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-022.jpg)

### 更新税务信息

如果不更新税务信息将无法收款和提现, 所以按照如下内容进行设置

![23.jpg](https://ima-knowledge.oss-cn-shanghai.aliyuncs.com/ima-file/2026-07-18/%E9%A6%99%E6%B8%AFStripe%E6%B3%A8%E5%86%8C%E6%95%99%E7%A8%8B%20%EF%BD%9C%20Web.Cafe%20(2026_7_18%2011%EF%BC%9A27%EF%BC%9A59).assets/image-023.jpg)

以上就是本次注册全过程了.

- 赞一个，请问是在香港用香港网络注册吗？
是的, 一定要模拟真实情况
- 感谢分享，很详细，请问这里的公司网站必须填到时候要接入支付的网站吗，还是接入支付使用另一个网站也不影响
- 不知道能不能使用静态IP来注册
- 香港手机号从哪里办呢，用其他的行不，然后用热点
- 非常棒
- 要看仔细了，我后面看写身份证，没仔细看文章，让我从现提交了。已过。
- 好像不用香港热点和不用香港手机号，审核也过了。
你是随便用的一个香港 IP 并且没用香港手机号，也通过了吗？
- 手机号码写内地的也可以
- 感谢分享，今天按照这个教程注册成了。 我是弄了香港的Clubsim esim卡，填的香港号码，和汇丰银行。 最后一步提交护照，在电脑上开了梯子也提示地区不可用。 手机上开了香港全局代理，成功提交了。 如果不想填大陆手机号的，手机支持esim的话，可以考虑开个Clubsim的esim卡。
