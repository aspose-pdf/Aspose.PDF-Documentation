---
title: XMP‑метаданные
linktitle: XMP‑метаданные
type: docs
weight: 80
url: /ru/reportingservices/xmp-metadata/
description: Научитесь управлять XMP‑метаданными в PDF‑отчётах с помощью Aspose.PDF for Reporting Services. Улучшите обработку метаданных документа.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Конструктор отчётов Reporting Services не поддерживает встраивание XMP‑метаданных в документ. Aspose.PDF for Reporting Services предоставляет четыре параметра для установки соответствующих XMP‑метаданных, они:

{{% /alert %}}

{{% alert color="primary" %}}
**Имя параметра**: CreationDate  
**Тип даты**: String  
**Поддерживаемые значения**: Дата в одном из форматов даты

**Имя параметра**: ModifyDate  
**Тип даты**: String  
**Поддерживаемые значения**: Дата в одном из форматов даты 

**Имя параметра**: MetaDataDate  
**Тип даты**: String  
**Поддерживаемые значения**: Дата в одном из форматов даты 

**Имя параметра**: CreatorTool  
**Тип даты**: String  
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
    <CreatorTool>Aspose.PDF for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

