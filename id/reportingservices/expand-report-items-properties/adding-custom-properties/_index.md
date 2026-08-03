---
title: Menambahkan Properti Kustom
linktitle: Adding Custom Properties
type: docs
weight: 10
url: /reportingservices/adding-custom-properties/
description: Pelajari cara menambahkan properti khusus ke laporan PDF dengan Aspose.PDF untuk Layanan Pelaporan. Sesuaikan dokumen Anda secara efisien.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Anda dapat menambahkan properti khusus untuk beberapa item laporan guna memperluas penggunaannya, seperti ToC, panah garis, dan sebagainya. Bagian ini menjelaskan proses ini.

{{% /alert %}}

Anda dapat menambahkan properti khusus untuk beberapa item laporan guna memperluas penggunaannya, seperti Daftar Isi, panah garis, dan sebagainya. Bagian ini menjelaskan proses ini.

Untuk menambahkan properti khusus, Anda perlu mengedit file kode dokumen RDL dengan langkah-langkah berikut:

1. Seperti pada gambar berikut, buka proyek Anda, navigasikan ke penjelajah solusi, dan klik kanan pada file laporan yang dipilih, lalu pilih item menu 'Lihat Kode'.

![Add Custom Properties](adding-custom-properties_1.png)

2. Edit file kode XML. Misalnya, jika Anda ingin menambahkan properti khusus untuk item laporan bagan, Anda perlu menambahkan kode yang mirip dengan teks merah pada contoh berikut.

## Contoh

```xml
<chart Name="chart1">
    <Left>5.5cm</Left>
    <Top>0.5cm</Top>
      ......
    <Style>
      ......
    </style>     
    <CustomProperties>
      <CustomProperty>
        <Name>IsInList</Name>
        <Value>True</Value>
      </CustomProperty>
    </CustomProperties>
</chart> 
```

Dalam contoh fragmen kode ini, nama properti khusus adalah IsInList, dan nilainya adalah `True`.

