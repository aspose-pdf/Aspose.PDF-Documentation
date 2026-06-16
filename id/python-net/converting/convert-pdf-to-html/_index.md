---
title: Konversi PDF ke HTML dalam Python
linktitle: Konversi PDF ke format HTML
type: docs
weight: 50
url: /id/python-net/convert-pdf-to-html/
lastmod: "2026-06-12"
description: Pelajari cara mengonversi PDF ke HTML dalam Python dengan Aspose.PDF for Python via .NET, termasuk output multi-halaman, gambar eksternal, penanganan SVG, dan perenderan HTML berlapis.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cara Mengonversi PDF ke HTML dalam Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang mengonversi file PDF ke HTML menggunakan Python, khususnya melalui library Aspose.PDF for Python via .NET. Artikel ini menjabarkan langkah-langkah yang diperlukan untuk melakukan konversi ini secara programatis, menyoroti pembuatan objek `Document` dari PDF sumber dan penggunaan `HtmlSaveOptions` untuk menyimpan dokumen dalam format HTML. Artikel ini menyertakan potongan kode Python yang singkat yang mendemonstrasikan proses konversi. Selain itu, artikel ini memperkenalkan alat daring, aplikasi “PDF to HTML” milik Aspose.PDF, bagi pengguna untuk menjelajahi fungsionalitas dan kualitas konversi. Artikel ini disusun untuk mencakup berbagai topik terkait, memastikan pemahaman menyeluruh tentang penggunaan Python untuk konversi PDF ke HTML.
---

## Konversi PDF ke HTML

**Aspose.PDF for Python via .NET** menyediakan banyak fitur untuk mengonversi berbagai format file menjadi dokumen PDF dan mengonversi file PDF ke berbagai format output. Artikel ini membahas cara mengonversi file PDF menjadi <abbr title="HyperText Markup Language">HTML</abbr>. Anda dapat menggunakan hanya beberapa baris kode Python untuk mengonversi PDF ke HTML. Anda mungkin perlu mengonversi PDF ke HTML jika ingin membuat situs web atau menambahkan konten ke forum online. Salah satu cara mengonversi PDF ke HTML adalah dengan menggunakan Python secara programatis.

{{% alert color="success" %}}
**Coba ubah PDF ke HTML secara daring**

Aspose.PDF for Python menyajikan aplikasi online kepada Anda ["PDF ke HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Konversi PDF ke HTML dengan Aplikasi Aspose.PDF](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Langkah: Mengonversi PDF ke HTML di Python

1. Buat sebuah instance dari [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek dengan dokumen PDF sumber.
1. Simpan ke [HtmlSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlsaveoptions/) dengan memanggil [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Konversi terkait

- [Konversi HTML ke PDF](/pdf/id/python-net/convert-html-to-pdf/) ketika Anda memerlukan alur kerja web-ke-dokumen yang terbalik.
- [Konversi PDF ke Word](/pdf/id/python-net/convert-pdf-to-word/) jika keluaran dokumen yang dapat diedit lebih berguna daripada HTML.
- [Konversi PDF ke format gambar](/pdf/id/python-net/convert-pdf-to-images-format/) untuk skenario ekspor raster.

### Konversi PDF ke HTML dengan menyimpan gambar di folder yang ditentukan

Fungsi ini mengonversi file PDF menjadi format HTML menggunakan Aspose.PDF for Python via .NET. Semua gambar yang diekstrak disimpan di folder yang ditentukan alih-alih disematkan dalam file HTML.

1. Konfigurasikan opsi penyimpanan HTML.
1. Simpan sebagai HTML dengan gambar eksternal.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_images(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "images")
    save_options.special_folder_for_all_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Ubah PDF menjadi HTML multi halaman

Fungsi ini mengonversi file PDF menjadi HTML multi‑halaman, di mana setiap halaman PDF diekspor sebagai file HTML terpisah. Hal ini membuat output lebih mudah dinavigasi dan mengurangi waktu pemuatan untuk PDF berukuran besar.

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan atur `split_into_pages`.
1. Simpan dokumen sebagai HTML dengan halaman dipisah menjadi file terpisah.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_multi_page(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke HTML dengan menyimpan gambar SVG di folder yang ditentukan

Fungsi ini mengonversi PDF menjadi format HTML sambil menyimpan semua gambar sebagai file SVG di folder yang ditentukan, alih-alih menyematkannya langsung di HTML.

1. Muat PDF sumber menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan atur `special_folder_for_svg_images' ke folder target.
1. Simpan dokumen sebagai HTML dengan gambar SVG eksternal.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_storing_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke HTML dan menyimpan gambar SVG terkompresi

Potongan kode ini mengonversi PDF menjadi format HTML, menyimpan semua gambar sebagai file SVG di folder yang ditentukan dan mengompresnya untuk mengurangi ukuran file.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan:
   - Atur 'special_folder_for_svg_images' untuk menyimpan gambar SVG secara eksternal.
   - Aktifkan 'compress_svg_graphics_if_any' untuk mengompres gambar SVG.
1. Simpan dokumen sebagai HTML dengan gambar SVG eksternal yang terkompresi.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_compress_svg(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    images_path = path.join(path.dirname(infile), "svg_images")
    save_options.special_folder_for_svg_images = images_path
    save_options.compress_svg_graphics_if_any = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke HTML dengan kontrol Gambar Raster yang disematkan

Potongan kode ini mengonversi PDF menjadi format HTML, menyematkan gambar raster sebagai latar belakang halaman PNG. Pendekatan ini mempertahankan kualitas gambar dan tata letak halaman dalam HTML.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan 'set raster_images_saving_mode' ke 'AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND'.
1. Simpan dokumen sebagai HTML dengan gambar raster yang disematkan.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_PNG_background(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.raster_images_saving_mode = ap.HtmlSaveOptions.RasterImagesSavingModes.AS_EMBEDDED_PARTS_OF_PNG_PAGE_BACKGROUND
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke halaman HTML yang hanya berisi konten bagian tubuh

Fungsi ini mengonversi PDF ke format HTML, menghasilkan konten 'body-only' tanpa tag 'html' atau 'head' tambahan, dan membagi output menjadi halaman terpisah.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan konfigurasikan:
   - 'html_markup_generation_mode = WRITE_ONLY_BODY_CONTENT' untuk menghasilkan hanya konten 'body'.
   - 'split_into_pages' untuk membuat file HTML terpisah untuk setiap halaman PDF.
1. Simpan dokumen sebagai HTML dengan opsi yang ditentukan.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_body_content(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.html_markup_generation_mode = (
        ap.HtmlSaveOptions.HtmlMarkupGenerationModes.WRITE_ONLY_BODY_CONTENT
    )
    save_options.split_into_pages = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke HTML dengan Rendering Teks Transparan

Fungsi ini mengubah PDF menjadi format HTML, menampilkan semua teks sebagai transparan, termasuk teks yang berbayang, yang menjaga kesetiaan visual sambil memungkinkan penataan fleksibel dalam HTML output.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan konfigurasikan:
    - 'save_transparent_texts' untuk merender teks normal sebagai transparan.
    - 'save_shadowed_texts_as_transparent_texts' untuk merender teks berbayang sebagai transparan.
1. Simpan dokumen sebagai HTML dengan rendering teks transparan.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_transparent_text_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.save_transparent_texts = True
    save_options.save_shadowed_texts_as_transparent_texts = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke HTML dengan Rendering Lapisan Dokumen

Fungsi ini mengkonversi PDF menjadi format HTML, mempertahankan lapisan dokumen dengan mengubah konten yang ditandai menjadi lapisan terpisah dalam HTML output. Ini memungkinkan elemen berlapis (seperti anotasi, latar belakang, dan overlay) dirender dengan akurat.

1. Muat dokumen PDF menggunakan 'ap.Document'.
1. Buat 'HtmlSaveOptions' dan aktifkan 'convert_marked_content_to_layers' untuk mempertahankan lapisan.
1. Simpan dokumen sebagai HTML dengan konten berlapis.
1. Cetak pesan konfirmasi.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_HTML_document_layers_rendering(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.HtmlSaveOptions()
    save_options.convert_marked_content_to_layers = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

