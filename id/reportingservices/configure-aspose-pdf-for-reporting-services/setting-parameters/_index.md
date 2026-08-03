---
title: Parameter Pengaturan
linktitle: Setting Parameters
type: docs
weight: 10
url: /reportingservices/setting-parameters/
description: Cari tahu cara mengatur parameter untuk rendering PDF di Aspose.PDF untuk Layanan Pelaporan. Mencapai kontrol yang tepat atas output.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Anda dapat menentukan parameter konfigurasi tertentu yang memengaruhi cara Aspose.PDF untuk Layanan Pelaporan menghasilkan dokumen. Bagian ini menjelaskan proses ini.

{{% /alert %}}

Untuk mengonfigurasi Aspose.Pdf untuk Layanan Pelaporan, Anda perlu mengedit file `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config`. Ini adalah file XML dan konfigurasi penyajinya ada di dalam elemen `<Extension>` yang sesuai dengan penyaji Aspose.PDF.

## Contoh

```xml
<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Insert configuration elements for exporting to PDF here. The following is an example
For PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>
```

{{% alert color="primary" %}}

Jika Anda ingin menetapkan parameter untuk file laporan tertentu namun tidak untuk setiap laporan di server, Anda dapat menambahkan parameter laporan untuk laporan tertentu di Pembuat Laporan dengan langkah-langkah berikut (misalnya, kami akan menambahkan parameter 'IsLandscape' yang ditunjukkan sebelumnya):

1. Buka laporan di Perancang Laporan, klik kanan folder 'Parameter' di panel 'Data Laporan', dan pilih 'Tambahkan Parameter…' (atau, sebagai alternatif, tarik daftar 'Baru' dan pilih 'Parameter…').

![Parameters set up. Step 1](setting-parameters_1.png)

1. Dalam dialog 'Report Parameter Properties', buat parameter bernama 'IsLandscape', dengan tipe data Boolean, dan tambahkan nilai True di tab 'Default Values'.

![Parameters set up. Step 2](setting-parameters_2.png)

{{% /alert %}}
