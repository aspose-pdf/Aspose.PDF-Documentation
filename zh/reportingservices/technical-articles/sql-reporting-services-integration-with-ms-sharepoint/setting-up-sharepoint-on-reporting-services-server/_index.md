---
title: 在报告服务服务器上设置 SharePoint
type: docs
weight: 30
url: /zh/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

现在我们需要执行与 SharePoint WFE 类似的步骤。首先是安装先决条件，一旦完成，就启动 SharePoint 设置。

{{% /alert %}}

对于设置，我选择了服务器场和完整安装，以匹配我的 SharePoint Box，因为我不想为 SharePoint 进行独立安装。

## SharePoint 配置

{{% alert color="primary" %}}

**在 SharePoint 配置向导中，我们希望连接到现有的场。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**图片1：- SharePoint 配置向导**
{{% /alert %}}

{{% alert color="primary" %}}

**然后我们将指向我们的场正在使用的 SharePoint_Config 数据库。**
```  如果您不知道它在哪里，可以通过中央管理中的系统设置 -> 管理此农场中的服务器来查找。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**图片2:- 指定数据库配置设置**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**图片3:- SharePoint 配置向导**
{{% /alert %}}

{{% alert color="primary" %}}

**一旦向导完成，这就是我们现在在报表服务器上需要做的全部事情。返回到 ReportServer URL，我们将看到另一个错误，但那是因为我们还没有通过中央管理器进行配置。**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**图片4:- 报表服务器错误**
{{% /alert %}}