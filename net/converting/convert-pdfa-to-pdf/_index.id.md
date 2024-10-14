---
title: Mengonversi format PDF/A ke PDF
linktitle: Mengonversi format PDF/A ke PDF
type: docs
weight: 110
url: /net/convert-pdfa-to-pdf/
lastmod: "2021-11-01"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF/A ke dokumen PDF dengan perpustakaan .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Mengonversi dokumen PDF/A ke PDF

Mengonversi dokumen PDF/A ke PDF berarti menghilangkan pembatasan <abbr title="Portable Document Format Archive">PDF/A</abbr> dari dokumen asli.
Kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) memiliki metode [RemovePdfaCompliance(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/removepdfacompliance) untuk menghapus informasi kepatuhan PDF dari file sumber/masukan.

```csharp
public static void ConvertPDFAtoPDF()
{
    // Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Hapus informasi kepatuhan PDF/A
    pdfDocument.RemovePdfaCompliance();
    // Simpan dokumen yang telah diperbarui
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
Informasi ini juga dihapus jika Anda melakukan perubahan pada dokumen (misalnya, menambah halaman). Pada contoh berikut, dokumen keluaran kehilangan kepatuhan PDF/A setelah penambahan halaman.

```csharp
public static void ConvertPDFAtoPDFAdvanced()
{
    // Untuk contoh lengkap dan berkas data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    Document pdfDocument = new Document(_dataDir + "PDFAToPDF.pdf");
    // Menambahkan halaman baru (kosong) menghilangkan informasi kepatuhan PDF/A.
    pdfDocument.Pages.Add();
    // Simpan dokumen yang telah diperbarui
    pdfDocument.Save(_dataDir + "PDFAToPDF_out.pdf");
}
```
