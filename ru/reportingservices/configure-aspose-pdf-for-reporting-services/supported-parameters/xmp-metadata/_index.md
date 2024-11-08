---
title: XMP Metadata
type: docs
weight: 80
url: /ru/reportingservices/xmp-metadata/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Дизайнер отчетов Reporting Services не поддерживает встраивание XMP метаданных в документ. Aspose.Pdf для Reporting Services предоставляет четыре параметра для установки соответствующих XMP метаданных, это:

{{% /alert %}}

{{% alert color="primary" %}}
**Имя параметра**: CreationDate  
**Тип данных**: String  
**Поддерживаемые значения**: Дата в одном из форматов даты

**Имя параметра**: ModifyDate  
**Тип данных**: String  
**Поддерживаемые значения**: Дата в одном из форматов даты

**Имя параметра**: MetaDataDate  
**Тип данных**: String  
**Поддерживаемые значения**: Дата в одном из форматов даты

**Имя параметра**: CreatorTool  
**Тип данных**: String  
**Поддерживаемые значения**: Любой простой текст

**Пример**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>

    <CreationDate>2017-12-10</CreationDate>
```

<ModifyDate>2018-1-12</ModifyDate>
<MetaDataDate>2018-3-7</MetaDataDate>
<CreatorTool>Aspose.Pdf для Reporting Services</CreatorTool>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```