---
title: "Menyalin Field luar"
linktitle: "Menyalin Field luar"
type: docs
weight: 80
url: /id/java/copy-outer-field/
description: "Pelajari cara menyalin bidang formulir dari satu dokumen PDF ke dokumen lain dalam Java menggunakan fasad FormEditor di Aspose.PDF."
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Menyalin bidang formulir PDF antar dokumen dalam Java"
Abstract: "Artikel ini menunjukkan cara membuat PDF tujuan, mengaitkannya dengan fasad FormEditor, menyalin sebuah bidang dari dokumen lain, dan menyimpan hasilnya menggunakan Aspose.PDF for Java."
---
## Menyalin sebuah bidang dari PDF lain

1. Buat PDF tujuan dengan setidaknya satu halaman.
2. Ikat PDF tujuan ke fasad `FormEditor`.
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
