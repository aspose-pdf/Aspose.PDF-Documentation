---
title: PDF_A 적합성
linktitle: PDF_A 적합성
type: docs
weight: 100
url: /ko/reportingservices/pdf_a-conformance/
description: Aspose.PDF for Reporting Services에서 PDF/A 적합성을 활성화합니다. 아카이브 요구 사항을 충족하는 문서를 손쉽게 생성합니다.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Aspose.PDF 문서에서 PDF/A(아카이브 가능한 PDF) 적합성에 대한 소개를 확인할 수 있습니다.

PDF/A 문서를 만들고 싶다면, 다음 보고서 매개변수를 추가하십시오.

{{% /alert %}}


{{% alert color="primary" %}}

**매개변수 이름**: PdfConformance  
**데이터 유형**: 문자열  
**지원되는 값**: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  

**예시**
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
