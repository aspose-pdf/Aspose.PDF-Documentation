---
title: Ekstrak Data dari AcroForm menggunakan Python
linktitle: Ekstrak Data dari AcroForm
type: docs
weight: 50
url: /id/python-net/extract-data-from-acroform/
description: Aspose.PDF memudahkan ekstraksi data bidang formulir dari file PDF. Pelajari cara mengekstrak data dari AcroForms dan menyimpannya ke dalam format JSON, XML, atau FDF.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengekstrak Data dari AcroForm dengan Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang penggunaan Aspose.PDF untuk Python dalam mengelola bidang formulir pada dokumen PDF. Artikel ini menjelaskan berbagai metode untuk mengekstrak, memanipulasi, dan mengekspor data formulir dari PDF. Artikel dimulai dengan memperlihatkan cara mengekstrak nilai bidang formulir dan menyimpannya dalam kamus, kemudian mengeluarkan data dalam format JSON. Selanjutnya artikel menunjukkan cara mengekspor data formulir langsung ke file JSON, meningkatkan kemampuan serialisasi data. Selain itu, artikel mencakup ekspor data formulir ke format lain seperti XML, FDF (Forms Data Format), dan XFDF, yang berguna untuk pertukaran data dan penyimpanan data terstruktur. Setiap bagian menyertakan cuplikan kode Python untuk membantu pemahaman dan implementasi. Secara keseluruhan, artikel ini menjadi sumber praktis bagi pengembang yang ingin mengintegrasikan penanganan formulir PDF ke dalam aplikasi Python mereka.
---

## Ekstrak bidang formulir dari dokumen PDF

Selain memungkinkan Anda menghasilkan bidang formulir dan mengisi bidang formulir, Aspose.PDF untuk Python memudahkan ekstraksi data bidang formulir atau informasi tentang bidang formulir dari file PDF.

Cuplikan kode ini membuat sebuah kamus untuk menyimpan nilai semua bidang dalam formulir PDF. Ia mengiterasi nama-nama bidang formulir, mengambil nilai mereka, dan mengisi kamus dengan data tersebut. Akhirnya, ia mencetak nilai formulir yang terkumpul.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## Mengambil nilai bidang formulir berdasarkan judul

## Ekstrak bidang formulir dari dokumen PDF ke JSON

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

Cuplikan kode Python yang diberikan mengekstrak nilai bidangnya dan menyerialisasikan data ini ke dalam format JSON. Ia mengimpor modul yang diperlukan, membangun jalur file masukan dan keluaran, mengambil nama dan nilai bidang dari formulir PDF, dan menulis string JSON yang diserialisasi ke file keluaran yang ditentukan.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if need
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    # Output the JSON string
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Ekstrak Data ke XML dari File PDF

Cuplikan kode Python berikutnya membuat objek formulir, mengikat sebuah dokumen PDF ke objek tersebut, dan mengekspor data formulir ke file XML. Kode ini secara otomatis mengekstrak data dari formulir PDF dan menyimpannya dalam format XML terstruktur.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## Ekspor Data ke FDF dari File PDF

Cuplikan kode berikut membuat objek formulir, mengikat sebuah dokumen PDF ke formulir tersebut, dan kemudian mengekspor data formulir ke file FDF (Forms Data Format). File FDF adalah format yang digunakan untuk menyimpan data formulir dari dokumen PDF, memungkinkan pertukaran data yang mudah.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Ekspor Data ke XFDF dari File PDF

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

