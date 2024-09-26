---
title: ASP - VBScript via COM Interop
type: docs
weight: 30
url: /net/asp-vbscript-via-com-interop/
---

## Prasyarat

{{% alert color="primary" %}}

    Mohon periksa artikel yang berjudul Gunakan Aspose.pdf untuk .NET via COM Interop.

{{% /alert %}}

## Contoh Hello World! pada VB Script

{{% alert color="primary" %}}

Ini adalah aplikasi ASP sederhana yang menunjukkan cara membuat file PDF dengan teks contoh menggunakan [Aspose.PDF for .NET](/pdf/net/) dan VBScript via COM Interop.

{{% /alert %}}

```vb

<%@ LANGUAGE = VBScript %>
<% Option Explicit %>
<html>
    <head>
        <title> menggunakan Aspose.PDF untuk .NET dalam contoh ASP klasik</title>
    </head>
<body>

<h3>pembuatan dokumen PDF contoh dengan menggunakan Aspose.PDF untuk .NET bersama ASP klasik dan VBScript</h3>

<%

'set lisensi
Dim lic
Set lic = CreateObject("Aspose.PDF.License")
lic.SetLicense("D:\ASPOSE\Licences\Aspose.Total licenses\Aspose.Total.lic")

'Buat instans Pdf dengan memanggil konstruktornya yang kosong
Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

'Buat bagian baru dalam objek Pdf
Dim pdfsection
Set pdfsection = CreateObject("Aspose.PDF.Generator.Section")

'Tambahkan bagian ke objek Pdf
pdf.Sections.Add(pdfsection)

' Buat objek Teks
Dim SampleText
Set SampleText = CreateObject("Aspose.PDF.Generator.Text")

'Tambahkan Segmen Teks ke objek teks
Dim seg1
Set seg1 = CreateObject("Aspose.PDF.Generator.Segment")

'Berikan beberapa konten ke segmen
seg1.Content = "HelloWorld menggunakan ASP dan VBScript"

'Tambahkan segmen (dengan warna teks merah) ke paragraf
SampleText.Segments.Add(seg1)

' Tambahkan paragraf Teks ke koleksi paragraf dari sebuah bagian
pdfsection.Paragraphs.Add(SampleText)

' Simpan dokumen PDF
pdf.Save("d:\pdftest\HelloWorldinASP.pdf")

%>

    </body>
</html>
```
## Mengekstrak Teks menggunakan VBScript

{{% alert color="primary" %}}
    Contoh VBScript ini mengekstrak teks dari dokumen PDF yang sudah ada melalui COM Interop.
    Error rendering macro 'code' : Invalid value specified for parameter lang
{{% /alert %}}
