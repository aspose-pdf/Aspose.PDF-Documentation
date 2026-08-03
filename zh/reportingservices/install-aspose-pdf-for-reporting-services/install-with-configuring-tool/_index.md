---
title: 使用配置工具安装
linktitle: 使用配置工具安装
type: docs
weight: 30
url: /reportingservices/install-with-configuring-tool/
description: 使用配置工具安装 Aspose.PDF for Reporting Services 的分步指南以实现无缝集成。
lastmod: "2021-06-05"
---

Aspose.PDF for Reporting Services 配置工具可以帮助您为任何受支持的报表服务器 (RS) 版本配置 Aspose.PDF for Reporting Services 扩展。目前它支持RS2016、RS2017、RS2019、RS2022和Power BI报表服务器。配置工具需要 .NET Framework 4.8。

如果要安装扩展并将其注册到报表服务器，请选择 `Register` 操作类型。要取消注册和卸载扩展，请选择 `Unregister` 操作类型。

![Install with configuring tool](install-with-configuring-tool_1.png)

**以下步骤详细描述了如何使用它：**

1. 输入或浏览Aspose.PDF for Reporting Services扩展的DLL文件的路径；
1. 选择对应的动作类型：注册或取消注册；
1. 选择与您要配置的报表服务器版本相对应的选项卡。请确保您选择了适用于您的 RS 版本的 DLL 文件。如果机器上没有安装所请求的产品版本，配置工具会提示您。如果您要为指定的 RS2016 实例（不是默认的“MSSQLSERVER”实例）配置扩展，请输入自定义实例名称，然后按“刷新”按钮。
1. 确保底部文本框中显示的配置文件路径和名称正确。如果没有，您可以按“刷新”按钮再次尝试查找 RS 实例，或者您可以手动查找它们。
1. 按“配置”按钮。该工具现在将尝试进行所请求的配置，并通知您配置是否成功。
