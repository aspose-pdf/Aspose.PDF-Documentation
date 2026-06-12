---
title: Buat AcroForm - Buat PDF yang dapat diisi dalam Python
linktitle: Buat AcroForm
type: docs
weight: 10
url: /id/python-net/create-form/
description: Buat bidang AcroForm dari awal dalam dokumen PDF dengan menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara membuat AcroForm dalam PDF menggunakan Python
Abstract: Artikel ini menjelaskan cara membuat bidang AcroForm dalam dokumen PDF dengan menggunakan Aspose.PDF for Python via .NET. Artikel ini mencakup pembuatan bidang dasar dengan TextBoxField, penyesuaian tampilan kotak teks multi-widget, dan tipe bidang tambahan seperti radio buttons, combo boxes, checkboxes, list boxes, signature fields, dan barcode fields. Contoh-contoh ini membantu Anda membangun formulir PDF interaktif untuk pengumpulan data dan alur kerja otomatisasi dokumen.
---

## Buat Form dari Awal

### Tambahkan Form Field dalam Dokumen PDF

The [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas menyediakan koleksi bernama [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) yang membantu Anda mengelola bidang formulir dalam dokumen PDF.

Untuk menambahkan bidang formulir:

1. Buat bidang formulir yang ingin Anda tambahkan.
1. Panggil koleksi Form [tambahkan](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) metode.

### Menambahkan TextBoxField

Contoh berikut menunjukkan cara menambahkan [BidangKotakTeks](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rectangle = ap.Rectangle(10, 600, 110, 620, True)
    text_box_field = ap.forms.TextBoxField(page, rectangle)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Text Box"

    text_box_field.default_appearance = ap.annotations.DefaultAppearance(
        "Arial", 10, drawing.Color.dark_blue
    )

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field, 1)
    document.save(output_file_name)
```

### Bidang Kotak Teks Multi-Widget dalam PDF

Buat sebuah bidang formulir kotak teks dengan beberapa penampilan widget dalam PDF menggunakan Python dan Aspose.PDF. Ini menempatkan beberapa area input teks pada sebuah halaman, menerapkan font dan warna yang berbeda pada setiap widget, menyesuaikan batas, dan mengatur gaya latar belakang untuk formulir PDF interaktif.

1. Buat Dokumen PDF Baru.
1. Definisikan Posisi Kolom Teks.
1. Buat Penampilan Default yang Berbeda.
1. Buat bidang Kotak Teks.
1. Terapkan Penampilan pada Setiap Widget.
1. Sesuaikan Gaya Border.
1. Tambahkan Field ke Form.
1. Simpan File PDF.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_text_box_field_nt(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    rects = [
        ap.Rectangle(10, 600, 110, 620, normalize_coordinates=True),
        ap.Rectangle(10, 630, 110, 650, normalize_coordinates=True),
        ap.Rectangle(10, 660, 110, 680, normalize_coordinates=True),
    ]

    default_appearances = [
        ap.annotations.DefaultAppearance("Arial", 10, drawing.Color.dark_blue),
        ap.annotations.DefaultAppearance("Helvetica", 12, drawing.Color.dark_green),
        ap.annotations.DefaultAppearance(
            ap.text.FontRepository.find_font("Calibri"), 14, drawing.Color.dark_magenta
        ),
    ]

    text_box_field = ap.forms.TextBoxField(page, rects)
    text_box_field.partial_name = "textbox1"
    text_box_field.value = "Some text"

    for i, widget in enumerate(text_box_field):
        widget.default_appearance = default_appearances[i]

    border = ap.annotations.Border(text_box_field)
    border.width = 1
    border.style = ap.annotations.BorderStyle.DASHED
    border.dash = ap.annotations.Dash(3, 3)
    text_box_field.border = border

    text_box_field.characteristics.border = ap.Color.red.to_rgb()
    text_box_field.characteristics.background = ap.Color.yellow.to_rgb()

    document.form.add(text_box_field)
    document.save(output_file_name)
```

## Menambahkan Bidang Form Lain

Cuplikan kode berikut menunjukkan cara menambahkan berbagai jenis bidang, seperti tombol radio, kotak kombo, kotak centang, kotak daftar, bidang tanda tangan, dan bidang kode batang. Setiap fungsi membuat dokumen PDF baru, menambahkan bidang target dengan opsi yang dipilih, dan menyimpan file yang telah diperbarui.

1. Tambahkan Bidang Tombol Radio
1. Tambahkan Field Combo Box
1. Tambahkan Bidang Kotak Centang
1. Tambahkan Bidang Kotak Daftar
1. Tambahkan Bidang Tanda Tangan
1. Tambahkan Field Barcode

### Tambahkan Bidang Tombol Radio

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_radio_button(output_file_name):
    document = ap.Document()
    document.pages.add()

    radio = ap.forms.RadioButtonField(document.pages[1])
    radio.add_option(
        "Option 1", ap.Rectangle(100, 640, 120, 680, normalize_coordinates=True)
    )
    radio.add_option(
        "Option 2", ap.Rectangle(140, 640, 160, 680, normalize_coordinates=True)
    )

    document.form.add(radio)
    document.save(output_file_name)
```

### Tambahkan Field Combo Box

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_combo_box(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    combo = ap.forms.ComboBoxField(
        page, ap.Rectangle(100, 640, 150, 656, normalize_coordinates=True)
    )
    combo.add_option("Red")
    combo.add_option("Yellow")
    combo.add_option("Green")
    combo.add_option("Blue")
    combo.selected = 3

    document.form.add(combo)
    document.save(output_file_name)
```

### Tambahkan Bidang Kotak Centang

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_checkbox_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    checkbox = ap.forms.CheckboxField(
        page, ap.Rectangle(50, 620, 100, 650, normalize_coordinates=True)
    )
    checkbox.characteristics.background = ap.Color.aqua.to_rgb()
    checkbox.style = ap.forms.BoxStyle.CIRCLE

    document.form.add(checkbox)
    document.save(output_file_name)
```

### Tambahkan Bidang Kotak Daftar

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_list_box_field_to_pdf(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    list_box = ap.forms.ListBoxField(
        page, ap.Rectangle(50, 650, 100, 700, normalize_coordinates=True)
    )
    list_box.partial_name = "list"
    list_box.add_option("Red")
    list_box.add_option("Green")
    list_box.add_option("Blue")

    document.form.add(list_box)
    document.save(output_file_name)
```

### Tambahkan Bidang Tanda Tangan

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_signature_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    signature_field = ap.forms.SignatureField(
        page, ap.Rectangle(100, 700, 200, 800, True)
    )
    signature_field.partial_name = "Signature1"
    document.form.add(signature_field)
    document.save(output_file_name)
```

### Tambahkan Field Barcode

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

def add_barcode_field(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    barcode = ap.forms.BarcodeField(page, ap.Rectangle(100, 700, 200, 740, True))
    barcode.partial_name = "Barcode1"
    barcode.add_barcode("1234567890")
    document.form.add(barcode)
    document.save(output_file_name)
```

## Topik Terkait

- [Isi AcroForm](/pdf/id/python-net/fill-form/)
- [Ekstrak AcroForm](/pdf/id/python-net/extract-form/)
- [Memodifikasi AcroForm](/pdf/id/python-net/modifying-form/)
- [Impor dan Ekspor Data Form](/pdf/id/python-net/import-export-form-data/)
