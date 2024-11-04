---
title: Ekstrak Gambar dari PDF C#
linktitle: Ekstrak Gambar dari PDF
type: docs
weight: 20
url: /net/extract-images-from-the-pdf-file/
description: Cara mengekstrak bagian gambar dari PDF menggunakan Aspose.PDF untuk .NET di C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Gambar disimpan dalam koleksi [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) dari setiap halaman, dalam koleksi [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images). Untuk mengekstrak halaman tertentu, kemudian dapatkan gambar dari koleksi Images menggunakan indeks gambar yang spesifik.

Indeks gambar mengembalikan objek [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage). Objek ini menyediakan metode Save yang dapat digunakan untuk menyimpan gambar yang diekstrak. Potongan kode berikut menunjukkan cara mengekstrak gambar dari file PDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

 ```csharp
 // Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 ```

// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "ExtractImages.pdf");

// Ekstrak gambar tertentu
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// Simpan gambar keluaran
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// Simpan file PDF yang telah diperbarui
pdfDocument.Save(dataDir);
```
