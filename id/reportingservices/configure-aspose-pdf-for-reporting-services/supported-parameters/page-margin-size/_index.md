---
title: Ukuran margin halaman
linktitle: Ukuran margin halaman
type: docs
weight: 70
url: /id/reportingservices/page-margin-size/
description: Sesuaikan ukuran margin halaman dalam laporan PDF dengan Aspose.PDF for Reporting Services untuk meningkatkan keterbacaan dan tata letak.
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Perancang laporan Reporting Services tidak mendukung pengaturan ukuran margin halaman. Aspose.Pdf for Reporting Services menyediakan empat parameter untuk mengatur ukuran margin halaman yang sesuai, yaitu:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**Nama Parameter**: PageMarginLeft  
**Tipe Tanggal**: Float  
**Nilai yang didukung**:  Setiap angka positif atau nol

2)  
**Nama Parameter**: PageMarginRight  
**Tipe Tanggal**: Float  
**Nilai yang didukung**:  Setiap angka positif atau nol

3)  
**Nama Parameter**: PageMarginTop  
**Tipe Tanggal**: Float  
**Nilai yang didukung**:  Setiap angka positif atau nol

4)  
**Nama Parameter**: PageMarginBottom  
**Tipe Tanggal**: Float  
**Nilai yang didukung**:  Setiap angka positif atau nol

**Contoh**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type=" Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices ">
    <Configuration>
    <PageMarginLeft>50</PageMarginLeft>
    <PageMarginRight>50</PageMarginRight>
    <PageMarginTop>50</PageMarginTop>
    <PageMarginBottom>50</PageMarginBottom>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}

