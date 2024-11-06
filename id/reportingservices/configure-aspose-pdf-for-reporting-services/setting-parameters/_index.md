---
title: Mengatur Parameter
type: docs
weight: 10
url: id/reportingservices/setting-parameters/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Anda dapat menentukan parameter konfigurasi tertentu yang mempengaruhi bagaimana Aspose.Pdf untuk Reporting Services menghasilkan dokumen. Bagian ini menjelaskan proses ini.

{{% /alert %}}

Untuk mengonfigurasi Aspose.Pdf untuk Reporting Services, Anda perlu mengedit file C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config. Ini adalah file XML dan konfigurasi renderer berada di dalam elemen ```<Extension>``` yang sesuai dengan renderer Aspose.PDF.

**Contoh**

{{< highlight csharp >}}

<Render>
…
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
<!--Masukkan elemen konfigurasi untuk mengekspor ke PDF di sini. Berikut ini adalah contoh
Untuk PageOrientation -->
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
</Extension>
</Render>

{{< /highlight >}}

Jika Anda ingin mengatur parameter untuk file laporan tertentu tetapi tidak untuk setiap laporan di server, Anda dapat menambahkan parameter laporan untuk laporan tertentu di Report Builder dengan langkah-langkah berikut (misalnya, kita akan menambahkan parameter 'IsLandscape' yang ditunjukkan sebelumnya):
{{% alert color="primary" %}}

1. Buka laporan di Report Designer, klik kanan pada folder 'Parameters' di panel 'Report Data', dan pilih 'Add Parameter…' (atau, sebagai alternatif, tarik daftar 'New' dan pilih 'Parameter…').

![todo:image_alt_text](setting-parameters_1.png)

1. Di dialog 'Report Parameter Properties', buat parameter bernama 'IsLandscape', dengan tipe data Boolean, dan tambahkan nilai True di tab 'Default Values'.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}