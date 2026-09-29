---
title: Hapus Halaman dari PDF
linktitle: Hapus Halaman dari PDF
type: docs
weight: 20
url: /id/java/delete-pages-from-pdf/
description: Hapus halaman terpilih dari PDF di Java dengan facade PdfFileEditor.
lastmod: "2026-09-29"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus halaman tertentu dari dokumen PDF dengan Java
Abstract: Pelajari cara menghapus halaman dari PDF dengan Aspose.PDF for Java. Contoh Java menggunakan PdfFileEditor untuk menghapus sekumpulan nomor halaman yang ditentukan dan menyimpan halaman yang tersisa sebagai dokumen baru.
---
## Hapus halaman dari PDF

Contoh Java menghapus halaman 2 dan 4 dari dokumen sumber.

### Langkah

1. Buat sebuah `PdfFileEditor` instansi.
2. Buat array dengan nomor halaman yang akan dihapus.
3. Panggil `delete` dengan file input, array halaman, dan file output.
4. Simpan PDF yang dihasilkan.

### Contoh Java

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
