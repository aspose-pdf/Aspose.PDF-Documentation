---
title: PDF_A 合规性
type: docs
weight: 100
url: zh/reportingservices/pdf_a-conformance/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

您可以在 Aspose.PDF 文档中获取有关 PDF/A（可归档 PDF）合规性的介绍。

如果您想创建一个 PDF/A 文档，请添加以下报告参数。

{{% /alert %}}


{{% alert color="primary" %}}

**参数名称**: PdfConformance  
**数据类型**: String  
**支持的值**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U  

**示例**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PdfConformance>PdfA1A</PdfConformance>
    </Configuration>
    </Extension>
</Render>
{{< /highlight >}}

{{% /alert %}}