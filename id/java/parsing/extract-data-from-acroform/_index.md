---
title: "Mengekstrak data dari AcroForm menggunakan Java"
linktitle: "Mengekstrak data dari AcroForm"
type: docs
weight: 50
url: /id/java/extract-data-from-acroform/
description: Aspose.PDF memudahkan mengekstrak data bidang formulir dari file PDF. Pelajari cara mengekstrak data dari AcroForms dan menyimpannya ke dalam format JSON, XML, atau FDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengekstrak data dari AcroForm melalui Java"
Abstract: Artikel ini menjelaskan cara mengekstrak dan mengekspor data AcroForm dari file PDF dengan Aspose.PDF for Java. Ini mencakup membaca semua bidang formulir, mengambil nilai bidang berdasarkan nama, mengekspor data bidang ke JSON, dan menulis data formulir ke format XML, FDF, dan XFDF.
---

## Mengekstrak bidang formulir dari dokumen PDF

Gunakan `com.aspose.pdf.facades.Form` untuk membaca nama bidang dan nilai tanpa melalui model objek dokumen secara lengkap.

1. Buka formulir PDF sumber dengan fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) sehingga bidang AcroForm dapat dibaca tanpa menelusuri seluruh model objek dokumen.
1. Panggil `getFieldNames()` untuk mengumpulkan semua pengidentifikasi bidang yang ada di formulir.
1. Iterasikan melalui nama-nama bidang tersebut dan panggil `getField(fieldName)` untuk membaca setiap nilai bidang.
1. Bangun string output dari pasangan kunci-nilai yang diekstrak dan cetak data formulir yang teragregasi.
1. Tutup fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) dalam blok `finally`.

```java
public static void extractFormFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder formValues = new StringBuilder("{");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            if (i > 0) {
                formValues.append(", ");
            }
            formValues.append(fieldNames[i]).append("=").append(form.getField(fieldNames[i]));
        }
        formValues.append("}");
        System.out.println(formValues);
    } finally {
        form.close();
    }
}
```

## Mengambil nilai bidang formulir berdasarkan nama

Ketika Anda mengetahui nama bidang yang tepat yang didefinisikan dalam formulir PDF, Anda dapat mengambil nilainya secara langsung dengan `getField(fieldName)`
tanpa mengiterasi seluruh koleksi bidang.

1. Buka formulir PDF sumber dengan fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Panggil `getField(fieldName)` dengan nama bidang yang diminta untuk membaca nilai saat ini dari data AcroForm.
1. Cetak nilai bidang yang diekstrak.
1. Tutup fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) dalam blok `finally`.

```java
public static void extractFormFieldByTitle(Path inputFile, String fieldName) {
    Form form = new Form(inputFile.toString());
    try {
        String formValue = form.getField(fieldName);
        System.out.println(formValue);
    } finally {
        form.close();
    }
}
```

## Mengekstrak bidang formulir dari dokumen PDF ke JSON

Nilai bidang formulir juga dapat diekstrak dan disimpan sebagai JSON. Ini berguna ketika data formulir PDF perlu dikonsumsi oleh
aplikasi web, API, atau sistem lain yang bekerja dengan JSON.

1. Buka formulir PDF sumber dengan fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/).
1. Panggil `getFieldNames()` untuk mengumpulkan semua pengidentifikasi bidang yang tersedia dari AcroForm.
1. Iterasikan melalui bidang-bidang tersebut, escape nama dan nilai, dan bangun string objek JSON.
1. Tuliskan hasil JSON ke file output.
1. Tutup fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) dalam blok `finally`.

```java
public static void extractFormFieldsJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```

## Mengekspor data formulir ke XML dari file PDF

Ekspor XML berguna ketika data formulir PDF perlu dikonsumsi oleh sistem yang bekerja dengan data XML terstruktur.

1. Buat fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) tanpa mengikat dokumen terlebih dahulu.
1. Buka aliran output untuk file XML dan hubungkan PDF sumber ke fasad dengan `bindPdf(...)`.
1. Panggil `exportXml(stream)` sehingga data bidang formulir saat ini diserialkan sebagai XML.
1. Tutup fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) setelah ekspor selesai.

```java
public static void extractDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## Mengekspor data ke FDF dari file PDF

FDF (Forms Data Format) biasanya digunakan untuk menukar data bidang AcroForm secara independen dari dokumen PDF.

1. Buat fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) tanpa mengikat dokumen terlebih dahulu.
1. Buka aliran output untuk file FDF dan ikat PDF sumber ke fasad dengan `bindPdf(...)`.
1. Panggil `exportFdf(stream)` sehingga data bidang formulir diserialkan dalam format FDF.
1. Tutup fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) setelah ekspor selesai.

```java
public static void extractDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## Mengekspor data ke XFDF dari file PDF

XFDF adalah representasi berbasis XML dari Forms Data Format dan memudahkan pertukaran data formulir dengan sistem yang bekerja dengan XML.

1. Buat fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) tanpa mengikat dokumen terlebih dahulu.
1. Buka aliran output untuk file XFDF dan kaitkan PDF sumber ke antarmuka dengan `bindPdf(...)`.
1. Panggil `exportXfdf(stream)` sehingga data bidang formulir diserialkan dalam format XFDF.
1. Tutup fasad [`Form`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) setelah ekspor selesai.

```java
public static void extractDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```
