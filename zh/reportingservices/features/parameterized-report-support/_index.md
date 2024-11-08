---
title: 简单且轻量的部署
type: docs
weight: 40
url: /zh/reportingservices/easy-and-lightweight-deployment/
lastmod: "2021-06-05"
---

**Aspose.Pdf for Reporting Services** 是一个为 Microsoft SQL Server 2016/2017/2019/2022 Reporting Services 和 Power BI Report Server 提供的自定义渲染扩展。Aspose.Pdf for Reporting Services 作为一个单一的 MSI 安装程序提供，可以安装在运行以下任一系统的计算机上：

- Microsoft SQL Server 2016 Reporting Services  
- Microsoft SQL Server 2017 Reporting Services  
- Microsoft SQL Server 2019 Reporting Services  
- Microsoft SQL Server 2022 Reporting Services  
- Microsoft Power BI Report Server

Aspose.Pdf for Reporting Services 易于部署和管理，因为它仅由一个 .NET 程序集 Aspose.Pdf.ReportingServices.dll 组成，完全用 C# 编写，符合 CLS，并且只包含安全的托管代码。服务器上需要安装 .NET Framework 4.8.1。

必须将 Aspose.Pdf.ReportingServices.dll 复制到 ReportServer\bin 目录，并且必须更新配置文件，以便 Reporting Services 能够识别新的渲染扩展。 这些步骤由 Aspose.Pdf for Reporting Services 安装程序执行，但您也可以按照本文档中进一步描述的手动执行这些步骤。