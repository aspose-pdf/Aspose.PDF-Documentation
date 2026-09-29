---
title: Membaca Nilai Form
linktitle: Membaca Nilai Form
type: docs
weight: 60
url: /id/java/reading-form-values/
description: Pelajari cara memeriksa nama bidang Form PDF dan nilai-nilainya di Java menggunakan Form facade di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Baca nama bidang Form PDF dan nilai-nilainya di Java
Abstract: Bagian ini mencakup alur kerja pembacaan Form Java yang diimplementasikan dalam set contoh Form facade saat ini untuk Aspose.PDF for Java. Repository menyediakan contoh inspeksi bidang umum dan menggunakan catatan ruang lingkup eksplisit untuk halaman khusus yang belum memiliki contoh Java yang cocok.
---
Java `FormExamples` kelas menunjukkan alur kerja pemrosesan formulir utama yang diungkapkan oleh API Facades.

## Dapatkan Nilai Bidang

Gunakan `FormExamples.inspectFormFields(...)` untuk memeriksa nama field dan nilai mereka saat ini.

```java
public static void inspectFormFields(Path inputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        System.out.println("Field names: " + Arrays.toString(form.getFieldNames()));
        for (String fieldName : form.getFieldNames()) {
            System.out.println(fieldName + " = " + form.getField(fieldName));
        }
    } finally {
        form.close();
    }
}
```
