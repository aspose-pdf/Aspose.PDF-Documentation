---
title: Reporting Services 和 SharePoint 配置
linktitle: Reporting Services 和 SharePoint 配置
type: docs
weight: 40
url: /reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

现在，SharePoint 已在 RS 服务器上安装和配置，并且 RS 已通过 Reporting Services 配置管理器进行设置和设置，我们可以继续在 Central Admin 中进行配置。 RS 2008 R2 确实简化了这个过程。我们过去有一个 3 步流程，您必须执行该流程才能使其发挥作用。现在我们只差一步了。

{{% /alert %}}

{{% alert color="primary" %}}

我们想要访问中央管理员网站，然后进入常规应用程序设置。在底部，我们将看到报告服务。

![Configuration-step1](reporting-services-and-sharepoint-configuration_1.png)
**图片1**：- SharePoint 配置对话框

选择“Reporting Services 集成”链接。将显示以下屏幕。

![Configuration-step2](reporting-services-and-sharepoint-configuration_2.png)
**Image2**：- 指定 Reporting Services 集成凭据

{{% /alert %}}

## 网络服务网址：

**我们将提供在 Reporting Services 配置管理器中找到的报表服务器的 URL。**

## 认证方式：

**我们还将选择一种身份验证模式。以下 MSDN 链接详细介绍了这些内容。
SharePoint 集成模式下 Reporting Services 的安全概述**

{{% alert color="primary" %}}

**简而言之，如果您的网站使用声明身份验证，则无论您在此处选择什么，您都将始终使用受信任的身份验证。如果您想传递 Windows 凭据，则需要选择 Windows 身份验证。对于可信身份验证，我们将传递 SPUser 令牌，而不依赖于 Windows 凭据。如果您已为 NTLM 配置了经典模式站点并且为 NTLM 设置了 RS，您还需要使用受信任的身份验证。需要 Kerberos 来使用 Windows 身份验证并将其传递给您的数据源。**

{{% /alert %}}

## 激活功能：

{{% alert color="primary" %}}

**这为您提供了在所有网站集上激活 Reporting Services 的选项，或者您可以选择要在哪些网站集上激活它。这实际上意味着哪些站点将能够使用 Reporting Services。完成后，您应该看到以下结果**

![Configuration-step3](reporting-services-and-sharepoint-configuration_3.png)

**图片 3：**- Reporting Services 与 SharePoint 环境成功集成
{{% /alert %}}

{{% alert color="primary" %}}

返回到 ReportServer URL，我们应该看到类似于以下内容的内容

![Configuration-step4](reporting-services-and-sharepoint-configuration_4.png)

**图片4：**- Reporting Services 已成功连接 SharePoint 环境

**注意：** ***如果您的 SharePoint 网站配置了 SSL，则它不会显示在此列表中。这是一个已知问题，并不意味着存在问题。您的报告应该仍然有效。***
{{% /alert %}}

{{% alert color="primary" %}}

现在我们已经成功集成了这两个产品，我们已经准备好在 SharePoint 2010 中使用 Reporting Services。与之前的版本一样，我们在“网站集功能”中拥有一个功能（在配置 Reporting Services 集成时激活）。此外，安装还添加了 3 种内容类型以添加​​到我们的网站。在图 7 中，我们可以看到文档库中添加了其中 2 个内容类型，以使用 来创建自定义报告，如下面的图 5 所示。

![Configuration-step5](reporting-services-and-sharepoint-configuration_5.png)

**图片 5：**- 报告生成器

“Reporter Builder”是一个 ActiveX 控件，因此我们需要通过服务器下载它，如下图 6 所示。

![Configuration-step6](reporting-services-and-sharepoint-configuration_6.png)

**图片 6：**- 下载并安装报表生成器
{{% /alert %}}

{{% alert color="primary" %}}

下载过程完成后，加载“Report Builder”控件。现在我们准备设计我们的第一份报告，如下图 7 所示。

![Configuration-step7](reporting-services-and-sharepoint-configuration_7.png)

**图片 7：**- 报告生成器 – 新的报告生成向导
{{% /alert %}}

{{% alert color="primary" %}}

创建报告后，我们可以将其保存在为将报告放入 SharePoint 2010 中而创建的文档库中。必须使用其他内容类型来创建共享连接作为数据源，并将它们保存在 SharePoint 的文档库中。我们可以创建一个文档库，添加此内容类型，然后我们可以使用我们的连接来更改报告的数据源。

![Configuration-step8](reporting-services-and-sharepoint-configuration_8.png)

**图片 8：**- Aspose.PDF for Reporting Services 与 MS SharePoint 成功集成
{{% /alert %}}

