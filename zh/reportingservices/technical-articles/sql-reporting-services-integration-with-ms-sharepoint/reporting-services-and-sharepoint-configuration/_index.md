---
title: Reporting Services 和 SharePoint 配置
linktitle: Reporting Services 和 SharePoint 配置
type: docs
weight: 40
url: /zh/reportingservices/reporting-services-and-sharepoint-configuration/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

现在，SharePoint 已经在 RS 服务器上安装并配置，且 RS 已通过 Reporting Services Configuration Manager 完成设置，我们可以继续在 Central Admin 中进行配置。RS 2008 R2 实际上大大简化了此过程。我们过去需要执行一个 3 步的过程才能使其工作，而现在只需一步。

{{% /alert %}}

{{% alert color="primary" %}}

我们想要访问 Central Administrator 网站，然后进入 General Application Settings。在页面底部会看到 Reporting Services。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_1.png)
**Image1**:- SharePoint 配置对话框

选择 "Reporting Services Integration" 链接。将显示以下屏幕。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_2.png)
**Image2**:- 指定 Reporting Services 集成凭据

{{% /alert %}}

## Web Service URL:

**我们将在 Reporting Services 配置管理器中找到的报告服务器的 URL 提供给您。**

## Authentication Mode:

**我们还将选择一个身份验证模式。以下 MSDN 链接详细说明了这些内容。
SharePoint 集成模式下 Reporting Services 的安全概述**

{{% alert color="primary" %}}

**简而言之，如果您的站点使用声明式身份验证，无论此处选择什么，您都将使用受信任身份验证。如果您想传递 Windows 凭据，应选择 Windows 身份验证。对于受信任身份验证，我们将传递 SPUser 令牌，而不依赖 Windows 凭据。如果您已为经典模式站点配置了 NTLM 并且 RS 也设置为 NTLM，您也应使用受信任身份验证。使用 Windows 身份验证并将其传递给数据源需要 Kerberos。**

{{% /alert %}}

## 激活功能：

{{% alert color="primary" %}}

**这让您可以选择在所有站点集合上激活 Reporting Services，或者仅选择您想要激活的站点集合。这实际上意味着哪些站点可以使用 Reporting Services。完成后，您应该会看到以下结果**

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_3.png)

**Image3:**- Reporting Services 与 SharePoint 环境成功集成
{{% /alert %}}

{{% alert color="primary" %}}

返回 ReportServer URL 时，我们应该看到类似以下内容

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_4.png)

**Image4:**- Reporting Services 已成功连接到 SharePoint 环境

**NOTE:** ***如果您的 SharePoint 站点已配置为 SSL，它将不会出现在此列表中。这是已知问题，并不意味着出现了问题。您的报告仍应正常工作。***
{{% /alert %}}

{{% alert color="primary" %}}

现在我们已经成功集成了两个产品，准备在 SharePoint 2010 中使用 Reporting Services。与之前的版本一样，我们在“Site Collection Feature”（在配置 Reporting Services Integration 时激活）中有一个功能。安装还向我们的网站添加了 3 种内容类型。在 Image 7 中可以看到其中 2 种内容类型已在文档库中添加，用于创建自定义报告，如下图 Image5 所示。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_5.png)

**Image5:**- Report Builder

“Reporter Builder” 是一个 ActiveX 控件，所以我们需要在服务器上下载它，如下图 Image 6 所示。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_6.png)

**Image6:**- 下载并安装 Report Builder
{{% /alert %}}

{{% alert color="primary" %}}

下载过程完成后，加载 “Report Builder” 控件。现在我们准备好设计我们的第一个报告，如下图 Image7 所示。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_7.png)

**Image7:**- Report Builder – 新建报告向导
{{% /alert %}}

{{% alert color="primary" %}}

创建报告后，我们可以将其保存到已创建的文档库中，以放置在 SharePoint 2010 中的报告。必须使用另一种内容类型来创建共享连接作为数据源，并将其保存到 SharePoint 中的文档库。我们可以创建文档库，添加此内容类型，随后即可拥有可用的连接，以更改报告的数据源。

![todo:image_alt_text](reporting-services-and-sharepoint-configuration_8.png)

**Image8:**- 成功集成 Aspose.PDF for Reporting Services 与 MS SharePoint
{{% /alert %}}

