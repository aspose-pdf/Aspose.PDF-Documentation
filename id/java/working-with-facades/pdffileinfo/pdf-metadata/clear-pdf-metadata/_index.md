---
title: Hapus Metadata PDF
linktitle: Hapus Metadata PDF
type: docs
weight: 10
url: /id/java/clear-pdf-metadata/
description: Pelajari cara menghapus metadata PDF di Java dengan facade PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menghapus Metadata PDF Menggunakan Aspose.PDF for Java
Abstract: Pelajari cara menghapus metadata PDF dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileInfo untuk menghapus informasi dokumen yang disimpan dengan `clearInfo()` dan kemudian menyimpan PDF yang telah dibersihkan ke file baru.
---
## Hapus metadata PDF

Gunakan alur kerja ini ketika Anda perlu menghapus informasi dokumen yang disimpan sebelum membagikan atau mengarsipkan PDF.

### Langkah

1. Buat sebuah `PdfFileInfo` objek untuk PDF input.
2. Panggil `clearInfo()` untuk menghapus metadata dokumen.
3. Simpan hasil ke file baru dengan `save()`.
4. Tutup `PdfFileInfo` instans.

### Contoh Java

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
