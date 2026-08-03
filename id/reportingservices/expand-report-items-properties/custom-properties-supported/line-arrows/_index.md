---
title: Panah Garis
linktitle: Line Arrows
type: docs
weight: 20
url: /reportingservices/line-arrows/
description: Pelajari cara menambahkan panah garis dalam laporan PDF menggunakan Aspose.PDF untuk Layanan Pelaporan. Sempurnakan visual laporan dengan mudah.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Spesifikasi RDL tidak menentukan panah pada elemen garis, sehingga pembuat laporan tidak mendukung pengaturan panah untuk garis. Dengan Aspose.PDF untuk Layanan Pelaporan Anda dapat melakukannya dengan mudah.

{{% /alert %}}

Saat ini, perender Aspose.PDF mendukung penambahan panah di awal atau akhir baris dengan menambahkan properti khusus.

```text
Add Start Arrow for Line  
Custom Property `Name`: HasArrowAtStart  
Custom Property `Value`: True  
```

```text
Add End Arrow for Line  
Custom Property `Name`: HasArrowAtEnd  
Custom Property `Value`: True  
```

Misalnya, ada dua baris yang diberi nama `line1` Dan `line2` dalam file laporan saat ini, dan baris1 memiliki panah awal, baris2 memiliki panah awal dan akhir, untuk memenuhi persyaratan ini, Anda dapat menambahkan properti khusus seperti pada potongan kode berikut.

## Contoh

```xml
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
```

