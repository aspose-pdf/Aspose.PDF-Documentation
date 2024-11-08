---
title: Mengonversi Format PDF ke PDF/A
linktitle: Mengonversi Format PDF ke PDF/A
type: docs
weight: 100
url: /id/net/convert-pdf-to-pdfa/
lastmod: "2021-11-01"
description: Topik ini menunjukkan bagaimana Aspose.PDF memungkinkan untuk mengonversi file PDF menjadi file PDF yang sesuai dengan PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF untuk .NET** memungkinkan Anda untuk mengonversi file PDF menjadi file PDF yang sesuai dengan <abbr title="Portable Document Format / A">PDF/A</abbr>. Sebelum melakukan hal tersebut, file harus divalidasi. Topik ini menjelaskan bagaimana caranya.

{{% alert color="primary" %}}

Harap dicatat kami mengikuti Adobe Preflight untuk validasi kesesuaian PDF/A. Semua alat di pasar memiliki "representasi" mereka sendiri tentang kesesuaian PDF/A. Silakan periksa artikel ini tentang alat validasi PDF/A untuk referensi. Kami memilih produk Adobe untuk memverifikasi bagaimana Aspose.PDF menghasilkan file PDF karena Adobe berada di pusat segala hal yang terhubung dengan PDF.

{{% /alert %}}

Konversikan file menggunakan metode Convert dari kelas Document.
{{% alert color="success" %}}
**Coba konversi PDF ke PDF/A secara online**

Aspose.PDF untuk .NET mempersembahkan Anda aplikasi gratis secara online ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba untuk menginvestigasi fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF PDF ke PDF/A dengan Aplikasi Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

Snippet kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Konversi file PDF ke PDF/A-1b

Snippet kode berikut menunjukkan cara mengonversi file PDF menjadi PDF yang mematuhi PDF/A-1b.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "PDFToPDFA.pdf");
           
// Konversi ke dokumen yang mematuhi PDF/A
// Selama proses konversi, validasi juga dilakukan
pdfDocument.Convert(dataDir + "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA_out.pdf";
// Simpan dokumen keluaran
pdfDocument.Save(dataDir);
```
Untuk melakukan validasi saja, gunakan baris kode berikut:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "ValidatePDFAStandard.pdf");

// Validasi PDF untuk PDF/A-1a
pdfDocument.Validate(dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1B);
```

## Konversi file PDF ke PDF/A-3b

Aspose.PDF untuk .NET juga mendukung fitur untuk mengonversi file PDF ke format PDF/A-3b.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "input.pdf");           

pdfDocument.Convert(new MemoryStream(), PdfFormat.PDF_A_3B, ConvertErrorAction.Delete);

dataDir = dataDir + "PDFToPDFA3b_out.pdf";
// Simpan dokumen keluaran
pdfDocument.Save(dataDir);
```
## Mengonversi File PDF ke Format PDF/A-2u

Aspose.PDF untuk .NET juga mendukung fitur untuk mengonversi file PDF ke format PDF/A-2u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_2U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Mengonversi File PDF ke Format PDF/A-3u

Aspose.PDF untuk .NET juga mendukung fitur untuk mengonversi file PDF ke format PDF/A-3u.

```csharp
string inFile = "input.pdf";
string outFile = "output.pdf";
Aspose.PDF.Document doc = new Aspose.PDF.Document(inFile);
doc.Convert(new MemoryStream(), PdfFormat.PDF_A_3U, ConvertErrorAction.Delete);
doc.Save(outFile);
```

## Menambahkan Lampiran ke File PDF/A

Jika Anda memiliki kebutuhan untuk melampirkan file ke format kepatuhan PDF/A, maka kami merekomendasikan menggunakan nilai PDF_A_3A dari enumerasi Aspose.PDF.PdfFormat.
PDF/A_3a adalah format yang menyediakan fitur untuk melampirkan berbagai format file sebagai lampiran ke file yang mematuhi PDF/A.

```csharp
## Ganti font yang hilang dengan font alternatif

Sesuai dengan standar PDFA, font harus tertanam dalam dokumen PDFA.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instansiasi instansi Dokumen untuk memuat file yang ada
Aspose.Pdf.Document doc = new Document(dataDir + "input.pdf");
// Siapkan file baru untuk ditambahkan sebagai lampiran
FileSpecification fileSpecification = new FileSpecification(dataDir + "aspose-logo.jpg", "File gambar besar");
// Tambahkan lampiran ke koleksi lampiran dokumen
doc.EmbeddedFiles.Add(fileSpecification);
// Lakukan konversi ke PDF/A_3a sehingga lampiran termasuk dalam file hasil
doc.Convert(dataDir + "log.txt", Aspose.Pdf.PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
// Simpan file hasil
doc.Save(dataDir + "AddAttachmentToPDFA_out.pdf");
```
Sesuai dengan standar PDFA, font harus disematkan dalam dokumen PDFA.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Aspose.Pdf.Text.Font originalFont = null;
try
{
    originalFont = FontRepository.FindFont("AgencyFB");
}
catch (Exception)
{
    // Font tidak tersedia di mesin tujuan
    FontRepository.Substitutions.Add(new SimpleFontSubstitution("AgencyFB", "Arial"));
}
var fileNew = new FileInfo(dataDir + "newfile_out.pdf");
var pdf = new Document(dataDir + "input.pdf");
pdf.Convert( dataDir +  "log.xml", PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
pdf.Save(fileNew.FullName);
```
