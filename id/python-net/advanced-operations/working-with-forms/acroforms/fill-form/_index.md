---
title: Isi AcroForm - Isi Form PDF menggunakan Python
linktitle: Isi AcroForm
type: docs
weight: 20
url: /id/python-net/fill-form/
description: Isi bidang AcroForm dalam dokumen PDF dengan menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengisi bidang formulir dalam PDF menggunakan Python
Abstract: Artikel ini menjelaskan cara mengisi bidang AcroForm dalam dokumen PDF dengan menggunakan Aspose.PDF for Python via .NET. Contoh ini menggunakan Form facade, memetakan nama bidang ke nilai baru dalam sebuah kamus, memperbarui bidang yang cocok, dan menyimpan PDF output. Pendekatan ini berguna untuk alur kerja penyelesaian dokumen otomatis dan pemrosesan formulir massal.
---

## Isi Bidang Form dalam Dokumen PDF

Contoh berikut mengisi beberapa bidang dalam formulir PDF yang ada dengan menggunakan [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) antarmuka.

Gunakan langkah-langkah berikut:

1. Buat kamus dengan nama bidang dan nilai.
1. Hubungkan PDF input ke objek Form.
1. Iterasi melalui bidang form yang tersedia.
1. Isi bidang yang terdapat dalam kamus.
1. Simpan PDF yang diperbarui.

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## Topik Terkait

- [Buat AcroForm](/pdf/id/python-net/create-form/)
- [Ekstrak AcroForm](/pdf/id/python-net/extract-form/)
- [Impor dan Ekspor Data Form](/pdf/id/python-net/import-export-form-data/)