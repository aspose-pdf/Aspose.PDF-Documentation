---
title: Konversi PDF ke Excel di Python
linktitle: Konversi PDF ke Excel
type: docs
weight: 20
url: id/python-net/convert-pdf-to-excel/
lastmod: "2022-12-23"
keywords: konversi PDF ke Excel menggunakan python, konversi PDF ke XLS menggunakan python, konversi PDF ke XLSX menggunakan python, ekspor tabel dari PDF ke Excel di python.
description: Aspose.PDF untuk perpustakaan Python memungkinkan Anda mengonversi PDF ke format Excel menggunakan Python. Format ini termasuk XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ikhtisar

Artikel ini menjelaskan cara **mengonversi PDF ke format Excel menggunakan Python**. Ini mencakup topik-topik berikut.

_Format_: **XLS**

- [Python PDF ke XLS](#python-pdf-to-xls)
- [Python Konversi PDF ke XLS](#python-pdf-to-xls)
- [Python Cara mengonversi file PDF ke XLS](#python-pdf-to-xls)

_Format_: **XLSX**

- [Python PDF ke XLSX](#python-pdf-to-xlsx)
- [Python Konversi PDF ke XLSX](#python-pdf-to-xlsx)
- [Python Cara mengonversi file PDF ke XLSX](#python-pdf-to-xlsx)


_Format_: **Excel**

- [Python PDF ke Excel](#python-pdf-to-xlsx)
- [Python PDF ke Excel XLS](#python-pdf-to-xls)
- [Python PDF ke Excel XLSX](#python-pdf-to-xlsx)

_Format_: **CSV**

- [Python PDF ke CSV](#python-pdf-to-csv)
- [Python Ubah PDF ke CSV](#python-pdf-to-csv)
- [Python Cara mengubah file PDF ke CSV](#python-pdf-to-csv)

_Format_: **ODS**

- [Python PDF ke ODS](#python-pdf-to-ods)
- [Python Ubah PDF ke ODS](#python-pdf-to-ods)
- [Python Cara mengubah file PDF ke ODS](#python-pdf-to-ods)

## Konversi PDF ke EXCEL melalui Python

**Aspose.PDF untuk Python via .NET** mendukung fitur mengkonversi file PDF ke format Excel, dan CSV.

Aspose.PDF untuk Python via .NET adalah komponen manipulasi PDF, kami telah memperkenalkan fitur yang merender file PDF ke buku kerja Excel (file XLSX). Selama konversi ini, halaman individu dari file PDF dikonversi ke lembar kerja Excel.

{{% alert color="success" %}}
**Coba mengkonversi PDF ke Excel secara online**

Aspose.PDF menghadirkan aplikasi online gratis ["PDF ke XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Cuplikan kode berikut menunjukkan proses untuk mengonversi file PDF ke format XLS atau XLSX dengan Aspose.PDF untuk Python via .NET.

<a name="python-pdf-to-xls"><strong>Langkah-langkah: Mengonversi PDF ke XLS di Python</strong></a>

1. Buat instance dari objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Buat instance dari [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. Simpan dalam format **XLS** dengan menentukan **ekstensi .xls** dengan memanggil metode [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dan melewatkannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xls.xls"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003

    # Simpan file ke dalam format MS Excel
    document.save(output_pdf, save_option)
```


<a name="python-pdf-to-xlsx"><strong>Langkah-langkah: Konversi PDF ke XLSX di Python</strong></a>

1. Buat instance dari objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Buat instance dari [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
3. Simpan ke format **XLSX** dengan menentukan **ekstensi .xlsx** dengan memanggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dan melewatkannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_xlsx.xlsx"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()

    # Simpan file ke dalam format MS Excel
    document.save(output_pdf, save_option)
```

## Konversi PDF ke XLS dengan kontrol Kolom

Saat mengonversi PDF ke format XLS, kolom kosong ditambahkan ke file keluaran sebagai kolom pertama.
 Dalam opsi 'ExcelSaveOptions class' InsertBlankColumnAtFirst digunakan untuk mengontrol kolom ini. Nilai defaultnya adalah true.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_with_control_column.xls"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.insert_blank_column_at_first = True

    # Simpan file ke dalam format MS Excel
    document.save(output_pdf, save_option)
```

## Mengonversi PDF ke Lembar Kerja Excel Tunggal

Saat mengekspor file PDF dengan banyak halaman ke XLS, setiap halaman diekspor ke lembar yang berbeda dalam file Excel. Ini karena properti MinimizeTheNumberOfWorksheets diatur ke false secara default. Untuk memastikan bahwa semua halaman diekspor ke satu lembar saja dalam file Excel keluaran, atur properti MinimizeTheNumberOfWorksheets ke true.

<a name="python-pdf-to-excel-single"><strong>Langkah-langkah: Mengonversi PDF ke Lembar Kerja XLS atau XLSX Tunggal di Python</strong></a>
1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Buat instance [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) dengan **MinimizeTheNumberOfWorksheets = true**.
3. Simpan ke format **XLS** atau **XLSX** dengan satu worksheet dengan memanggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dan meneruskannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xlsx_single_excel_worksheet.xls"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    save_option.minimize_the_number_of_worksheets = True

    # Simpan file ke dalam format MS Excel
    document.save(output_pdf, save_option)

```


## Konversi ke format spreadsheet lain

### Konversi ke CSV

Konversi ke format CSV dilakukan dengan cara yang sama seperti di atas. Yang Anda butuhkan - setel format yang sesuai.

<a name="python-pdf-to-csv"><strong>Langkah-langkah: Konversi PDF ke CSV dalam Python</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Buat instance [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) dengan **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Simpan ke format **CSV** dengan memanggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* dan melewatkannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).


```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_csv.csv"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.CSV

    # Simpan file
    document.save(output_pdf, save_option)
```


### Konversi ke ODS

<a name="python-pdf-to-ods"><strong>Langkah-langkah: Konversi PDF ke ODS dalam Python</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Buat instance [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) dengan **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Simpan ke format **ODS** dengan memanggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dan meneruskannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

Konversi ke format ODS dilakukan dengan cara yang sama seperti semua format lainnya.

```python

    import aspose.pdf as ap
    
    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_ods.ods"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)

    save_option = ap.ExcelSaveOptions()
    save_option.format = ap.ExcelSaveOptions.ExcelFormat.ODS

    # Simpan file
    document.save(output_pdf, save_option)
```


## Lihat Juga

Artikel ini juga mencakup topik-topik ini. Kode-kode sama seperti di atas.

_Format_: **Excel**
- [Kode Python PDF ke Excel](#python-pdf-to-xlsx)
- [API Python PDF ke Excel](#python-pdf-to-xlsx)
- [Python PDF ke Excel secara Programatis](#python-pdf-to-xlsx)
- [Library Python PDF ke Excel](#python-pdf-to-xlsx)
- [Python Simpan PDF sebagai Excel](#python-pdf-to-xlsx)
- [Python Hasilkan Excel dari PDF](#python-pdf-to-xlsx)
- [Python Buat Excel dari PDF](#python-pdf-to-xlsx)
- [Konverter Python PDF ke Excel](#python-pdf-to-xlsx)

_Format_: **XLS**
- [Kode Python PDF ke XLS](#python-pdf-to-xls)
- [API Python PDF ke XLS](#python-pdf-to-xls)
- [Python PDF ke XLS secara Programatis](#python-pdf-to-xls)
- [Library Python PDF ke XLS](#python-pdf-to-xls)
- [Python Simpan PDF sebagai XLS](#python-pdf-to-xls)
- [Python Hasilkan XLS dari PDF](#python-pdf-to-xls)
- [Python Buat XLS dari PDF](#python-pdf-to-xls)
- [Konverter Python PDF ke XLS](#python-pdf-to-xls)

_Format_: **XLSX**

- [Kode Python PDF ke XLSX](#python-pdf-to-xlsx)
- [Python PDF ke XLSX API](#python-pdf-to-xlsx)
- [Python PDF ke XLSX Secara Programatik](#python-pdf-to-xlsx)
- [Python PDF ke XLSX Perpustakaan](#python-pdf-to-xlsx)
- [Python Simpan PDF sebagai XLSX](#python-pdf-to-xlsx)
- [Python Hasilkan XLSX dari PDF](#python-pdf-to-xlsx)
- [Python Buat XLSX dari PDF](#python-pdf-to-xlsx)
- [Pengonversi Python PDF ke XLSX](#python-pdf-to-xlsx)

_Format_: **CSV**
- [Kode Python PDF ke CSV](#python-pdf-to-csv)
- [Python PDF ke CSV API](#python-pdf-to-csv)
- [Python PDF ke CSV Secara Programatik](#python-pdf-to-csv)
- [Python PDF ke CSV Perpustakaan](#python-pdf-to-csv)
- [Python Simpan PDF sebagai CSV](#python-pdf-to-csv)
- [Python Hasilkan CSV dari PDF](#python-pdf-to-csv)
- [Python Buat CSV dari PDF](#python-pdf-to-csv)
- [Pengonversi Python PDF ke CSV](#python-pdf-to-csv)

_Format_: **ODS**
- [Kode Python PDF ke ODS](#python-pdf-to-ods)
- [Python PDF ke ODS API](#python-pdf-to-ods)
- [Python PDF ke ODS Secara Programatik](#python-pdf-to-ods)
- [Python PDF ke ODS Perpustakaan](#python-pdf-to-ods)

- [Python Simpan PDF sebagai ODS](#python-pdf-to-ods)
- [Python Menghasilkan ODS dari PDF](#python-pdf-to-ods)
- [Python Membuat ODS dari PDF](#python-pdf-to-ods)
- [Konverter PDF ke ODS Python](#python-pdf-to-ods)