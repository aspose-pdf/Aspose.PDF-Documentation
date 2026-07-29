---
title: 调试信息
linktitle: 调试信息
type: docs
weight: 90
url: /zh/reportingservices/debug-information/
description: 访问并分析 Aspose.PDF for Reporting Services 中 PDF 渲染的调试信息，以有效排查问题。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

渲染或渲染结果出现问题是不可避免的。由于保密或隐私等原因，我们无法获取用户报告中使用的数据源，因而无法复现报告中的错误。为促进客户与开发者之间的交流更加便捷顺畅，我们添加了此参数。如果在使用 Aspose.PDF for Reporting Services 渲染报告时遇到问题，请设置此报告参数，您将得到以 XML 格式呈现的渲染文档。随后，请在产品论坛中将该 XML 文件发布给我们。

{{% /alert %}}

{{% alert color="primary" %}}
**参数名称**: SavingXmlFormat  
**日期类型**: 布尔  
**支持的值**: True, False (默认)  

**示例**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > 真 </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
