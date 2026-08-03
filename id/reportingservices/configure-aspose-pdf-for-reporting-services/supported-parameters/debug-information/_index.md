---
title: Informasi Debug
linktitle: Debug Information
type: docs
weight: 90
url: /reportingservices/debug-information/
description: Akses dan analisis informasi debug untuk rendering PDF di Aspose.PDF untuk Layanan Pelaporan guna memecahkan masalah secara efektif.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Tidak dapat dipungkiri jika ada yang salah pada rendering atau hasil yang dirender. Karena beberapa alasan seperti kerahasiaan atau privasi, kami tidak dapat menggunakan sumber data dalam laporan pengguna, sehingga tidak dapat mereproduksi kesalahan dalam laporan. Untuk membuat komunikasi antara pelanggan dan pengembang lebih mudah dan lancar, kami menambahkan parameter ini. Jika Anda menemui kendala saat merender laporan Anda dengan Aspose.PDF untuk Reporting Services, silakan atur parameter laporan ini, maka Anda akan mendapatkan dokumen yang dirender dengan format XML. Setelah itu, silakan posting file XML untuk kami di forum produk.

{{% /alert %}}

{{% alert color="primary" %}}

```txt
Parameter Name: SavingXmlFormat
Date Type: Boolean  
Values supported**: True, False (default)
```

## Contoh

```xml
<Render>
...
<Extension Name="APPDF" Type=" Aspose.PDF.ReportingServices.Renderer,Aspose.PDF.ReportingServices">
<Configuration>
<SavingXmlFormat > True </SavingXmlFormat>
</Configuration>
</Extension>
</Render>
```

{{% /alert %}}
