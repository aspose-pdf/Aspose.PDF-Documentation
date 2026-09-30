---
title: "Menambahkan cap karet"
linktitle: "Menambahkan cap karet"
type: docs
weight: 10
url: /id/java/add-rubber-stamp/
description: Pelajari cara menambahkan anotasi cap karet ke dokumen PDF dalam Java menggunakan fasad PdfContentEditor di Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Menambahkan cap karet ke PDF dalam Java"
Abstract: Artikel ini menunjukkan cara mengaitkan PDF, membuat anotasi cap karet dengan teks label dan warna, serta menyimpan dokumen yang diperbarui menggunakan fasad PdfContentEditor di Aspose.PDF for Java.
---
## Menambahkan cap karet

1. Ikat PDF sumber ke fasad `PdfContentEditor`.
2. Panggil `createRubberStamp(...)` dengan nomor halaman, persegi panjang, judul, isi, dan warna.
3. Simpan dokumen PDF yang diperbarui.

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
