---
title: Setting Parameters
linktitle: Setting Parameters
type: docs
weight: 10
url: /id/reportingservices/setting-parameters/
description: Pelajari cara mengatur parameter untuk rendering PDF di Aspose.PDF for Reporting Services agar output dapat dikendalikan dengan presisi.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Anda dapat menentukan parameter konfigurasi tertentu yang memengaruhi cara Aspose.PDF for Reporting Services membuat dokumen. Bagian ini menjelaskan proses tersebut.

{{% /alert %}}

Untuk mengonfigurasi Aspose.PDF for Reporting Services, Anda perlu mengedit file `C:\Program Files\Microsoft SQL Server\<Instance>\Reporting Services\ReportServer\rsreportserver.config`. Ini adalah file XML, dan konfigurasi renderer berada di dalam elemen ```<Extension>``` yang sesuai dengan renderer Aspose.PDF.

**Example**

{{< highlight csharp >}}

<Render>
...
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

Jika Anda ingin mengatur parameter hanya untuk file laporan tertentu, bukan untuk setiap laporan di server, Anda dapat menambahkan parameter laporan untuk laporan tersebut di Report Builder dengan langkah-langkah berikut (misalnya, kita akan menambahkan parameter `IsLandscape` yang ditunjukkan sebelumnya):

1. Buka laporan di Report Designer, klik kanan folder `Parameters` pada panel `Report Data`, lalu pilih `Add Parameter...` (atau, sebagai alternatif, buka daftar `New` lalu pilih `Parameter...`).
 
![todo:image_alt_text](setting-parameters_1.png)

1. Di dialog `Report Parameter Properties`, buat parameter bernama `IsLandscape`, pilih tipe data Boolean, lalu tambahkan nilai True pada tab `Default Values`.

![todo:image_alt_text](setting-parameters_2.png)

{{% /alert %}}
