---
title: Memodifikasi AcroForm
linktitle: Memodifikasi AcroForm
type: docs
weight: 45
url: /id/python-net/modifying-form/
description: Modifikasi bidang AcroForm dalam dokumen PDF dengan menggunakan Aspose.PDF for Python via .NET, termasuk menghapus teks, mengatur batas, menata tampilan bidang, dan menghapus bidang.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mengelola dan Menyesuaikan Bidang Formulir PDF
Abstract: Artikel ini menyajikan contoh praktis untuk memodifikasi bidang AcroForm dengan menggunakan Aspose.PDF for Python via .NET. Artikel ini mencakup penghapusan teks dari konten formulir Typewriter, pengaturan dan pembacaan batas karakter bidang teks, penerapan tampilan font khusus, serta penghapusan bidang berdasarkan nama. Alur kerja ini mendukung tugas pemeliharaan formulir yang umum dalam pipeline pemrosesan PDF otomatis.
---

## Hapus Teks dalam Formulir

Contoh ini menunjukkan cara menghapus teks dari bidang formulir Typewriter dalam PDF menggunakan Aspose.PDF for Python via .NET. Ini memindai halaman pertama PDF, mengidentifikasi formulir Typewriter, menghapus kontennya, dan menyimpan dokumen yang diperbarui. Pendekatan ini berguna untuk mengatur ulang atau membersihkan bidang formulir sebelum mendistribusikan kembali PDF.

1. Muat dokumen PDF masukan.
1. Akses formulir pada halaman pertama.
1. Iterasi setiap formulir dan periksa apakah itu `Typewriter` formulir.
1. Gunakan TextFragmentAbsorber untuk menemukan fragmen teks dalam formulir.
1. Bersihkan teks dari setiap fragmen.
1. Simpan PDF yang dimodifikasi ke file output.

```python
import aspose.pdf as ap


def clear_text_in_form(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    forms = document.pages[1].resources.forms

    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            absorber = ap.text.TextFragmentAbsorber()
            absorber.visit(form)

            for fragment in absorber.text_fragments:
                fragment.text = ""

    document.save(output_file_name)
```

## Atur Batas Field

Gunakan `set_field_limit(field, limit)` dari `FormEditor` untuk menentukan jumlah maksimum karakter yang diizinkan dalam bidang teks.

1. Buat sebuah `FormEditor` objek.
1. Gabungkan PDF input.
1. Atur batas bidang untuk bidang target.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap


def set_field_limit(input_file_name, output_file_name):
    form = ap.facades.FormEditor()
    form.bind_pdf(input_file_name)
    form.set_field_limit("First Name", 15)
    form.save(output_file_name)
```

## Dapatkan Batas Field

Anda juga dapat membaca batas karakter dari field teks.

1. Muat dokumen PDF.
1. Akses field formulir target.
1. Pastikan bidang tersebut `TextBoxField`.
1. Baca dan cetak `max_len`.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def get_field_limit(input_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {text_box_field.max_len}")
```

## Setel Font Kustom untuk Form Field

Contoh ini mengatur tampilan default kustom untuk bidang kotak teks, termasuk font, ukuran, dan warna.

1. Muat dokumen PDF.
1. Akses bidang target dan verifikasi tipenya.
1. Temukan font di `FontRepository`.
1. Terapkan yang baru `DefaultAppearance`.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable


def set_form_field_font(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        text_box_field = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        text_box_field.default_appearance = ap.annotations.DefaultAppearance(
            font, 10, ap.Color.black.to_rgb()
        )

    document.save(output_file_name)
```

## Hapus Field dalam Form yang Ada

Kode ini menghapus bidang formulir tertentu (berdasarkan namanya) dari dokumen PDF dan menyimpan file yang diperbarui menggunakan Aspose.PDF for Python via .NET.

1. Muat dokumen PDF.
1. Hapus bidang formulir berdasarkan nama.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap


def delete_form_field(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    document.form.delete("First Name")
    document.save(output_file_name)
```

## Topik Terkait

- [Buat AcroForm](/pdf/id/python-net/create-form/)
- [Isi AcroForm](/pdf/id/python-net/fill-form/)
- [Ekstrak AcroForm](/pdf/id/python-net/extract-form/)
- [Impor dan Ekspor Data Form](/pdf/id/python-net/import-export-form-data/)
