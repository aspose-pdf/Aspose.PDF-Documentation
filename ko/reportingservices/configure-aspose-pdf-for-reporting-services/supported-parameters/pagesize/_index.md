---
title: 페이지 크기
linktitle: 페이지 크기
type: docs
weight: 60
url: /reportingservices/pagesize/
description: 특정 문서 요구 사항을 충족하려면 Reporting Services용 Aspose.PDF에서 PDF 보고서의 페이지 크기를 사용자 지정하세요.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Reporting Services 보고서 디자이너는 A4, B5, Letter 등과 같은 일반적인 페이지 크기를 지원하지 않습니다. Reporting Services용 Aspose.PDF를 사용하면 다음 예와 같이 얻을 수 있습니다.

{{% /alert %}}

```text
Parameter Name: PageSize  
Date Type: String  
Values supported: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  
```

## 예

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>
```
