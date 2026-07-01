---
title: Konversi PDF ke Excel
linktitle: Konversi PDF ke Excel
type: docs
weight: 90
url: /id/androidjava/convert-pdf-to-excel/
lastmod: "2026-07-01"
description: Aspose.PDF for Android via Java memungkinkan Anda mengonversi PDF ke format Excel. Selama proses ini, halaman individual dari file PDF dikonversi menjadi lembar kerja Excel.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

API Aspose.PDF for Android via Java memungkinkan Anda merender file PDF Anda ke Excel [XLS](https://docs.fileformat.com/spreadsheet/xls/) dan [XLSX](https://docs.fileformat.com/spreadsheet/xlsx/) format file. Kami sudah memiliki API lain, yang dikenal sebagai [Aspose.Cells for Java](https://products.aspose.com/cells/java), yang menyediakan kemampuan untuk membuat dan memanipulasi buku kerja Excel yang ada. It juga menyediakan kemampuan untuk mengubah buku kerja Excel menjadi format PDF.

{{% alert color="primary" %}}

Coba secara daring. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara daring di tautan ini [products.aspose.app/pdf/conversion/pdf-to-xlsx](https://products.aspose.app/pdf/conversion/pdf-to-xlsx) 

{{% /alert %}}

## Konversi PDF ke Excel XLS

Untuk mengonversi file PDF ke format XLS, Aspose.PDF memiliki kelas yang disebut [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions). Sebuah objek dari [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) kelas dilewatkan sebagai argumen kedua ke konstruktor Document.Save(..) . 

Mengonversi file PDF ke format XLSX merupakan bagian dari pustaka Aspose.PDF untuk Java versi 18.6. Untuk mengonversi file PDF ke format XLSX, Anda harus mengatur format menjadi XLSX menggunakan metode setFormat() dari [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) Kelas.

Potongan kode berikut menunjukkan cara mengonversi file PDF menjadi format xls dan .xlsx:

```java
public void convertPDFtoExcelSimple() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), SaveFormat.Excel);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Konversi PDF ke XLS dengan Kolom Kontrol

Saat mengonversi PDF ke format XLS, kolom kosong ditambahkan ke file output sebagai kolom pertama. The in [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) Opsi class InsertBlankColumnAtFirst digunakan untuk mengontrol kolom ini. Nilai defaultnya adalah true.

```java
public void convertPDFtoExcelAdvanced_InsertBlankColumnAtFirst() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setInsertBlankColumnAtFirst(false);

        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS document format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

## Konversi PDF ke Lembar Kerja Excel Tunggal 

Saat mengekspor file PDF dengan banyak halaman ke XLS, setiap halaman diekspor ke lembar terpisah dalam file Excel. Hal ini terjadi karena properti MinimizeTheNumberOfWorksheets secara default diatur ke false. Untuk memastikan semua halaman diekspor ke satu lembar tunggal dalam file Excel output, atur properti MinimizeTheNumberOfWorksheets ke true.

```java
 public void convertPDFtoExcelAdvanced_MinimizeTheNumberOfWorksheets() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setMinimizeTheNumberOfWorksheets(true);

        // Save the output in XLSX
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.xlsx");
        try {
            // Save the file into MS Excel format
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

Secara default Aspose.PDF menggunakan XML Spreadsheet 2003 untuk menyimpan data. Untuk mengonversi file PDF ke format XLSX, Aspose.PDF memiliki kelas yang disebut ExcelSaveOptions dengan Format. Sebuah objek dari [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/ExcelSaveOptions) kelas tersebut dilewatkan sebagai argumen kedua ke metode Document.Save(..).

```java
 public void convertPDFtoExcelAdvanced_SaveCSV() {
        // Load PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Instantiate ExcelSave Option object
        ExcelSaveOptions excelSaveOptions = new ExcelSaveOptions();
        excelSaveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);

        // Save the output in CSV
        File xlsFileName = new File(fileStorage, "PDF-to-Excel.csv");
        try {
            // Save the file into CSV format
            document.save(xlsFileName.toString(), excelSaveOptions);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```
