---
title: 使用MSI安装程序安装
type: docs
weight: 10
url: zh/reportingservices/install-with-msi-installer/
lastmod: "2021-06-05"
---

您可以使用MSI安装程序安装Aspose.Pdf for Reporting Services。运行Aspose.Pdf.ReportingServices.msi并按照安装程序提供的步骤进行操作。安装程序将程序集和其他文件复制到指定目录，并在默认的Reporting Services实例上安装产品。除非您想添加特殊配置参数（如“配置Aspose.Pdf for Reporting Services”部分中所述），否则无需手动复制或修改任何文件。

自动安装是在大多数情况下最好的选择。然而，在某些情况下，您可能需要手动安装产品，例如：

- 由于I/O安全问题自动安装失败。
- 您需要在Reporting Services 2016的命名（非默认）实例或多个实例上安装产品。

- 您升级到最新版本，只想替换程序集，而不是使用MSI安装程序卸载旧版本并安装新版本。
{{% alert color="primary" %}}

注意：请注意，在后一种情况下，您可能会遇到其他组件（例如离线文档）未升级到相应版本的问题。

{{% /alert %}}