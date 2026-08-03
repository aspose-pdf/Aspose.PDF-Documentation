---
title: PDF_A 적합성
linktitle: PDF_A 적합성
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
description: Reporting Services에 대해 Aspose.PDF에서 PDF/A 규격을 활성화합니다. 보관 규정을 준수하는 문서를 손쉽게 생성하세요.
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

Aspose.PDF 문서에서 PDF/A(보관 가능 PDF) 적합성에 대한 소개를 얻을 수 있습니다.

PDF/A 문서를 생성하려면 다음 보고서 매개변수를 추가하세요.

{{% /alert %}}

```text
Parameter Name: PdfConformance  
Date Type: String  
Values supported: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  
```

## 예

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
