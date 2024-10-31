---
title: Mengonversi PDF ke Dokumen Microsoft Word dalam Python
linktitle: Mengonversi PDF ke Word 2003/2019
type: docs
weight: 10
url: /python-java/convert-pdf-to-word/
lastmod: "2023-04-06"
description: Pelajari cara menulis kode Python untuk konversi format PDF ke Microsoft Word dengan Aspose.PDF untuk Python via .NET. dan tingkatkan konversi PDF ke DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Gambaran Umum

Artikel ini menjelaskan cara **mengonversi PDF ke Dokumen Microsoft Word menggunakan Python**. Ini mencakup topik-topik berikut.

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

## Konversi PDF ke DOC dan DOCX Python

Salah satu fitur paling populer adalah konversi PDF ke Microsoft Word DOC, yang memudahkan pengelolaan konten. **Aspose.PDF untuk Python** memungkinkan Anda mengkonversi file PDF tidak hanya ke DOC tetapi juga ke format DOCX, dengan mudah dan efisien.

## Konversi PDF ke file DOC (Word 97-2003)

Konversi file PDF ke format DOC dengan mudah dan kontrol penuh. Aspose.PDF untuk Python adalah fleksibel dan mendukung berbagai macam konversi. Mengonversi halaman dari dokumen PDF ke gambar, misalnya, adalah fitur yang sangat populer.

Salah satu konversi yang banyak diminta oleh pelanggan kami adalah PDF ke DOC: mengonversi file PDF ke dokumen Microsoft Word. Pelanggan menginginkan ini karena file PDF tidak dapat dengan mudah diedit, sedangkan dokumen Word dapat. Beberapa perusahaan menginginkan agar pengguna mereka dapat memanipulasi teks, tabel, dan gambar dalam file yang dimulai sebagai PDF.

Menjaga tradisi membuat segala sesuatu menjadi sederhana dan dapat dipahami, Aspose.PDF untuk Python memungkinkan Anda mengubah file PDF sumber menjadi file DOC dengan dua baris kode.
 Untuk menyelesaikan fitur ini, kami telah memperkenalkan enumerasi bernama SaveFormat dan nilainya .Doc memungkinkan Anda menyimpan file sumber ke format Microsoft Word.

Cuplikan kode Python berikut menunjukkan proses mengonversi file PDF ke format DOC.

<a name="csharp-pdf-to-doc"><strong>Langkah-langkah: Mengonversi PDF ke DOC dalam Python</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Simpan ke format [SaveFormat.Doc](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) dengan memanggil metode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python

from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/out.doc"
doc.save(documentOutName, Api.SaveFormat.Doc)
```

### Menggunakan Kelas DocSaveOptions

Kelas [DocSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/docsaveoptions/) menyediakan berbagai properti yang meningkatkan proses konversi file PDF ke format DOC. Di antara properti ini, Mode memungkinkan Anda untuk menentukan mode pengenalan untuk konten PDF. Anda dapat menentukan nilai apa pun dari enumerasi RecognitionMode untuk properti ini. Masing-masing nilai ini memiliki manfaat dan keterbatasan spesifik:

```python

from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
# Buka dokumen PDF
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Doc
# Atur mode pengenalan sebagai Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# Atur kedekatan Horizontal sebagai 2.5
save_options.relative_horizontal_proximity = 2.5
# Aktifkan nilai untuk mengenali bullet selama proses konversi
save_options.recognize_bullets = True

# Simpan file ke format dokumen MS Word
document.save(output_pdf, save_options)

```

{{% alert color="success" %}}
**Coba konversi PDF ke DOC online**

Aspose.PDF untuk Python menyajikan aplikasi gratis online ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.
[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## Mengkonversi PDF ke DOCX

Aspose.PDF untuk API Python memungkinkan Anda membaca dan mengkonversi dokumen PDF ke DOCX menggunakan Python via .NET. DOCX adalah format yang terkenal untuk dokumen Microsoft Word yang strukturnya diubah dari biner biasa menjadi kombinasi file XML dan biner. File Docx dapat dibuka dengan Word 2007 dan versi lateral tetapi tidak dengan versi MS Word sebelumnya yang mendukung ekstensi file DOC.

Cuplikan kode Python berikut menunjukkan proses mengkonversi file PDF menjadi format DOCX.

<a name="csharp-pdf-to-docx"><strong>Langkah-langkah: Mengkonversi PDF ke DOCX dalam Python</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) dengan dokumen PDF sumber.

2. Simpan ke format [SaveFormat.DocX](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) dengan memanggil metode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.docx"
# Buka dokumen PDF
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Docx
# Atur mode pengenalan sebagai Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# Atur kedekatan horizontal sebagai 2.5
save_options.relative_horizontal_proximity = 2.5
# Aktifkan nilai untuk mengenali bullet selama proses konversi
save_options.recognize_bullets = True

# Simpan file ke dalam format dokumen MS Word
document.save(output_pdf, save_options)
```

Kelas [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) memiliki properti bernama Format yang menyediakan kemampuan untuk menentukan format dokumen hasil, yaitu, DOC atau DOCX.
 Untuk mengonversi file PDF ke format DOCX, silakan gunakan nilai Docx dari enumerasi DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Cobalah mengonversi PDF ke DOCX secara online**

Aspose.PDF untuk Python menyajikan aplikasi gratis online ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aplikasi Gratis Aspose.PDF Konversi PDF ke Word](/pdf/java/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Lihat Juga

Artikel ini juga mencakup topik-topik ini. Kodenya sama seperti di atas.

_Format_: **Word**
- [Python PDF ke Kode Word](#python-pdf-to-docx)
- [Python PDF ke API Word](#python-pdf-to-docx)
- [Python PDF ke Word Secara Programatis](#python-pdf-to-docx)
- [Python PDF ke Perpustakaan Word](#python-pdf-to-docx)
- [Python Simpan PDF sebagai Word](#python-pdf-to-docx)
- [Python Hasilkan Word dari PDF](#python-pdf-to-docx)
- [Python Buat Word dari PDF](#python-pdf-to-docx)

- [Python PDF ke Konverter Word](#python-pdf-to-docx)
_Format_: **DOC**
- [Kode Python PDF ke DOC](#python-pdf-to-doc)
- [API Python PDF ke DOC](#python-pdf-to-doc)
- [Python PDF ke DOC Secara Program](#python-pdf-to-doc)
- [Perpustakaan Python PDF ke DOC](#python-pdf-to-doc)
- [Python Simpan PDF sebagai DOC](#python-pdf-to-doc)
- [Python Menghasilkan DOC dari PDF](#python-pdf-to-doc)
- [Python Membuat DOC dari PDF](#python-pdf-to-doc)
- [Pengonversi PDF ke DOC Python](#python-pdf-to-doc)

_Format_: **DOCX**
- [Kode Python PDF ke DOCX](#python-pdf-to-docx)
- [API Python PDF ke DOCX](#python-pdf-to-docx)
- [Python PDF ke DOCX Secara Program](#python-pdf-to-docx)
- [Perpustakaan Python PDF ke DOCX](#python-pdf-to-docx)
- [Python Simpan PDF sebagai DOCX](#python-pdf-to-docx)
- [Python Menghasilkan DOCX dari PDF](#python-pdf-to-docx)
- [Python Membuat DOCX dari PDF](#python-pdf-to-docx)
- [Pengonversi PDF ke DOCX Python](#python-pdf-to-docx)