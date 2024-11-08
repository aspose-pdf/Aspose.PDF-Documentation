---
title: Mengonversi PDF ke Dokumen Microsoft Word dalam .NET
linktitle: Mengonversi PDF ke Word
type: docs
weight: 10
url: /id/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Pelajari cara menulis kode C# untuk konversi PDF ke format Microsoft Word dengan Aspose.PDF untuk .NET dan meningkatkan konversi PDF ke DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Overview

Artikel ini menjelaskan cara **mengonversi PDF ke Dokumen Microsoft Word menggunakan C#**. Topik-topik yang dibahas adalah sebagai berikut.

_Format_: **DOC**

- [C# PDF ke DOC](#csharp-pdf-to-doc)
- [C# Mengonversi PDF ke DOC](#csharp-pdf-to-doc)
- [C# Cara mengonversi file PDF ke DOC](#csharp-pdf-to-doc)

_Format_: **DOCX**

- [C# PDF ke DOCX](#csharp-pdf-to-docx)
- [C# Mengonversi PDF ke DOCX](#csharp-pdf-to-docx)
- [C# Cara mengonversi file PDF ke DOCX](#csharp-pdf-to-docx)

_Format_: **Word**

- [C# PDF ke Word](#csharp-pdf-to-docx)
- [C# Mengonversi PDF ke Word](#csharp-pdf-to-doc)
- [C# Cara mengonversi file PDF ke Word](#csharp-pdf-to-docx)

Potongan kode berikut juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).
Potongan kode berikut ini juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Konversi PDF ke DOC dan DOCX

Salah satu fitur yang paling populer adalah konversi PDF ke Microsoft Word DOC, yang membuat pengelolaan konten menjadi lebih mudah. **Aspose.PDF for .NET** memungkinkan Anda untuk mengonversi file PDF ke format DOC dan DOCX dengan cepat dan efisien.

## Konversi PDF ke DOC (file Microsoft Word 97-2003)

Konversikan file PDF ke format DOC dengan mudah dan kontrol penuh. Aspose.PDF for .NET sangat fleksibel dan mendukung berbagai macam konversi. Mengonversi halaman dari dokumen PDF ke gambar, misalnya, adalah fitur yang sangat populer.

Banyak pelanggan kami telah meminta konversi dari PDF ke DOC: mengonversi file PDF menjadi dokumen Microsoft Word. Pelanggan menginginkan ini karena file PDF tidak mudah untuk diedit, sedangkan dokumen Word dapat. Beberapa perusahaan ingin penggunanya dapat memanipulasi teks, tabel, dan gambar dalam file yang awalnya adalah PDF.

Mempertahankan tradisi membuat segala sesuatu menjadi sederhana dan mudah dipahami, Aspose.PDF for .NET memungkinkan Anda mengubah file PDF sumber menjadi file DOC dengan dua baris kode.
Memelihara tradisi membuat segalanya menjadi sederhana dan mudah dimengerti, Aspose.PDF untuk .NET memungkinkan Anda mengubah file PDF sumber menjadi file DOC hanya dengan dua baris kode.

Potongan kode C# berikut menunjukkan cara mengonversi file PDF ke format DOC.

<a name="csharp-pdf-to-doc"><strong>Langkah: Mengonversi PDF ke DOC dalam C#</strong></a>

1. Buat sebuah instance dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Simpan ke format **SaveFormat.Doc** dengan memanggil metode **Document.Save()**.

```csharp
public static void ConvertPDFtoWord()
{
    // Buka dokumen PDF sumber
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Simpan file ke format dokumen MS
    pdfDocument.Save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);

}
```

### Menggunakan Kelas DocSaveOptions

Kelas [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) menyediakan banyak properti yang meningkatkan konversi file PDF ke format DOC.
Kelas [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) menyediakan berbagai properti yang meningkatkan konversi file PDF ke format DOC.

- Mode [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) cepat dan baik untuk mempertahankan tampilan asli dari file PDF, namun kemampuan edit dokumen hasilnya bisa terbatas. Setiap blok teks yang secara visual dikelompokkan dalam PDF asli dikonversi menjadi kotak teks dalam dokumen hasil. Ini mencapai kemiripan maksimal dengan asli, sehingga dokumen hasil terlihat bagus, tetapi seluruhnya terdiri dari kotak teks, yang bisa diedit di Microsoft Word, yang cukup menantang.
- Mode [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) adalah mode pengenalan penuh, di mana mesin melakukan pengelompokan dan analisis multi-level untuk mengembalikan dokumen asli sesuai dengan maksud penulis sambil menghasilkan dokumen yang mudah diedit.
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) adalah mode pengenalan penuh, di mana mesin melakukan pengelompokan dan analisis multi-level untuk mengembalikan dokumen asli sesuai dengan maksud penulis sambil menghasilkan dokumen yang mudah diedit.

Properti [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) dapat digunakan untuk mengontrol kedekatan relatif antara elemen teks. Ini berarti bahwa jarak dinormalkan oleh ukuran font. Font yang lebih besar mungkin memiliki spasi yang lebih besar antara suku kata dan masih dianggap sebagai satu kesatuan. Ini ditentukan sebagai persentase dari ukuran font; misalnya, 1 = 100%. Ini berarti dua karakter 12pt yang ditempatkan 12 pt terpisah adalah berdekatan.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) digunakan untuk mengaktifkan pengenalan bullet selama konversi.

```csharp
public static void ConvertPDFtoWordDocAdvanced()
{
    var pdfFile = Path.Combine(_dataDir, "PDF-to-DOC.pdf");
    var docFile = Path.Combine(_dataDir, "PDF-to-DOC.doc");
    Document pdfDocument = new Document(pdfFile);
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        Format = DocSaveOptions.DocFormat.Doc,
        // Atur mode pengenalan sebagai Flow
        Mode = DocSaveOptions.RecognitionMode.Flow,
        // Atur kedekatan Horizontal sebagai 2.5
        RelativeHorizontalProximity = 2.5f,
        // Aktifkan nilai untuk mengenali bullet selama proses konversi
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```
{{% alert color="success" %}}
**Cobalah Mengonversi PDF ke DOC Secara Online**

Aspose.PDF untuk .NET menghadirkan aplikasi gratis online ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba untuk mengeksplorasi fungsionalitas dan kualitas kerjanya.

[![Convert PDF to DOC](/pdf/id/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Konversi PDF ke DOCX (file Microsoft Word 2007-2021)

Aspose.PDF untuk API .NET memungkinkan Anda membaca dan mengonversi dokumen PDF ke DOCX menggunakan C# dan bahasa .NET lainnya. DOCX adalah format yang dikenal untuk dokumen Microsoft Word yang strukturnya diubah dari biner murni menjadi kombinasi file XML dan biner. File docx dapat dibuka dengan Word 2007 dan versi lebih baru tetapi tidak dengan versi sebelumnya dari MS Word, yang mendukung ekstensi file DOC.

Potongan kode C# berikut menunjukkan mengonversi file PDF ke format DOCX.

<a name="csharp-pdf-to-docx"><strong>Langkah-langkah: Mengonversi PDF ke DOCX di C#</strong></a>

1.
1.
2. Simpan dalam format **SaveFormat.DocX** dengan memanggil metode **Document.Save()**.

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // Buka dokumen PDF sumber
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Simpan file DOC hasil
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

### Konversi PDF ke DOCX dalam Mode Tingkat Lanjut

Untuk mendapatkan hasil yang lebih baik dari konversi PDF ke DOCX, Anda dapat menggunakan mode `EnhancedFlow`.
Perbedaan utama antara Flow dan Enhanced Flow adalah bahwa tabel (baik dengan dan tanpa batas) dikenali sebagai tabel nyata, bukan sebagai teks dengan gambar di latar belakang.
Ada juga pengenalan daftar bernomor dan banyak hal kecil lainnya.

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{    
    // Buka dokumen PDF sumber
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // Buat objek DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // Tentukan format keluaran sebagai DOCX
        Format = DocSaveOptions.DocFormat.DocX
        // Atur parameter DocSaveOptions lainnya
        Mode = DocSaveOptions.RecognitionMode.EnhancedFlow
    };
    // Simpan dokumen dalam format docx
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```
{{% alert color="warning" %}}
**Cobalah Mengonversi PDF ke DOCX Secara Online**

Aspose.PDF untuk .NET memperkenalkan Anda pada aplikasi gratis online ["PDF ke Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aplikasi Gratis Aspose.PDF Konversi PDF ke Word](/pdf/id/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Lihat Juga

Artikel ini juga membahas topik-topik berikut. Kode-kodenya sama seperti di atas.

_Format_: **Word**

- [Kode C# PDF ke Word](#csharp-pdf-to-docx)
- [API C# PDF ke Word](#csharp-pdf-to-docx)
- [C# PDF ke Word Secara Pemrograman](#csharp-pdf-to-docx)
- [Pustaka C# PDF ke Word](#csharp-pdf-to-docx)
- [C# Simpan PDF sebagai Word](#csharp-pdf-to-docx)
- [C# Hasilkan Word dari PDF](#csharp-pdf-to-docx)
- [C# Buat Word dari PDF](#csharp-pdf-to-docx)
- [Pengonversi C# PDF ke Word](#csharp-pdf-to-docx)

_Format_: **DOC**

- [Kode C# PDF ke DOC](#csharp-pdf-to-doc)
- [API C# PDF ke DOC](#csharp-pdf-to-doc)
- [C# PDF ke DOC API](#csharp-pdf-to-doc)
- [C# PDF ke DOC Secara Pemrograman](#csharp-pdf-to-doc)
- [C# Perpustakaan PDF ke DOC](#csharp-pdf-to-doc)
- [C# Simpan PDF sebagai DOC](#csharp-pdf-to-doc)
- [C# Hasilkan DOC dari PDF](#csharp-pdf-to-doc)
- [C# Buat DOC dari PDF](#csharp-pdf-to-doc)
- [C# Konverter PDF ke DOC](#csharp-pdf-to-doc)

_Format_: **DOCX**

- [C# Kode PDF ke DOCX](#csharp-pdf-to-docx)
- [C# PDF ke DOCX API](#csharp-pdf-to-docx)
- [C# PDF ke DOCX Secara Pemrograman](#csharp-pdf-to-docx)
- [C# Perpustakaan PDF ke DOCX](#csharp-pdf-to-docx)
- [C# Simpan PDF sebagai DOCX](#csharp-pdf-to-docx)
- [C# Hasilkan DOCX dari PDF](#csharp-pdf-to-docx)
- [C# Buat DOCX dari PDF](#csharp-pdf-to-docx)
- [C# Konverter PDF ke DOCX](#csharp-pdf-to-docx)
