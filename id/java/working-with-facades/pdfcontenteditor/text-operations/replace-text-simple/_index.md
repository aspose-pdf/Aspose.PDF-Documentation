---
title: "Mengganti teks sederhana"
linktitle: "Mengganti teks sederhana"
type: docs
weight: 10
url: /id/java/replace-text-simple/
description: Pelajari cara mengganti teks di seluruh dokumen PDF dalam Java menggunakan antarmuka PdfContentEditor di Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: "Mengganti teks dalam PDF di Java"
Abstract: Artikel ini menunjukkan cara mengikat PDF, mengonfigurasi ruang lingkup penggantian teks, mengganti semua kemunculan teks yang cocok, dan menyimpan dokumen yang diperbarui menggunakan antarmuka PdfContentEditor di Aspose.PDF for Java.
---
## Mengganti teks di seluruh dokumen

1. Ikat PDF sumber ke fasad `PdfContentEditor`.
2. Atur ruang lingkup replace-text ke `ReplaceAll`.
3. Panggil `replaceText(...)` dengan teks pencarian dan teks pengganti.
4. Simpan dokumen PDF yang diperbarui.

```java
public static void replaceTextSimple(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("33", "XXXIII ");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
