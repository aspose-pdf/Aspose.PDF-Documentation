---
title: Debug Information
type: docs
weight: 90
url: /reportingservices/debug-information/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Tidak dapat dihindari bahwa ada sesuatu yang salah dengan rendering atau hasil yang dirender. Untuk beberapa alasan seperti kerahasiaan atau privasi, kami tidak dapat memperoleh sumber data yang digunakan dalam laporan pengguna, sehingga tidak dapat mereproduksi kesalahan dalam laporan. Untuk membuat komunikasi antara pelanggan dan pengembang lebih mudah dan lancar, kami menambahkan parameter ini. Jika Anda mengalami masalah saat merender laporan Anda dengan Aspose.PDF untuk Layanan Pelaporan, silakan atur parameter laporan ini, kemudian Anda akan mendapatkan dokumen yang dirender dengan format XML. Setelah itu, silakan unggah file XML kepada kami di forum produk.

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
```
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
```