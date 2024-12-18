---
title: Mengkonversi PDF ke Excel 
linktitle: Mengkonversi PDF ke Excel
type: docs
weight: 20
url: /id/java/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF untuk Java memungkinkan Anda mengkonversi PDF ke format Excel menggunakan java. Selama ini, halaman individu dari file PDF dikonversi ke lembar kerja Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF untuk Java API memungkinkan Anda merender file PDF Anda ke format file Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) dan [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Kami sudah memiliki API lain, yang dikenal sebagai [Aspose.Cells untuk Java](https://products.aspose.com/cells/java), yang menyediakan kemampuan untuk membuat dan memanipulasi workbook Excel yang ada. Ini juga menyediakan kemampuan untuk mengubah workbook Excel ke format PDF.

{{% alert color="primary" %}}

**Coba mengkonversi PDF ke Excel secara online**

Aspose.PDF for Java menghadirkan aplikasi online gratis ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Excel dengan Aplikasi Gratis](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Mengonversi PDF ke Excel XLS

Untuk mengonversi file PDF ke format XLS, Aspose.PDF memiliki kelas yang disebut [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Sebuah objek dari kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) diteruskan sebagai argumen kedua ke metode Document.Save(..).

Mengonversi file PDF ke format XLSX adalah bagian dari pustaka dari Aspose.PDF untuk versi Java 18.6. Untuk mengonversi file PDF ke format XLSX, Anda perlu mengatur format sebagai XLSX menggunakan metode setFormat() dari Kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Cuplikan kode berikut menunjukkan cara mengonversi file PDF menjadi format xls dan .xlsx:

```java
package com.aspose.pdf.examples;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

import com.aspose.pdf.*;

public final class ConvertPDFtoXLSX {

    private ConvertPDFtoXLSX() {

    }

    // Jalur ke direktori dokumen.
    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) throws IOException {

        ConvertPDFtoExcelSimple();
        ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst();
        ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets();
        ConvertPDFtoExcelAdvanced_SaveXLSX();
    }

    public static void ConvertPDFtoExcelSimple() {
        // Memuat dokumen PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Membuat objek ExcelSave Option
        ExcelSaveOptions excelsave = new ExcelSaveOptions();

        // Simpan keluaran dalam format XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
}
```

## Mengonversi PDF ke XLS dengan Kolom Kontrol

Ketika mengonversi PDF ke format XLS, kolom kosong ditambahkan ke file keluaran sebagai kolom pertama. Opsi InsertBlankColumnAtFirst dalam kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) digunakan untuk mengontrol kolom ini. Nilai defaultnya adalah true.

```java
    public static void ConvertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Memuat dokumen PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // Memeriksa objek Opsi ExcelSave
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setInsertBlankColumnAtFirst(false);
        // Menyimpan keluaran dalam format XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## Mengonversi PDF ke Satu Lembar Kerja Excel

Ketika mengekspor file PDF dengan banyak halaman ke XLS, setiap halaman diekspor ke lembar berbeda dalam file Excel.
 Ini karena properti MinimizeTheNumberOfWorksheets diatur ke false secara default. Untuk memastikan bahwa semua halaman diekspor ke satu lembar dalam file Excel keluaran, atur properti MinimizeTheNumberOfWorksheets ke true.

```java
    public static void ConvertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Memuat dokumen PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Memuat objek ExcelSave Option
        ExcelSaveOptions excelsave = new ExcelSaveOptions();
        excelsave.setMinimizeTheNumberOfWorksheets(true);

        // Menyimpan keluaran dalam format XLS
        pdfDocument.save("PDFToXLS_out.xls", excelsave);
    }
```

## Konversi ke format XLSX

Secara default Aspose.PDF menggunakan XML Spreadsheet 2003 untuk menyimpan data. Untuk mengonversi file PDF ke format XLSX, Aspose.PDF memiliki kelas bernama ExcelSaveOptions dengan Format. Sebuah objek dari kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) diberikan sebagai argumen kedua untuk metode Document.Save(..).

```java
    public static void ConvertPDFtoExcelAdvanced_SaveXLSX() {
        // Muat dokumen PDF
        Document pdfDocument = new Document(_dataDir + "input.pdf");

        // Instansiasi objek ExcelSave Option
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);

        // Simpan keluaran dalam format XLS
        pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
    }
```