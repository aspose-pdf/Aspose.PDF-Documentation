---
title: 在 Reporting ServicesReporting Services 服务器上设置 SharePoint
linktitle: 在 Reporting ServicesReporting Services 服务器上设置 SharePoint
type: docs
weight: 30
url: /reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

现在我们需要执行与 SharePoint WFE 类似的步骤。首先是完成 Prereq uisites 安装，完成后启动 SharePoint 设置。

{{% /alert %}}

对于设置，我选择服务器场和完整安装以匹配我的 SharePoint Box，因为我不想要 SharePoint 的独立安装。

## SharePoint 配置

{{% alert color="primary" %}}

**在 SharePoint 配置向导中，我们想要连接到现有场。**

![SharePoint 配置向导](setting-up-sharepoint-on-reporting-services-server_1.png)

**图片1：- SharePoint 配置向导**
{{% /alert %}}

{{% alert color="primary" %}}

**然后，我们将其指向我们场正在使用的 SharePoint_Config 数据库。如果您不知道这是在哪里，您可以通过中央管理通过系统设置 -> 该场中的管理服务器来查找。**

![SharePoint 配置数据库](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- 指定数据库配置设置**

![SharePoint 配置向导](setting-up-sharepoint-on-reporting-services-server_3.png)

**图片3：- SharePoint 配置向导**
{{% /alert %}}

{{% alert color="primary" %}}

**向导完成后，这就是我们现在需要在报表服务器盒上执行的操作。返回到 ReportServer URL，我们将看到另一个错误，但那是因为我们尚未通过 Central Administrator 配置它。**

![SharePoint 配置错误](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- 报告服务器错误**
{{% /alert %}}
