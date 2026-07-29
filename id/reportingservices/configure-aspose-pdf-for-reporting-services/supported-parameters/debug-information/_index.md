---
title: Informasi Debug
linktitle: Informasi Debug
type: docs
weight: 90
url: /id/reportingservices/debug-information/
description: Akses dan analisis informasi debug untuk rendering PDF di Aspose.PDF for Reporting Services guna memecahkan masalah secara efektif.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Tidak dapat dihindari bahwa ada sesuatu yang salah dengan rendering atau hasil rendering. Karena beberapa alasan seperti kerahasiaan atau privasi, kami tidak dapat memperoleh sumber data yang digunakan dalam laporan pengguna, sehingga tidak dapat mereproduksi kesalahan dalam laporan tersebut. Untuk mempermudah dan memperlancar komunikasi antara pelanggan dan pengembang, kami menambahkan parameter ini. Jika Anda mengalami masalah saat merender laporan Anda dengan Aspose.PDF for Reporting Services, silakan atur parameter laporan ini, maka Anda akan mendapatkan dokumen yang dirender dalam format XML. Setelah itu, harap unggah file XML tersebut kepada kami di forum produk.

{{% /alert %}}

{{% alert color="primary" %}}
**Nama Parameter**: SavingXmlFormat  
**Tipe Tanggal**: Boolean  
**Nilai yang didukung**: True, False (default)  

**Contoh**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > Benar </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
