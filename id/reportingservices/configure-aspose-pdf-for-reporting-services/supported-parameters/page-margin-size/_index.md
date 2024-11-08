```
---
title: Ukuran margin halaman
type: docs
weight: 70
url: /id/reportingservices/page-margin-size/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Perancang laporan Layanan Pelaporan tidak mendukung pengaturan ukuran margin halaman. Aspose.Pdf untuk Layanan Pelaporan menyediakan empat parameter untuk mengatur ukuran margin halaman yang sesuai, yaitu:

{{% /alert %}}

{{% alert color="primary" %}}
1)  
**Nama Parameter**: PageMarginLeft  
**Tipe Data**: Float  
**Nilai yang didukung**: Angka positif atau nol

2)  
**Nama Parameter**: PageMarginRight  
**Tipe Data**: Float  
**Nilai yang didukung**: Angka positif atau nol

3)  
**Nama Parameter**: PageMarginTop  
**Tipe Data**: Float  
**Nilai yang didukung**: Angka positif atau nol

4)  
**Nama Parameter**: PageMarginBottom  
**Tipe Data**: Float  
**Nilai yang didukung**: Angka positif atau nol

**Contoh**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type=" Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices ">

    <Configuration>
```
<PageMarginLeft>50</PageMarginLeft>
<PageMarginRight>50</PageMarginRight>
<PageMarginTop>50</PageMarginTop>
<PageMarginBottom>50</PageMarginBottom>
</Configuration>
</Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}