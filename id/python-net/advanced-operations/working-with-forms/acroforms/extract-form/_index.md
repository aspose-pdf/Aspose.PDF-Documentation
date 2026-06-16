---
title: Ekstrak AcroForm - Ekstrak Data Formulir dari PDF dalam Python
linktitle: Ekstrak AcroForm
type: docs
weight: 30
url: /id/python-net/extract-form/
description: Ekstrak nilai dari bidang AcroForm dalam dokumen PDF dengan menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mendapatkan Data Formulir dari PDF menggunakan Python
Abstract: Artikel ini menunjukkan cara mengekstrak data dari bidang AcroForm dalam dokumen PDF dengan menggunakan Aspose.PDF for Python via .NET. Contohnya mengulangi nama-nama bidang formulir, membaca nilai dengan menggunakan fasad Form, dan mengembalikan kamus untuk pemrosesan selanjutnya. Alur kerja ini berguna untuk pelaporan, validasi, dan integrasi dengan sistem eksternal.
---

## Ekstrak Data dari Formulir

### Dapatkan Nilai dari Semua Bidang dalam Dokumen PDF

Untuk membaca nilai dari semua bidang dalam dokumen PDF, iterasi melalui nama-nama bidang formulir dan dapatkan setiap nilai dari [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) antarmuka.

Gunakan langkah-langkah berikut:

1. Mengikat PDF masukan ke sebuah `Form` objek.
1. Iterasi melalui `field_names`.
1. Baca setiap nilai dengan `get_field()`.
1. Simpan nilai dalam kamus.
1. Kembalikan atau proses nilai yang diekstrak.

Potongan kode Python berikut menunjukkan pendekatan ini.

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## Topik Terkait

- [Buat AcroForm](/pdf/id/python-net/create-form/)
- [Isi AcroForm](/pdf/id/python-net/fill-form/)
- [Impor dan Ekspor Data Form](/pdf/id/python-net/import-export-form-data/)
- [Memodifikasi AcroForm](/pdf/id/python-net/modifying-form/)