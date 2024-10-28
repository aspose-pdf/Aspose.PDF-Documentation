---
title: Orientasi Halaman
type: docs
weight: 10
url: /reportingservices/page-orientation/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Bahasa Definisi Laporan tidak memungkinkan untuk menentukan orientasi halaman dalam laporan secara eksplisit. Dengan Aspose.Pdf untuk Layanan Pelaporan, Anda dapat dengan mudah menginstruksikan eksportir untuk menghasilkan dokumen PDF dengan orientasi halaman lanskap. Orientasi default adalah potret.

{{% /alert %}}

{{% alert color="primary" %}}

Orientasi default adalah potret.
**Nama Parameter**: IsLandscape
**Tipe Data**: Boolean
**Nilai yang didukung**: True, False (default)

**Contoh**
{{< highlight csharp >}}
<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <IsLandscape>True</IsLandscape>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}