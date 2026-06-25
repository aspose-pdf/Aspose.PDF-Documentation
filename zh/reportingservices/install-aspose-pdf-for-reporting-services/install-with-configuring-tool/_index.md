---
title: 使用配置工具进行安装
linktitle: 使用配置工具进行安装
type: docs
weight: 30
url: /zh/reportingservices/install-with-configuring-tool/
description: 使用配置工具无缝集成的 Aspose.PDF for Reporting Services 安装分步指南。
lastmod: "2026-06-19"
---

Aspose.PDF for Reporting Services 配置工具可以帮助您为任何受支持的报表服务器 (RS) 版本配置 Aspose.PDF for Reporting Services 扩展。目前支持 RS2016、RS2017、RS2019、RS2022 和 Power BI Report Server。该配置工具需要 .NET Framework 4.8。

如果您想安装扩展并在报表服务器上注册它，请选择 \u0027Register\u0027 操作类型。若要取消注册并卸载扩展，请选择 \u0027Unregister\u0027 操作类型。

![todo:image_alt_text](install-with-configuring-tool_1.png)

**以下步骤详细描述了如何使用它：**

1. 输入或浏览 Aspose.Pdf for Reporting Services 扩展的 DLL 文件路径；
1. 选择相应的操作类型：Register 或 Unregister；
1. 选择对应于您想要配置的 Report Server 版本的选项卡。请确保您选择的 DLL 文件适用于您的 RS 版本。如果机器上未安装所请求的产品版本，配置工具会以提示的形式通知您。如果您正在为指定的 RS2016 实例（而非默认的 \u0027MSSQLSERVER\u0027 实例）配置扩展，请输入自定义实例名称，然后按下 \u0027Refresh\u0027 按钮。
1. 确保底部文本框中显示的配置文件路径和名称是正确的。如果不正确，您可以按下 \u0027Refresh\u0027 按钮尝试重新查找 RS 实例，或手动查找它们。
1. 按下 \u0027Config\u0027 按钮。工具将尝试执行所请求的配置，并告知您配置是否成功。
 

