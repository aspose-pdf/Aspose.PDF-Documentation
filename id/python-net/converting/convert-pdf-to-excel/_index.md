---
title: Konversi PDF ke Excel dengan Python
linktitle: Konversi PDF ke Excel
type: docs
weight: 20
url: /id/python-net/convert-pdf-to-excel/
lastmod: "2025-09-27"
description: Konversi PDF ke spreadsheet Excel dengan mudah menggunakan Aspose.PDF untuk Python via .NET. Ikuti panduan ini untuk konversi PDF ke XLSX yang akurat
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengonversi PDF ke Excel dengan Python
Abstract: Artikel ini memberikan panduan lengkap tentang mengonversi file PDF ke berbagai format Excel menggunakan Python, khususnya dengan perpustakaan Aspose.PDF untuk Python via .NET. Artikel ini merinci proses konversi untuk format XLS, XLSX, CSV, dan ODS. Dokumen menjelaskan langkah‑langkah yang diperlukan untuk mengonversi PDF ke XLS dan XLSX, menyoroti pembuatan instance Document dan ExcelSaveOptions, serta penggunaan metode Document.Save() untuk menentukan format output. Artikel ini juga membahas fitur seperti mengontrol penyisipan kolom kosong dan meminimalkan jumlah lembar kerja selama konversi. Selain itu, disediakan contoh konversi PDF ke lembar kerja Excel tunggal serta format lain seperti CSV dan ODS, menekankan fleksibilitas dan fungsi Aspose.PDF. Sebuah alat daring untuk konversi PDF ke XLSX juga disebutkan, memungkinkan pengguna mengevaluasi kualitas konversi. Artikel ditutup dengan daftar topik terkait dan potongan kode untuk membantu pemahaman serta penerapan konversi ini secara programatis.
---

## Konversi PDF ke EXCEL dengan Python

**Aspose.PDF untuk Python via .NET** mendukung fitur mengonversi file PDF ke format Excel, dan CSV.

Aspose.PDF untuk Python via .NET adalah komponen manipulasi PDF, kami telah memperkenalkan fitur yang merender file PDF ke workbook Excel (file XLSX). Selama konversi ini, halaman‑halaman individual dari file PDF dikonversi menjadi lembar kerja Excel.

{{% alert color="success" %}}
**Coba konversi PDF ke Excel secara daring**

Aspose.PDF mempersembahkan aplikasi daring gratis ["PDF ke XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Potongan kode berikut menunjukkan proses mengonversi file PDF ke format XLS atau XLSX dengan Aspose.PDF untuk Python via .NET.

Langkah: Mengonversi file PDF ke format Excel (XML Spreadsheet 2003)

1. Muat dokumen PDF.
1. Siapkan opsi penyimpanan Excel menggunakan [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Simpan file yang telah dikonversi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XML_SPREAD_SHEET2003
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

Langkah: Mengonversi file PDF ke format XLSX (Excel 2007+)

1. Muat dokumen PDF.
1. Siapkan opsi penyimpanan Excel menggunakan [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Simpan file yang telah dikonversi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Mengonversi PDF ke XLS dengan Kontrol Kolom

Saat mengonversi PDF ke format XLS, kolom kosong ditambahkan ke file output sebagai kolom pertama. Pada kelas 'ExcelSaveOptions' opsi 'insert_blank_column_at_first' digunakan untuk mengontrol kolom ini. Nilai defaultnya adalah true.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.insert_blank_column_at_first = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Mengonversi PDF ke Lembar Kerja Excel Tunggal

Aspose.PDF untuk Python via .NET menunjukkan cara mengonversi PDF ke file Excel (.xlsx), dengan opsi 'minimize_the_number_of_worksheets' diaktifkan.

Langkah: Mengonversi PDF ke Lembar Kerja Tunggal XLS atau XLSX dengan Python

1. Muat dokumen PDF.
1. Siapkan opsi penyimpanan Excel menggunakan [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).
1. Opsi 'minimize_the_number_of_worksheets' mengurangi jumlah lembar Excel dengan menggabungkan halaman PDF menjadi lebih sedikit lembar kerja (mis., satu lembar kerja untuk seluruh dokumen jika memungkinkan).
1. Simpan file yang telah dikonversi.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSX
    save_options.minimize_the_number_of_worksheets = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## Mengonversi file PDF menjadi file Excel dalam format XLSM

Contoh Python ini menunjukkan cara mengonversi file PDF menjadi file Excel dalam format XLSM (Workbook Excel yang Mendukung Makro).

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.XLSM
    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## Mengonversi ke format spreadsheet lain

### Mengonversi ke CSV

Fungsi 'convert_pdf_to_excel_2007_csv' melakukan operasi yang sama seperti sebelumnya, tetapi kali ini format targetnya adalah CSV (Comma-Separated Values) alih‑alih XLSM.

Langkah: Mengonversi PDF ke CSV dengan Python

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
1. Buat instance [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) dengan **ExcelSaveOptions.ExcelFormat.CSV**
1. Simpan ke format **CSV** dengan memanggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)* dan memberikan [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

```python

from os import path
import aspose.pdf as apdf

def convert_pdf_to_excel_2007_csv(infile, outfile):
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

### Mengonversi ke ODS

Langkah: Mengonversi PDF ke ODS dengan Python

1. Buat instance dari objek [Dokumen](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
1. Buat sebuah instance dari [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) dengan **ExcelSaveOptions.ExcelFormat.ODS**
1. Simpan ke format **ODS** dengan memanggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dan meneruskan [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/).

Konversi ke format ODS dilakukan dengan cara yang sama seperti semua format lain.

```python

    from os import path
    import aspose.pdf as apdf
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.ExcelSaveOptions()
    save_options.format = apdf.ExcelSaveOptions.ExcelFormat.ODS
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

