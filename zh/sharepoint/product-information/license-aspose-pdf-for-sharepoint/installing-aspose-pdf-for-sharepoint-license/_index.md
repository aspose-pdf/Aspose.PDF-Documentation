---
title: 安装 Aspose.Pdf for SharePoint 许可证
linktitle: 安装 Aspose.Pdf for SharePoint 许可证
type: docs
weight: 10
url: /zh/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: 当您对评估满意后，您可以购买 PDF SharePoint API 的许可证，并遵循安装说明进行应用。
---

{{% alert color="primary" %}}

当您对评估满意后，您可以 [购买许可证](https://purchase.aspose.com/buy). 在购买之前，请确保您了解并同意许可证订阅条款。

{{% /alert %}}

{{% alert color="primary" %}}

付款后，许可证将通过电子邮件发送给您。该许可证是一个包含常规 SharePoint 解决方案包的 .zip 压缩文件。

此归档包含：

- Aspose.PDF.SharePoint.License.wsp

SharePoint 解决方案包文件。Aspose.PDF for SharePoint 许可证被打包为 SharePoint 解决方案，以便在服务器场中进行部署/撤回。

- readme.txt

许可证安装说明。许可证安装通过 stsadm.exe 在服务器控制台上执行。以下给出安装许可证所需的步骤。

**注意：** 为了清晰起见，路径已省略。执行时可能需要添加 stsadm.exe 和/或解决方案文件的实际路径。

1. 运行 stsadm 将解决方案添加到 SharePoint 解决方案存储中：

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. 将解决方案部署到农场中的所有服务器：

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. 立即执行管理计时器作业以完成部署。

stsadm.exe -o execadmsvcjobs

**注意：** 如果 Windows SharePoint Services Administration 服务未启动，在运行部署步骤时您将收到警告。Stsadm.exe 依赖此服务和 Windows SharePoint Timer Service 在整个农场中复制解决方案数据。如果这些服务未在您的服务器农场上运行，您可能需要在每台服务器上部署许可证。


{{% /alert %}}
