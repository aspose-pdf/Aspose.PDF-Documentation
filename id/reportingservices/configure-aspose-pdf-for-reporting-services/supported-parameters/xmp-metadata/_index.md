---
title: Metadata XMP
linktitle: Metadata XMP
type: docs
weight: 80
url: /id/reportingservices/xmp-metadata/
description: Pelajari cara mengelola metadata XMP dalam laporan PDF menggunakan Aspose.PDF for Reporting Services. Tingkatkan penanganan metadata dokumen.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Desainer laporan Reporting Services tidak mendukung penyisipan metadata XMP ke dalam dokumen. Aspose.PDF for Reporting Services menyediakan empat parameter untuk mengatur metadata XMP yang sesuai, yaitu:

{{% /alert %}}

{{% alert color="primary" %}}
**Nama Parameter**: CreationDate  
**Tipe Tanggal**: String  
**Nilai yang didukung**: Tanggal dalam salah satu format tanggal

**Nama Parameter**: ModifyDate  
**Tipe Tanggal**: String  
**Nilai yang didukung**: Tanggal dalam salah satu format tanggal 

**Nama Parameter**: MetaDataDate  
**Tipe Tanggal**: String  
**Nilai yang didukung**: Tanggal dalam salah satu format tanggal 

**Nama Parameter**: CreatorTool  
**Tipe Tanggal**: String  
**Nilai yang didukung**: Teks biasa apa saja  

**Contoh**
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

