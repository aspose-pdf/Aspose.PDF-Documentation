---
title: 更多安装细节
linktitle: 更多安装细节
type: docs
weight: 30
url: /zh/sharepoint/more-installation-details/
lastmod: "2026-08-13"
description: 有关安装 PDF SharePoint API 的更多信息解释了如何在网站集上部署、激活和停用它。
---

## 部署

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint 在部署期间执行以下操作：**

- 将 Aspose.PDF.SharePoint.dll 安装到全局程序集缓存中，并将 SafeControl 条目添加到 web.config 文件中。
- 将功能清单和其他必要的文件安装到适当的目录。
- 在 SharePoint 数据库中注册该功能并使其可在功能范围内激活。

{{% /alert %}}

## 激活

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint 被打包为网站（网站集）级功能，可以在网站集上激活和停用。**

{{% /alert %}}

{{% alert color="primary" %}}

在激活过程中，该功能会对网站集的父 Web 应用程序的虚拟目录进行一些更改： 将转换设置页面添加到站点地图文件。将必要的资源文件复制到虚拟目录中的App_GlobalResources文件夹中。

{{% /alert %}}
