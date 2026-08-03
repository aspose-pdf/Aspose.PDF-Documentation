---
title: Ukuran margin halaman
linktitle: Page margin size
type: docs
weight: 70
url: /reportingservices/page-margin-size/
description: Sesuaikan ukuran margin halaman dalam laporan PDF dengan Aspose.PDF untuk Layanan Pelaporan untuk meningkatkan keterbacaan dan tata letak.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Perancang laporan Layanan Pelaporan tidak mendukung pengaturan ukuran margin halaman. Aspose.PDF untuk Layanan Pelaporan menyediakan empat parameter untuk mengatur ukuran margin halaman yang sesuai, yaitu:

{{% /alert %}}

```text
Parameter Name: PageMarginLeft  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginRight  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginTop  
Date Type: Float  
Values supported:  Any positive number or zero
```

```text
Parameter Name: PageMarginBottom  
Date Type: Float  
Values supported:  Any positive number or zero
```

## Contoh

```xml
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
```
