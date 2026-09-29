---
title: Menggabungkan Dua File PDF
linktitle: Menggabungkan Dua File PDF
type: docs
weight: 60
url: /id/java/concatenate-two-files/
description: Gabungkan dua file PDF menjadi satu dokumen di Java dengan facade PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gabungkan dua file PDF menjadi satu dokumen output dengan Java
Abstract: Pelajari cara menggabungkan dua file PDF dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileEditor dan overload `concatenate` berbasis array untuk menggabungkan dua dokumen sumber menjadi satu PDF output.
---
## Gabungkan dua file PDF

Artikel ini memetakan langsung ke `mergePdfDocuments` contoh dalam `PdfFileEditorExamples.java`.

### Langkah

1. Buat `PdfFileEditor` instansi.
2. Berikan dua jalur file input sebagai array string.
3. Panggilan `concatenate` dengan array dan jalur file output.
4. Simpan PDF yang digabungkan.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
