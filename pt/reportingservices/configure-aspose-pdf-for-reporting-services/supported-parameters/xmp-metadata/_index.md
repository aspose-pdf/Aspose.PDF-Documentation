---
title: Metadados XMP
linktitle: XMP Metadata
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
description: Aprenda a gerenciar metadados XMP em relatórios PDF usando Aspose.PDF para Reporting Services. Aprimore o manuseio de metadados de documentos.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

O designer de relatórios do Reporting Services não dá suporte à incorporação de metadados XMP no documento. Aspose.PDF para Reporting Services fornece quatro parâmetros para definir os metadados XMP correspondentes, são eles:

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

## Exemplo

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


