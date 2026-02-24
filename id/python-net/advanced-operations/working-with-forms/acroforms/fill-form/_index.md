---
title: Isi AcroForm - Isi Form PDF menggunakan Python
linktitle: Isi AcroForm
type: docs
weight: 20
url: /id/python-net/fill-form/
description: Anda dapat mengisi formulir di dokumen PDF Anda dengan pustaka Aspose.PDF untuk Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengisi bidang formulir di PDF menggunakan Python
Abstract: Artikel ini memberikan panduan tentang cara mengisi bidang formulir dalam dokumen PDF menggunakan pustaka Aspose.PDF untuk Python. Artikel ini menjelaskan proses mengakses bidang formulir dari koleksi formulir dokumen dan mengatur nilainya melalui properti value bidang tersebut. Kode contoh menunjukkan cara membuka dokumen PDF, mengiterasi bidang formulirnya untuk menemukan bidang tertentu berdasarkan nama parsialnya (dalam hal ini, "Field 1"), dan mengubah nilai TextBoxField menjadi "777". Akhirnya, dokumen yang diperbarui disimpan ke file output. Tautan ke dokumentasi Aspose yang relevan disediakan untuk referensi lebih lanjut.
---

## Isi Bidang Formulir di Dokumen PDF

Contoh berikut mengisi bidang formulir PDF dengan nilai baru menggunakan Aspose.PDF untuk Python via .NET dan menyimpan dokumen yang diperbarui. Mendukung pembaruan banyak bidang dengan menentukan kamus nama bidang dan nilai.

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Define the new field values
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New"
    }

    # Create a Form object from the input PDF file
    form = ap.facades.Form(path_infile)

    # Fill out the form fields with the new values
    for formField in form.field_names:
        if formField in new_field_values:
            form.fill_field(formField, new_field_values[formField])

    # Save the modified form to the output PDF file
    form.save(path_outfile)
```



