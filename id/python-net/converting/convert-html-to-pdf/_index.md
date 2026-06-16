---
title: Konversi HTML ke PDF di Python
linktitle: Konversi HTML ke file PDF
type: docs
weight: 40
url: /id/python-net/convert-html-to-pdf/
lastmod: "2026-06-12"
description: Pelajari cara mengonversi HTML dan MHTML ke PDF dalam Python dengan Aspose.PDF for Python via .NET, termasuk pengaturan media CSS, Font yang disematkan, dan output Tagged PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Cara mengonversi HTML ke PDF dalam Python dengan Aspose.PDF
Abstract: Artikel ini menjelaskan cara mengonversi file HTML dan MHTML ke PDF menggunakan Aspose.PDF for Python via .NET. Ini mencakup alur kerja dasar HTML-ke-PDF dan menunjukkan cara mengontrol rendering dengan tipe media, prioritas aturan halaman CSS, font yang disematkan, output satu halaman, dan pembuatan struktur logis untuk Tagged PDF yang dapat diakses.
---

## Konversi Python HTML ke PDF

**Aspose.PDF for Python via .NET** memungkinkan Anda mengonversi dokumen HTML yang ada ke PDF dengan opsi rendering yang fleksibel. Anda dapat menyesuaikan secara halus bagaimana output dihasilkan untuk mencocokkan tata letak, gaya, aksesibilitas, dan kebutuhan pengarsipan Anda.

## Konversi HTML ke PDF

Contoh Python berikut menunjukkan alur kerja dasar untuk mengonversi dokumen HTML ke PDF.

1. Buat sebuah instance dari [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) kelas.
1. Inisialisasi a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek dengan file HTML sumber.
1. Simpan dokumen PDF output dengan memanggil `document.save()`.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.page_layout_option = ap.HtmlPageLayoutOption.SCALE_TO_PAGE_WIDTH
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Konversi terkait

- [Konversi PDF ke HTML](/pdf/id/python-net/convert-pdf-to-html/) ketika Anda membutuhkan output siap web dari file PDF yang ada.
- [Konversi format file lain ke PDF](/pdf/id/python-net/convert-other-files-to-pdf/) untuk alur kerja konversi EPUB, XPS, teks, dan PostScript.
- [Konversi gambar ke PDF](/pdf/id/python-net/convert-images-format-to-pdf/) ketika konten sumber Anda berbasis gambar bukan markup HTML.

{{% alert color="success" %}}
**Coba konversi HTML ke PDF secara online**

Aspose mempersembahkan aplikasi online ["HTML ke PDF"](https://products.aspose.app/html/en/conversion/html-to-pdf), di mana Anda dapat menguji kualitas konversi dan output.

[![Konversi HTML ke PDF menggunakan Aspose.PDF](html.png)](https://products.aspose.app/html/en/conversion/html-to-pdf)
{{% /alert %}}

## Konversi HTML ke PDF menggunakan tipe media

Contoh ini menunjukkan cara mengonversi file HTML ke PDF menggunakan opsi rendering khusus.

1. Buat sebuah instance dari [HtmlLoadOptions()](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) kelas.
1. Setel `html_media_type` untuk menerapkan aturan CSS yang ditujukan untuk tata letak layar atau cetak, seperti `HtmlMediaType.SCREEN` atau `HtmlMediaType.PRINT`.
1. Muat HTML ke dalam sebuah `ap.Document` menggunakan opsi pemuatan.
1. Simpan dokumen sebagai PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.html_media_type = ap.HtmlMediaType.SCREEN
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Prioritaskan CSS `@page` aturan selama konversi HTML-ke-PDF

Beberapa dokumen menggunakan [itu `@page` aturan](https://developer.mozilla.org/en-US/docs/Web/CSS/@page) untuk tata letak halaman. Jika gaya tersebut bertentangan dengan pengaturan lain, Anda dapat mengontrol prioritas dengan `is_priority_css_page_rule`.

1. Buat sebuah instance dari [HtmlLoadOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlloadoptions/) kelas.
1. Setel `is_priority_css_page_rule = False` untuk membiarkan gaya lain memiliki prioritas lebih tinggi `@page` aturan.
1. Muat HTML ke dalam sebuah `ap.Document` dengan opsi yang dikonfigurasi.
1. Simpan dokumen sebagai PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
# load_options.is_priority_css_page_rule = False
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Konversi HTML ke PDF dengan font yang tertanam

Contoh ini menunjukkan cara mengonversi file HTML ke PDF sambil menyematkan font. Jika Anda memerlukan PDF output mempertahankan tipografi asli, atur `is_embed_fonts` ke `True`.

1. Buat `HtmlLoadOptions()` untuk mengonfigurasi konversi HTML-ke-PDF.
1. Setel `is_embed_fonts = True` untuk menyematkan font yang digunakan dalam HTML langsung ke PDF.
1. Muat HTML ke dalam sebuah `ap.Document` dengan opsi-opsi ini.
1. Simpan dokumen sebagai PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.HtmlLoadOptions()
load_options.is_embed_fonts = True
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Render konten HTML pada satu halaman PDF

Contoh ini menunjukkan cara mengonversi file HTML menjadi PDF satu halaman menggunakan Aspose.PDF for Python via .NET. Gunakan `is_render_to_single_page` properti ketika Anda ingin seluruh konten HTML dirender pada satu halaman kontinu.

1. Buat sebuah instance dari `HtmlLoadOptions()` untuk mengonfigurasi proses konversi.
1. Aktifkan `is_render_to_single_page` untuk merender seluruh konten HTML pada satu halaman.
1. Muat dokumen dengan opsi yang dikonfigurasi ke dalam sebuah `ap.Document`.
1. Simpan hasil sebagai file PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

options = ap.HtmlLoadOptions()
options.is_render_to_single_page = True

doc = ap.Document(path_infile, options)
doc.save(path_outfile)
```

## Buat struktur logis dari tag HTML

Struktur logis, yang juga disebut tagged PDF, mempertahankan hierarki semantik dari HTML asli, seperti judul, paragraf, dan daftar. Ini membuat PDF yang dihasilkan lebih dapat diakses, dapat dicari, dan cocok untuk alur kerja dokumen terstruktur.

Dengan mengaktifkan struktur logis selama konversi, DOM HTML dipetakan ke dalam pohon tag PDF alih-alih hanya dirender sebagai konten visual.

Untuk memenuhi persyaratan aksesibilitas, sebuah PDF harus menyertakan elemen struktur logis yang menentukan urutan bacaan, memberikan teks alternatif untuk pembaca layar, dan mempertahankan hierarki konten.

> Kualitas struktur logis dalam PDF output bergantung langsung pada kualitas markup HTML asli. HTML yang terstruktur buruk atau tidak valid dapat menghasilkan penandaan yang tidak lengkap atau tidak akurat dalam PDF yang dikonversi.

1. Buat instance HtmlLoadOptions untuk mengontrol bagaimana HTML dikonversi.
1. Aktifkan penandaan semantik sehingga PDF berisi elemen terstruktur.
1. Buka file HTML menggunakan opsi yang dikonfigurasi.
1. Simpan PDF terstruktur.

```python
import aspose.pdf as ap

# Path to the source HTML
input_html_path = "input.html"
# Path for the Logical Structure PDF
output_pdf_path = "output_logical_structure.pdf"
# Initialize HtmlLoadOptions
options = ap.HtmlLoadOptions()
# Convert HTML markup to PDF logical structure elements
options.create_logical_structure = True
# Open PDF document
with ap.Document(input_html_path, options) as document:
    # Save PDF document
    document.save(output_pdf_path)
```

## Konversi MHTML ke PDF

Contoh ini menunjukkan cara mengonversi file MHT atau MHTML menjadi dokumen PDF menggunakan Aspose.PDF for Python via .NET dengan dimensi halaman tertentu.

1. Buat sebuah instance dari `ap.MhtLoadOptions()` untuk mengonfigurasi pemrosesan file MHTML.
1. Atur berbagai parameter, seperti ukuran halaman.
1. Inisialisasi dokumen dengan file input dan opsi pemuatan yang dikonfigurasi.
1. Simpan dokumen hasil sebagai PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
load_options = ap.MhtLoadOptions()
load_options.page_info.width = 842
load_options.page_info.height = 1191
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```
