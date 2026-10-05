---
title: "Daftar stempel"
linktitle: "Daftar stempel"
type: docs
weight: 20
url: /id/java/list-stamps/
description: Pelajari cara membuat daftar stempel karet pada halaman dengan Java menggunakan antarmuka PdfContentEditor di Aspose.PDF.
lastmod: "2026-09-30"
TechArticle: true
AlternativeHeadline: Daftar stempel karet PDF dalam Java
Abstract: Artikel ini menunjukkan cara mengikat PDF, mengambil stempel pada sebuah halaman, dan memeriksa koleksi yang dihasilkan menggunakan antarmuka PdfContentEditor di Aspose.PDF for Java.
---
## Daftar stempel pada halaman

1. Ikat PDF sumber ke fasad `PdfContentEditor`.
2. Panggil `getStamps(pageNumber)` untuk mengambil stempel pada halaman target.
3. Periksa hasilnya `StampInfo[]` koleksi.

```java
public static void listStamps(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        StampInfo[] stamps = editor.getStamps(1);
        System.out.println("Stamps on page 1: " + stamps.length);
    } finally {
        editor.close();
    }
}
```
