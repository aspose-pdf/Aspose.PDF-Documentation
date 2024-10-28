---
title: Reporting Services 和 SharePoint 配置
type: docs
weight: 40
url: /reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

现在，SharePoint 已经在 RS 服务器上安装和配置完毕，并且通过 Reporting Services Configuration Manager 设置和配置了 RS，我们可以继续在中央管理中进行配置。RS 2008 R2 真正简化了这个过程。我们过去需要执行一个三步过程才能完成这个工作。现在我们只需要一步。

{{% /alert %}}

{{% alert color="primary" %}}

我们想要进入中央管理员网站，然后进入常规应用程序设置。在底部附近，我们将看到 Reporting Services。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**图片1**:- SharePoint 配置对话框

选择 “Reporting Services Integration” 链接。将显示以下屏幕。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- 指定 Reporting Services 集成凭据

{{% /alert %}}

## Web Service URL:

**我们将提供在 Reporting Services 配置管理器中找到的报表服务器的 URL。**

## Authentication Mode:

**我们还将选择一种身份验证模式。以下 MSDN 链接详细介绍了这些模式。
SharePoint 集成模式下 Reporting Services 的安全概述**

{{% alert color="primary" %}}

**简而言之，如果您的网站使用声明身份验证，无论您在此选择什么，您始终会使用受信任身份验证。如果您想传递 Windows 凭据，您将选择 Windows 身份验证。对于受信任身份验证，我们将传递 SPUser 令牌，而不依赖于 Windows 凭据。如果您已将经典模式网站配置为 NTLM 并且 RS 设置为 NTLM，则也需要使用受信任身份验证。Kerberos 将是使用 Windows 身份验证并通过它传递给您的数据源所需的。**

{{% /alert %}}

## 激活功能：

{{% alert color="primary" %}}

**这为您提供了在所有网站集合上激活报表服务的选项，或者您可以选择要在哪些网站上激活。这实际上意味着哪些网站将能够使用报表服务。完成后，您应该看到以下结果**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**图3：**- 报表服务与 SharePoint 环境的成功集成
{{% /alert %}}

{{% alert color="primary" %}}

回到 ReportServer URL，我们应该看到类似以下内容

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**图4：**- 报表服务已成功连接到 SharePoint 环境

**注意：** ***如果您的 SharePoint 站点配置了 SSL，它将不会出现在此列表中。这是一个已知问题，并不意味着存在问题。您的报告仍应正常工作。***
{{% /alert %}}

现在我们已经成功集成了这两个产品，我们准备在 SharePoint 2010 中使用 Reporting Services。与之前的版本一样，我们在“网站集合功能”中有一个功能（在我们配置 Reporting Services 集成时激活）。安装还添加了 3 个内容类型到我们的网站。在图7中，我们可以看到在文档库中添加了其中的2个内容类型，以创建自定义报告，如下图5所示。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**图5:**- 报表生成器

“Reporter Builder” 是一个 ActiveX 控件，所以我们需要通过服务器下载它，如下图6所示。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**图6:**- 下载并安装报表生成器
{{% /alert %}}

{{% alert color="primary" %}}

下载过程完成后，加载“Report Builder”控件。现在我们准备设计我们的第一个报告，如下图7所示。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- 报告生成器 – 新报告生成向导 {{% /alert %}}

{{% alert color="primary" %}}

在创建报告后，我们可以将其保存在为我们的 SharePoint 2010 创建的文档库中。其他内容类型必须用于创建共享连接作为数据源，并将其保存在 SharePoint 的文档库中。我们可以创建一个文档库，添加此内容类型，然后我们可以更改报告数据源的连接。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- Aspose.PDF for Reporting Services 与 MS SharePoint 的成功集成 {{% /alert %}}