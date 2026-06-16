---
title: Konversi PDF ke Word di Python
linktitle: Konversi PDF ke Word
type: docs
weight: 10
url: /id/python-net/convert-pdf-to-word/
lastmod: "2026-06-12"
description: Pelajari cara mengkonversi PDF ke Word di Python, termasuk PDF ke DOC, PDF ke DOCX, dan pengenalan tata letak lanjutan dengan Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Konversi PDF ke DOC dan DOCX di Python
Abstract: Artikel ini menunjukkan cara mengkonversi file PDF ke format Microsoft Word dengan Aspose.PDF for Python via .NET. Ini mencakup PDF ke DOC, PDF ke DOCX, dan opsi pengenalan tata letak lanjutan untuk membuat dokumen Word yang dapat diedit dari konten PDF.
---

Halaman ini menunjukkan cara **mengonversi PDF ke Word dalam Python**. Gunakan contoh-contoh ini ketika Anda membutuhkan output DOC atau DOCX yang dapat diedit dari file PDF untuk revisi, penggunaan kembali, atau alur kerja dokumen kantor.

## Konversi PDF ke DOC dengan Python

Salah satu fitur paling populer adalah konversi PDF ke Microsoft Word DOC, yang mempermudah manajemen konten. **Aspose.PDF for Python via .NET** memungkinkan Anda mengonversi file PDF tidak hanya ke DOC tetapi juga ke format DOCX, dengan mudah dan efisien.

Gunakan konversi Word ketika Anda perlu merevisi teks, menggunakan kembali konten dalam alur kerja kantor, atau memindahkan konten PDF ke dalam dokumen DOC atau DOCX yang dapat diedit.

The [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) kelas menyediakan banyak properti yang meningkatkan proses mengonversi file PDF ke format DOC. Di antara properti-properti ini, Mode memungkinkan Anda menentukan mode pengenalan untuk konten PDF. Anda dapat menentukan nilai apa pun dari enumerasi RecognitionMode untuk properti ini. Setiap nilai tersebut memiliki manfaat dan keterbatasan khusus:

Langkah-langkah: Mengonversi PDF ke DOC di Python

1. Muat PDF ke dalam objek 'ap.Document'.
1. Buat instance 'DocSaveOptions'.
1. Atur properti format ke 'DocFormat.DOC' untuk memastikan keluaran dalam format .doc (format Word lama).
1. Simpan PDF sebagai dokumen Word menggunakan opsi penyimpanan yang ditentukan.
1. Cetak pesan konfirmasi.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOC(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba mengonversi PDF ke DOC secara daring**

Aspose.PDF for Python mempersembahkan Anda aplikasi online ["PDF ke DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi PDF ke DOC](/pdf/id/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Konversi PDF ke DOCX dengan Python

Aspose.PDF for Python API memungkinkan Anda membaca dan mengonversi dokumen PDF ke DOCX menggunakan Python via .NET. DOCX adalah format yang dikenal luas untuk dokumen Microsoft Word yang strukturnya diubah dari binary polos menjadi kombinasi file XML dan binary. File Docx dapat dibuka dengan Word 2007 dan versi lainnya tetapi tidak dapat dibuka dengan versi‑versi lebih lama dari MS Word yang mendukung ekstensi file DOC.

Potongan kode Python berikut menunjukkan proses konversi file PDF ke format DOCX.

Langkah: Mengonversi PDF ke DOCX di Python

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat sebuah instance dari 'DocSaveOptions'.
1. Setel properti format ke 'DocFormat.DOC_X' untuk menghasilkan file .docx (format Word modern).
1. Simpan PDF sebagai file DOCX dengan opsi penyimpanan yang telah dikonfigurasi.
1. Cetak pesan konfirmasi setelah konversi.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    document.save(outfile, save_options)
```

## Konversi PDF ke DOCX dengan Pengakuan Tata Letak Lanjutan

Konversi dokumen PDF menjadi file DOCX (Word) menggunakan Python dan Aspose.PDF dengan pengaturan pengenalan lanjutan. Ini menggunakan mode aliran yang ditingkatkan untuk mempertahankan struktur dokumen, sehingga output lebih dapat diedit dan lebih mirip dengan tata letak asli.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_PDF_to_DOCX_advanced(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    save_options.mode = ap.DocSaveOptions.RecognitionMode.ENHANCED_FLOW
    document.save(outfile, save_options)
```

The [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) kelas memiliki properti bernama Format yang menyediakan kemampuan untuk menentukan format dokumen hasil, yaitu DOC atau DOCX. Untuk mengonversi file PDF ke format DOCX, silakan berikan nilai Docx dari enumerasi DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**Coba konversi PDF ke DOCX secara daring**

Aspose.PDF for Python mempersembahkan Anda aplikasi online ["PDF ke Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke Word App](/pdf/id/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Konversi terkait

- [Konversi PDF ke Excel](/pdf/id/python-net/convert-pdf-to-excel/) untuk ekspor berorientasi spreadsheet.
- [Konversi PDF ke PowerPoint](/pdf/id/python-net/convert-pdf-to-powerpoint/) ketika Anda membutuhkan slide presentasi alih-alih output pengolah kata.
- [Konversi PDF ke HTML](/pdf/id/python-net/convert-pdf-to-html/) untuk penerbitan web dan alur kerja konten berbasis peramban.
