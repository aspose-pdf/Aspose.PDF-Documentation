---
title: Размер полей страницы
type: docs
weight: 70
url: /reportingservices/page-margin-size/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Дизайнер отчетов Reporting Services не поддерживает установку размера полей страницы. Aspose.Pdf for Reporting Services предоставляет четыре параметра для установки соответствующего размера полей страницы, они такие:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**Имя параметра**: PageMarginLeft  
**Тип данных**: Float  
**Поддерживаемые значения**: Любое положительное число или ноль

2)  
**Имя параметра**: PageMarginRight  
**Тип данных**: Float  
**Поддерживаемые значения**: Любое положительное число или ноль

3)  
**Имя параметра**: PageMarginTop  
**Тип данных**: Float  
**Поддерживаемые значения**: Любое положительное число или ноль

4)  
**Имя параметра**: PageMarginBottom  
**Тип данных**: Float  
**Поддерживаемые значения**: Любое положительное число или ноль

**Пример**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type=" Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices ">

    <Configuration>
```


<PageMarginLeft>50</PageMarginLeft>
<PageMarginRight>50</PageMarginRight>
<PageMarginTop>50</PageMarginTop>
<PageMarginBottom>50</PageMarginBottom>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```