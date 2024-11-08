---
title: ASP - JScript via COM Interop
type: docs
weight: 40
url: /id/net/asp-jscript-via-com-interop/
---
{{% alert color="primary" %}}

Ini adalah aplikasi ASP sederhana yang menunjukkan cara menambahkan string teks sederhana ke file PDF menggunakan [Aspose.PDF for .NET](/pdf/id/net/) dan JScript melalui COM Interop.

{{% /alert %}}

Contoh:

{{% alert color="primary" %}}

```javascript
<%@ LANGUAGE = JScript %>
<html>
    <head>
        <title> menggunakan Aspose.PDF for .NET dalam contoh ASP klasik</title>
    </head>
    <body>
        <h3>pembuatan dokumen PDF contoh dengan menggunakan Aspose.PDF for .NET dengan ASP klasik dan JScript</h3>
<%
// set lisensi
var lic = Server.CreateObject("Aspose.PDF.License");
lic.SetLicense("D:\\ASPOSE\\Aspose.Total.lic");

// Instansiasi instansi Pdf dengan memanggil konstruktornya yang kosong
var pdf = Server.CreateObject("Aspose.PDF.Document");

// Buat halaman baru dalam objek PDF
var pdfpage = pdf.Pages.Add();

// Buat objek Fragmen Teks
var sampleText = Server.CreateObject("Aspose.Pdf.Text.TextFragment");

// Berikan beberapa konten ke Fragmen
sampleText.Text = "HelloWorld menggunakan ASP dan JScript";

// Tambahkan paragraf Teks ke koleksi paragraf dari sebuah bagian
pdfpage.Paragraphs.Add(sampleText);

// Simpan dokumen PDF
pdf.Save("d:\\pdftest\\HelloWorldinASP.pdf");

%>
    </body>
</html>
```
{{% /alert %}}
