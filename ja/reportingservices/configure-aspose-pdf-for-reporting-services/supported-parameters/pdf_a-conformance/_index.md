---
title: PDF_A 準拠
linktitle: PDF_A 準拠
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
description: Reporting Services の Aspose.PDF で PDF/A 準拠を有効にします。アーカイブに準拠したドキュメントを簡単に作成できます。
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

PDF/A (アーカイブ可能 PDF) 準拠の概要については、Aspose.PDF ドキュメントを参照してください。

PDF/A ドキュメントを作成する場合は、次のレポート パラメーターを追加します。

{{% /alert %}}

```text
Parameter Name: PdfConformance  
Date Type: String  
Values supported: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  
```

## 例

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PdfConformance>PdfA1A</PdfConformance>
    </Configuration>
    </Extension>
</Render>
```