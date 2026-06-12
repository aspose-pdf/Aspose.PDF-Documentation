---
title: Hapus Forms dari PDF di Python
linktitle: Hapus Forms
type: docs
weight: 70
url: /id/python-net/remove-form/
description: Hapus objek Form dari halaman PDF dengan menggunakan Aspose.PDF for Python via .NET, termasuk pembersihan lengkap dan penghapusan terarah.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Forms dari PDF dengan Aspose.PDF for Python via .NET
Abstract: Artikel ini menyajikan dua pendekatan untuk menghapus elemen Form dari dokumen PDF dengan menggunakan Aspose.PDF for Python via .NET. Metode pertama membersihkan semua objek Form dari halaman yang dipilih, sementara metode kedua menghapus hanya sumber daya Form Typewriter yang cocok. Contoh-contoh ini membantu dalam pembersihan Form, persiapan templat, dan alur kerja normalisasi dokumen.
---

## Hapus Semua Forms dari Halaman

Kode ini menghapus semua objek form dari halaman yang ditentukan oleh `page_num` dan menyimpan dokumen yang diperbarui.

1. Muat dokumen PDF.
1. Akses sumber daya halaman.
1. Bersihkan objek form.
1. Simpan dokumen yang diperbarui.

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## Hapus Tipe Form Tertentu

Contoh berikut mengulangi objek form pada halaman PDF tertentu, mengidentifikasi anotasi form typewriter, menghapusnya, dan kemudian menyimpan PDF yang diperbarui menggunakan Aspose.PDF for Python via .NET.

1. Muat dokumen PDF.
1. Akses form halaman.
1. Iterasi pada form.
1. Periksa form typewriter.
1. Hapus form yang cocok.
1. Simpan dokumen yang diperbarui.

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## Topik Terkait

- [Buat AcroForm](/pdf/id/python-net/create-form/)
- [Isi AcroForm](/pdf/id/python-net/fill-form/)
- [Memodifikasi AcroForm](/pdf/id/python-net/modifying-form/)
- [Memposting Formulir](/pdf/id/python-net/posting-form/)
