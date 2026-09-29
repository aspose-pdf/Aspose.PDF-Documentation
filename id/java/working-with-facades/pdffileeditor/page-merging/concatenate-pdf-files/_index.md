---
title: Menggabungkan Beberapa File PDF
linktitle: Menggabungkan Beberapa File PDF
type: docs
weight: 20
url: /id/java/concatenate-pdf-files/
description: Gabungkan file PDF di Java dengan alur kerja concatenate berbasis array PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gabungkan beberapa file PDF menjadi satu dokumen dengan Java
Abstract: Pelajari cara menggabungkan file PDF dengan Aspose.PDF for Java. Contoh dalam repositori menggunakan overload `concatenate` berbasis array dengan dua masukan, dan alur kerja yang sama dapat diperluas ke daftar file yang lebih panjang karena metode tersebut menerima array string dari jalur sumber.
---
## Menggabungkan file PDF

Contoh Java menggabungkan dua file dengan melewatkannya ke array‑based `concatenate` memuat berlebih.

### Langkah

1. Buat `PdfFileEditor` contoh.
2. Bangun array string dengan jalur PDF masukan.
3. Panggil `concatenate` dengan array input dan jalur file output.
4. Simpan dokumen yang digabungkan.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```

Untuk menggabungkan lebih dari dua file, perpanjang array string yang diberikan ke `concatenate`.
