---
title: 페이지 여백 크기
linktitle: 페이지 여백 크기
type: docs
weight: 70
url: /ko/reportingservices/page-margin-size/
description: PDF 보고서에서 Aspose.PDF for Reporting Services를 사용하여 페이지 여백 크기를 조정하면 가독성과 레이아웃이 개선됩니다.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Reporting Services 보고서 디자이너는 페이지 여백 크기 설정을 지원하지 않습니다. Aspose.PDF for Reporting Services는 해당 페이지 여백 크기를 설정하기 위한 네 가지 매개변수를 제공하며, 그들은 다음과 같습니다:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**매개변수 이름**: PageMarginLeft  
**날짜 유형**: Float  
**지원되는 값**:  양수 또는 0

2)  
**매개변수 이름**: PageMarginRight  
**날짜 유형**: Float  
**지원되는 값**:  양수 또는 0

3)  
**매개변수 이름**: PageMarginTop  
**날짜 유형**: Float  
**지원되는 값**:  양수 또는 0

4)  
**매개변수 이름**: PageMarginBottom  
**날짜 유형**: Float  
**지원되는 값**:  양수 또는 0

**예시**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type=" Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices ">
    <Configuration>
    <PageMarginLeft>50</PageMarginLeft>
    <PageMarginRight>50</PageMarginRight>
    <PageMarginTop>50</PageMarginTop>
    <PageMarginBottom>50</PageMarginBottom>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}


