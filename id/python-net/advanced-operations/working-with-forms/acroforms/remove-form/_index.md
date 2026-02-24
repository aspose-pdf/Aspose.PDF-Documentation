---
title: Hapus Formulir dari PDF dengan Python
linktitle: Hapus Formulir
type: docs
weight: 70
url: /id/python-net/remove-form/
description: Hapus Teks berdasarkan subtype/formulir dengan Aspose.PDF untuk Python via .NET library. Hapus semua formulir dari PDF.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Formulir dari PDF dengan Aspose.PDF untuk Python via .NET
Abstract: Dokumen ini menyajikan dua pendekatan berbasis Python untuk menghapus elemen formulir dari file PDF menggunakan Aspose.PDF untuk Python via .NET. Metode pertama memperlihatkan cara membersihkan semua objek formulir dari halaman tertentu dengan mengakses kamus sumber dayanya dan memanggil metode clear() pada koleksi formulir. Metode kedua memberikan solusi yang lebih terarah dengan mengiterasi anotasi formulir, mengidentifikasi formulir tipe mesin tik, dan menghapusnya secara selektif berdasarkan atributnya. Kedua teknik tersebut diakhiri dengan menyimpan PDF yang diperbarui ke jalur output yang ditentukan, menawarkan opsi fleksibel untuk pembersihan formulir dan penyempurnaan dokumen dalam alur kerja otomatis.
---

## Hapus Semua Formulir dari PDF

Kode ini menghapus semua elemen formulir dari halaman pertama dokumen PDF dan kemudian menyimpan dokumen yang dimodifikasi ke jalur output yang ditentukan.

1. Muat dokumen PDF.
1. Akses sumber daya halaman.
1. Bersihkan objek formulir.
1. Simpan dokumen yang diperbarui.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(data_dir, infile)
    path_outfile = os.path.join(data_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(path_outfile)
```

## Hapus Formulir Tertentu

Contoh berikut mengiterasi objek formulir pada halaman PDF tertentu, mengidentifikasi anotasi formulir tipe mesin tik, menghapusnya, dan kemudian menyimpan PDF yang diperbarui menggunakan Aspose.PDF untuk Python via .NET.

1. Muat dokumen PDF.
1. Akses formulir halaman.
1. Iterasi formulir.
1. Periksa formulir tipe mesin tik.
1. Hapus formulir yang cocok.
1. Simpan dokumen yang diperbarui.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if (form.it == "Typewriter" and form.subtype == "Form"):
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(path_outfile)
```
