---
title: Konversi PDF ke Excel dalam Python
linktitle: Konversi PDF ke Excel
type: docs
weight: 20
url: /id/python-net/convert-pdf-to-excel/
lastmod: "2026-06-12"
description: Pelajari cara mengonversi PDF ke Excel di Python, termasuk XLS, XLSX, CSV, ODS, output lembar kerja tunggal, dan penanganan kolom dengan Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Konversi PDF ke Excel, XLSX, CSV, dan ODS di Python
Abstract: Artikel ini menunjukkan cara mengonversi file PDF ke format spreadsheet dengan Aspose.PDF for Python via .NET. Ini mencakup output XLS, XLSX, XLSM, CSV, dan ODS, serta opsi untuk mengendalikan kolom kosong dan mengurangi jumlah lembar kerja yang dihasilkan.
---

## Konversi PDF ke Excel dalam Python

**Aspose.PDF for Python via .NET** mendukung konversi file PDF ke Excel dan format spreadsheet lainnya dari kode Python.

Gunakan halaman ini saat Anda perlu mengonversi PDF ke XLS, XLSX, CSV, atau ODS untuk ekstraksi tabel, penggunaan kembali laporan, penyortiran, penyaringan, atau analisis lanjutan. Selama konversi PDF ke Excel, halaman PDF individual dapat dirender sebagai lembar kerja Excel.

Contoh pertama mengonversi file PDF ke format Spreadsheet 2003 XML. Bagian selanjutnya menunjukkan output XLSX, XLSM, CSV, ODS, dan lembar kerja tunggal.

{{% alert color="success" %}}
**Coba konversi PDF ke Excel secara online**

Aspose.PDF mempersembahkan aplikasi online Anda ["PDF ke XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya bekerja.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Cuplikan kode berikut menunjukkan proses mengonversi file PDF menjadi format XLS atau XLSX dengan Aspose.PDF for Python via .NET.

Langkah: Mengonversi file PDF ke format Excel (XML Spreadsheet 2003)

1. Muat dokumen PDF.
1. Atur opsi penyimpanan Excel menggunakan [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Simpan file yang dikonversi.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_spread_sheet2003(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Konversi PDF ke XLSX dengan Python

Langkah: Mengonversi file PDF ke format XLSX (Excel 2007+)

1. Muat dokumen PDF.
1. Atur opsi penyimpanan Excel menggunakan [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Simpan file yang dikonversi.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Konversi PDF ke XLSX dengan Kontrol Kolom

Saat mengonversi PDF ke format Excel, kolom kosong dapat ditambahkan sebagai kolom pertama dalam file output. Gunakan `insert_blank_column_at_first` opsi dari `ExcelSaveOptions` kelas untuk mengontrol perilaku ini. Nilai defaultnya adalah `true`.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_control_column(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Konversi PDF ke Satu Lembar Kerja Excel

Aspose.PDF for Python via .NET menunjukkan cara mengonversi PDF ke file Excel (.xlsx), dengan opsi 'minimize_the_number_of_worksheets' diaktifkan.

Langkah: Mengonversi PDF ke XLS atau XLSX Lembar Kerja Tunggal di Python

1. Muat dokumen PDF.
1. Atur opsi penyimpanan Excel menggunakan [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Opsi 'minimize_the_number_of_worksheets' mengurangi jumlah lembar kerja Excel dengan menggabungkan halaman PDF menjadi lebih sedikit lembar kerja (mis., satu lembar kerja untuk seluruh dokumen jika memungkinkan).
1. Simpan file yang dikonversi.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_single_excel_worksheet(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Konversi PDF ke Excel 2007 yang Mendukung Makro (XLSM)

Contoh Python ini menunjukkan cara mengonversi file PDF menjadi file Excel dalam format XLSM (Workbook Excel yang Mendukung Makro).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_macro(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Konversi ke format spreadsheet lain

### Konversi PDF ke CSV

Fungsi 'convert_pdf_to_excel_2007_csv' melakukan operasi yang sama seperti sebelumnya, tetapi kali ini format targetnya adalah CSV (Comma-Separated Values) alih-alih XLSM.

Langkah: Mengonversi PDF ke CSV di Python

1. Buat sebuah instance dari [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek dengan dokumen PDF sumber.
1. Buat sebuah instance dari [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) dengan **ExcelSaveOptions.ExcelFormat.CSV**
1. Simpan ke format **CSV** dengan memanggil [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* metode dan melewatkannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_excel_2007_csv(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.CSV
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Konversi PDF ke ODS

Langkah: Konversi PDF ke ODS di Python

1. Buat sebuah instance dari [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek dengan dokumen PDF sumber.
1. Buat sebuah instance dari [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) dengan **ExcelSaveOptions.ExcelFormat.ODS**
1. Simpan ke format **ODS** dengan memanggil [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode dan melewatkannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

Konversi ke format ODS dilakukan dengan cara yang sama seperti semua format lainnya.

```python
from os import path
import aspose.pdf as ap
import sys

def convert_pdf_to_ods(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.ExcelSaveOptions()
    save_options.format = ap.ExcelSaveOptions.ExcelFormat.ODS
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Konversi terkait

- [Konversi PDF ke Word](/pdf/id/python-net/convert-pdf-to-word/) jika prioritas Anda adalah aliran teks yang dapat diedit daripada struktur spreadsheet.
- [Konversi PDF ke HTML](/pdf/id/python-net/convert-pdf-to-html/) ketika Anda membutuhkan output yang ramah peramban.
- [Konversi PDF ke format lain](/pdf/id/python-net/convert-pdf-to-other-files/) untuk EPUB, Markdown, teks, XPS, dan alur kerja ekspor terkait.
