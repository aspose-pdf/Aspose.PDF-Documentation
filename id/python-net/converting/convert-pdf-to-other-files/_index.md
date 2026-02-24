---
title: Konversi PDF ke EPUB, LaTeX, Teks, XPS dengan Python
linktitle: Konversi PDF ke format lain
type: docs
weight: 90
url: /id/python-net/convert-pdf-to-other-files/
lastmod: "2025-09-27"
description: Topik ini menunjukkan cara mengonversi file PDF ke format file lain seperti EPUB, LaTeX, Teks, XPS, dll menggunakan Python.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cara Mengonversi PDF ke format lain dengan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang cara mengonversi file PDF ke berbagai format dengan menggunakan Aspose.PDF untuk Python. Artikel ini mencakup konversi PDF ke format EPUB, LaTeX/TeX, Teks, XPS, dan XML. Setiap bagian dimulai dengan ajakan untuk mencoba aplikasi daring gratis yang disediakan oleh Aspose untuk mengonversi PDF ke format masing‑masing, menyoroti kemudahan penggunaan dan kualitas alat‑alat tersebut.
---

## Konversi PDF ke EPUB

{{% alert color="success" %}}
**Coba konversi PDF ke EPUB secara online**

Aspose.PDF untuk Python mempersembahkan aplikasi daring gratis ["PDF ke EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), dimana Anda dapat mencoba memeriksa fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> adalah standar e-book gratis dan terbuka dari International Digital Publishing Forum (IDPF). File memiliki ekstensi .epub.
EPUB dirancang untuk konten yang dapat mengalir ulang, yang berarti pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten berlayout tetap. Format ini dimaksudkan sebagai format tunggal yang dapat digunakan penerbit dan rumah konversi secara internal, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook.

Aspose.PDF untuk Python juga mendukung fitur mengonversi dokumen PDF ke format EPUB. Aspose.PDF untuk Python memiliki kelas bernama 'EpubSaveOptions' yang dapat digunakan sebagai argumen kedua untuk metode [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), untuk menghasilkan file EPUB.
Silakan coba menggunakan cuplikan kode berikut untuk memenuhi kebutuhan ini dengan Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = (
        ap.EpubSaveOptions.RecognitionMode.FLOW
    )
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Konversi PDF ke LaTeX/TeX

**Aspose.PDF untuk Python via .NET** mendukung konversi PDF ke LaTeX/TeX.
Format file LaTeX adalah format file teks dengan markup khusus dan digunakan dalam sistem persiapan dokumen berbasis TeX untuk penataan berkualitas tinggi.

{{% alert color="success" %}}
**Coba konversi PDF ke LaTeX/TeX secara online**

Aspose.PDF untuk Python mempersembahkan aplikasi daring gratis ["PDF ke LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), dimana Anda dapat mencoba memeriksa fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Untuk mengonversi file PDF ke TeX, Aspose.PDF memiliki kelas [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) yang menyediakan properti OutDirectoryPath untuk menyimpan gambar sementara selama proses konversi.

Cuplikan kode berikut menunjukkan proses mengonversi file PDF ke format TEX dengan Python.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.LaTeXSaveOptions()

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## Konversi PDF ke Teks

**Aspose.PDF untuk Python** mendukung konversi seluruh dokumen PDF dan halaman tunggal ke file Teks. Anda dapat mengonversi dokumen PDF ke file TXT menggunakan kelas 'TextDevice'. Cuplikan kode berikut menjelaskan cara mengekstrak teks dari semua halaman.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Coba konversi PDF ke Teks secara online**

Aspose.PDF untuk Python mempersembahkan aplikasi daring gratis ["PDF ke Teks"](https://products.aspose.app/pdf/conversion/pdf-to-txt), dimana Anda dapat mencoba memeriksa fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Konversi PDF ke XPS

**Aspose.PDF untuk Python** memberikan kemungkinan untuk mengonversi file PDF ke format XPS. Mari coba gunakan cuplikan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan Python.

{{% alert color="success" %}}
**Coba konversi PDF ke XPS secara online**

Aspose.PDF untuk Python mempersembahkan aplikasi daring gratis ["PDF ke XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), dimana Anda dapat mencoba memeriksa fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke XPS dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Jenis file XPS terutama terkait dengan XML Paper Specification oleh Microsoft Corporation. XML Paper Specification (XPS), yang sebelumnya diberi nama kode Metro dan mencakup konsep pemasaran Next Generation Print Path (NGPP), merupakan inisiatif Microsoft untuk mengintegrasikan pembuatan dan penampilan dokumen ke dalam sistem operasi Windows.

Untuk mengonversi file PDF ke XPS, Aspose.PDF memiliki kelas [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) yang digunakan sebagai argumen kedua untuk metode [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) guna menghasilkan file XPS.

Cuplikan kode berikut menunjukkan proses mengonversi file PDF ke format XPS.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Mengonversi PDF ke MD

Aspose.PDF memiliki kelas 'MarkdownSaveOptions()', yang mengonversi dokumen PDF menjadi format Markdown (MD) sambil menjaga gambar dan sumber daya.

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat instance dari 'MarkdownSaveOptions'.
1. Atur 'resources_directory_name' ke 'images' – gambar yang diekstrak akan disimpan di folder ini.
1. Simpan dokumen Markdown yang telah dikonversi menggunakan opsi yang dikonfigurasi.
1. Tampilkan pesan konfirmasi setelah konversi.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.MarkdownSaveOptions()
    # save_options.extract_vector_graphics = True
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

File Markdown dengan teks dan gambar tertaut yang disimpan di folder gambar yang ditentukan.

## Mengonversi PDF ke MobiXML

Metode ini mengonversi dokumen PDF ke format MOBI (MobiXML), yang umum digunakan untuk eBook pada perangkat Kindle.

1. Muat dokumen PDF sumber menggunakan 'ap.Document'.
1. Simpan dokumen dengan format 'ap.SaveFormat.MOBI_XML'.
1. Tampilkan pesan konfirmasi setelah konversi selesai.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.save(path_outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
