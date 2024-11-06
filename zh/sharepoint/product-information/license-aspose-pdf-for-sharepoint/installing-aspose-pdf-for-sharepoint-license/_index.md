---
title: 安装 Aspose.Pdf for SharePoint 许可证
type: docs
weight: 10
url: zh/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: 一旦您对评估满意，您可以购买 PDF SharePoint API 的许可证并按照安装说明进行应用。
---

{{% alert color="primary" %}}

一旦您对评估满意，您可以[购买许可证](https://purchase.aspose.com/buy)。在购买之前，请确保您理解并同意许可证订阅条款。

{{% /alert %}}

{{% alert color="primary" %}}

订单支付后，许可证将通过电子邮件发送给您。许可证是一个包含常规 SharePoint 解决方案包的 .zip 压缩文件。
{{% /alert %}}

此压缩文件包含：

- Aspose.PDF.SharePoint.License.wsp

SharePoint 解决方案包文件。Aspose.PDF for SharePoint 许可证被打包为一个 SharePoint 解决方案，以便于在服务器场的部署/收回。

- readme.txt

许可证安装说明。
 许可证安装通过服务器控制台上的 stsadm.exe 执行。安装许可证所需的步骤如下。

**注意：** 为了清晰起见，路径被省略。执行时可能需要添加 stsadm.exe 和/或解决方案文件的实际路径。

1. 运行 stsadm 将解决方案添加到 SharePoint 解决方案存储：

   stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. 将解决方案部署到场中的所有服务器：

   stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. 执行管理计时器作业以立即完成部署。

   stsadm.exe -o execadmsvcjobs

**注意：** 如果 Windows SharePoint Services 管理服务未启动，运行部署步骤时会收到警告。Stsadm.exe 依赖于此服务和 Windows SharePoint 计时器服务来跨场复制解决方案数据。如果这些服务未在您的服务器场中运行，则可能需要在每台服务器上部署许可证。