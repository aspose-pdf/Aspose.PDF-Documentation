---
title: 设置报表服务
type: docs
weight: 20
url: zh/reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

我们在报表服务服务器上的第一站是报表服务配置管理器。

{{% /alert %}}

## 服务账户：

**一定要了解您正在为报表服务使用哪个服务账户。如果我们遇到问题，可能与您使用的服务账户有关。默认是网络服务。当我们要部署新版本时，我们总是使用域账户，因为这就是我们可能遇到问题的地方。对于这个服务器实例，我们使用了一个名为 RSService 的域账户。**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**图1：- 设置服务账户**

## Web 服务 URL：

{{% alert color="primary" %}}

**我们需要配置 Web 服务 URL。 这是承载 Web 服务的 ReportServer 虚拟目录（vdir），Reporting Services 使用它，SharePoint 将与其通信。除非您想自定义 vdir 的属性（例如 SSL、端口、主机头等），否则您只需点击应用即可完成设置。**

![todo:image_alt_text](setting-up-reporting-services_2.png)

**图片2：- 设置 Web 服务 URL 一旦设置了 Web 服务 URL，您应该能够看到以下结果**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**图片3：- 成功设置 Web 服务 URL**
{{% /alert %}}

## 数据库：

**我们需要创建 Reporting Services 目录数据库。这可以放在任何 SQL 2008 或 SQL 2008 R2 数据库引擎上。SQL11 也可以正常工作，但它仍处于 BETA 阶段。此操作将默认创建两个数据库，ReportServer 和 ReportServerTempDB。**

{{% alert color="primary" %}}
**另一个重要步骤是确保您选择 SharePoint Integrated 作为数据库类型。 一旦做出此选择，就无法更改。**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**图片4:- 创建报告服务器数据库**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**图片5:- 设置数据库服务器和身份验证类型**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**图片6:- 设置数据库名称和模式**
{{% /alert %}}

**对于凭证，这就是报告服务器与SQL Server通信的方式。无论选择哪个帐户，都会在目录数据库以及通过RSExecRole在一些系统数据库中获得某些权限。MSDB是其中一个用于订阅用途的数据库，因为我们使用SQL代理。**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**图片7:- 设置报告服务器数据库凭证**

{{% alert color="primary" %}}

**一旦指定了数据库凭证，我们应该能够获得如下所示的结果。**

![todo:image_alt_text](setting-up-reporting-services_8.png)
**Image8:- 报表服务器数据库创建进度**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- 报表服务器数据库完成摘要**
{{% /alert %}}

## 报表管理器URL:

**我们可以跳过报表管理器URL，因为在SharePoint集成模式下不使用它。SharePoint是我们的前端。报表管理器不起作用。**

## 加密密钥:

{{% alert color="primary" %}}
**备份您的加密密钥，并确保您知道将它们存放在哪里。如果您需要迁移数据库或恢复它，您将需要这些密钥。**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- 报表服务器加密密钥备份**
{{% /alert %}}

{{% alert color="primary" %}}
**恭喜！我们已成功使用配置管理器配置了报表服务。如果您在Web服务URL选项卡中浏览到该URL，它应该显示类似于以下内容。**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- 安装后报告服务器的访问**

**错误原因：SharePoint 安装在我们的 WFE 上，我们完成了报表服务的设置。在此示例中，报表服务和 SharePoint 位于不同的机器上。如果它们在同一台机器上，您就不会看到此错误。我们从技术上需要在 RS 机器上安装 SharePoint。这意味着 IIS 也将被启用。**
{{% /alert %}}
