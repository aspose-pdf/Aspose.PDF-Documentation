---
title: 设置 Reporting Services
linktitle: 设置 Reporting Services
type: docs
weight: 20
url: /zh/reportingservices/setting-up-reporting-services/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

我们在 Reporting Services 服务器的第一站是 Reporting Services 配置管理器。

{{% /alert %}}

## 服务账户：

**请务必了解您在 Reporting Services 中使用的服务账户。如果我们遇到问题，可能与您使用的服务账户有关。默认是 Network Service。当我们部署新版本时，始终使用域账户，因为这通常是会出现问题的地方。对于该服务器实例，我们使用了名为 RSService 的域账户。**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- 设置服务账户**

## Web Service URL：

{{% alert color="primary" %}}

**我们需要配置 Web Service URL。这是承载 Web Services Reporting Services 使用的 Web Services 的 ReportServer 虚拟目录 (vdir)，也是 SharePoint 将要通信的目标。除非您想自定义 vdir 的属性（即 SSL、端口、主机头等…），否则只需点击此处的 Apply 即可，操作完成。**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- 设置 Web Service URL 后，一旦 Web Service URL 已设置，您应该能够看到以下结果**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- 成功设置 Web Service URL**
{{% /alert %}}

## 数据库：

**我们需要创建 Reporting Services 目录数据库。此数据库可以放置在任何 SQL 2008 或 SQL 2008 R2 数据库引擎上。SQL11 也可以正常工作，但仍处于 BETA 阶段。此操作默认会创建两个数据库：ReportServer 和 ReportServerTempDB。**

{{% alert color="primary" %}}
**另一关键步骤是确保为数据库类型选择 SharePoint 集成。做出此选择后将无法更改。**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4:- 创建报表服务器数据库**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5:- 设置数据库服务器和身份验证类型**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6:- 设置数据库名称和模式**
{{% /alert %}}

**对于凭据，这就是报表服务器与 SQL Server 通信的方式。无论您选择哪个帐户，都将通过 RSExecRole 获得在 Catalog 数据库以及一些系统数据库中的特定权限。MSDB 是其中一个用于订阅的数据库，因为我们使用 SQL Agent。**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7:- 设置报表服务器数据库凭据**

{{% alert color="primary" %}}

**一旦指定了数据库凭据，我们应该能够获得如下所示的结果。**

![todo:image_alt_text](setting-up-reporting-services_8.png)

**Image8:- 报表服务器数据库创建进度**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- 报表服务器数据库完成摘要**
{{% /alert %}}

## 报告管理器 URL:

**当我们处于 SharePoint 集成模式时，可以跳过 Report Manager URL，因为它未被使用。SharePoint 是我们的前端。Report Manager 无法工作。**

## 加密密钥：

{{% alert color="primary" %}}
**备份您的加密密钥，并确保您知道它们的存放位置。如果遇到需要迁移数据库或恢复数据库的情况，您将需要这些密钥。**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- 报表服务器加密密钥备份**
{{% /alert %}}

{{% alert color="primary" %}}
**恭喜！我们已成功使用配置管理器配置了 Reporting Services。如果您在“Web Service URL”选项卡中浏览该 URL，应该会看到类似以下内容。**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- 安装后报告服务器访问**

**错误原因：SharePoint 已在我们的 WFE 上安装，我们已完成 Reporting Services 的设置。在本例中，Reporting Services 和 SharePoint 位于不同的机器上。如果它们在同一台机器上，就不会出现此错误。实际上我们需要在 RS 服务器上安装 SharePoint。这意味着 IIS 也将被启用。**
{{% /alert %}}

