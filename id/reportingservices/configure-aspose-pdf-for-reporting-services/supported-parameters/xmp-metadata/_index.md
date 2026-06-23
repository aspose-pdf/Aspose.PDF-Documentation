---
title: Metadata XMP
linktitle: Metadata XMP
type: docs
weight: 80
url: /id/reportingservices/xmp-metadata/
description: Pelajari cara mengelola metadata XMP dalam laporan PDF menggunakan Aspose.PDF untuk Reporting Services. Tingkatkan penanganan metadata dokumen.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Desainer laporan Reporting Services tidak mendukung penyematan metadata XMP dalam dokumen. Aspose.PDF untuk Reporting Services menyediakan empat parameter untuk mengatur metadata XMP yang sesuai, yaitu:

{{% /alert %}}

{{% alert color="primary" %}}
**Nama Parameter**: CreationDate  
**Jenis Tanggal**: String  
**Nilai yang didukung**: Tanggal dalam salah satu format tanggal

**Nama Parameter**: ModifyDate  
**Jenis Tanggal**: String  
**Nilai yang didukung**: Tanggal dalam salah satu format tanggal 

**Nama Parameter**: MetaDataDate  
**Jenis Tanggal**: String  
**Nilai yang didukung**: Tanggal dalam salah satu format tanggal 

**Nama Parameter**: CreatorTool  
**Jenis Tanggal**: String  
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
    <CreatorTool>Aspose.Pdf for Reporting Services</CreatorTool>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}


