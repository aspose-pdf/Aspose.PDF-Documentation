---
title: Convert PDF to Excel 
linktitle: Convert PDF to Excel 
type: docs
weight: 90
url: /androidjava/convert-pdf-to-excel/
lastmod: "2021-06-05"
description: Aspose.PDF untuk Android melalui Java memungkinkan Anda mengonversi PDF ke format Excel. Selama ini, halaman individu dari file PDF dikonversi ke lembar kerja Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF untuk Android melalui API Java memungkinkan Anda merender file PDF Anda ke format file Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) dan [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/). Kami sudah memiliki API lain, yang dikenal sebagai [Aspose.Cells for Java](https://products.aspose.com/cells/java), yang menyediakan kemampuan untuk membuat dan memanipulasi buku kerja Excel yang ada. Ini juga menyediakan kemampuan untuk mengubah buku kerja Excel ke format PDF.

{{% alert color="primary" %}}

Coba online.
 Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)

{{% /alert %}}

## Konversi PDF ke Excel XLS

Untuk mengonversi file PDF ke format XLS, Aspose.PDF memiliki kelas bernama [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Sebuah objek dari kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) diteruskan sebagai argumen kedua ke konstruktor Document.Save(..).

Mengonversi file PDF ke format XLSX adalah bagian dari pustaka dari Aspose.PDF untuk versi Java 18.6. Untuk mengonversi file PDF ke format XLSX, Anda perlu mengatur format sebagai XLSX menggunakan metode setFormat() dari Kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions).

Cuplikan kode berikut menunjukkan cara mengonversi file PDF menjadi format xls dan .xlsx:

```java
public void convertPDFtoExcelSimple() {
        // Buka dokumen PDF sumber
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Inisialisasi objek ExcelSave Option
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Simpan file ke dalam format dokumen MS
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Konversi PDF ke XLS dengan Kontrol Kolom

Saat mengonversi PDF ke format XLS, kolom kosong ditambahkan ke file output sebagai kolom pertama. Opsi InsertBlankColumnAtFirst dalam kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) digunakan untuk mengontrol kolom ini. Nilai defaultnya adalah true.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Buka dokumen PDF sumber
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instansiasi objek ExcelSave Option
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Simpan file dalam format dokumen MS
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Mengonversi PDF ke Lembar Kerja Excel Tunggal

Ketika mengekspor file PDF dengan banyak halaman ke XLS, setiap halaman diekspor ke lembar yang berbeda dalam file Excel. Ini karena properti MinimizeTheNumberOfWorksheets diatur ke false secara default. Untuk memastikan bahwa semua halaman diekspor ke satu lembar tunggal dalam file Excel keluaran, atur properti MinimizeTheNumberOfWorksheets ke true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Buka dokumen PDF sumber
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instansiasi objek ExcelSave Option
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Simpan keluaran dalam format XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Simpan file ke dalam format MS Excel
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }

```


## Konversi ke format XLSX

Secara default, Aspose.PDF menggunakan XML Spreadsheet 2003 untuk menyimpan data. Untuk mengonversi file PDF ke format XLSX, Aspose.PDF memiliki kelas bernama ExcelSaveOptions dengan Format. Sebuah objek dari kelas [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) dilewatkan sebagai argumen kedua ke metode Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Muat dokumen PDF
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instansiasi objek ExcelSave Option
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Simpan keluaran dalam CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Simpan file ke dalam format CSV
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```