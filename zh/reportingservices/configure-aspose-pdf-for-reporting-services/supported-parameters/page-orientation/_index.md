---
title: 页面方向
linktitle: 页面方向
type: docs
weight: 10
url: /zh/reportingservices/page-orientation/
description: 在 Aspose.PDF for Reporting Services 中配置 PDF 报告的页面方向。自定义布局以获得更好的呈现。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

报告定义语言不允许显式指定报告中页面的方向。使用 Aspose.PDF for Reporting Services，您可以轻松指示导出器生成横向页面方向的 PDF 文档。默认方向为纵向。

{{% /alert %}}

{{% alert color="primary" %}}

默认方向为纵向。
**参数名称**: IsLandscape
**数据类型**: Boolean
**支持的值**: True, False (默认)

**示例**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>真</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
