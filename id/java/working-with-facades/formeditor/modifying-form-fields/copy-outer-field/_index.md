---
title: Salin Field Luar
linktitle: Salin Field Luar
type: docs
weight: 80
url: /id/java/copy-outer-field/
description: Pelajari cara menyalin field formulir dari satu dokumen PDF ke dokumen lain dalam Java menggunakan facade FormEditor di Aspose.PDF.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Salin field formulir PDF antar dokumen dalam Java
Abstract: Artikel ini menunjukkan cara membuat PDF tujuan, mengaitkannya dengan facade FormEditor, menyalin sebuah field dari dokumen lain, dan menyimpan hasilnya menggunakan Aspose.PDF for Java.
---
## Salin sebuah field dari PDF lain

1. Buat PDF tujuan dengan setidaknya satu halaman.
2. Mengikat PDF tujuan ke `FormEditor` fasad.
3. Panggil `copyOuterField(...)` dengan jalur dokumen sumber, nama bidang, halaman target, dan koordinat.
4. Simpan dokumen tujuan yang diperbarui.

```java
public static void copyOuterField(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();
        document.save(outputFile.toString());
    }

    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(outputFile.toString());
        editor.copyOuterField(inputFile.toString(), "First Name", 1, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
