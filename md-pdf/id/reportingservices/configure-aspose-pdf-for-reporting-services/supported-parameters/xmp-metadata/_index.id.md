```
---
title: XMP Metadata
type: docs
weight: 80
url: /reportingservices/xmp-metadata/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Perancang laporan Layanan Pelaporan tidak mendukung penyematan metadata XMP dalam dokumen. Aspose.Pdf untuk Layanan Pelaporan menyediakan empat parameter untuk menetapkan metadata XMP yang sesuai, yaitu:

{{% /alert %}}

{{% alert color="primary" %}}
**Nama Parameter**: CreationDate  
**Tipe Data**: String  
**Nilai yang didukung**: Tanggal dalam salah satu format tanggal

**Nama Parameter**: ModifyDate  
**Tipe Data**: String  
**Nilai yang didukung**: Tanggal dalam salah satu format tanggal

**Nama Parameter**: MetaDataDate  
**Tipe Data**: String  
**Nilai yang didukung**: Tanggal dalam salah satu format tanggal

**Nama Parameter**: CreatorTool  
**Tipe Data**: String  
**Nilai yang didukung**: Teks biasa apa pun  

**Contoh**
{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer, Aspose.Pdf.ReportingServices">
    <Configuration>

    <CreationDate>2017-12-10</CreationDate>
```
<ModifyDate>2018-1-12</ModifyDate> <MetaDataDate>2018-3-7</MetaDataDate> <CreatorTool>Aspose.Pdf untuk Layanan Pelaporan</CreatorTool> </Configuration> </Extension> </Render> 

{{< /highlight >}} 

{{% /alert %}}