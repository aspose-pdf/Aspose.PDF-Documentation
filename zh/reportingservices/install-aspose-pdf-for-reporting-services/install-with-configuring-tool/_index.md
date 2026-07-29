---
title: 使用配置工具安装
linktitle: 使用配置工具安装
type: docs
weight: 30
url: /zh/reportingservices/install-with-configuring-tool/
description: 使用配置工具无缝集成 Aspose.PDF for Reporting Services 的分步安装指南。
lastmod: "2026-07-29"
---

Aspose.PDF for Reporting Services 配置工具可以帮助您为所有受支持的报表服务器（RS）版本配置 Aspose.PDF for Reporting Services 扩展。目前它支持 RS2016、RS2017、RS2019、RS2022 以及 Power BI Report Server。该配置工具需要 .NET Framework 4.8。

如果您想安装扩展并在报表服务器上注册，请选择 ‘Register’ 操作类型。要注销并卸载扩展，请选择 ‘Unregister’ 操作类型。

![todo:image_alt_text](install-with-configuring-tool_1.png)

**以下步骤详细描述了如何使用它：**

1. 输入或浏览 Aspose.PDF for Reporting Services 扩展的 DLL 文件路径；
1. 选择相应的操作类型：注册或注销；
1. 选择对应于您要配置的报表服务器版本的选项卡。请确保您选择的 DLL 文件适用于您的 RS 版本。如果机器上未安装所需版本的产品，配置工具会以提示形式通知您。如果您正在为命名的 RS2016 实例（而非默认的 \u0027MSSQLSERVER\u0027 实例）配置扩展，请输入自定义实例名称，然后点击 \u0027Refresh\u0027 按钮。
1. 确保底部文本框中显示的配置文件路径和名称正确。如果不正确，您可以按下 \u0027Refresh\u0027 按钮再次尝试查找 RS 实例，或者手动查找它们。
1. 按下 \u0027Config\u0027 按钮。工具现在将尝试执行请求的配置，并会告知您配置是否成功。
 
