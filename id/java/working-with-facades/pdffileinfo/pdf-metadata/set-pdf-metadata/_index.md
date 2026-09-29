---
title: Atur Metadata PDF
linktitle: Atur Metadata PDF
type: docs
weight: 50
url: /id/java/set-pdf-metadata/
description: Pelajari cara memperbarui metadata PDF di Java dengan antarmuka PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Memperbarui Metadata PDF Menggunakan Aspose.PDF untuk Java
Abstract: Pelajari cara memperbarui metadata PDF dengan Aspose.PDF untuk Java. Contoh Java ini menggunakan PdfFileInfo untuk mengatur bidang metadata standar seperti subjek, judul, kata kunci, dan pembuat, menambahkan entri metadata khusus, dan menyimpan hasilnya ke PDF baru.
---
## Atur metadata PDF

Gunakan alur kerja ini ketika Anda perlu menormalkan atau memperkaya informasi dokumen sebelum menyimpan PDF.

### Langkah

1. Buat sebuah `PdfFileInfo` objek untuk PDF sumber.
2. Setel bidang metadata standar yang ingin Anda perbarui.
3. Tambahkan metadata kustom apa pun dengan `setMetaInfo`.
4. Simpan dokumen yang diperbarui dengan `save()`.
5. Tutup `PdfFileInfo` instansi.

### Contoh Java

```java
public static void setPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.setMetaInfo("CustomKey", "CustomValue");
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
