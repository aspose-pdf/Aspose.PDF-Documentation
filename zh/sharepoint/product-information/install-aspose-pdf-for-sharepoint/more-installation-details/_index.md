---
title: 更多安装详情
type: docs
weight: 30
url: zh/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: 有关PDF SharePoint API安装的更多信息，解释如何在网站集合上部署、激活和停用。
---

## **部署**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint在部署期间执行以下操作：**
- 将Aspose.PDF.SharePoint.dll安装到全局程序集缓存中，并在web.config文件中添加SafeControl条目。
- 将功能清单和其他必要文件安装到适当的目录。
- 在SharePoint数据库中注册功能，并使其可在功能范围内激活。

{{% /alert %}}


## **激活**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint被打包为一个站点（网站集合）级别的功能，可以在网站集合上激活和停用。**

{{% /alert %}}

{{% alert color="primary" %}}

在激活期间，该功能会对网站集合的父Web应用程序的虚拟目录进行一些更改：将转换设置页面添加到sitemap文件。

{{% /alert %}}
 将必要的资源文件复制到虚拟目录中的 App_GlobalResources 文件夹。