---
title: "Mengonversi PDF ke PDF/A, PDF/E, dan PDF/X di Java"
linktitle: "Mengonversi PDF ke PDF/A, PDF/E, dan PDF/X"
type: docs
weight: 120
url: /id/java/convert-pdf-to-pdf_x/
lastmod: "2026-09-30"
description: Pelajari cara mengonversi file PDF ke PDF/A, PDF/E, dan PDF/X di Java dengan Aspose.PDF untuk alur kerja arsip, teknik, aksesibilitas, dan pencetakan.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: "Mengonversi PDF ke format PDF/x"
Abstract: Artikel ini menjelaskan cara memvalidasi dan mengonversi dokumen PDF ke format PDF/A, PDF/E, dan PDF/X menggunakan Aspose.PDF for Java. Artikel ini mencakup pembuatan log, pelestarian lampiran untuk PDF/A-3, substitusi font yang hilang, penandaan otomatis, konfigurasi profil ICC, dan pengaturan output intent.
---
Aspose.PDF for Java dapat memvalidasi dan mengonversi file PDF standar menjadi standar PDF arsip dan pertukaran.

## Mengonversi PDF ke PDF/A

Gunakan contoh ini ketika PDF standar harus dikonversi menjadi dokumen arsip yang mematuhi PDF/A.

1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Panggil `document.convert(...)` dengan [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_1B` dan [`ConvertErrorAction`](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction/) `Delete`.
1. Tulis log validasi ke file XML sidecar sehingga masalah kepatuhan tercatat selama konversi.
1. Simpan output PDF/A yang telah divalidasi.

```java
public static void convertPdfToPdfA(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.convert(logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_A_1B, ConvertErrorAction.Delete);
        document.save(outputFile.toString());
    }
}
```

## Mengonversi PDF ke PDF/E

Gunakan contoh ini ketika sebuah PDF harus dikonversi ke standar PDF/E yang berorientasi teknik.

1. Buat [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) untuk [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_E_1` dan jalur file log yang diinginkan.
1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Panggil `document.convert(options)` sehingga konversi kepatuhan dijalankan dengan objek opsi yang telah disiapkan.
1. Simpan file PDF yang mematuhi hasil konversi.

```java
public static void convertPdfToPdfE(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_E_1, ConvertErrorAction.Delete);

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```

## Mengonversi PDF ke PDF/X

Gunakan contoh ini ketika PDF harus dikonversi ke standar PDF/X yang berorientasi cetak.

1. Buat [`PdfFormatConversionOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) untuk [`PdfFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_X_4` dan jalur file log yang diinginkan.
1. Konfigurasikan sebuah [`OutputIntent`](https://reference.aspose.com/pdf/java/com.aspose.pdf/outputintent/) seperti `FOGRA39` jadi profil warna target cetak disematkan ke dalam pengaturan konversi.
1. Buka PDF sumber dalam sebuah instans [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) dan panggil `document.convert(options)`.
1. Simpan output PDF/X yang telah dikonversi.

```java
public static void convertPdfToPdfX(Path inputFile, Path outputFile) {
    PdfFormatConversionOptions options = new PdfFormatConversionOptions(
            logFile(outputFile, "-log.xml").toString(), PdfFormat.PDF_X_4, ConvertErrorAction.Delete);
    options.setOutputIntent(new OutputIntent("FOGRA39"));

    try (Document document = new Document(inputFile.toString())) {
        document.convert(options);
        document.save(outputFile.toString());
    }
}
```
