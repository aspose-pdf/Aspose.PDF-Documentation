---
title: Menambahkan Properti Kustom
type: docs
weight: 10
url: /id/reportingservices/adding-custom-properties/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Anda dapat menambahkan properti kustom untuk beberapa item laporan untuk memperluas penggunaannya, seperti Daftar Isi, panah garis, dan sebagainya. Bagian ini menjelaskan proses ini.

{{% /alert %}}

{{% alert color="primary" %}}

Anda dapat menambahkan properti kustom untuk beberapa item laporan untuk memperluas penggunaannya, seperti Daftar Isi, panah garis, dan sebagainya. Bagian ini menjelaskan proses ini.

Untuk menambahkan properti kustom, Anda perlu mengedit file kode dokumen RDL dengan langkah-langkah berikut:

1. Seperti pada gambar berikut, buka proyek Anda, navigasikan ke penjelajah solusi, dan klik kanan pada file laporan yang dipilih, lalu pilih item menu 'View Code'.

![todo:image_alt_text](adding-custom-properties_1.png)

2. Edit file kode XML. Sebagai contoh, jika Anda ingin menambahkan properti kustom untuk item laporan grafik, Anda perlu menambahkan kode yang mirip dengan teks merah dalam contoh berikut.
```

**Example**

{{< highlight csharp >}}

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

{{< /highlight >}}

Dalam contoh cuplikan kode ini, nama properti kustom adalah IsInList, dan nilainya adalah 'True'.

{{% /alert %}}