---
title: PDF_A Conformance
type: docs
weight: 100
url: ja/reportingservices/pdf_a-conformance/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF のドキュメントで PDF/A (アーカイブ可能な PDF) 準拠の紹介を得ることができます。

PDF/A ドキュメントを作成する場合は、次のレポートパラメータを追加してください。

{{% /alert %}}


{{% alert color="primary" %}}

**パラメータ名**: PdfConformance  
**データ型**: String  
**サポートされる値**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U  

**例**
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