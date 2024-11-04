---
title: Convert PDF to Microsoft Word Documents in C++
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /cpp/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Aspose.PDF for C++ library memungkinkan Anda untuk mengonversi PDF ke format Word menggunakan C++ dengan mudah dan kontrol penuh. Format-format ini termasuk DOC dan DOCX. Pelajari lebih lanjut bagaimana menyesuaikan konversi dokumen PDF ke Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Overview

Artikel ini menjelaskan cara mengonversi PDF ke Dokumen Microsoft Word menggunakan C++. Ini mencakup topik-topik berikut.

_Format_: **DOC**
- [C++ PDF ke DOC](#cpp-pdf-to-doc)
- [C++ Konversi PDF ke DOC](#cpp-pdf-to-doc)
- [C++ Cara mengonversi file PDF ke DOC](#cpp-pdf-to-doc)

_Format_: **DOCX**
- [C++ PDF ke DOCX](#cpp-pdf-to-docx)
- [C++ Konversi PDF ke DOCX](#cpp-pdf-to-docx)
- [C++ Cara mengonversi file PDF ke DOCX](#cpp-pdf-to-docx)

_Format_: **Format Microsoft Word DOC**
- [C++ PDF ke Word](#cpp-pdf-to-word-doc)
- [C++ Konversi PDF ke Word](#cpp-pdf-to-word-doc)
- [C++ Cara mengonversi file PDF ke Word](#cpp-pdf-to-word-doc)

_Format_: **Format Microsoft Word DOCX**
- [C++ PDF ke Word](#cpp-pdf-to-word-docx)
- [C++ Konversi PDF ke Word](#cpp-pdf-to-word-docx)
- [C++ Cara mengonversi file PDF ke Word](#cpp-pdf-to-word-docx)

Topik lain yang dibahas dalam artikel ini
- [Lihat Juga](#see-also)

## Konversi PDF ke Word C++

Salah satu fitur paling populer adalah konversi PDF ke Microsoft Word DOC, yang membuat konten mudah untuk dimanipulasi. Aspose.PDF untuk C++ memungkinkan Anda mengonversi file PDF ke DOC.

## Mengonversi file PDF ke DOC (Word 97-2003)

Mengonversi file PDF ke format DOC dengan mudah dan kontrol penuh. Aspose.PDF untuk C++ fleksibel dan mendukung berbagai macam konversi. Mengonversi halaman dari dokumen PDF ke gambar, misalnya, adalah fitur yang sangat populer.

Sebuah konversi yang banyak diminta oleh pelanggan kami adalah PDF ke DOC: mengonversi file PDF ke dokumen Microsoft Word. 
Pelanggan menginginkan ini karena file PDF tidak dapat dengan mudah diedit, sedangkan dokumen Word dapat. Beberapa perusahaan ingin pengguna mereka dapat memanipulasi teks, tabel, dan gambar dalam file yang dimulai sebagai PDF.

Menjaga tradisi membuat sesuatu yang sederhana dan dapat dimengerti, Aspose.PDF untuk C++ memungkinkan Anda mengubah file PDF sumber menjadi file DOC dengan dua baris kode. Untuk mencapai fitur ini, kami telah memperkenalkan enumerasi bernama SaveFormat dan nilainya .Doc memungkinkan Anda menyimpan file sumber ke format Microsoft Word.

Cuplikan kode C++ berikut menunjukkan proses konversi file PDF ke format DOC.

<a name="cpp-pdf-to-doc" id="cpp-pdf-to-doc"><strong>Langkah-langkah: Mengonversi PDF ke DOC di C++</strong></a> | <a name="cpp-pdf-to-word-doc" id="cpp-pdf-to-word-doc"><strong>Langkah-langkah: Mengonversi PDF ke format Microsoft Word DOC di C++</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan dokumen PDF sumber.
2.
``` Simpan ke format **SaveFormat::Doc** dengan memanggil metode **Document->Save()**.

```cpp
void ConvertPDFtoWord()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Simpan file ke dalam format dokumen MS
        document->Save(_dataDir + outfilename, SaveFormat::Doc);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Selesai" << std::endl;
}
```

Cuplikan kode berikut menunjukkan proses mengubah file PDF menjadi versi DOC Lanjutan:

```cpp
void ConvertPDFtoWordDocAdvanced()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.doc");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::Doc);
    // Atur mode pengenalan sebagai Flow
    saveOptions->set_Mode(DocSaveOptions::RecognitionMode::Flow);
    // Atur kedekatan Horizontal sebagai 2.5
    saveOptions->set_RelativeHorizontalProximity(2.5f);
    // Aktifkan nilai untuk mengenali bullet selama proses konversi
    saveOptions->set_RecognizeBullets(true);

    try {
        // Simpan file ke dalam format dokumen MS
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Selesai" << std::endl;
}
```
{{% alert color="success" %}}
**Cobalah mengonversi PDF ke DOC secara online**

Aspose.PDF untuk C++ menghadirkan aplikasi online gratis ["PDF ke DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi PDF ke DOC](pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Konversi PDF ke DOCX

Aspose.PDF untuk API C++ memungkinkan Anda membaca dan mengonversi dokumen PDF ke DOCX menggunakan bahasa C++. DOCX adalah format terkenal untuk dokumen Microsoft Word yang strukturnya diubah dari biner biasa menjadi kombinasi file XML dan biner. File Docx dapat dibuka dengan Word 2007 dan versi lateral tetapi tidak dengan versi MS Word sebelumnya yang mendukung ekstensi file DOC.

Cuplikan kode C++ berikut menunjukkan proses mengonversi file PDF ke format DOCX.


<a name="cpp-pdf-to-docx" id="cpp-pdf-to-docx"><strong>Langkah-langkah: Konversi PDF ke DOCX dalam C++</strong></a> | <a name="cpp-pdf-to-word-docx" id="cpp-pdf-to-word-docx"><strong>Langkah-langkah: Konversi PDF ke format Microsoft Word DOCX dalam C++</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan dokumen PDF sumber.
2. Simpan ke format **SaveFormat::DocX** dengan memanggil metode **Document->Save()**.

```cpp
void ConvertPDFtoWord_DOCX_Format()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
        // Simpan file ke dalam format dokumen MS
        document->Save(_dataDir + outfilename, SaveFormat::DocX);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Finish" << std::endl;
}
```

Kelas [`DocSaveOptions`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) memiliki properti bernama Format yang menyediakan kemampuan untuk menentukan format dokumen hasil, yaitu, DOC atau DOCX. Untuk mengkonversi file PDF ke format DOCX, silakan gunakan nilai Docx dari enumerasi DocSaveOptions.DocFormat.

Silakan lihat potongan kode berikut yang menyediakan kemampuan untuk mengkonversi file PDF ke format DOCX dengan C++.

```cpp
void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToDOC.docx");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto saveOptions = MakeObject<DocSaveOptions>();
    saveOptions->set_Format(DocSaveOptions::DocFormat::DocX);

    // Setel parameter DocSaveOptions lainnya
    // ...

    // Simpan file ke dalam format dokumen MS

    try {
        // Simpan file ke dalam format dokumen MS
        document->Save(_dataDir + outfilename, saveOptions);
    }
    catch (Exception ex) {
        std::cerr << ex->get_Message();
    }

    std::clog << __func__ << ": Selesai" << std::endl;
}
```
{{% alert color="warning" %}}
**Coba untuk mengonversi PDF ke DOCX secara online**

Aspose.PDF untuk C++ menghadirkan aplikasi gratis online ["PDF ke DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aplikasi Gratis Aspose.PDF Konversi PDF ke Word](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Lihat Juga

Artikel ini juga mencakup topik-topik ini. Kode-kodenya sama seperti di atas.

_Format_: **Format Microsoft Word DOC**
- [Kode C++ PDF ke Word](#cpp-pdf-to-word-doc)
- [API C++ PDF ke Word](#cpp-pdf-to-word-doc)
- [C++ PDF ke Word Secara Program](#cpp-pdf-to-word-doc)
- [Perpustakaan C++ PDF ke Word](#cpp-pdf-to-word-doc)
- [C++ Simpan PDF sebagai Word](#cpp-pdf-to-word-doc)
- [C++ Hasilkan Word dari PDF](#cpp-pdf-to-word-doc)
- [C++ Buat Word dari PDF](#cpp-pdf-to-word-doc)
- [Konverter C++ PDF ke Word](#cpp-pdf-to-word-doc)

_Format_: **Format Microsoft Word DOCX**

- [Kode C++ PDF ke Word](#cpp-pdf-to-word-docx)
- [C++ PDF ke Word API](#cpp-pdf-to-word-docx)
- [C++ PDF ke Word Secara Programatik](#cpp-pdf-to-word-docx)
- [C++ PDF ke Word Library](#cpp-pdf-to-word-docx)
- [C++ Simpan PDF sebagai Word](#cpp-pdf-to-word-docx)
- [C++ Hasilkan Word dari PDF](#cpp-pdf-to-word-docx)
- [C++ Buat Word dari PDF](#cpp-pdf-to-word-docx)
- [C++ PDF ke Word Converter](#cpp-pdf-to-word-docx)

_Format_: **DOC**
- [C++ PDF ke DOC Code](#cpp-pdf-to-doc)
- [C++ PDF ke DOC API](#cpp-pdf-to-doc)
- [C++ PDF ke DOC Secara Programatik](#cpp-pdf-to-doc)
- [C++ PDF ke DOC Library](#cpp-pdf-to-doc)
- [C++ Simpan PDF sebagai DOC](#cpp-pdf-to-doc)
- [C++ Hasilkan DOC dari PDF](#cpp-pdf-to-doc)
- [C++ Buat DOC dari PDF](#cpp-pdf-to-doc)
- [C++ PDF ke DOC Converter](#cpp-pdf-to-doc)

_Format_: **DOC**
- [C++ PDF ke DOCX Code](#cpp-pdf-to-docx)
- [C++ PDF ke DOCX API](#cpp-pdf-to-docx)
- [C++ PDF ke DOCX Secara Programatik](#cpp-pdf-to-docx)
- [C++ PDF ke DOCX Library](#cpp-pdf-to-docx)
- [C++ Simpan PDF sebagai DOCX](#cpp-pdf-to-docx)

- [C++ Hasilkan DOCX dari PDF](#cpp-pdf-to-docx)

- [C++ Membuat DOCX dari PDF](#cpp-pdf-to-docx)
- [C++ Pengonversi PDF ke DOCX](#cpp-pdf-to-docx)
```