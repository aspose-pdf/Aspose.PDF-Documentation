---
title: PageSize
type: docs
weight: 60
url: /ko/reportingservices/pagesize/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services 보고서 디자이너는 A4, B5, Letter 등과 같은 일반적인 페이지 크기를 지원하지 않습니다. Aspose.Pdf for Reporting Services를 사용하면 다음 예와 같이 사용할 수 있습니다.

{{% /alert %}}

{{% alert color="primary" %}}

**매개변수 이름**: PageSize  
**데이터 유형**: String  
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