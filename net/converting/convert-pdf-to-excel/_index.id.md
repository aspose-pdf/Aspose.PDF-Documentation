---
title: Mengonversi PDF ke Excel di .NET
linktitle: Mengonversi PDF ke Excel
type: docs
weight: 20
url: /net/convert-pdf-to-excel/
lastmod: "2021-11-01"
keywords: mengonversi PDF ke Excel menggunakan c#, mengonversi PDF ke XLS menggunakan csharp, mengonversi PDF ke XLSX menggunakan csharp, mengekspor tabel dari PDF ke Excel dalam csharp.
description: Perpustakaan Aspose.PDF untuk .NET memungkinkan Anda untuk mengonversi PDF ke format Excel menggunakan C#. Format ini termasuk XLS, XLSX, XML 2003 Spreadsheet, CSV, ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Overview

Artikel ini menjelaskan cara **mengonversi PDF ke format Excel menggunakan C#**. Ini mencakup topik-topik berikut.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

_Format_: **XLS**

- [C# PDF ke XLS](#csharp-pdf-to-xls)
- [C# Mengonversi PDF ke XLS](#csharp-pdf-to-xls)
- [C# Cara mengonversi file PDF ke XLS](#csharp-pdf-to-xls)

_Format_: **XLSX**

- [C# PDF ke XLSX](#csharp-pdf-to-xlsx)
- [C# Mengonversi PDF ke XLSX](#csharp-pdf-to-xlsx)
- [C# Cara mengonversi file PDF ke XLSX](#csharp-pdf-to-xlsx)
- [C# Bagaimana Mengonversi Berkas PDF ke XLSX](#csharp-pdf-to-xlsx)

_Format_: **Excel**

- [C# PDF ke Excel](#csharp-pdf-to-xlsx)
- [C# PDF ke Excel XLS](#csharp-pdf-to-xls)
- [C# PDF ke Excel XLSX](#csharp-pdf-to-xlsx)

_Format_: **Single Excel Worksheet**

- [C# Mengonversi PDF ke XLS dengan Satu Lembar Kerja](#csharp-pdf-to-excel-single)
- [C# Mengonversi PDF ke XLSX dengan Satu Lembar Kerja](#csharp-pdf-to-excel-single)

_Format_: **XML Spreadsheet 2003 format**

- [C# PDF ke XML Excel](#csharp-pdf-to-excel-xml-2003)
- [C# Mengonversi PDF ke Spreadsheet XML Excel](#csharp-pdf-to-excel-xml-2003)

_Format_: **CSV**

- [C# PDF ke CSV](#csharp-pdf-to-csv)
- [C# Mengonversi PDF ke CSV](#csharp-pdf-to-csv)
- [C# Bagaimana Mengonversi Berkas PDF ke CSV](#csharp-pdf-to-csv)

_Format_: **ODS**

- [C# PDF ke ODS](#csharp-pdf-to-ods)
- [C# Mengonversi PDF ke ODS](#csharp-pdf-to-ods)
- [C# Bagaimana Mengonversi Berkas PDF ke ODS](#csharp-pdf-to-ods)

## C# Konversi PDF ke Excel

**Aspose.PDF for .NET** mendukung fitur mengonversi berkas PDF ke format Excel 2007, CSV, dan SpeadsheetML.
**Aspose.PDF untuk .NET** mendukung fitur mengonversi file PDF ke format Excel 2007, CSV, dan SpeadsheetML.

Aspose.PDF untuk .NET adalah komponen manipulasi PDF, kami telah memperkenalkan fitur yang mengonversi file PDF ke buku kerja Excel (file XLSX). Selama konversi ini, halaman-halaman individu dari file PDF diubah menjadi lembar kerja Excel.

{{% alert color="success" %}}
**Coba konversi PDF ke Excel secara online**

Aspose.PDF untuk .NET menyajikan aplikasi gratis online ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

Untuk mengonversi file PDF ke format <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF memiliki kelas yang disebut [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).
Untuk mengonversi file PDF ke format <abbr title="Microsoft Excel Open XML Spreadsheet">XLSX</abbr>, Aspose.PDF memiliki kelas yang disebut [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions).

Potongan kode berikut menunjukkan proses konversi file PDF menjadi format XLS atau XLSX dengan Aspose.PDF untuk .NET.

<a name="csharp-pdf-to-xls"><strong>Langkah: Mengonversi PDF ke XLS di C#</strong></a>

1. Buat sebuah instansi dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instansi dari **ExcelSaveOptions**.
3. Simpan dalam format **XLS** dengan menentukan **ekstensi .xls** dengan memanggil metode **Document.Save()** dan memberikannya **ExcelSaveOptions**

<a name="csharp-pdf-to-xlsx"><strong>Langkah: Mengonversi PDF ke XLSX di C#</strong></a>

1. Buat sebuah instansi dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instansi dari **ExcelSaveOptions**.
3. Simpan dalam format **XLSX** dengan menentukan **ekstensi .xlsx** dengan memanggil metode **Document.Save()** dan memberikannya **ExcelSaveOptions**

```csharp
```
## Konversi PDF ke XLS dengan Kontrol Kolom

Saat mengonversi PDF ke format XLS, kolom kosong ditambahkan ke file output sebagai kolom pertama. Opsi `InsertBlankColumnAtFirst` di kelas ExcelSaveOptions digunakan untuk mengontrol kolom ini. Nilai default adalah `false`, yang berarti kolom kosong tidak akan dimasukkan.

```csharp
public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst()
{
    // Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Muat dokumen PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");
    // Instansiasi objek Opsi Simpan Excel
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {InsertBlankColumnAtFirst = false};
    // Simpan output dalam format XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## Mengonversi PDF ke Satu Lembar Kerja Excel

Ketika mengekspor file PDF dengan banyak halaman ke XLS, setiap halaman diekspor ke lembar yang berbeda dalam file Excel. Hal ini karena properti MinimizeTheNumberOfWorksheets diatur ke false secara default. Untuk memastikan bahwa semua halaman diekspor ke satu lembar tunggal dalam file Excel keluaran, atur properti MinimizeTheNumberOfWorksheets ke true.

<a name="csharp-pdf-to-excel-single"><strong>Langkah: Mengonversi PDF ke XLS atau XLSX Satu Lembar Kerja dalam C#</strong></a>

1. Buat sebuah instansi dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instansi dari **ExcelSaveOptions** dengan **MinimizeTheNumberOfWorksheets = true**.
3. Simpan ke format **XLS** atau **XLSX** yang memiliki satu lembar kerja dengan memanggil metode **Document.Save()** dan melewatinya **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets()
{
    // Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
    // Muat dokumen PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Buat instance opsi penyimpanan Excel
    Aspose.Pdf.ExcelSaveOptions excelsave = new ExcelSaveOptions {MinimizeTheNumberOfWorksheets = true};
    // Simpan keluaran dalam format XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelsave);
}
```
## Konversi ke format spreadsheet lain

### Konversi ke format XML Spreadsheet 2003

Sejak versi 20.8 Aspose.PDF menggunakan format file Microsoft Excel Open XML Spreadsheet 2007 sebagai default untuk menyimpan data. Untuk mengubah file PDF ke format XML Spreadsheet 2003, Aspose.PDF memiliki kelas yang disebut [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) dengan [Format](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions/properties/format). Sebuah objek dari kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/excelsaveoptions) ini diberikan sebagai argumen kedua untuk metode [Document.Save(..)](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

Potongan kode berikut menunjukkan proses untuk mengonversi file PDF menjadi format XLS Excel 2003 XML.

<a name="csharp-pdf-to-excel-xml-2003"><strong>Langkah: Konversi PDF ke Format Excel 2003 XML dalam C#</strong></a>

1. Buat sebuah instansi dari objek **Document** dengan dokumen PDF sumber.
2.
Simpan dalam format **XLS - Excel 2003 XML Format** dengan memanggil metode **Document.Save()** dan memberikan **ExcelSaveOptions**.

```csharp
public static void ConvertPDFtoExcelAdvanced_SaveXLS2003()
{
    // Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Muat dokumen PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Buat objek opsi penyimpanan Excel
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003 };

    // Simpan keluaran dalam format XLS
    pdfDocument.Save("PDFToXLS_out.xls", excelSave);
}
```

### Konversi ke CSV

Konversi ke format CSV dilakukan dengan cara yang sama seperti di atas. Yang Anda perlukan hanyalah mengatur format yang sesuai.

<a name="csharp-pdf-to-csv"><strong>Langkah: Mengonversi PDF ke CSV dalam C#</strong></a>

1. Buat sebuah instance dari objek **Document** dengan dokumen PDF sumber.
2.
Simpan dalam format **CSV** dengan memanggil metode **Document.Save()** dan memberikan **ExcelSaveOptions**.

```csharp
 // Instansiasi objek ExcelSave Option
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };
```

### Konversi ke ODS

<a name="csharp-pdf-to-ods"><strong>Langkah: Konversi PDF ke ODS di C#</strong></a>

1. Buat sebuah instansi dari objek **Document** dengan dokumen PDF sumber.
2. Buat sebuah instansi dari **ExcelSaveOptions** dengan **Format = ExcelSaveOptions.ExcelFormat.ODS**
3. Simpan dalam format **ODS** dengan memanggil metode **Document.Save()** dan memberikan **ExcelSaveOptions**.

Konversi ke format ODS dilakukan dengan cara yang sama seperti format lain.

```csharp
 // Instansiasi objek ExcelSave Option
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.ODS };
```

## Lihat Juga 

Artikel ini juga mencakup topik-topik berikut. Kode-kodenya sama seperti di atas.

_Format_: **Excel**
- [Kode C# PDF ke Excel](#csharp-pdf-to-xlsx)
- [API C# PDF ke Excel](#csharp-pdf-to-xlsx)
- [API C# PDF ke Excel](#csharp-pdf-to-xlsx)
- [C# PDF ke Excel Secara Pemrograman](#csharp-pdf-to-xlsx)
- [Perpustakaan C# PDF ke Excel](#csharp-pdf-to-xlsx)
- [C# Simpan PDF sebagai Excel](#csharp-pdf-to-xlsx)
- [C# Hasilkan Excel dari PDF](#csharp-pdf-to-xlsx)
- [C# Buat Excel dari PDF](#csharp-pdf-to-xlsx)
- [Konverter C# PDF ke Excel](#csharp-pdf-to-xlsx)

_Format_: **XLS**
- [Kode C# PDF ke XLS](#csharp-pdf-to-xls)
- [API C# PDF ke XLS](#csharp-pdf-to-xls)
- [C# PDF ke XLS Secara Pemrograman](#csharp-pdf-to-xls)
- [Perpustakaan C# PDF ke XLS](#csharp-pdf-to-xls)
- [C# Simpan PDF sebagai XLS](#csharp-pdf-to-xls)
- [C# Hasilkan XLS dari PDF](#csharp-pdf-to-xls)
- [C# Buat XLS dari PDF](#csharp-pdf-to-xls)
- [Konverter C# PDF ke XLS](#csharp-pdf-to-xls)

_Format_: **XLSX**
- [Kode C# PDF ke XLSX](#csharp-pdf-to-xlsx)
- [API C# PDF ke XLSX](#csharp-pdf-to-xlsx)
- [C# PDF ke XLSX Secara Pemrograman](#csharp-pdf-to-xlsx)
- [Perpustakaan C# PDF ke XLSX](#csharp-pdf-to-xlsx)
- [C# Simpan PDF sebagai XLSX](#csharp-pdf-to-xlsx)
- [C# Hasilkan XLSX dari PDF](#csharp-pdf-to-xlsx)
- [C# Menghasilkan XLSX dari PDF](#csharp-pdf-to-xlsx)
- [C# Membuat XLSX dari PDF](#csharp-pdf-to-xlsx)
- [C# Konverter PDF ke XLSX](#csharp-pdf-to-xlsx)

_Format_: **CSV**
- [C# Kode PDF ke CSV](#csharp-pdf-to-csv)
- [C# API PDF ke CSV](#csharp-pdf-to-csv)
- [C# PDF ke CSV Secara Pemrograman](#csharp-pdf-to-csv)
- [C# Perpustakaan PDF ke CSV](#csharp-pdf-to-csv)
- [C# Simpan PDF sebagai CSV](#csharp-pdf-to-csv)
- [C# Menghasilkan CSV dari PDF](#csharp-pdf-to-csv)
- [C# Membuat CSV dari PDF](#csharp-pdf-to-csv)
- [C# Konverter PDF ke CSV](#csharp-pdf-to-csv)

_Format_: **ODS**
- [C# Kode PDF ke ODS](#csharp-pdf-to-ods)
- [C# API PDF ke ODS](#csharp-pdf-to-ods)
- [C# PDF ke ODS Secara Pemrograman](#csharp-pdf-to-ods)
- [C# Perpustakaan PDF ke ODS](#csharp-pdf-to-ods)
- [C# Simpan PDF sebagai ODS](#csharp-pdf-to-ods)
- [C# Menghasilkan ODS dari PDF](#csharp-pdf-to-ods)
- [C# Membuat ODS dari PDF](#csharp-pdf-to-ods)
- [C# Konverter PDF ke ODS](#csharp-pdf-to-ods)
