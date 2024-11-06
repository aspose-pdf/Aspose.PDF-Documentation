---
title: ASP.NET tanpa menggunakan Visual Studio
type: docs
weight: 60
url: id/net/asp-net-without-using-visual-studio/
---

{{% alert color="primary" %}}

[Aspose.PDF for .NET](/pdf/net/) dapat digunakan untuk mengembangkan halaman atau aplikasi ASP.NET tanpa menggunakan Visual Studio. Dalam contoh ini, kita akan menulis HTML dan kode C# atau VB.NET dalam satu file .aspx; ini umumnya dikenal sebagai Instant ASP.NET.

{{% /alert %}}

## Detail Implementasi

{{% alert color="primary" %}}

Buat aplikasi web sampel dan salin Aspose.PDF.dll ke dalam direktori bernama "Bin" di direktori situs web Anda (*jika folder bin tidak ada, buat satu*). Kemudian buat halaman .aspx Anda dan salin kode berikut ke dalamnya.
Contoh ini menunjukkan cara menggunakan [Aspose.PDF for .NET](/pdf/net/) dengan kode inline di halaman ASP.NET untuk membuat dokumen PDF sederhana dengan beberapa teks sampel di dalamnya.
{{% /alert %}}

```cs

<%@ Page Language ="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.IO" %>
<%@ Import Namespace="System.Data" %>
<%@ Import Namespace="Aspose.PDF" %>

<html>
    <head>
        <title> menggunakan Aspose.PDF for .NET dengan ASP.NET Inline</title>
    </head>
    <body>
        <h3>pembuatan dokumen PDF sederhana saat menggunakan Aspose.PDF for .NET dengan ASP.NET Inline</h3>
<%
    // set lisensi
    Aspose.PDF.License lic = new Aspose.PDF.License();
    lic.SetLicense("D:\\ASPOSE\\Licences\\Aspose.Total licenses\\Aspose.Total.lic");

    // Inisialisasi objek dokumen
    Document document = new Document();
    // Tambah halaman
    Page page = document.Pages.Add();
    // Tambah teks ke halaman baru
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
    // Simpan PDF yang telah diperbarui
    var outputFileName = Path.Combine(_dataDir, "HelloWorld_out.pdf");
    document.Save( outputFileName );
%>

    </body>
</html>
```

