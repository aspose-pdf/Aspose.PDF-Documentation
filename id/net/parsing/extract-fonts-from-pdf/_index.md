---
title: Ekstrak font dari PDF C#
linktitle: Ekstrak font dari PDF
type: docs
weight: 30
url: id/net/extract-fonts-from-pdf/
description: Gunakan pustaka Aspose.PDF untuk .NET untuk mengekstrak semua font yang tertanam dari dokumen PDF Anda.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Jika Anda ingin mendapatkan semua font dari dokumen PDF, Anda dapat menggunakan metode FontUtilities.GetAllFonts() yang disediakan dalam kelas Document. Silakan periksa cuplikan kode berikut untuk mendapatkan semua font dari dokumen PDF yang ada:

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

