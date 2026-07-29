---
title: PDF_A 準拠
linktitle: PDF_A 準拠
type: docs
weight: 100
url: /ja/reportingservices/pdf_a-conformance/
description: Aspose.PDF for Reporting Services で PDF/A 準拠を有効にします。アーカイブ対応のドキュメントを簡単に作成できます。
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Aspose.PDF のドキュメントで PDF/A（アーカイブ可能な PDF）準拠の概要を確認できます。

PDF/A ドキュメントを作成したい場合は、次のレポート パラメータを追加してください。

{{% /alert %}}


{{% alert color="primary" %}}

**パラメータ名**: PdfConformance  
**データ型**: 文字列  
**サポートされている値**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  

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
