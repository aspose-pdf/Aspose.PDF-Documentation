---
title: PDF_A コンプライアンス
linktitle: PDF_A コンプライアンス
type: docs
weight: 100
url: /ja/reportingservices/pdf_a-conformance/
description: Aspose.PDF for Reporting Services で PDF/A のコンプライアンスを有効にします。アーカイブ準拠のドキュメントを簡単に作成できます。
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Aspose.PDF のドキュメントで PDF/A（アーカイブ可能な PDF）コンプライアンスの概要を得ることができます。

PDF/A ドキュメントを作成したい場合は、次のレポート パラメータを追加してください。

{{% /alert %}}


{{% alert color="primary" %}}

**パラメータ名**: PdfConformance  
**データ型**: String  
**サポートされる値**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  

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

