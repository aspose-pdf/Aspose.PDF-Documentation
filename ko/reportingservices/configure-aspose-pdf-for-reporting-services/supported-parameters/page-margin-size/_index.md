---
title: 페이지 여백 크기
type: docs
weight: 70
url: /ko/reportingservices/page-margin-size/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

보고서 작성 서비스의 보고서 디자이너는 페이지 여백 크기를 설정하는 것을 지원하지 않습니다. Aspose.Pdf for Reporting Services는 해당 페이지 여백 크기를 설정하기 위한 네 가지 매개변수를 제공합니다. 그것들은:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**매개변수 이름**: PageMarginLeft  
**데이터 유형**: Float  
**지원되는 값**:  0 또는 양수

2)  
**매개변수 이름**: PageMarginRight  
**데이터 유형**: Float  
**지원되는 값**:  0 또는 양수

3)  
**매개변수 이름**: PageMarginTop  
**데이터 유형**: Float  
**지원되는 값**:  0 또는 양수

4)  
**매개변수 이름**: PageMarginBottom  
**데이터 유형**: Float  
**지원되는 값**:  0 또는 양수

**예제**

{{< highlight csharp >}}

<Render>
â¦
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
