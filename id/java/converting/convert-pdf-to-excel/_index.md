---
title: "Mengonversi PDF ke Excel di Java"
linktitle: "Mengonversi PDF ke Excel"
type: docs
weight: 20
url: /id/java/convert-pdf-to-excel/
lastmod: "2026-09-30"
description: Pelajari cara mengonversi file PDF ke Excel dalam Java dengan Aspose.PDF, termasuk output XML Spreadsheet 2003, XLSX, XLSM, CSV, dan ODS.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengonversi PDF ke Excel dalam Java"
Abstract: Artikel ini menjelaskan cara mengonversi file PDF ke format yang kompatibel dengan Excel menggunakan Aspose.PDF for Java. Artikel ini mencakup output XML Spreadsheet 2003, XLSX, XLSM, CSV, dan ODS, serta opsi untuk menyisipkan kolom kosong dan meminimalkan jumlah lembar kerja.
---
Aspose.PDF for Java dapat mengekspor konten PDF ke berbagai format spreadsheet dengan opsi tata letak yang berbeda. Gunakan [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) untuk memilih format buku kerja target dan mengendalikan bagaimana konten halaman dipetakan ke dalam lembar kerja dan kolom.

## Mengonversi PDF ke Excel 2003 XML

Gunakan contoh ini ketika konten PDF perlu diekspor ke format spreadsheet XML Excel 2003.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) dan atur formatnya ke `XMLSpreadSheet2003`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga PDF yang dimuat diserialkan dalam skema XML Excel 2003.
1. Simpan file output yang telah dikonversi.

```java
public static void convertPdfToExcelSpreadSheet2003(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XMLSpreadSheet2003);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke XLSX

Gunakan contoh ini ketika konten PDF harus dikonversi ke format Excel 2007+ XLSX.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) dan atur formatnya ke `XLSX`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga tata letak PDF diekspor sebagai buku kerja Office Open XML.
1. Simpan file spreadsheet output.

```java
public static void convertPdfToExcel2007(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke XLSX dengan kontrol kolom

Gunakan contoh ini ketika penanganan kolom perlu disesuaikan selama konversi PDF ke Excel.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) untuk `XLSX` keluaran.
1. Aktifkan `setInsertBlankColumnAtFirst(true)` ketika diperlukan kolom tambahan di depan untuk meningkatkan tata letak lembar kerja yang dihasilkan dari PDF.
1. Panggil `document.save(outputFile.toString(), saveOptions)` dan menulis file XLSX yang telah dikonversi.

```java
public static void convertPdfToExcel2007ControlColumn(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setInsertBlankColumnAtFirst(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke satu lembar kerja Excel

Gunakan contoh ini ketika semua halaman PDF harus diekspor ke dalam satu lembar kerja.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) untuk `XLSX` ekspor.
1. Aktifkan `setMinimizeTheNumberOfWorksheets(true)` sehingga beberapa halaman PDF dikonsolidasi menjadi lebih sedikit lembar kerja.
1. Panggil `document.save(outputFile.toString(), saveOptions)` dan simpan file output XLSX.

```java
public static void convertPdfToExcel2007SingleExcelWorksheet(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        saveOptions.setMinimizeTheNumberOfWorksheets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke XLSM

Gunakan contoh ini ketika output PDF harus disimpan sebagai buku kerja Excel yang mendukung makro.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) dan atur format ke `XLSM`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga konten PDF diekspor ke dalam kontainer workbook yang mendukung makro.
1. Simpan file XLSM.

```java
public static void convertPdfToExcel2007Macro(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.XLSM);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke CSV

Gunakan contoh ini ketika konten tabel PDF harus diekspor sebagai CSV.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) dan atur format ke `CSV`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga konten PDF diratakan menjadi output teks yang dipisahkan dengan koma.
1. Simpan file CSV yang dihasilkan.

```java
public static void convertPdfToExcel2007Csv(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.CSV);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Mengonversi PDF ke ODS

Gunakan contoh ini ketika konten PDF harus diekspor ke format spreadsheet OpenDocument.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat [`ExcelSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) dan atur format ke `ODS`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` sehingga PDF diekspor dalam format spreadsheet OpenDocument.
1. Simpan file ODS yang telah dikonversi.

```java
public static void convertPdfToOds(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions saveOptions = new ExcelSaveOptions();
        saveOptions.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
