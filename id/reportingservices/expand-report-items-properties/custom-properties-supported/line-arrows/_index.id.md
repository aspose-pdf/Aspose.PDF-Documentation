---
title: Panah Garis
type: docs
weight: 20
url: /reportingservices/line-arrows/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Spesifikasi RDL tidak menentukan panah tentang elemen garis, jadi pembuat laporan tidak mendukung pengaturan panah untuk garis. Dengan Aspose.Pdf untuk Layanan Pelaporan, Anda dapat melakukannya dengan mudah.

{{% /alert %}}

{{% alert color="primary" %}}

Saat ini, renderer Aspose.PDF mendukung penambahan panah di awal atau akhir garis dengan menambahkan properti khusus.

Tambahkan Panah Awal untuk Garis  
**Nama Properti Khusus**: HasArrowAtStart  
**Nilai Properti Khusus**: True  

Tambahkan Panah Akhir untuk Garis  
**Nama Properti Khusus**: HasArrowAtEnd  
**Nilai Properti Khusus**: True  

Sebagai contoh, ada dua garis bernama 'line1' dan 'line2' dalam file laporan saat ini, dan line1 memiliki panah awal, line2 memiliki panah awal dan akhir, untuk memenuhi persyaratan ini, Anda dapat menambahkan properti khusus seperti dalam fragmen kode berikut.

**Contoh**

{{< highlight csharp >}}

 <Line Name="line1">

<Style>
  ......
</Style>
<CustomProperties>
  <CustomProperty>
    <Name>HasArrowAtStart</Name>
    <Value>True</Value>
  </CustomProperty>
</CustomProperties>
</Line>
......
<Line Name="line2">
<Style>
  ......
</Style>
<CustomProperties>
  <CustomProperty>
    <Name>HasArrowAtStart</Name>
    <Value>True</Value>
  </CustomProperty>
  <CustomProperty>
    <Name>HasArrowAtEnd</Name>
    <Value>True</Value>
  </CustomProperty>
</CustomProperties>
</Line>

{{< /highlight >}}
{{% /alert %}}
```