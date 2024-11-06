---
title: Mengonversi PDF ke Excel di Python
linktitle: Mengonversi PDF ke Excel
type: docs
weight: 20
url: id/python-java/convert-pdf-to-excel/
lastmod: "2022-12-23"
keywords: mengonversi PDF ke Excel menggunakan python, mengonversi PDF ke XLS menggunakan python, mengonversi PDF ke XLSX menggunakan python, mengekspor tabel dari PDF ke Excel di python.
description: Aspose.PDF untuk pustaka Python memungkinkan Anda untuk mengonversi PDF ke format Excel menggunakan Python. Format ini termasuk XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ikhtisar

Artikel ini menjelaskan cara **mengonversi PDF ke format Excel menggunakan Python**. Ini mencakup topik berikut.

_Format_: **XLS**
- [Python PDF ke XLS](#python-pdf-to-xls)
- [Python Mengonversi PDF ke XLS](#python-pdf-to-xls)
- [Python Cara mengonversi file PDF ke XLS](#python-pdf-to-xls)

_Format_: **XLSX**
- [Python PDF ke XLSX](#python-pdf-to-xlsx)
- [Python Mengonversi PDF ke XLSX](#python-pdf-to-xlsx)
- [Python Cara mengonversi file PDF ke XLSX](#python-pdf-to-xlsx)

_Format_: **Excel**
- [Python PDF ke Excel](#python-pdf-to-xlsx)
- [Python PDF ke Excel XLS](#python-pdf-to-xls)
- [Python PDF ke Excel XLSX](#python-pdf-to-xlsx)

_Format_: **CSV**
- [Python PDF ke CSV](#python-pdf-to-csv)
- [Python Mengonversi PDF ke CSV](#python-pdf-to-csv)
- [Python Cara mengonversi file PDF ke CSV](#python-pdf-to-csv)

_Format_: **ODS**
- [Python PDF ke ODS](#python-pdf-to-ods)
- [Python Mengonversi PDF ke ODS](#python-pdf-to-ods)
- [Python Cara mengonversi file PDF ke ODS](#python-pdf-to-ods)

## Konversi PDF ke EXCEL melalui Python

**Aspose.PDF untuk Python melalui .NET** mendukung fitur mengonversi file PDF ke Excel, dan format CSV.

Aspose.PDF untuk Python melalui Java adalah komponen manipulasi PDF, kami telah memperkenalkan fitur yang merender file PDF ke buku kerja Excel (file XLSX). Selama konversi ini, halaman individu dari file PDF diubah menjadi lembar kerja Excel.

{{% alert color="success" %}}
**Coba konversi PDF ke Excel secara online**

Aspose.PDF mempersembahkan aplikasi online gratis ["PDF ke XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Cuplikan kode berikut menunjukkan proses konversi file PDF ke format XLS atau XLSX dengan Aspose.PDF untuk Python via Java.

<a name="python-pdf-to-xls"><strong>Langkah-langkah: Mengonversi PDF ke XLS di Python</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Buat instance [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Simpan ke format **XLS** dengan menentukan **ekstensi .xls** dengan memanggil metode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) dan melewatkan [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python



from asposepdf import Api


# inisialisasi lisensi
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# konversi dari array byte
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result1.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)

# konversi dari file
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result2.xls"
doc.save(documentOutName, Api.SaveFormat.Excel)


# konversi dari array byte
documentName = "testdata/source.pdf"
with open(documentName, "rb") as file:
    byte_array = file.read()
doc = Api.Document(byte_array)
documentOutName = "testout/result3.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)

# konversi dari file
documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result4.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
doc.save(documentOutName, Api.SaveFormat.Excel)
```


<a name="python-pdf-to-xlsx"><strong>Langkah-langkah: Mengonversi PDF ke XLSX dalam Python</strong></a>

1. Buat instance dari objek [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Buat instance dari [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).
3. Simpan ke format **XLSX** dengan menentukan **ekstensi .xlsx** dengan memanggil metode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) dan meneruskannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
doc.save(documentOutName, save_option)
```

## Konversi PDF ke XLS dengan kontrol Kolom

Saat mengonversi PDF ke format XLS, kolom kosong ditambahkan ke file keluaran sebagai kolom pertama.
 Opsi InsertBlankColumnAtFirst dalam 'kelas ExcelSaveOptions' digunakan untuk mengontrol kolom ini. Nilai defaultnya adalah true.

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xlsx"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._insertBlankColumnAtFirst = True
doc.save(documentOutName, save_option)

```

## Konversi PDF ke Satu Lembar Kerja Excel

Saat mengekspor file PDF dengan banyak halaman ke XLS, setiap halaman diekspor ke lembar yang berbeda dalam file Excel. Ini karena properti MinimizeTheNumberOfWorksheets diatur ke false secara default. Untuk memastikan bahwa semua halaman diekspor ke satu lembar dalam file Excel keluaran, atur properti MinimizeTheNumberOfWorksheets ke true.

<a name="python-pdf-to-excel-single"><strong>Langkah-langkah: Konversi PDF ke Lembar Kerja XLS atau XLSX Tunggal di Python</strong></a>
1. Buat sebuah instance dari objek [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Buat sebuah instance dari [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) dengan **MinimizeTheNumberOfWorksheets = True**.
3. Simpan ke format **XLS** atau **XLSX** dengan lembar kerja tunggal dengan memanggil metode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) dan melewatkannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.xls"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003
save_option._minimizeTheNumberOfWorksheets = True
# Simpan file ke dalam format MS Excel
doc.save(documentOutName, save_option)

```

## Konversi ke format spreadsheet lainnya

### Konversi ke CSV

Konversi ke format CSV dilakukan dengan cara yang sama seperti di atas. Yang perlu Anda lakukan - tetapkan format yang sesuai.

<a name="python-pdf-to-csv"><strong>Langkah-langkah: Konversi PDF ke CSV di Python</strong></a>

1. Buat instance objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Buat instance dari [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) dengan **Format = ExcelSaveOptions.ExcelFormat.CSV**
3. Simpan ke format **CSV** dengan memanggil metode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) dan melewatkannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).


```python

from asposepdf import Api

documentName = "testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/result.csv"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.CSV
doc.save(documentOutName, save_option)
```


### Konversi ke ODS

<a name="python-pdf-to-ods"><strong>Langkah-langkah: Konversi PDF ke ODS di Python</strong></a>

1. Buat instance dari objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan dokumen PDF sumber.
2. Buat instance dari [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/) dengan **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Simpan ke format **ODS** dengan memanggil metode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) dan meneruskannya [ExcelSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/excelsaveoptions/).

Konversi ke format ODS dilakukan dengan cara yang sama seperti semua format lainnya.

```python

from asposepdf import Api

documentName = "../../testdata/source.pdf"
doc = Api.Document(documentName)
documentOutName = "../../testout/result1.ods"
save_option = Api.ExcelSaveOptions()
save_option._format = Api.ExcelSaveOptions.ExcelFormat.ODS
doc.save(documentOutName, save_option)
```


## Lihat Juga

Artikel ini juga mencakup topik-topik ini. Kode-kodenya sama seperti di atas.

_Format_: **Excel**
- [Kode Python PDF ke Excel](#python-pdf-to-xlsx)
- [API Python PDF ke Excel](#python-pdf-to-xlsx)
- [Python PDF ke Excel Secara Programatik](#python-pdf-to-xlsx)
- [Perpustakaan Python PDF ke Excel](#python-pdf-to-xlsx)
- [Python Simpan PDF sebagai Excel](#python-pdf-to-xlsx)
- [Python Hasilkan Excel dari PDF](#python-pdf-to-xlsx)
- [Python Buat Excel dari PDF](#python-pdf-to-xlsx)
- [Pengonversi Python PDF ke Excel](#python-pdf-to-xlsx)

_Format_: **XLS**
- [Kode Python PDF ke XLS](#python-pdf-to-xls)
- [API Python PDF ke XLS](#python-pdf-to-xls)
- [Python PDF ke XLS Secara Programatik](#python-pdf-to-xls)
- [Perpustakaan Python PDF ke XLS](#python-pdf-to-xls)
- [Python Simpan PDF sebagai XLS](#python-pdf-to-xls)
- [Python Hasilkan XLS dari PDF](#python-pdf-to-xls)
- [Python Buat XLS dari PDF](#python-pdf-to-xls)
- [Pengonversi Python PDF ke XLS](#python-pdf-to-xls)

_Format_: **XLSX**

- [Kode Python PDF ke XLSX](#python-pdf-to-xlsx)
- [API Python PDF ke XLSX](#python-pdf-to-xlsx)
- [Program Python PDF ke XLSX](#python-pdf-to-xlsx)
- [Library Python PDF ke XLSX](#python-pdf-to-xlsx)
- [Simpan PDF sebagai XLSX dengan Python](#python-pdf-to-xlsx)
- [Hasilkan XLSX dari PDF dengan Python](#python-pdf-to-xlsx)
- [Buat XLSX dari PDF dengan Python](#python-pdf-to-xlsx)
- [Konverter PDF ke XLSX dengan Python](#python-pdf-to-xlsx)

_Format_: **CSV**
- [Kode Python PDF ke CSV](#python-pdf-to-csv)
- [API Python PDF ke CSV](#python-pdf-to-csv)
- [Program Python PDF ke CSV](#python-pdf-to-csv)
- [Library Python PDF ke CSV](#python-pdf-to-csv)
- [Simpan PDF sebagai CSV dengan Python](#python-pdf-to-csv)
- [Hasilkan CSV dari PDF dengan Python](#python-pdf-to-csv)
- [Buat CSV dari PDF dengan Python](#python-pdf-to-csv)
- [Konverter PDF ke CSV dengan Python](#python-pdf-to-csv)

_Format_: **ODS**
- [Kode Python PDF ke ODS](#python-pdf-to-ods)
- [API Python PDF ke ODS](#python-pdf-to-ods)
- [Program Python PDF ke ODS](#python-pdf-to-ods)
- [Library Python PDF ke ODS](#python-pdf-to-ods)

- [Simpan PDF sebagai ODS dengan Python](#python-pdf-to-ods)
- [Python Menghasilkan ODS dari PDF](#python-pdf-to-ods)
- [Python Membuat ODS dari PDF](#python-pdf-to-ods)
- [Pengonversi PDF ke ODS Python](#python-pdf-to-ods)