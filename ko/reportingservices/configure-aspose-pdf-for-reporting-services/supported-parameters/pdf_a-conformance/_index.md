---
title: PDF_A 적합성
type: docs
weight: 100
url: /ko/reportingservices/pdf_a-conformance/
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

Aspose.PDF 문서에서 PDF/A (보관 가능한 PDF) 적합성에 대한 소개를 받을 수 있습니다.

PDF/A 문서를 생성하려면 다음 보고서 매개변수를 추가하세요.

{{% /alert %}}


{{% alert color="primary" %}}

**매개변수 이름**: PdfConformance  
**데이터 유형**: 문자열  
**지원되는 값**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  

**예**
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