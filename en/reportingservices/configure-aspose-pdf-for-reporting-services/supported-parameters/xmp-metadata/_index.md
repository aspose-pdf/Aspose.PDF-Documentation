---
title: XMP Metadata
linktitle: XMP Metadata
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
description: Learn to manage XMP metadata in PDF reports using Aspose.PDF for Reporting Services. Enhance document metadata handling.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Reporting Services report designer does not support embedding XMP metadata in the document. Aspose.PDF for Reporting Services provides four parameters to set the corresponding XMP metadata, they are:

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

## Example

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


