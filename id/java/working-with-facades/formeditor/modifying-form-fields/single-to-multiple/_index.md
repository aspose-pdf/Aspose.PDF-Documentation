---
title: Single ke Multiple
linktitle: Single ke Multiple
type: docs
weight: 60
url: /id/java/single-to-multiple/
description: Pelajari cara mengonversi bidang teks satu baris menjadi bidang multi-baris dalam dokumen PDF di Java menggunakan facade FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Konversi bidang PDF satu baris ke multi-baris dalam Java
Abstract: Artikel ini menunjukkan cara mengaitkan PDF yang ada, mengonversi bidang satu baris menjadi bidang multi-baris, dan menyimpan dokumen yang diperbarui menggunakan facade FormEditor di Aspose.PDF for Java.
---
## Konversi bidang satu baris menjadi beberapa baris

1. Ikat PDF sumber ke `FormEditor` fasad.
2. Panggil `single2Multiple(...)` untuk nama bidang target.
3. Simpan dokumen yang diperbarui.

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
