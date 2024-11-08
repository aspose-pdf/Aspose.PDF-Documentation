---
title: PageSize
type: docs
weight: 60
url: /id/reportingservices/pagesize/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Perancang laporan Reporting Services tidak mendukung ukuran halaman umum seperti A4, B5, Letter, dan sebagainya. Dengan Aspose.Pdf untuk Reporting Services, Anda dapat mendapatkannya seperti dalam contoh berikut.

{{% /alert %}}

{{% alert color="primary" %}}

**Nama Parameter**: PageSize  
**Jenis Data**: String  
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