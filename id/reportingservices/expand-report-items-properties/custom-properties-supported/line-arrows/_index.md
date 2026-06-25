---
title: Panah Garis
linktitle: Panah Garis
type: docs
weight: 20
url: /id/reportingservices/line-arrows/
description: Pelajari cara menambahkan panah garis dalam laporan PDF menggunakan Aspose.PDF for Reporting Services. Tingkatkan tampilan laporan dengan mudah.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Spesifikasi RDL tidak menentukan panah untuk elemen garis, sehingga report builder tidak mendukung pengaturan panah untuk garis. Dengan Aspose.Pdf for Reporting Services Anda dapat melakukannya dengan mudah.

{{% /alert %}}

{{% alert color="primary" %}}

Saat ini, renderer Aspose.PDF mendukung penambahan panah di awal atau akhir garis dengan menambahkan properti khusus.

Tambahkan Panah Awal untuk Garis  
**Properti Kustom** **Nama**: HasArrowAtStart  
**Nilai Properti Kustom**: True  

Tambahkan Panah Akhir untuk Garis  
**Properti Kustom** **Nama**: HasArrowAtEnd  
**Nilai Properti Kustom**: True  

Sebagai contoh, terdapat dua garis bernama ‘line1’ dan ‘line2’ dalam file laporan saat ini, dan line1 memiliki panah awal, line2 memiliki panah awal dan akhir, untuk memenuhi persyaratan ini, Anda dapat menambahkan properti kustom seperti pada potongan kode berikut.

**Contoh**

{{< highlight csharp >}}
 <Line Name="line1">
    <Style>
      ......
    </style>
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
    </style>
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

