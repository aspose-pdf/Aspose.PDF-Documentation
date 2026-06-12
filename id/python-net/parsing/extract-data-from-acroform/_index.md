---
title: Ekstrak Data dari AcroForm menggunakan Python
linktitle: Ekstrak Data dari AcroForm
type: docs
weight: 50
url: /id/python-net/extract-data-from-acroform/
description: Aspose.PDF memudahkan ekstraksi data bidang formulir dari file PDF. Pelajari cara mengekstrak data dari AcroForms dan menyimpannya dalam format JSON, XML, atau FDF.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengekstrak Data dari AcroForm melalui Python
Abstract: Artikel ini menyediakan panduan komprehensif tentang penggunaan Aspose.PDF for Python untuk mengelola bidang formulir dalam dokumen PDF. Artikel ini merinci berbagai metode untuk mengekstrak, memanipulasi, dan mengekspor data formulir dari PDF. Artikel dimulai dengan mendemonstrasikan cara mengekstrak nilai bidang formulir dan menyimpannya dalam kamus, kemudian mengeluarkan data dalam format JSON. Selanjutnya artikel menggambarkan cara mengekspor data formulir langsung ke file JSON, meningkatkan kemampuan serialisasi data. Selain itu, artikel mencakup ekspor data formulir ke format lain seperti XML, FDF (Forms Data Format), dan XFDF, yang berguna untuk pertukaran data dan penyimpanan data terstruktur. Setiap bagian menyertakan potongan kode Python untuk membantu pemahaman dan implementasi. Secara keseluruhan, artikel ini berfungsi sebagai sumber praktis bagi pengembang yang ingin mengintegrasikan penanganan formulir PDF ke dalam aplikasi Python mereka.
---

## Ekstrak bidang formulir dari dokumen PDF

[Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) dari `aspose.pdf.facades` namespace menyediakan cara yang sederhana untuk membaca data bidang AcroForm tanpa membuka model objek dokumen secara lengkap. Iterasi atas `form.field_names` untuk mendapatkan setiap nama bidang yang ada dalam formulir, kemudian panggil `form.get_field(name)` untuk mengambil nilai saat ini.

1. Bangun sebuah `Form` objek dengan melewatkan jalur file input.
1. Iterasi atas `form.field_names` untuk mendaftar semua nama bidang.
1. Panggil `form.get_field(name)` untuk setiap nama dan simpan hasilnya dalam kamus.

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

## Ambil nilai bidang formulir berdasarkan judul

Ketika Anda mengetahui nama bidang (title) yang tepat yang didefinisikan dalam formulir PDF, Anda dapat mengambil nilainya secara langsung dengan `form.get_field(name)` tanpa iterasi seluruh koleksi bidang. Ini adalah pendekatan tercepat ketika hanya bidang tertentu yang diperlukan.

1. Bangun sebuah [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) objek dengan jalur file input.
1. Panggil `form.get_field("FieldName")` menggunakan judul bidang yang persis seperti yang muncul di PDF.
1. Gunakan nilai string yang dikembalikan sesuai kebutuhan dalam aplikasi Anda.

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## Ekstrak bidang formulir dari dokumen PDF ke JSON

Ada dua cara untuk mengekspor data AcroForm ke JSON. Yang pertama menggunakan built-in `export_json` metode pada [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), yang menserialisasi semua data field secara langsung ke aliran file dalam satu panggilan.

1. Bangun sebuah `Form` objek dengan jalur file input.
1. Buka file output sebagai aliran biner menggunakan `FileIO`.
1. Panggil `form.export_json(stream, True)` untuk menulis output JSON.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

Pendekatan kedua membangun kamus Python dari `field_names` dan `get_field`, lalu menyerialkannya dengan `json.dumps`. Gunakan ini ketika Anda perlu mengubah atau memfilter data sebelum menulisnya.

1. Iterasi atas `form.field_names` dan mengisi kamus dengan nilai bidang.
1. Serialisasi kamus dengan `json.dumps(form_data, indent=4)`.
1. Tuliskan string JSON yang dihasilkan ke file output.

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Ekstrak Data ke XML dari File PDF

Ekspor XML berguna untuk mengintegrasikan data formulir PDF dengan sistem yang mengonsumsi umpan XML terstruktur atau skema. The [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) kelas menyediakan `export_xml` untuk menangani konversi dalam satu langkah.

1. Buat sebuah `Form` instans dan ikat PDF dengan `form.bind_pdf(path)`.
1. Buka file keluaran sebagai aliran biner.
1. Panggil `form.export_xml(stream)` menulis semua data bidang sebagai XML.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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

FDF (Forms Data Format) adalah format pertukaran standar untuk data AcroForm dan secara luas didukung oleh penampil PDF serta alat pemrosesan. Gunakan `export_fdf` pada [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) kelas untuk menghasilkan file FDF mandiri yang dapat diimpor kembali ke PDF asli atau formulir kompatibel lainnya.

1. Buat sebuah `Form` instance dan mengikat PDF sumber dengan `form.bind_pdf(path)`.
1. Buka file keluaran sebagai aliran biner.
1. Panggil `form.export_fdf(stream)` untuk menulis data FDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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

XFDF (XML Forms Data Format) adalah penerus berbasis XML untuk FDF dan lebih cocok untuk digunakan dalam layanan web dan alur data modern. Seperti FDF, file XFDF dapat diimpor kembali ke dalam formulir PDF yang kompatibel. Gunakan `export_xfdf` pada [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) kelas untuk menghasilkan keluaran.

1. Buat sebuah `Form` instance dan mengikat PDF sumber dengan `form.bind_pdf(path)`.
1. Buka file keluaran sebagai aliran biner.
1. Panggil `form.export_xfdf(stream)` untuk menulis data XFDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

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
