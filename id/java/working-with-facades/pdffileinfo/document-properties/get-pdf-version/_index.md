---
title: Dapatkan Versi PDF
linktitle: Dapatkan Versi PDF
type: docs
weight: 20
url: /id/java/get-pdf-version/
description: Pelajari cara mengambil versi dokumen PDF di Java dengan fasad PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ambil Versi PDF Menggunakan Aspose.PDF for Java
Abstract: Pelajari cara mengambil versi PDF dengan Aspose.PDF for Java. Contoh Java membuat objek PdfFileInfo, membaca string versi dengan `getPdfVersion()`, mencetak hasilnya, dan menutup objek informasi file.
---
## Dapatkan versi PDF

Gunakan alur kerja ini ketika Anda perlu memeriksa kompatibilitas file atau mengarahkan dokumen melalui logika pemrosesan yang spesifik versi.

### Langkah

1. Buat `PdfFileInfo` objek untuk file PDF.
2. Panggil `getPdfVersion()` untuk mengambil versi yang dilaporkan.
3. Gunakan atau cetak nilai versi.
4. Tutup `PdfFileInfo` instansi.

### Contoh Java

```java
public static void getPdfVersion(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println();
    System.out.println("PDF Version: " + pdfInfo.getPdfVersion());
    pdfInfo.close();
}
```
