---
title: Membuat dokumen PDF secara programatis
linktitle: Membuat PDF
type: docs
weight: 10
url: id/net/create-document/
description: Halaman ini menjelaskan bagaimana cara membuat dokumen PDF dari awal dengan perpustakaan Aspose.PDF.
---

Aspose.PDF untuk API .NET memungkinkan Anda untuk membuat dan membaca file PDF menggunakan C# dan VB.NET. API ini dapat digunakan dalam berbagai aplikasi .NET termasuk WinForms, ASP.NET, dan beberapa lainnya. Dalam artikel ini, kami akan menunjukkan cara menggunakan Aspose.PDF untuk API .NET untuk dengan mudah menghasilkan dan membaca file PDF dalam aplikasi .NET.

## Cara Membuat File PDF menggunakan C#

Untuk membuat file PDF menggunakan C#, langkah-langkah berikut dapat digunakan.

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
2. Tambahkan objek [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) ke koleksi [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) dari objek Document
3.
1. Simpan dokumen PDF yang dihasilkan

Potongan kode berikut juga bekerja dengan antarmuka grafis [Aspose.Drawing](/pdf/net/drawing/) yang baru.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Inisialisasi objek dokumen
Document document = new Document();
// Tambah halaman
Page page = document.Pages.Add();
// Tambah teks ke halaman baru
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// Simpan PDF yang telah diperbarui
document.Save(dataDir + "HelloWorld_out.pdf")
```

Dalam kasus ini, kita membuat dokumen PDF satu halaman dengan ukuran halaman A4, orientasi potret. Halaman kita akan berisi "Hello, World" di bagian kiri atas halaman.
