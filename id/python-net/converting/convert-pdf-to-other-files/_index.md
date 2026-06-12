---
title: Konversi PDF ke EPUB, Teks, XPS, dan Lainnya di Python
linktitle: Konversi PDF ke format lain
type: docs
weight: 90
url: /id/python-net/convert-pdf-to-other-files/
lastmod: "2026-06-12"
description: Pelajari cara mengonversi file PDF ke EPUB, LaTeX, Markdown, teks, XPS, dan MobiXML di Python dengan Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cara Mengonversi PDF ke format lain di Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengonversi file PDF ke berbagai format menggunakan Aspose.PDF for Python. Panduan ini mencakup konversi PDF ke format EPUB, LaTeX/TeX, Text, XPS, dan XML. Setiap bagian dimulai dengan undangan untuk mencoba aplikasi online yang disediakan oleh Aspose untuk mengonversi PDF ke format masing‑masing, menyoroti kemudahan penggunaan dan kualitas alat‑alat ini.
---

## Konversi PDF ke EPUB

{{% alert color="success" %}}
**Coba mengonversi PDF ke EPUB secara daring**

Aspose.PDF for Python menyajikan aplikasi online kepada Anda ["PDF ke EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi PDF ke EPUB dengan Aplikasi](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> adalah standar e-book gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub.
EPUB dirancang untuk konten yang dapat diatur ulang, yang berarti pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten tata letak tetap. Format ini dimaksudkan sebagai satu format yang dapat digunakan oleh penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Format ini menggantikan standar Open eBook.

Aspose.PDF for Python juga mendukung fitur untuk mengonversi dokumen PDF ke format EPUB. Aspose.PDF for Python memiliki kelas bernama 'EpubSaveOptions' yang dapat digunakan sebagai argumen kedua untuk [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode, untuk menghasilkan file EPUB.
Silakan coba gunakan potongan kode berikut untuk memenuhi persyaratan ini dengan Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_EPUB(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Konversi terkait

- [Konversi PDF ke Word](/pdf/id/python-net/convert-pdf-to-word/) untuk output dokumen kantor yang dapat diedit.
- [Konversi PDF ke HTML](/pdf/id/python-net/convert-pdf-to-html/) untuk output yang berorientasi pada peramban.
- [Ubah PDF menjadi PDF/A, PDF/E, dan PDF/X](/pdf/id/python-net/convert-pdf-to-pdf_x/) untuk alur kerja konversi yang mematuhi standar dan arsip.

## Konversi PDF ke LaTeX/TeX

**Aspose.PDF for Python via .NET** mendukung mengonversi PDF ke LaTeX/TeX.
Format file LaTeX adalah format file teks dengan markup khusus dan digunakan dalam sistem persiapan dokumen berbasis TeX untuk penataan huruf berkualitas tinggi.

{{% alert color="success" %}}
**Coba konversi PDF ke LaTeX/TeX secara online**

Aspose.PDF for Python menyajikan aplikasi online kepada Anda ["PDF ke LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi PDF ke LaTeX/TeX dengan Aplikasi Aspose.PDF](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Untuk mengonversi file PDF ke TeX, Aspose.PDF memiliki kelas [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) yang menyediakan properti OutDirectoryPath untuk menyimpan gambar sementara selama proses konversi.

Cuplikan kode berikut menunjukkan proses mengonversi file PDF ke format TEX dengan Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TeX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Ubah PDF menjadi Teks

**Aspose.PDF for Python** mendukung konversi seluruh dokumen PDF dan halaman tunggal ke file Text. Anda dapat mengonversi dokumen PDF ke file TXT menggunakan kelas 'TextDevice'. Cuplikan kode berikut menjelaskan cara mengekstrak teks dari semua halaman.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TXT(infile, outfile):
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba ubah PDF ke Teks secara online**

Aspose.PDF for Python menyajikan aplikasi online kepada Anda ["PDF ke Teks"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi PDF ke Teks dengan App Aspose.PDF](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Konversi PDF ke XPS

**Aspose.PDF for Python** memberikan kemungkinan untuk mengonversi file PDF ke format XPS. Mari coba menggunakan potongan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan Python.

{{% alert color="success" %}}
**Coba konversi PDF ke XPS secara online**

Aspose.PDF for Python menyajikan aplikasi online kepada Anda ["PDF ke XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi PDF ke XPS dengan Aplikasi](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Jenis file XPS terutama terkait dengan XML Paper Specification oleh Microsoft Corporation. XML Paper Specification (XPS), yang sebelumnya bernama kode Metro dan mencakup konsep pemasaran Next Generation Print Path (NGPP), merupakan inisiatif Microsoft untuk mengintegrasikan pembuatan dan penampilan dokumen ke dalam sistem operasi Windows.

Untuk mengonversi file PDF ke XPS, Aspose.PDF memiliki kelas [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) yang digunakan sebagai argumen kedua untuk [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode untuk menghasilkan file XPS.

Potongan kode berikut menunjukkan proses mengonversi file PDF ke format XPS.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_XPS(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Ubah PDF ke MD

Aspose.PDF memiliki kelas 'MarkdownSaveOptions()', yang mengonversi dokumen PDF ke format Markdown (MD) sambil mempertahankan gambar dan sumber daya.

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat sebuah instance dari 'MarkdownSaveOptions'.
1. Set 'resources_directory_name' ke 'images' – gambar yang diekstrak akan disimpan di folder ini.
1. Simpan dokumen Markdown yang telah dikonversi menggunakan opsi yang telah dikonfigurasi.
1. Cetak pesan konfirmasi setelah konversi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MD(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

File Markdown dengan teks dan gambar yang ditautkan disimpan di folder gambar yang ditentukan.

## Konversi PDF ke MobiXML

Metode ini mengonversi dokumen PDF menjadi format MOBI (MobiXML), yang biasanya digunakan untuk eBook pada perangkat Kindle.

1. Muat dokumen PDF sumber menggunakan 'ap.Document'.
1. Simpan dokumen dengan format 'ap.SaveFormat.MOBI_XML'.
1. Cetak pesan konfirmasi setelah konversi selesai.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MobiXML(infile, outfile):
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
