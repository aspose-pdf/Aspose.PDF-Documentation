---
title: Konversi PDF ke Word di Java
linktitle: Konversi PDF ke Word
type: docs
weight: 10
url: /id/java/convert-pdf-to-word/
lastmod: "2026-09-29"
description: Pelajari cara mengonversi file PDF ke DOC dan DOCX dalam Java dengan Aspose.PDF untuk pengeditan dokumen yang lebih mudah dan penggunaan kembali.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara Mengonversi PDF ke Word dalam Java
Abstract: Artikel ini menjelaskan cara mengonversi file PDF ke format Microsoft Word menggunakan Aspose.PDF for Java. Artikel ini mencakup output DOC, output DOCX, konversi DOCX aliran‑tinggi, menjaga jeda baris, pengenalan bullet, dan kontrol resolusi gambar melalui `DocSaveOptions`.
---
Aspose.PDF for Java dapat mengekspor dokumen PDF ke format Microsoft Word dengan berbagai opsi pengenalan dan tata letak. Gunakan [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) untuk mengontrol bagaimana teks PDF, daftar, dan gambar dipetakan ke output Word.

## Konversi PDF ke DOC

Gunakan contoh ini ketika dokumen PDF harus diekspor ke format DOC lama. Kode tersebut membuat `DocSaveOptions`, mengatur format ke `Doc`, dan meneruskan opsi ke metode penyimpanan bersama.

1. Buka PDF sumber di a [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) contoh.
1. Buat [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) dan atur format ke `Doc`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` jadi PDF diekspor ke format dokumen biner Microsoft Word.
1. Simpan file DOC yang telah dikonversi.

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Konversi PDF ke DOCX

Gunakan contoh ini ketika dokumen PDF harus diekspor sebagai file DOCX. DOCX adalah format yang lebih disukai untuk sebagian besar alur kerja pengolahan kata baru karena didukung secara luas dan lebih mudah diedit.

1. Buka PDF sumber di a [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) contoh.
1. Buat [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) dan atur format ke `DocX`.
1. Panggil `document.save(outputFile.toString(), saveOptions)` jadi konten PDF diekspor sebagai dokumen Word Office Open XML.
1. Simpan file DOCX yang dihasilkan.

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Konversi PDF ke DOCX dengan pengenalan alur yang ditingkatkan

Gunakan contoh ini ketika ekspor Word seharusnya memprioritaskan konten yang dapat diedit secara mengalir daripada tata letak visual yang tetap.

1. Buka PDF sumber di a [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) contoh.
1. Buat [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) untuk `DocX` output.
1. Aktifkan `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` jadi konverter menggunakan pengenalan aliran yang ditingkatkan selama pembuatan DOCX.
1. Panggil `document.save(outputFile.toString(), saveOptions)` dan simpan output DOCX yang telah dikonversi.

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Konversi PDF ke DOCX dengan mempertahankan jeda baris

Gunakan contoh ini ketika akhir baris dari PDF sumber harus dipertahankan dalam output Word.

1. Buka PDF sumber di a [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) contoh.
1. Buat [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) untuk `DocX` ekspor.
1. Aktifkan `setAddReturnToLineEnd(true)` sehingga jeda baris eksplisit dipertahankan selama konversi.
1. Panggil `document.save(outputFile.toString(), saveOptions)` dan simpan file DOCX.

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Konversi PDF ke DOCX dengan pengenalan bullet

Gunakan contoh ini ketika bullet daftar dari PDF sumber harus dikenali dan dipertahankan sebagai struktur daftar di Word.

1. Buka PDF sumber di a [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) contoh.
1. Buat [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) untuk `DocX` ekspor.
1. Aktifkan `setRecognizeBullets(true)` sehingga konten PDF yang mirip daftar dikenali sebagai daftar bullet selama konversi.
1. Panggil `document.save(outputFile.toString(), saveOptions)` dan simpan file DOCX.

```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Konversi PDF ke DOCX dengan resolusi gambar khusus

Gunakan contoh ini ketika fidelitas gambar dalam DOCX yang dihasilkan harus dikontrol selama konversi.

1. Buka PDF sumber di a [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) contoh.
1. Buat [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) untuk `DocX` ekspor.
1. Atur `setImageResolutionX(300)` dan `setImageResolutionY(300)` jadi konten raster dihasilkan pada resolusi yang diminta.
1. Panggil `document.save(outputFile.toString(), saveOptions)` dan simpan output DOCX.

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
