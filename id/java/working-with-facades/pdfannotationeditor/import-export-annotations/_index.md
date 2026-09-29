---
title: Impor dan Ekspor Anotasi menggunakan Java
linktitle: Impor dan Ekspor Anotasi
type: docs
weight: 80
url: /id/java/pdfannotationeditor-class/import-export-annotations/
description: Pelajari cara menyalin anotasi dari satu dokumen PDF ke dokumen PDF lainnya menggunakan Java.
lastmod: "2026-09-29"
TechArticle: true
AlternativeHeadline: Transfer anotasi PDF antar dokumen dalam Java
Abstract: Artikel ini menjelaskan cara menyalin anotasi dari PDF sumber dan mengekspornya ke dalam dokumen PDF baru menggunakan Java. Alur kerja memuat file sumber, membuat dokumen tujuan, menambahkan halaman, menyalin anotasi dari halaman sumber pertama, dan menyimpan hasilnya.
---
## Salin anotasi dari satu PDF ke PDF lain

1. Buka PDF sumber dan buat dokumen tujuan baru dengan halaman target.
2. Enumerasikan anotasi pada halaman sumber pertama dan tambahkan masing-masing ke halaman tujuan.
3. Simpan dokumen tujuan untuk mempertahankan anotasi yang disalin.

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
