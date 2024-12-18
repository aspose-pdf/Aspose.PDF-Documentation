---
title: Mengonversi PDF ke Dokumen Microsoft Word dalam Python
linktitle: Mengonversi PDF ke Word 2003/2019
type: docs
weight: 10
url: /id/python-net/convert-pdf-to-word/
lastmod: "2022-12-23"
description: Pelajari cara menulis kode Python untuk konversi format PDF ke Microsoft Word dengan Aspose.PDF untuk Python via .NET dan menyetel konversi PDF ke DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ikhtisar

Artikel ini menjelaskan bagaimana **mengonversi PDF ke Dokumen Microsoft Word menggunakan Python**. Artikel ini mencakup topik-topik berikut.

_Format_: **DOC**
- [Python PDF ke DOC](#python-pdf-to-doc)
- [Python Mengonversi PDF ke DOC](#python-pdf-to-doc)
- [Python Cara mengonversi file PDF ke DOC](#python-pdf-to-doc)

_Format_: **DOCX**
- [Python PDF ke DOCX](#python-pdf-to-docx)
- [Python Mengonversi PDF ke DOCX](#python-pdf-to-docx)
- [Python Cara mengonversi file PDF ke DOCX](#python-pdf-to-docx)

_Format_: **Word**
- [Python PDF ke Word](#python-pdf-to-docx)
- [Python Mengonversi PDF ke Word](#python-pdf-to-doc)
- [Python Cara mengonversi file PDF ke Word](#python-pdf-to-docx)

## Konversi PDF ke DOC dan DOCX dengan Python

Salah satu fitur paling populer adalah konversi PDF ke Microsoft Word DOC, yang memudahkan pengelolaan konten. **Aspose.PDF untuk Python** memungkinkan Anda mengkonversi file PDF tidak hanya ke DOC tetapi juga ke format DOCX, dengan mudah dan efisien.

## Konversi PDF ke file DOC (Word 97-2003)

Konversi file PDF ke format DOC dengan mudah dan kendali penuh. Aspose.PDF untuk Python fleksibel dan mendukung berbagai macam konversi. Konversi halaman dari dokumen PDF ke gambar, misalnya, adalah fitur yang sangat populer.

Sebuah konversi yang banyak diminta oleh pelanggan kami adalah PDF ke DOC: mengkonversi file PDF menjadi dokumen Microsoft Word. Pelanggan menginginkan ini karena file PDF tidak dapat dengan mudah diedit, sedangkan dokumen Word dapat. Beberapa perusahaan ingin pengguna mereka dapat memanipulasi teks, tabel, dan gambar dalam file yang awalnya berupa PDF.

Menjaga tradisi membuat segala sesuatu menjadi sederhana dan mudah dimengerti, Aspose.PDF untuk Python memungkinkan Anda mengubah file PDF sumber menjadi file DOC dengan dua baris kode.
 Untuk mencapai fitur ini, kami telah memperkenalkan enumerasi bernama SaveFormat dan nilainya .Doc memungkinkan Anda menyimpan file sumber ke format Microsoft Word.

Cuplikan kode Python berikut menunjukkan proses mengonversi file PDF menjadi format DOC.

<a name="csharp-pdf-to-doc"><strong>Langkah-langkah: Konversi PDF ke DOC dalam Python</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Simpan ke format [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) dengan memanggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)
    # Simpan file ke dalam format dokumen MS Word
    document.save(output_pdf, ap.SaveFormat.DOC)
```

### Menggunakan Kelas DocSaveOptions

Kelas [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) menyediakan banyak properti yang meningkatkan proses konversi file PDF ke format DOC. Di antara properti-properti ini, Mode memungkinkan Anda untuk menentukan mode pengenalan untuk konten PDF. Anda dapat menentukan nilai apa pun dari enumerasi RecognitionMode untuk properti ini. Masing-masing nilai ini memiliki manfaat dan keterbatasan tertentu:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    # Atur mode pengenalan sebagai Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Atur kedekatan horizontal sebagai 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Aktifkan nilai untuk mengenali bullet selama proses konversi
    save_options.recognize_bullets = True

    # Simpan file ke dalam format dokumen MS Word
    document.save(output_pdf, save_options)
```

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke DOC secara online**


Aspose.PDF untuk Python mempersembahkan aplikasi online gratis ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.
[![Convert PDF to DOC](/pdf/id/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## Konversi PDF ke DOCX

Aspose.PDF untuk Python API memungkinkan Anda membaca dan mengonversi dokumen PDF ke DOCX menggunakan Python via .NET. DOCX adalah format terkenal untuk dokumen Microsoft Word yang strukturnya diubah dari biner biasa menjadi kombinasi file XML dan biner. File DOCX dapat dibuka dengan Word 2007 dan versi lateral tetapi tidak dengan versi MS Word sebelumnya yang mendukung ekstensi file DOC.

Cuplikan kode Python berikut menunjukkan proses konversi file PDF menjadi format DOCX.

<a name="csharp-pdf-to-docx"><strong>Langkah-langkah: Konversi PDF ke DOCX dalam Python</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.

2. Simpan ke format [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) dengan memanggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_docx_options.docx"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    # Atur mode pengenalan sebagai Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # Atur kedekatan horizontal sebagai 2.5
    save_options.relative_horizontal_proximity = 2.5
    # Aktifkan nilai untuk mengenali peluru selama proses konversi
    save_options.recognize_bullets = True

    # Simpan file ke dalam format dokumen MS Word
    document.save(output_pdf, save_options)
```

Kelas [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) memiliki properti bernama Format yang menyediakan kemampuan untuk menentukan format dokumen hasil, yaitu DOC atau DOCX.
 Untuk mengonversi file PDF ke format DOCX, harap lewati nilai Docx dari enumerasi DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Cobalah mengonversi PDF ke DOCX secara online**

Aspose.PDF untuk Python menghadirkan aplikasi online gratis ["PDF ke Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aplikasi Gratis Konversi Aspose.PDF PDF ke Word](/pdf/id/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Lihat Juga 

Artikel ini juga mencakup topik-topik ini. Kode-kodenya sama seperti di atas.

_Format_: **Word**
- [Kode Python PDF ke Word](#python-pdf-to-docx)
- [API Python PDF ke Word](#python-pdf-to-docx)
- [Python PDF ke Word Secara Program](#python-pdf-to-docx)
- [Perpustakaan Python PDF ke Word](#python-pdf-to-docx)
- [Python Simpan PDF sebagai Word](#python-pdf-to-docx)
- [Python Hasilkan Word dari PDF](#python-pdf-to-docx)
- [Python Buat Word dari PDF](#python-pdf-to-docx)

- [Pengonversi Python PDF ke Word](#python-pdf-to-docx)
_Format_: **DOC**
- [Kode Python PDF ke DOC](#python-pdf-to-doc)
- [API Python PDF ke DOC](#python-pdf-to-doc)
- [Programatis Python PDF ke DOC](#python-pdf-to-doc)
- [Pustaka Python PDF ke DOC](#python-pdf-to-doc)
- [Simpan PDF sebagai DOC dengan Python](#python-pdf-to-doc)
- [Hasilkan DOC dari PDF dengan Python](#python-pdf-to-doc)
- [Buat DOC dari PDF dengan Python](#python-pdf-to-doc)
- [Pengonversi PDF ke DOC dengan Python](#python-pdf-to-doc)

_Format_: **DOCX**
- [Kode Python PDF ke DOCX](#python-pdf-to-docx)
- [API Python PDF ke DOCX](#python-pdf-to-docx)
- [Programatis Python PDF ke DOCX](#python-pdf-to-docx)
- [Pustaka Python PDF ke DOCX](#python-pdf-to-docx)
- [Simpan PDF sebagai DOCX dengan Python](#python-pdf-to-docx)
- [Hasilkan DOCX dari PDF dengan Python](#python-pdf-to-docx)
- [Buat DOCX dari PDF dengan Python](#python-pdf-to-docx)
- [Pengonversi PDF ke DOCX dengan Python](#python-pdf-to-docx)