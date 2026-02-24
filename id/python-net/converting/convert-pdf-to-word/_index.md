---
title: Konversi PDF ke Dokumen Microsoft Word dalam Python
linktitle: Konversi PDF ke Word
type: docs
weight: 10
url: /id/python-net/convert-pdf-to-word/
lastmod: "2025-09-27"
description: Pelajari cara mengonversi dokumen PDF ke format Word dalam Python menggunakan Aspose.PDF untuk pengeditan dokumen yang mudah.
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengonversi PDF ke Word dalam Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengonversi file PDF ke format Microsoft Word (DOC dan DOCX) menggunakan Python, khususnya dengan memanfaatkan pustaka Aspose.PDF. Artikel ini menjelaskan keuntungan mengonversi PDF ke dokumen Word yang dapat diedit, memungkinkan manipulasi konten yang lebih mudah seperti teks, tabel, dan gambar. Artikel ini merinci proses mengonversi PDF ke DOC (format Word 97-2003) dan DOCX, dengan cuplikan kode yang menunjukkan konversi ini melalui Python. Prosesnya melibatkan pembuatan objek `Document` dari PDF dan menyimpannya dalam format yang diinginkan menggunakan metode `save()` dan enumerasi `SaveFormat`. Selain itu, diperkenalkan kelas `DocSaveOptions`, yang memungkinkan penyesuaian lebih lanjut pada proses konversi, seperti menentukan mode pengenalan. Artikel ini juga menyoroti aplikasi online yang disediakan oleh Aspose.PDF untuk menguji kualitas dan fungsi konversi. Konten mencakup ikhtisar terstruktur dan tautan ke bagian masing-masing format.
---

## Konversi PDF ke DOC

Salah satu fitur paling populer adalah konversi PDF ke Microsoft Word DOC, yang mempermudah manajemen konten. **Aspose.PDF untuk Python via .NET** memungkinkan Anda mengonversi file PDF tidak hanya ke DOC tetapi juga ke format DOCX, dengan mudah dan efisien.

Kelas [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) menyediakan banyak properti yang memperbaiki proses mengonversi file PDF ke format DOC. Di antara properti ini, Mode memungkinkan Anda menentukan mode pengenalan untuk konten PDF. Anda dapat menentukan nilai apa saja dari enumerasi RecognitionMode untuk properti ini. Setiap nilai tersebut memiliki manfaat dan keterbatasan spesifik:

Langkah-langkah: Konversi PDF ke DOC dalam Python

1. Muat PDF ke dalam objek 'ap.Document'.
1. Buat instance 'DocSaveOptions'.
1. Atur properti format menjadi 'DocFormat.DOC' untuk memastikan output dalam format .doc (format Word lama).
1. Simpan PDF sebagai dokumen Word menggunakan opsi penyimpanan yang ditentukan.
1. Tampilkan pesan konfirmasi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi PDF ke DOC secara online**

Aspose.PDF untuk Python menyediakan aplikasi gratis online ["PDF ke DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba meneliti fungsi dan kualitasnya.

[![Konversi PDF ke DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Konversi PDF ke DOCX

API Aspose.PDF untuk Python memungkinkan Anda membaca dan mengonversi dokumen PDF ke DOCX menggunakan Python via .NET. DOCX adalah format yang dikenal untuk dokumen Microsoft Word yang strukturnya berubah dari biner sederhana menjadi kombinasi file XML dan biner. File DOCX dapat dibuka dengan Word 2007 dan versi selanjutnya, tetapi tidak dapat dibuka dengan versi MS Word yang lebih lama yang hanya mendukung ekstensi file DOC.

Potongan kode Python berikut menunjukkan proses mengonversi file PDF ke format DOCX.

Langkah-langkah: Konversi PDF ke DOCX dalam Python

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat instance 'DocSaveOptions'.
1. Atur properti format menjadi 'DocFormat.DOC_X' untuk menghasilkan file .docx (format Word modern).
1. Simpan PDF sebagai file DOCX dengan opsi penyimpanan yang telah dikonfigurasi.
1. Tampilkan pesan konfirmasi setelah konversi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC_X
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

Kelas [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) memiliki properti bernama Format yang memberikan kemampuan untuk menentukan format dokumen hasil, yaitu DOC atau DOCX. Untuk mengonversi file PDF ke format DOCX, silakan berikan nilai Docx dari enumerasi DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Coba konversi PDF ke DOCX secara online**

Aspose.PDF untuk Python menyediakan aplikasi gratis online ["PDF ke Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba meneliti fungsi dan kualitasnya.

[![Aplikasi Gratis Konversi PDF ke Word Aspose.PDF](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

