---
title: Menyimpan Dokumen PDF Secara Pemrograman
linktitle: Simpan PDF
type: docs
weight: 30
url: /net/save-pdf-document/
description: Pelajari cara menyimpan file PDF dalam C# Aspose.PDF untuk perpustakaan PDF .NET. Simpan dokumen PDF ke sistem file, ke stream, dan dalam aplikasi Web.
aliases:
    - /net/saving/
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Potongan kode berikut juga bekerja dengan antarmuka grafis baru [Aspose.Drawing](/pdf/net/drawing/).

## Simpan Dokumen PDF ke Sistem File

Anda dapat menyimpan dokumen PDF yang telah dibuat atau dimanipulasi ke sistem file menggunakan metode `Save` dari kelas `Document`.
Ketika Anda tidak menyediakan jenis format (opsi), maka dokumen disimpan dalam format Aspose.PDF v.1.7 (*.pdf).

```csharp
public static void SaveDocument()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // melakukan beberapa manipulasi, misalnya menambah halaman kosong baru
    pdfDocument.Pages.Add();
    pdfDocument.Save(modifiedFileName);
}
```
## Simpan dokumen PDF ke stream

Anda juga dapat menyimpan dokumen PDF yang telah dibuat atau dimanipulasi ke stream dengan menggunakan overload dari metode `Save`.

```csharp
public static void SaveDocumentStream()
{
    var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
    var modifiedFileName = Path.Combine(_dataDir, "SimpleResumeModified.pdf");

    var pdfDocument = new Aspose.Pdf.Document(originalFileName);
    // lakukan beberapa manipulasi, misalnya tambahkan halaman kosong baru
    pdfDocument.Pages.Add();
    pdfDocument.Save(System.IO.File.OpenWrite(modifiedFileName));
}
```

## Simpan dokumen PDF dalam aplikasi Web

Untuk menyimpan dokumen dalam aplikasi Web, Anda dapat menggunakan cara yang diusulkan di atas. Selain itu, kelas `Document` memiliki metode `Save` yang kelebihan untuk digunakan dengan kelas [HttpResponse](https://docs.microsoft.com/en-us/dotnet/api/system.web.httpresponse?view=netframework-4.8).

```csharp
var originalFileName = Path.Combine(_dataDir, "SimpleResume.pdf");
var pdfDocument = new Aspose.Pdf.Document(originalFileName);
// lakukan beberapa manipulasi, misalnya tambahkan halaman kosong baru
pdfDocument.Pages.Add();
pdfDocument.Save(Response, originalFileName, ContentDisposition.Attachment, new PdfSaveOptions());
```
Untuk penjelasan lebih rinci, silakan mengikuti bagian [Showcase](/pdf/net/showcases/).

## Simpan format PDF/A atau PDF/X

PDF/A adalah versi yang distandarisasi ISO dari Format Dokumen Portabel (PDF) yang digunakan dalam pengarsipan dan pelestarian jangka panjang dokumen elektronik.
PDF/A berbeda dari PDF karena melarang fitur yang tidak cocok untuk pengarsipan jangka panjang, seperti penghubungan font (berbeda dengan penyertaan font) dan enkripsi. Persyaratan ISO untuk penampil PDF/A mencakup pedoman manajemen warna, dukungan font yang tertanam, dan antarmuka pengguna untuk membaca anotasi yang tertanam.

PDF/X adalah subset dari standar ISO PDF. Tujuan PDF/X adalah untuk memfasilitasi pertukaran grafis, dan oleh karena itu memiliki serangkaian persyaratan pencetakan yang tidak berlaku untuk file PDF standar.

Dalam kedua kasus, metode `Save` digunakan untuk menyimpan dokumen, sementara dokumen harus dipersiapkan menggunakan metode `Convert`.

```csharp
public static void SaveDocumentAsPDFx()
{
    var pdfDocument = new Aspose.Pdf.Document("..\\..\\..\\Samples\\SimpleResume.pdf");
    pdfDocument.Pages.Add();
    pdfDocument.Convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    pdfDocument.Save("..\\..\\..\\Samples\\SimpleResume_X3.pdf");
}
```

