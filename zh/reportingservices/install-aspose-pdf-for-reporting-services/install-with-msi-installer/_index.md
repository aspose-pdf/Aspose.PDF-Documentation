---
title: 使用 MSI 安装程序安装
linktitle: 使用 MSI 安装程序安装
type: docs
weight: 10
url: /reportingservices/install-with-msi-installer/
description: 了解如何使用 MSI 安装程序安装 Aspose.PDF for Reporting Services。快速设置的简单指南。
lastmod: "2021-06-05"
---

您可以使用 MSI 安装程序安装 Aspose.PDF for Reporting Services。运行 Aspose.Pdf.ReportingServices.msi 并按照安装程序提供的步骤进行操作。安装程序会将程序集和其他文件复制到指定目录，并将产品安装在 Reporting Services 的默认实例上。您不需要手动复制或修改任何文件，除非您想要添加特殊配置参数，如“为 Reporting Services 配置 Aspose.PDF”部分中所述。

自动安装是在大多数情况下有效的最佳选择。但是，在某些情况下您可能需要手动安装该产品，例如：

- 由于 I/O 安全问题，自动安装失败。
- 您需要在 Reporting Services 2016 的指定（非默认）实例或多个实例上安装该产品。
- 您升级到最新版本，只想替换程序集，而不是卸载旧版本并使用 MSI 安装程序安装新版本。
 
{{% alert color="primary" %}}

注意：请注意，在后一种情况下，您可能会遇到其他组件（例如离线文档）未升级到相应版本的情况。

{{% /alert %}}
