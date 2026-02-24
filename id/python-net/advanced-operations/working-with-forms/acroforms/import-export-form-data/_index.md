---
title: Impor dan Ekspor Data Formulir
type: docs
weight: 80
url: /id/python-net/import-export-form-data/
description: Bagian ini menjelaskan cara mengimpor dan Mengekspor Data Formulir.
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: Teknik Impor dan Ekspor menggunakan Aspose.PDF untuk Python via .NET.
Abstract: Komplikasi ini menyajikan rangkaian lengkap teknik impor dan ekspor data formulir menggunakan Aspose.PDF untuk Python via .NET. Ini mencakup alur kerja untuk mengintegrasikan formulir PDF dengan format data eksternal termasuk XML, FDF, XFDF, dan JSON. Pengguna dapat mengotomatisasi pengisian massal formulir dengan mengimpor data terstruktur ke dalam bidang interaktif, atau mengekstrak nilai bidang untuk analisis, cadangan, atau integrasi dengan sistem lain. Contoh-contoh menunjukkan cara mengikat formulir PDF, mentransfer data antar format, dan menyimpan dokumen yang diperbarui, memungkinkan pemrosesan dokumen yang skalabel dan konsisten di berbagai aplikasi.
---

## Impor Data Formulir dari file XML

Contoh berikut menunjukkan cara mengimpor data formulir dari file XML ke dalam formulir PDF yang ada menggunakan Aspose.PDF untuk Python. Dengan mengikat formulir PDF, memuat data XML, dan menyimpan file yang diperbarui, Anda dapat dengan cepat mengisi bidang formulir interaktif tanpa mengedit setiap halaman secara manual. Metode ini ideal untuk mengotomatisasi pengisian massal formulir, memproses set data besar, dan memastikan konsistensi data di seluruh dokumen.

Gunakan langkah-langkah berikut:

1. Buat objek Form menggunakan Aspose.PDF.
1. Ikat Formulir PDF.
1. Muat Data XML.
1. Impor XML ke dalam PDF.
1. Simpan PDF yang Diperbarui.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Define the working directory path
    workdir_path = "/path/to/working/directory"

    # Construct full file paths using the working directory
    path_infile = path.join(workdir_path, infile)
    path_datafile = path.join(workdir_path, datafile)
    path_outfile = path.join(workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()

    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
```

## Ekspor Data bidang Formulir dari dokumen PDF ke file XML

Pustaka Python menunjukkan cara mengekspor data bidang formulir dari dokumen PDF ke file XML menggunakan Aspose.PDF untuk Python. Dengan mengikat formulir PDF dan menyimpan nilai bidangnya dalam format XML, Anda dapat dengan mudah menyimpan, memproses, atau menggunakan kembali data formulir dalam aplikasi atau alur kerja lain. Pendekatan ini ideal untuk pencadangan data, analisis, dan integrasi dengan sistem eksternal.

Gunakan langkah-langkah berikut:

1. Buat objek Form menggunakan Aspose.PDF.
1. Ikat Formulir PDF
1. Ekspor Data Formulir
1. Simpan Nilai Bidang ke XML

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
        form.export_xml(f)
```

## Impor Data bidang Formulir dari FDF

Metode 'import_data_from_fdf' mengimpor data bidang formulir dari file FDF (Formats Data Formulir) ke dalam formulir PDF yang ada dan menyimpan dokumen yang diperbarui. Pendekatan ini berguna untuk mengisi sebelumnya atau memperbarui formulir PDF secara programatis tanpa mengubah struktur dokumen.

Gunakan langkah-langkah berikut:

1. Buat objek Form menggunakan Aspose.PDF.
1. Ikat PDF input.
1. Impor data formulir dengan import_fdf().
1. Simpan PDF dengan data yang diimpor ke jalur file output yang ditentukan.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
```

## Ekspor Data bidang Formulir ke FDF

Contoh ini menunjukkan cara mengekspor data formulir dari dokumen PDF ke file FDF (Formats Data Formulir) menggunakan Aspose.PDF untuk Python via .NET.

1. Buat objek Form menggunakan Aspose.PDF.
1. Ikat dokumen PDF.
1. Ekspor data formulir dengan export_fdf().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Impor Data bidang Formulir dari XFDF

Contoh ini mengekspor data bidang formulir dari dokumen PDF ke file XFDF (XML Forms Data Format) dan kemudian menyimpan PDF yang diperbarui menggunakan Aspose.PDF untuk Python via .NET.

1. Buat objek Form menggunakan Aspose.PDF.
1. Ikat dokumen PDF ke formulir.
1. Ekspor data formulir ke file XFDF.
1. Simpan formulir yang diproses.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_datafile, "w") as f:
        form.export_xfdf(f)
        form.save(path_outfile)
```

## Ekspor Data bidang Formulir ke XFDF

Kode ini mengekstrak data bidang formulir dari dokumen PDF dan mengekspornya ke file XFDF (XML Forms Data Format) menggunakan Aspose.PDF untuk Python.

1. Buat objek Form menggunakan Aspose.PDF.
1. Ikat dokumen PDF ke formulir.
1. Ekspor data formulir ke file FDF.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

## Impor Data dari PDF lain

Potongan kode ini menunjukkan cara mentransfer data bidang formulir dari PDF sumber ke PDF tujuan. Data formulir diekspor ke aliran XFDF dari PDF sumber dan kemudian diimpor ke PDF target menggunakan Aspose.PDF untuk Python via .NET.

1. Buat objek Form menggunakan Aspose.PDF.
1. Ikat dokumen PDF ke formulir.
1. Ekspor data formulir dari PDF sumber.
1. Impor data formulir ke PDF tujuan.
1. Simpan PDF tujuan yang telah diperbarui.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    # Bind PDF document
    form_source.bind_pdf(path_infile)
    form_dest.bind_pdf(path_outfile)

    # Export form data to an FDF file
    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## Ekstrak Bidang Formulir ke JSON

Metode ini mengekstrak bidang formulir dari file input dan mengekspornya ke file JSON.

1. Buat objek Form menggunakan Aspose.PDF.
1. Buka file output dalam mode menulis menggunakan FileIO().
1. Ekspor bidang formulir ke file JSON menggunakan metode form.export_json().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

## Ekstrak Bidang Formulir ke Dokumen JSON

1. Buat objek Form dari file input.
1. Inisialisasi kamus kosong untuk menyimpan data bidang formulir.
1. Iterasi melalui semua bidang formulir dan ekstrak nilainya.
1. Serialisasikan kamus data formulir ke string JSON dengan indentasi 4 spasi.
1. Tulis string JSON ke file output dengan encoding UTF-8.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

