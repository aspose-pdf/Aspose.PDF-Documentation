---
title: 在 Reporting Services 服务器上设置 SharePoint
linktitle: 在 Reporting Services 服务器上设置 SharePoint
type: docs
weight: 30
url: /zh/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

现在我们需要执行与 SharePoint WFE 相同的步骤。第一件事是完成 Prereq uisites 安装，一旦完成，就启动 SharePoint 设置。

{{% /alert %}}

对于设置，我选择 Server Farm 并进行完整安装以匹配我的 SharePoint Box，因为我不想为 SharePoint 使用独立安装。

## SharePoint 配置

{{% alert color="primary" %}}

**在 SharePoint Configuration Wizard 中，我们希望连接到现有的 Server Farm。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- SharePoint 配置向导**
{{% /alert %}}

{{% alert color="primary" %}}

**我们随后会将其指向我们农场使用的 SharePoint_Config 数据库。如果您不知道它在哪里，可以通过中央管理的系统设置 -> 管理服务器 来查找此农场。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- 指定数据库配置设置**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- SharePoint 配置向导**
{{% /alert %}}

{{% alert color="primary" %}}

**一旦向导完成，这就是我们目前在 Report Server 机器上需要做的全部工作。返回 ReportServer URL 时，我们会看到另一个错误，但那是因为我们尚未通过 Central Administrator 进行配置。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- 报告服务器错误**
{{% /alert %}}
