---
title: Orientasi Halaman
linktitle: Page Orientation
type: docs
weight: 10
url: /reportingservices/page-orientation/
description: Konfigurasikan orientasi halaman untuk laporan PDF di Aspose.PDF untuk Layanan Pelaporan. Sesuaikan tata letak untuk presentasi yang lebih baik.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Bahasa Definisi Laporan tidak memungkinkan penentuan orientasi halaman dalam laporan secara eksplisit. Dengan Aspose.PDF untuk Layanan Pelaporan Anda dapat dengan mudah menginstruksikan eksportir untuk menghasilkan dokumen PDF dengan orientasi halaman lanskap. Orientasi defaultnya adalah potret.

{{% /alert %}}

```text
The default orientation is portrait.
Parameter Name: IsLandscape
Date Type: Boolean
Values supported: True, False (default)
```

## Contoh

```xml
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>
```

