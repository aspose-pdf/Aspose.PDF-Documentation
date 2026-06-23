---
title: Метаданные XMP
linktitle: Метаданные XMP
type: docs
weight: 80
url: /ru/reportingservices/xmp-metadata/
description: Узнайте, как управлять метаданными XMP в PDF‑отчетах с помощью Aspose.PDF for Reporting Services. Улучшите обработку метаданных документа.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Конструктор отчетов Reporting Services не поддерживает встраивание метаданных XMP в документ. Aspose.Pdf for Reporting Services предоставляет четыре параметра для установки соответствующих метаданных XMP, они следующие:

{{% /alert %}}

{{% alert color="primary" %}}
**Имя параметра**: CreationDate  
**Тип даты**: Строка  
**Поддерживаемые значения**: Дата в одном из форматов даты

**Имя параметра**: ModifyDate  
**Тип даты**: Строка  
**Поддерживаемые значения**: Дата в одном из форматов даты 

**Имя параметра**: MetaDataDate  
**Тип даты**: Строка  
**Поддерживаемые значения**: Дата в одном из форматов даты 

**Имя параметра**: CreatorTool  
**Тип даты**: Строка  
**Поддерживаемые значения**: Любой простой текст  

**Пример**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>
    <CreationDate>2017-12-10</CreationDate>
    <ModifyDate>2018-1-12</ModifyDate>
    <MetaDataDate>2018-3-7</MetaDataDate>
    <CreatorTool>Aspose.Pdf for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}


