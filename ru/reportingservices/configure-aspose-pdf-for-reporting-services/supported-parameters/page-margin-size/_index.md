---
title: Размер полей страницы
linktitle: Размер полей страницы
type: docs
weight: 70
url: /ru/reportingservices/page-margin-size/
description: Настройте размеры полей страницы в PDF‑отчетах с помощью Aspose.PDF for Reporting Services для улучшения читаемости и макета.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Конструктор отчетов Reporting Services не поддерживает установку размера полей страницы. Aspose.PDF for Reporting Services предоставляет четыре параметра для установки соответствующего размера полей, они следующие:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**Имя параметра**: PageMarginLeft  
**Тип данных**: Float  
**Поддерживаемые значения**:  Любое положительное число или ноль

2)  
**Имя параметра**: PageMarginRight  
**Тип данных**: Float  
**Поддерживаемые значения**:  Любое положительное число или ноль

3)  
**Имя параметра**: PageMarginTop  
**Тип данных**: Float  
**Поддерживаемые значения**:  Любое положительное число или ноль

4)  
**Имя параметра**: PageMarginBottom  
**Тип данных**: Float  
**Поддерживаемые значения**:  Любое положительное число или ноль

**Пример**

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
