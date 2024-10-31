---
title: Convert PDF to EPUB, LaTeX, Text, XPS in Python
linktitle: Convert PDF to other formats 
type: docs
weight: 90
url: /python-net/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: convert, PDF, EPUB, LaText, Text, XPS, Python
description: Topik ini menunjukkan cara mengonversi file PDF ke format file lain seperti EPUB, LaTeX, Teks, XPS, dll menggunakan Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Mengonversi PDF ke EPUB

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke EPUB secara online**

Aspose.PDF untuk Python menyajikan aplikasi online gratis ["PDF ke EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Konversi Aspose.PDF PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** adalah standar buku elektronik gratis dan terbuka dari International Digital Publishing Forum (IDPF).
 Files memiliki ekstensi .epub.  
EPUB dirancang untuk konten yang dapat diatur ulang, artinya pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten dengan tata letak tetap. Format ini dimaksudkan sebagai format tunggal yang dapat digunakan penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook.

Aspose.PDF untuk Python juga mendukung fitur untuk mengonversi dokumen PDF ke format EPUB. Aspose.PDF untuk Python memiliki kelas bernama 'EpubSaveOptions' yang dapat digunakan sebagai argumen kedua untuk metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), untuk menghasilkan file EPUB. Silakan coba menggunakan potongan kode berikut untuk memenuhi persyaratan ini dengan Python.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_epub.epub"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # Instansiasi opsi Simpan Epub
    save_options = ap.EpubSaveOptions()

    # Tentukan tata letak untuk konten
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW

    # Simpan dokumen ePUB
    document.save(output_pdf, save_options)
```

## Mengubah PDF ke LaTeX/TeX

**Aspose.PDF untuk Python via .NET** mendukung konversi PDF ke LaTeX/TeX. Format file LaTeX adalah format file teks dengan markup khusus dan digunakan dalam sistem persiapan dokumen berbasis TeX untuk penyusunan berkualitas tinggi.

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke LaTeX/TeX secara online**

Aspose.PDF untuk Python menghadirkan aplikasi gratis online ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsi dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Untuk mengonversi file PDF ke TeX, Aspose.PDF memiliki kelas [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) yang menyediakan properti OutDirectoryPath untuk menyimpan gambar sementara selama proses konversi.

Cuplikan kode berikut menunjukkan proses mengonversi file PDF menjadi format TEX dengan Python.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tex.tex"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)
    # Instansiasi sebuah objek dari LaTeXSaveOptions
    saveOptions = ap.LaTeXSaveOptions()
    document.save(output_pdf, saveOptions)
```

## Mengonversi PDF ke Teks

**Aspose.PDF untuk Python** mendukung konversi seluruh dokumen PDF dan halaman tunggal ke file Teks.

### Mengonversi dokumen PDF ke file Teks

Anda dapat mengonversi dokumen PDF ke file TXT menggunakan kelas 'TextDevice'.

Cuplikan kode berikut menjelaskan cara mengekstrak teks dari semua halaman.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # Buat perangkat Teks
    textDevice = ap.devices.TextDevice()

    # Mengonversi halaman tertentu dan simpan
    textDevice.process(document.pages[1], output_pdf)

**Coba ubah Convert PDF ke Teks secara online**

Aspose.PDF untuk Python mempersembahkan kepada Anda aplikasi online gratis ["PDF ke Teks"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Ubah PDF ke XPS

**Aspose.PDF untuk Python** memberikan kemungkinan untuk mengonversi file PDF ke format <abbr title="XML Paper Specification">XPS</abbr>. Mari coba gunakan potongan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan Python.

{{% alert color="success" %}}
**Coba ubah PDF ke XPS secara online**

Aspose.PDF untuk Python mempersembahkan kepada Anda aplikasi online gratis ["PDF ke XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke XPS dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Jenis file XPS terutama diasosiasikan dengan XML Paper Specification oleh Microsoft Corporation. XML Paper Specification (XPS), yang sebelumnya diberi nama kode Metro dan mencakup konsep pemasaran Next Generation Print Path (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan penayangan dokumen ke dalam sistem operasi Windows.

Untuk mengonversi file PDF ke XPS, Aspose.PDF memiliki kelas [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) yang digunakan sebagai argumen kedua untuk metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) untuk menghasilkan file XPS.

Cuplikan kode berikut menunjukkan proses konversi file PDF ke format XPS.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xps.xps"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    # Memulai opsi simpan XPS
    save_options = ap.XpsSaveOptions()

    # Simpan dokumen XPS
    document.save(output_pdf, save_options)
```

## Mengonversi PDF ke XML

{{% alert color="success" %}}
**Cobalah mengonversi PDF ke XML secara online**

Aspose.PDF untuk Python menghadirkan aplikasi gratis online ["PDF to XML"](https://products.aspose.app/pdf/conversion/pdf-to-xml), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke XML dengan Aplikasi Gratis](pdf_to_xml.png)](https://products.aspose.app/pdf/conversion/pdf-to-xml)
{{% /alert %}}

<abbr title="Extensible Markup Language">XML</abbr> adalah bahasa markup dan format file untuk menyimpan, mentransmisikan, dan merekonstruksi data sembarang.

Aspose.PDF untuk Python juga mendukung fitur untuk mengonversi dokumen PDF ke format XML. Aspose.PDF untuk Python memiliki kelas bernama 'XmlSaveOptions' yang dapat digunakan sebagai argumen kedua untuk metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), untuk menghasilkan file XML.
Silakan coba gunakan potongan kode berikut untuk memenuhi persyaratan ini dengan Python.

```python

    import aspose.pdf as ap

    def convert_pdf_to_xml(self, infile, outfile):
        path_infile = self.dataDir + infile
        path_outfile = self.dataDir + outfile

        # Buka dokumen PDF

        document = ap.Document(path_infile)

        # Instansiasi opsi Simpan XML
        save_options = ap.XmlSaveOptions()

        # Simpan dokumen XML
        document.save(path_outfile, save_options)
        print(infile + " dikonversi menjadi " + outfile)
```