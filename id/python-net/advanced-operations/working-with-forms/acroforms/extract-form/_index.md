---
title: Ekstrak AcroForm - Ekstrak Data Formulir dari PDF dengan Python
linktitle: Ekstrak AcroForm
type: docs
weight: 30
url: /id/python-net/extract-form/
description: Ekstrak formulir dari dokumen PDF Anda dengan pustaka Aspose.PDF untuk Python. Dapatkan nilai dari setiap bidang individual dalam file PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mendapatkan Data Formulir dari PDF menggunakan Python
Abstract: Artikel ini menyediakan panduan tentang mengekstrak data dari bidang formulir dalam dokumen PDF menggunakan Python. Artikel ini menjelaskan cara menelusuri semua bidang menggunakan pustaka Aspose.PDF, khususnya dengan mengakses koleksi `Form` dan memanfaatkan tipe `Field` serta properti `value`-nya. Sebuah potongan kode Python contoh disertakan, yang mendemonstrasikan cara membuka dokumen PDF, mengiterasi bidang formulirnya, dan mencetak nama serta nilai setiap bidang. Metode ini berguna untuk secara programatis mengambil data formulir dari file PDF.
---

## Ekstrak data dari formulir

### Dapatkan Nilai dari Semua Bidang Dokumen PDF

Untuk mendapatkan nilai dari semua bidang dalam dokumen PDF, Anda perlu menelusuri semua bidang formulir dan kemudian mengambil nilainya menggunakan properti Value. Dapatkan setiap bidang dari koleksi Form, dalam tipe bidang dasar yang disebut [Bidang](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) dan akses properti [nilai](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties)-nya.

Potongan kode Python berikut menunjukkan cara mendapatkan nilai semua bidang dari dokumen PDF.

```python

    import aspose.pdf as ap

    # Construct the full path to the input PDF file
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    # Create a Form object from the PDF file
    form = ap.facades.Form(path_infile)

    # Initialize an empty dictionary to store form values
    form_values = {}

    # Iterate through all form fields in the PDF
    for formField in form.field_names:
        # Retrieve the value for each form field and store in the dictionary
        form_values[formField] = form.get_field(formField)

    # Print and return the extracted form values
    print(form_values)
```

