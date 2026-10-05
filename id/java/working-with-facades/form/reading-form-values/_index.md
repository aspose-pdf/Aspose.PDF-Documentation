---
title: "Membaca nilai Form"
linktitle: "Membaca nilai Form"
type: docs
weight: 60
url: /id/java/reading-form-values/
description: "Pelajari cara memeriksa nama bidang Form PDF dan nilai-nilainya di Java menggunakan fasad Form di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Membaca nama bidang Form PDF dan nilai-nilainya di Java"
Abstract: "Bagian ini mencakup alur kerja pembacaan Form Java yang diimplementasikan dalam set contoh fasad Form saat ini untuk Aspose.PDF for Java. Repository menyediakan contoh inspeksi bidang umum dan menggunakan catatan ruang lingkup eksplisit untuk halaman khusus yang belum memiliki contoh Java yang cocok."
---
Kelas `FormExamples` dalam Java menunjukkan alur kerja pemrosesan formulir utama yang diungkapkan oleh API Facades.

## Mendapatkan nilai bidang

Gunakan `FormExamples.inspectFormFields(...)` untuk memeriksa nama bidang dan nilai mereka saat ini.

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
