---
title: 页面方向
type: docs
weight: 10
url: /reportingservices/page-orientation/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

报表定义语言不允许明确指定报表中的页面方向。使用 Aspose.Pdf for Reporting Services，您可以轻松地指示导出器生成具有横向页面方向的 PDF 文档。默认方向为纵向。

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
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}