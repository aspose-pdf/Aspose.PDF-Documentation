---
title: 페이지 크기
linktitle: 페이지 크기
type: docs
weight: 60
url: /ko/reportingservices/pagesize/
description: Aspose.PDF for Reporting Services의 PDF 보고서에 대해 특정 문서 요구사항을 충족하도록 페이지 크기를 사용자 지정합니다.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Reporting Services 보고서 디자이너는 A4, B5, Letter 등과 같은 일반적인 페이지 크기를 지원하지 않습니다. Aspose.Pdf for Reporting Services를 사용하면 다음 예시와 같이 사용할 수 있습니다.

{{% /alert %}}

{{% alert color="primary" %}}

**매개변수 이름**: PageSize  
**날짜 유형**: String  
**지원되는 값**: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  

**예시**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}


