---
title: Memposting Formulir dalam PDF via Python
linktitle: Memposting Formulir
type: docs
weight: 75
url: /id/python-net/posting-form/
description: Tambahkan tombol kirim dan aksi pengiriman ke PDF AcroForms dengan menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Menambahkan Tombol Kirim dan Aksi Pengiriman Formulir ke PDF Menggunakan Python
Abstract: Artikel ini menunjukkan dua pendekatan untuk menambahkan fungsionalitas kirim ke formulir PDF dengan menggunakan Aspose.PDF for Python via .NET. Anda dapat menambahkan tombol kirim siap pakai melalui FormEditor atau membuat bidang tombol kustom dengan SubmitFormAction untuk kontrol lanjutan. Pola-pola ini membantu mengintegrasikan formulir PDF dengan endpoint pemrosesan formulir sisi server.
---

## Tambahkan Tombol Kirim dengan FormEditor

Cuplikan kode berikut menunjukkan cara menambahkan tombol kirim ke formulir PDF menggunakan kelas FormEditor di Aspose.PDF for Python via .NET. Tombol tersebut dikonfigurasi untuk mengirim data formulir ke URL tertentu saat diklik.

1. Buat sebuah `FormEditor` objek.
1. Tambahkan tombol kirim ke halaman target.
1. Atur URL pengiriman dan koordinat tombol.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap

def add_submit_button(input_file_name, output_file_name):
    editor = ap.facades.FormEditor(input_file_name, output_file_name)
    editor.add_submit_btn(
        "submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475
    )
    editor.save()
```

## Tambahkan Aksi Kirim Kustom

Potongan kode berikut menjelaskan cara membuat tombol kirim khusus dalam formulir PDF menggunakan Aspose.PDF for Python via .NET. Tombol ini dikonfigurasi untuk mengirim data formulir ke URL yang ditentukan saat diklik.

1. Buka PDF dengan ap.Document().
1. Buat aksi kirim.
1. Atur URL target dan flag pengiriman.
1. Buat bidang tombol dan kaitkan aksi kliknya.
1. Tambahkan tombol ke formulir.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap

def add_submit_action(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    submit_action = ap.annotations.SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        ap.annotations.SubmitFormAction.EXPORT_FORMAT
        | ap.annotations.SubmitFormAction.SUBMIT_COORDINATES
    )

    rect = ap.Rectangle(10, 10, 100, 40)
    submit_button = ap.forms.ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    document.form.add(submit_button, 1)
    document.save(output_file_name)
```

## Topik Terkait

- [Buat AcroForm](/pdf/id/python-net/create-form/)
- [Isi AcroForm](/pdf/id/python-net/fill-form/)
- [Memodifikasi AcroForm](/pdf/id/python-net/modifying-form/)
- [Impor dan Ekspor Data Form](/pdf/id/python-net/import-export-form-data/)