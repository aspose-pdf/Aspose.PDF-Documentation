---
title: Menambahkan Properti Kustom
linktitle: Menambahkan Properti Kustom
type: docs
weight: 10
url: /id/reportingservices/adding-custom-properties/
description: Pelajari cara menambahkan properti kustom ke laporan PDF dengan Aspose.PDF for Reporting Services. Sesuaikan dokumen Anda secara efisien.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Anda dapat menambahkan properti kustom untuk beberapa item laporan guna memperluas penggunaannya, seperti ToC, panah garis, dan sebagainya. Bagian ini menjelaskan proses tersebut.

{{% /alert %}}

{{% alert color="primary" %}}

Anda dapat menambahkan properti kustom untuk beberapa item laporan guna memperluas penggunaannya, seperti Daftar Isi, panah garis, dan sebagainya. Bagian ini menjelaskan proses tersebut.

Untuk menambahkan properti khusus, Anda perlu mengedit file kode dokumen RDL dalam langkah-langkah berikut:

1. Seperti pada gambar berikut, buka proyek Anda, navigasikan ke Solution Explorer, dan klik kanan pada file laporan yang dipilih, kemudian pilih item menu 'View Code'.

![todo:image_alt_text](adding-custom-properties_1.png)

2. Edit file kode XML. Misalnya, jika Anda ingin menambahkan properti khusus untuk item laporan diagram, Anda perlu menambahkan kode yang mirip dengan teks berwarna merah pada contoh berikut.

**Contoh**

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

Dalam contoh fragmen kode ini, nama properti khusus adalah IsInList, dan nilainya adalah 'True'.

{{% /alert %}}

