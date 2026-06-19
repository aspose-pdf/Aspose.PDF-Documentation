---
title: Informasi Debug
linktitle: Informasi Debug
type: docs
weight: 90
url: /id/reportingservices/debug-information/
description: Akses dan analisis informasi debug untuk rendering PDF di Aspose.PDF for Reporting Services untuk memperbaiki masalah secara efektif.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Tidak dapat dihindari bahwa ada sesuatu yang salah dengan proses rendering atau hasil yang dirender. Karena beberapa alasan seperti kerahasiaan atau privasi, kami tidak dapat memperoleh sumber data yang digunakan dalam laporan pengguna, sehingga tidak dapat mereproduksi kesalahan dalam laporan tersebut. Untuk mempermudah dan memperlancar komunikasi antara pelanggan dan pengembang, kami menambahkan parameter ini. Jika Anda mengalami masalah saat merender laporan Anda dengan Aspose.PDF for Reporting Services, silakan tetapkan parameter laporan ini, maka Anda akan menerima dokumen yang dirender dalam format XML. Setelah itu, harap unggah file XML tersebut untuk kami di forum produk.

{{% /alert %}}

{{% alert color="primary" %}}
**Nama Parameter**: SavingXmlFormat  
**Tipe Data**: Boolean  
**Nilai yang didukung**: True, False (default)  

**Contoh**
{{< highlight csharp >}}

<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

