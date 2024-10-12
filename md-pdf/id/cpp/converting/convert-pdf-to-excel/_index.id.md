```
---
title: Mengonversi PDF ke Excel dalam C++
linktitle: Mengonversi PDF ke Excel
type: docs
weight: 20
url: /cpp/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF untuk C++ memungkinkan Anda mengonversi PDF ke format Excel menggunakan C++. Selama ini, halaman-halaman individual dari file PDF dikonversi menjadi lembar kerja Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ikhtisar

Artikel ini menjelaskan bagaimana **mengonversi PDF ke format Excel menggunakan C++**. Ini mencakup topik-topik berikut.

_Format_: **XLS**
- [C++ PDF ke XLS](#cpp-pdf-to-xls)
- [C++ Mengonversi PDF ke XLS](#cpp-pdf-to-xls)
- [C++ Cara mengonversi file PDF ke XLS](#cpp-pdf-to-xls)

_Format_: **XLSX**
- [C++ PDF ke XLSX](#cpp-pdf-to-xlsx)
- [C++ Mengonversi PDF ke XLSX](#cpp-pdf-to-xlsx)
- [C++ Cara mengonversi file PDF ke XLSX](#cpp-pdf-to-xlsx)

_Format_: **Format Microsoft Excel XLS**
- [C++ PDF ke Excel](#cpp-pdf-to-excel-xls)
- [C++ Mengonversi PDF ke Excel](#cpp-pdf-to-excel-xls)
- [C++ Cara mengonversi file PDF ke Excel](#cpp-pdf-to-excel-xls)


_Format_: **Format Microsoft Excel XLSX**
```
- [C++ PDF ke Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Konversi PDF ke Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Cara mengonversi file PDF ke Excel](#cpp-pdf-to-excel-xlsx)

Topik lain yang dibahas dalam artikel ini
- [Lihat Juga](#see-also)

## Konversi C++ PDF ke Excel

**Aspose.PDF untuk C++** mendukung fitur konversi file PDF ke format Excel.

Aspose.PDF untuk C++ adalah komponen manipulasi PDF, kami telah memperkenalkan fitur yang merender file PDF ke buku kerja Excel (file XLS). Selama konversi ini, halaman-halaman individu dari file PDF dikonversi menjadi lembar kerja Excel.

Untuk mengonversi file PDF ke format <abbr title="Microsoft Excel Spreadsheet">XLS</abbr>, Aspose.PDF memiliki kelas bernama ExcelSaveOptions. Sebuah objek dari kelas ExcelSaveOptions diteruskan sebagai argumen kedua ke konstruktor Document.Save(..).

Cuplikan kode berikut menunjukkan proses konversi file PDF menjadi format XLS dengan Aspose.PDF untuk C++.


<a name="cpp-pdf-to-xls" id="cpp-pdf-to-xls"><strong>Langkah: Konversi PDF ke XLS dalam C++</strong></a> | <a name="cpp-pdf-to-excel-xls" id="cpp-pdf-to-excel-xls"><strong>Langkah: Konversi PDF ke format Excel XLS dalam C++</strong></a>

1. Buat instance dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan dokumen PDF sumber.
2. Simpan ke format _XLS_ dengan memanggil metode **Document->Save()**.

```cpp
void ConvertPDFtoExcel()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Simpan output dalam format XLS
    document->Save(_dataDir + outfilename, SaveFormat::Excel);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Konversi PDF ke XLS dengan Kontrol Kolom

Ketika mengonversi PDF ke format XLS, kolom kosong ditambahkan ke file output sebagai kolom pertama. Opsi InsertBlankColumnAtFirst dalam kelas ExcelSaveOptions digunakan untuk mengendalikan kolom ini. Nilai defaultnya adalah true.

```cpp
void ConvertPDFtoExcel_Advanced_InsertBlankColumnAtFirst()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();

    // Opsi InsertBlankColumnAtFirst dalam kelas ExcelSaveOptions digunakan untuk mengendalikan kolom ini. Nilai defaultnya adalah true.
    excelSave->set_InsertBlankColumnAtFirst(false);

    // Simpan keluaran dalam format XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Konversi PDF ke Lembar Kerja Excel Tunggal

Ketika mengekspor file PDF dengan banyak halaman ke XLS, setiap halaman diekspor ke lembar yang berbeda dalam file Excel. Dokumen ini karena properti MinimizeTheNumberOfWorksheets diatur ke false secara default. Untuk memastikan bahwa semua halaman diekspor ke satu lembar tunggal dalam file Excel output, atur properti MinimizeTheNumberOfWorksheets ke true.

```cpp
void ConvertPDFtoExcel_Advanced_MinimizeTheNumberOfWorksheets()
{
    std::clog << __func__ << ": Mulai" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_MinimizeTheNumberOfWorksheets(true);

    // Simpan output dalam format XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Selesai" << std::endl;
}
```

## Konversi ke format XLSX

Secara default Aspose.PDF menggunakan XML Spreadsheet 2003 untuk menyimpan data. Untuk mengonversi file PDF ke format XLSX, Aspose.PDF memiliki kelas bernama [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) dengan 'Format'. Sebuah objek dari kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) diteruskan sebagai argumen kedua ke metode [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

Cuplikan kode berikut menunjukkan proses untuk mengonversi file PDF menjadi format XLSX.

<a name="cpp-pdf-to-xlsx" id="cpp-pdf-to-xlsx"><strong>Langkah-langkah: Mengonversi PDF ke XLSX dalam C++</strong></a> | <a name="cpp-pdf-to-excel-xlsx" id="cpp-pdf-to-excel-xlsx"><strong>Langkah-langkah: Mengonversi PDF ke format Excel XLSX dalam C++</strong></a>

1. Buat sebuah instance dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) dengan dokumen PDF sumber.
2. Buat instance dari [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options).
3. Atur format sebagai _ExcelSaveOptions::ExcelFormat::XLSX_.
4. Simpan ke format _XLSX_ dengan memanggil metode **Document->Save()** dan melewatkan instance dari _ExcelSaveOptions_.

```cpp
void ConvertPDFtoExcel_Advanced_SaveXLSX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Conversion\\");

    // String untuk nama file
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);

    // Simpan output dalam format XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}

**Coba konversi PDF ke Excel secara online**
Aspose.PDF for C++ menyajikan aplikasi online gratis ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba untuk menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Lihat Juga

Artikel ini juga mencakup topik-topik berikut. Kode-kodenya sama seperti di atas.

_Format_: **Format Microsoft Excel XLS**
- [C++ PDF ke Excel XLS Code](#cpp-pdf-to-excel-xls)
- [C++ PDF ke Excel XLS Secara Program](#cpp-pdf-to-excel-xls)
- [C++ PDF ke Excel XLS Library](#cpp-pdf-to-excel-xls)
- [C++ Simpan PDF sebagai Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ Hasilkan Excel XLS dari PDF](#cpp-pdf-to-excel-xls)
- [C++ Buat Excel XLS dari PDF](#cpp-pdf-to-excel-xls)
- [C++ PDF ke Excel XLS Converter](#cpp-pdf-to-excel-xls)

_Format_: **Format Microsoft Excel XLSX**
- [C++ PDF ke Excel XLSX Code](#cpp-pdf-to-excel-xlsx)

- [C++ PDF ke Excel XLSX Secara Program](#cpp-pdf-to-excel-xlsx)
- [Perpustakaan C++ PDF ke Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ Simpan PDF sebagai Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ Hasilkan Excel XLSX dari PDF](#cpp-pdf-to-excel-xlsx)
- [C++ Buat Excel XLSX dari PDF](#cpp-pdf-to-excel-xlsx)
- [Konverter C++ PDF ke Excel XLSX](#cpp-pdf-to-excel-xlsx)

_Format_: **XLS**
- [Kode C++ PDF ke XLS](#cpp-pdf-to-xls)
- [C++ PDF ke XLS Secara Program](#cpp-pdf-to-xls)
- [Perpustakaan C++ PDF ke XLS](#cpp-pdf-to-xls)
- [C++ Simpan PDF sebagai XLS](#cpp-pdf-to-xls)
- [C++ Hasilkan XLS dari PDF](#cpp-pdf-to-xls)
- [C++ Buat XLS dari PDF](#cpp-pdf-to-xls)
- [Konverter C++ PDF ke XLS](#cpp-pdf-to-xls)

_Format_: **XLSX**
- [Kode C++ PDF ke XLSX](#cpp-pdf-to-xlsx)
- [C++ PDF ke XLSX Secara Program](#cpp-pdf-to-xlsx)
- [Perpustakaan C++ PDF ke XLSX](#cpp-pdf-to-xlsx)
- [C++ Simpan PDF sebagai XLSX](#cpp-pdf-to-xlsx)
- [C++ Hasilkan XLSX dari PDF](#cpp-pdf-to-xlsx)
- [C++ Buat XLSX dari PDF](#cpp-pdf-to-xlsx)
- [Konverter C++ PDF ke XLSX](#cpp-pdf-to-xlsx)