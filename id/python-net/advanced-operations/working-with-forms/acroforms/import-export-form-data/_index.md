---
title: Impor dan Ekspor Data Form
linktitle: Impor dan Ekspor Data Form
type: docs
weight: 80
url: /id/python-net/import-export-form-data/
description: Impor dan ekspor data bidang AcroForm dalam format XML, FDF, XFDF, dan JSON menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
TechArticle: true
AlternativeHeadline: Teknik impor dan ekspor menggunakan Aspose.PDF for Python via .NET.
Abstract: Komplikasi ini menyajikan rangkaian lengkap teknik impor dan ekspor data formulir menggunakan Aspose.PDF for Python via .NET. Ini mencakup alur kerja untuk mengintegrasikan formulir PDF dengan format data eksternal termasuk XML, FDF, XFDF, dan JSON. Pengguna dapat mengotomatiskan pengisian formulir secara massal dengan mengimpor data terstruktur ke dalam field interaktif, atau mengekstrak nilai field untuk analisis, cadangan, atau integrasi dengan sistem lain. Contoh-contoh menunjukkan cara mengikat formulir PDF, mentransfer data antar format, dan menyimpan dokumen yang diperbarui, memungkinkan pemrosesan dokumen yang skalabel dan konsisten di berbagai aplikasi.
---

Halaman ini menunjukkan alur kerja umum untuk mengimpor dan mengekspor data AcroForm dengan Aspose.PDF for Python via .NET. Semua operasi menggunakan [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) antarmuka.

## Impor data bidang formulir dari XML

Gunakan pendekatan ini untuk mengisi formulir PDF dari data XML eksternal.

1. Buat sebuah `Form` objek.
1. Gabungkan PDF input.
1. Buka file data XML.
1. Impor data XML ke dalam formulir.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## Ekspor data FormField ke XML

Metode ini mengekspor nilai bidang formulir dari dokumen PDF ke XML.

1. Buat sebuah `Form` objek.
1. Gabungkan PDF input.
1. Buka file output XML.
1. Ekspor data formulir ke XML.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## Impor data bidang formulir dari FDF

The `import_data_from_fdf` metode mengimpor data bidang formulir dari file FDF (Forms Data Format) ke dalam formulir PDF.

1. Buat sebuah `Form` objek.
1. Gabungkan PDF input.
1. Impor data formulir dengan `import_fdf()`.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## Ekspor data bidang formulir ke FDF

Contoh ini mengekspor data formulir dari dokumen PDF ke file FDF.

1. Buat sebuah `Form` objek.
1. Mengikat dokumen PDF.
1. Ekspor data formulir dengan `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## Impor data bidang formulir dari XFDF

Gunakan metode ini untuk mengimpor data bidang formulir dari file XFDF (XML Forms Data Format) ke dalam formulir PDF.

1. Buat sebuah `Form` objek.
1. Gabungkan PDF input.
1. Impor data formulir dari file XFDF.
1. Simpan PDF yang diperbarui.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## Ekspor data bidang formulir ke XFDF

Kode ini mengekspor data bidang formulir dari dokumen PDF ke file XFDF.

1. Buat sebuah `Form` objek.
1. Gabungkan PDF input.
1. Ekspor data formulir ke XFDF.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## Impor data dari PDF lain

Contoh ini mentransfer data bidang formulir dari PDF sumber ke PDF tujuan dengan mengekspor XFDF ke aliran memori dan mengimpornya ke formulir target.

1. Buat sumber dan tujuan `Form` objek.
1. Gabungkan PDF sumber dan tujuan.
1. Ekspor data formulir dari PDF sumber.
1. Impor data formulir ke PDF tujuan.
1. Simpan PDF tujuan yang diperbarui.

```python
from io import StringIO
import aspose.pdf as ap

def import_data_from_another_pdf(source_pdf_name, destination_pdf_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(source_pdf_name)
    form_dest.bind_pdf(destination_pdf_name)

    with StringIO() as xfdf_stream:
        form_source.export_xfdf(xfdf_stream)
        xfdf_stream.seek(0)
        form_dest.import_xfdf(xfdf_stream)

    form_dest.save(output_file_name)
```

## Ekstrak Bidang Form ke JSON

Metode ini mengekspor bidang formulir ke file JSON dengan menggunakan `export_json()`.

1. Buat sebuah `Form` objek.
1. Buka file output JSON.
1. Ekspor bidang formulir dengan menggunakan `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## Ekstrak Bidang Form ke Dokumen JSON

Contoh ini membuat dokumen JSON kustom dari nama dan nilai field formulir.

1. Buat objek Form dari file input.
1. Inisialisasi kamus kosong untuk menyimpan data bidang formulir.
1. Iterasi semua bidang formulir dan ekstrak nilai-nilainya.
1. Serialisasikan kamus data Form ke string JSON dengan indentasi 4 spasi.
1. Tuliskan string JSON ke file output dengan encoding UTF-8.

```python
import json
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for field_name in form.field_names:
        form_data[field_name] = form.get_field(field_name)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Topik Terkait (Pendekatan Facades)

- [Impor Data XML](/pdf/id/python-net/import-xml-data/)
- [Impor Data FDF](/pdf/id/python-net/import-fdf-data/)
- [Impor Data XFDF](/pdf/id/python-net/import-xfdf-data/)
- [Impor Data JSON](/pdf/id/python-net/import-json-data/)
- [Ekspor ke XML](/pdf/id/python-net/export-to-xml/)
- [Ekspor ke FDF](/pdf/id/python-net/export-to-fdf/)
- [Ekspor ke XFDF](/pdf/id/python-net/export-to-xfdf/)
- [Ekspor ke JSON](/pdf/id/python-net/export-to-json/)
