---
title: 使用配置工具安装
type: docs
weight: 30
url: /reportingservices/install-with-configuring-tool/
lastmod: "2021-06-05"
---

Aspose.Pdf for Reporting Services 配置工具可以帮助您为任何支持的报告服务器 (RS) 版本配置 Aspose.Pdf for Reporting Services 扩展。目前它支持 RS2016、RS2017、RS2019、RS2022 和 Power BI 报告服务器。配置工具需要 .NET Framework 4.8。

如果您想安装扩展并将其注册到报告服务器，请选择“注册”操作类型。要取消注册和卸载扩展，请选择“取消注册”操作类型。

![todo:image_alt_text](install-with-configuring-tool_1.png)

**以下步骤详细描述了如何使用它：**

1. 输入或浏览 Aspose.Pdf for Reporting Services 扩展的 DLL 文件路径；
1. 选择相应的操作类型：注册或取消注册；
1. 选择与您要配置的报表服务器版本相对应的选项卡。请确保选择适用于您的 RS 版本的 DLL 文件。如果机器上未安装所请求版本的产品，配置工具将通过提示通知您。如果您正在为命名的 RS2016 实例（而不是默认的 'MSSQLSERVER' 实例）配置扩展，请输入自定义实例名称，然后按 '刷新' 按钮。
1. 确保底部文本框中显示的配置文件路径和名称是正确的。如果不正确，您可以按 '刷新' 按钮再次尝试查找 RS 实例，或者您可以手动查找。
1. 按 '配置' 按钮。工具现在将尝试进行请求的配置，并会通知您配置是否成功。