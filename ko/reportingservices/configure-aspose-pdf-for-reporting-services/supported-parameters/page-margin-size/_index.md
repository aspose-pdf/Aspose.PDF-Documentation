---
title: 페이지 여백 크기
linktitle: 페이지 여백 크기
type: docs
weight: 70
url: /reportingservices/page-margin-size/
description: 향상된 가독성과 레이아웃을 위해 Reporting Services용 Aspose.PDF를 사용하여 PDF 보고서의 페이지 여백 크기를 조정하세요.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services 보고서 디자이너는 페이지 여백 크기 설정을 지원하지 않습니다. Reporting Services용 Aspose.PDF는 해당 페이지 여백 크기를 설정하는 네 가지 매개 변수를 제공합니다.

{{% /alert %}}

```text
Parameter Name: PageMarginLeft  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginRight  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginTop  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginBottom  
Date Type: Float  
Values supported:  Any positive number or zero
```

## 예

```xml
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
```
