---
title: 安装 Aspose.PDF for SharePoint 许可证
linktitle: 安装 Aspose.PDF for SharePoint 许可证
type: docs
weight: 10
url: /zh/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: 对评估感到满意后，您可以购买 PDF SharePoint API 许可证并按照安装说明进行应用。
---

{{% alert color="primary" %}}

一旦您对评估感到满意，您就可以 [购买许可证](https://purchase.aspose.com/buy)。购买之前，请确保您理解并同意许可证订阅条款。

{{% /alert %}}

{{% alert color="primary" %}}

订单付款后，许可证将通过电子邮件发送给您。该许可证是一个 .zip 存档，其中包含常规 SharePoint 解决方案包。

该档案包含：

- Aspose.PDF.SharePoint.License.wsp

SharePoint 解决方案包文件。 Aspose.PDF for SharePoint 许可证打包为 SharePoint 解决方案，以方便跨服务器场的部署/收回。

- 自述文件.txt

许可证安装说明。许可证安装是通过 stsadm.exe 从服务器控制台执行的。下面给出了安装许可证所需的步骤。

**注意：** 为了清楚起见，省略了路径。执行时，您可能需要添加 stsadm.exe 和/或解决方案文件的实际路径。

1. 运行 stsadm 将解决方案添加到 SharePoint 解决方案存储：

stsadm.exe -o addsolution -文件名 Aspose.PDF.SharePoint.License.wsp

2. 将解决方案部署到场中的所有服务器：

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. 执行管理计时器作业以立即完成部署。

stsadm.exe -o execadmsvcjobs

**注意：** 如果 Windows SharePoint Services 管理服务未启动，您在运行部署步骤时将收到警告。 Stsadm.exe 依赖此服务和 Windows SharePoint 定时服务在服务器场中复制解决方案数据。如果这些服务未在您的服务器场上运行，您可能需要在每台服务器上部署许可证。

{{% /alert %}}

