---
title: Orientasi Halaman
linktitle: Orientasi Halaman
type: docs
weight: 10
url: /id/reportingservices/page-orientation/
description: Konfigurasikan orientasi halaman untuk laporan PDF di Aspose.PDF for Reporting Services. Sesuaikan tata letak untuk presentasi yang lebih baik.
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Report Definition Language tidak memungkinkan menentukan orientasi halaman dalam laporan secara eksplisit. Dengan Aspose.PDF for Reporting Services Anda dapat dengan mudah menginstruksikan pengekspor untuk menghasilkan dokumen PDF dengan orientasi halaman lanskap. Orientasi default adalah potret.

{{% /alert %}}

{{% alert color="primary" %}}

Orientasi default adalah potret.
**Nama Parameter**: IsLandscape
**Tipe Data**: Boolean
**Nilai yang didukung**: True, False (bawaan)

**Contoh**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>Benar</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
