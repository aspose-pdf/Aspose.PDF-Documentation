---
title: 页面方向
linktitle: 页面方向
type: docs
weight: 10
url: /zh/reportingservices/page-orientation/
description: 在 Aspose.PDF for Reporting Services 中配置 PDF 报表的页面方向。自定义布局以获得更好的呈现效果。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

报表定义语言不允许在报表中显式指定页面方向。使用 Aspose.PDF for Reporting Services，您可以轻松指示导出器生成横向页面方向的 PDF 文档。默认方向为纵向。

{{% /alert %}}

{{% alert color="primary" %}}

默认方向为纵向。
**参数名称**: IsLandscape
**数据类型**: Boolean
**支持的值**: True, False (default)

**示例**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

