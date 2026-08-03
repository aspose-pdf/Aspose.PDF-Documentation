---
title: PDF_A Kesesuaian
linktitle: PDF_A Conformance
type: docs
weight: 100
url: /reportingservices/pdf_a-conformance/
description: Aktifkan kesesuaian PDF/A di Aspose.PDF untuk Layanan Pelaporan. Buat dokumen yang sesuai dengan arsip dengan mudah.
lastmod: "2025-05-22"
---

{{% alert color="primary" %}}

Anda bisa mendapatkan pengenalan Kesesuaian PDF/A (PDF yang Dapat Diarsipkan) di dokumentasi Aspose.PDF.

Jika Anda ingin membuat dokumen PDF/A, tambahkan parameter laporan berikut.

{{% /alert %}}

```text
Parameter Name: PdfConformance  
Date Type: String  
Values supported: PdfA1A, PdfA1B, PdfA2A, PdfA2B, PdfA2U, PdfA3A, PdfA3B, PdfA3U, PdfA4, PdfA4E, PdfA4F  
```

## Contoh

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <PdfConformance>PdfA1A</PdfConformance>
    </Configuration>
    </Extension>
</Render>
```