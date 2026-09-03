---
title: Размер поля страницы
linktitle: Размер поля страницы
type: docs
weight: 70
url: /ru/reportingservices/page-margin-size/
description: Настройте размеры полей страниц в отчетах PDF с помощью Aspose.PDF для Reporting Services для улучшения читаемости и макета.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Конструктор отчетов служб Reporting Services не поддерживает настройку размера полей страницы. Aspose.PDF для служб Reporting Services предоставляет четыре параметра для установки соответствующего размера поля страницы:

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

## Пример

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


