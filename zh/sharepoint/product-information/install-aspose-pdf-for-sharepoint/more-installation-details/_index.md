---
title: 更多安装细节
linktitle: 更多安装细节
type: docs
weight: 30
url: /zh/sharepoint/more-installation-details/
lastmod: "2026-06-18"
description: 关于 PDF SharePoint API 安装的更多信息解释了如何在站点集合上部署、激活和停用它。
---

## **部署**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint 在部署期间执行以下操作：**
- 将 Aspose.PDF.SharePoint.dll 安装到全局程序集缓存，并将 SafeControl 条目添加到 web.config 文件中。
- 将功能清单及其他必要文件安装到相应目录。
- 在 SharePoint 数据库中注册此功能，并使其在功能范围内可供激活。

{{% /alert %}}


## **激活**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint 被打包为站点（站点集合）级别的功能，可在站点集合上进行激活和停用。**

{{% /alert %}}

{{% alert color="primary" %}}

在激活期间，此功能会对站点集合的父 Web 应用程序的虚拟目录进行一些更改：将转换设置页面添加到站点映射文件。将必要的资源文件复制到虚拟目录中的 App_GlobalResources 文件夹。

{{% /alert %}}
