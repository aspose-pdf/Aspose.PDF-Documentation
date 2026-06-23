---
title: 使用 MSI 安装程序进行安装
linktitle: 使用 MSI 安装程序进行安装
type: docs
weight: 10
url: /zh/reportingservices/install-with-msi-installer/
description: 了解如何使用 MSI 安装程序安装 Aspose.PDF for Reporting Services。这是一份快速设置的简明指南。
lastmod: "2026-06-19"
---

您可以使用 MSI 安装程序来安装 Aspose.Pdf for Reporting Services。运行 Aspose.Pdf.ReportingServices.msi 并按照安装程序提供的步骤进行操作。安装程序会将程序集和其他文件复制到指定目录，并在 Reporting Services 的默认实例上安装该产品。除非您想按照 ‘Configure Aspose.Pdf for Reporting Services’ 部分所述添加特殊配置参数，否则无需手动复制或修改任何文件。

自动安装是大多数情况下最好的选项。然而，在某些情况下您可能需要手动安装产品，例如：
 
- 由于 I/O 安全问题，自动安装失败。
- 您需要在 Reporting Services 2016 的命名实例（非默认实例）或多个实例上安装该产品。
- 您升级到最新版本，只想替换程序集，而不是使用 MSI 安装程序卸载旧版本再安装新版本。
 
{{% alert color="primary" %}}

注意：请留意，在后者情况下，您可能会导致其他组件（例如离线文档）未升级到相应的版本。

{{% /alert %}}

