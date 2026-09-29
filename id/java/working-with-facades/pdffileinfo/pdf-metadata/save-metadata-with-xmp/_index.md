---
title: Simpan Metadata dengan XMP
linktitle: Simpan Metadata dengan XMP
type: docs
weight: 30
url: /id/java/save-metadata-with-xmp/
description: Pelajari cara menyimpan metadata PDF dengan XMP di Java menggunakan fasad PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menyimpan Metadata PDF dengan XMP Menggunakan Aspose.PDF untuk Java
Abstract: Pelajari cara menyimpan metadata PDF dengan XMP menggunakan Aspose.PDF untuk Java. Contoh Java memperbarui bidang metadata inti dengan PdfFileInfo dan menuliskannya kembali menggunakan `saveNewInfoWithXmp()` sehingga dokumen output menyimpan informasi dalam bentuk XMP.
---
## Simpan metadata dengan XMP

Gunakan alur kerja ini ketika Anda perlu informasi dokumen yang diperbarui disimpan dalam format XMP.

### Langkah

1. Buat `PdfFileInfo` objek untuk PDF sumber.
2. Atur bidang metadata yang ingin Anda perbarui, seperti subjek, judul, kata kunci, dan pembuat.
3. Panggil `saveNewInfoWithXmp()` dengan jalur file output.
4. Tutup `PdfFileInfo` instansi.

### Contoh Java

```java
public static void saveInfoWithXmp(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.saveNewInfoWithXmp(outputFile.toString());
    pdfInfo.close();
}
```
