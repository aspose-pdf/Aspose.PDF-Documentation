---
title: XMP-метаданные
linktitle: XMP-метаданные
type: docs
weight: 80
url: /ru/reportingservices/xmp-metadata/
description: Научитесь управлять метаданными XMP в отчетах PDF с помощью Aspose.PDF для Reporting Services. Улучшите обработку метаданных документа.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Конструктор отчетов служб Reporting Services не поддерживает встраивание метаданных XMP в документ. Aspose.PDF для служб Reporting Services предоставляет четыре параметра для установки соответствующих метаданных XMP:

{{% /alert %}}

```text
**Parameter Name: CreationDate  
**Date Type: String  
**Values supported: Date in one of the date formats
```

```text
**Parameter Name: ModifyDate  
**Date Type: String  
**Values supported: Date in one of the date formats 
```

```text
**Parameter Name: MetaDataDate  
**Date Type: String  
**Values supported: Date in one of the date formats 
```

```text
**Parameter Name: CreatorTool  
**Date Type: String  
**Values supported: Any plain text  
```

## Пример

```xml
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
```




