---
title: PageSize
linktitle: PageSize
type: docs
weight: 60
url: /id/reportingservices/pagesize/
description: Sesuaikan ukuran halaman untuk laporan PDF di Aspose.PDF for Reporting Services agar memenuhi persyaratan dokumen tertentu.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Desainer laporan Reporting Services tidak mendukung ukuran halaman umum seperti A4, B5, Letter, dan sebagainya. Dengan Aspose.PDF for Reporting Services, Anda dapat melakukannya seperti pada contoh berikut.

{{% /alert %}}

{{% alert color="primary" %}}

**Nama Parameter**: PageSize  
**Jenis Tanggal**: String  
**Nilai yang didukung**: A0, A1, A2, A3, A4, A5, A6, B5, Letter, Legal, Ledger, P11x17  

**Contoh**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PageSize>A4</PageSize>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
