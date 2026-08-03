---
title: Metadata XMP
linktitle: XMP Metadata
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
description: Pelajari cara mengelola metadata XMP dalam laporan PDF menggunakan Aspose.PDF untuk Layanan Pelaporan. Meningkatkan penanganan metadata dokumen.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Perancang laporan Layanan Pelaporan tidak mendukung penyematan metadata XMP dalam dokumen. Aspose.PDF untuk Layanan Pelaporan menyediakan empat parameter untuk mengatur metadata XMP yang sesuai, yaitu:

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

## Contoh

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


