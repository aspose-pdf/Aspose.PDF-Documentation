---
title: Mengatur Parameter
linktitle: Mengatur Parameter
type: docs
weight: 10
url: /id/reportingservices/setting-parameters/
description: Cari tahu cara mengatur parameter untuk render PDF di Aspose.PDF untuk Reporting Services. Capai kontrol yang tepat atas output.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Anda dapat menentukan parameter konfigurasi tertentu yang memengaruhi bagaimana Aspose.Pdf untuk Reporting Services menghasilkan dokumen. Bagian ini menjelaskan proses tersebut.

{{% /alert %}}

Untuk mengkonfigurasi Aspose.Pdf untuk Reporting Services, Anda perlu mengedit file C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config. Ini adalah file XML dan konfigurasi renderer berada di dalamnya. ```<Extension>``` elemen yang sesuai dengan renderer Aspose.PDF.

**Contoh**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% alert color="primary" %}}

Jika Anda ingin mengatur parameter untuk file laporan tertentu tetapi tidak untuk setiap laporan di server, Anda dapat menambahkan parameter laporan untuk laporan tertentu di Report Builder dengan langkah-langkah berikut (misalnya, kami akan menambahkan parameter ‘IsLandscape’ yang ditunjukkan sebelumnya):

1. Buka laporan di Report Designer, klik kanan pada folder ‘Parameters’ di panel ‘Report Data’, dan pilih ‘Add Parameter…’ (atau, alternatifnya, tarik turun daftar ‘New’ dan pilih ‘Parameter…’).
 
![todo:image_alt_text](setting-parameters_1.png)

1. Dalam dialog ‘Report Parameter Properties’, buat parameter dengan nama ‘IsLandscape’, dengan tipe data Boolean, dan tambahkan nilai True pada tab ‘Default Values’.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}

