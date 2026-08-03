---
title: Ukuran Halaman
linktitle: PageSize
type: docs
weight: 60
url: /reportingservices/pagesize/
description: Sesuaikan ukuran halaman untuk laporan PDF di Aspose.PDF untuk Layanan Pelaporan untuk memenuhi persyaratan dokumen tertentu.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Perancang laporan Layanan Pelaporan tidak mendukung ukuran halaman umum seperti A4, B5, Letter dan sebagainya. Dengan Aspose.PDF for Reporting Services, Anda bisa mendapatkannya seperti pada contoh berikut.

{{% /alert %}}

```text
Parameter Name: PageSize  
Date Type: String  
Values supported: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  
```

## Contoh

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>
```