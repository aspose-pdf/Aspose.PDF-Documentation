---
title: "Mendapatkan hak istimewa dokumen"
linktitle: "Mendapatkan hak istimewa dokumen"
type: docs
weight: 10
url: /id/java/get-document-privileges/
description: "Pelajari cara memeriksa hak istimewa dokumen PDF dalam Java dengan fasad PdfFileInfo."
lastmod: "2026-09-30"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengambil hak istimewa dokumen PDF menggunakan Aspose.PDF for Java"
Abstract: Pelajari cara mengambil hak istimewa dokumen dengan Aspose.PDF for Java. Contoh Java membuat objek PdfFileInfo, membaca pengaturan DocumentPrivilege-nya, dan mencetak bendera izin untuk mencetak, menyalin, memodifikasi, anotasi, mengisi formulir, pembaca layar, dan perakitan.
---
## Mendapatkan hak istimewa dokumen

Gunakan `PdfFileInfo.getDocumentPrivilege()` untuk memeriksa operasi apa yang diizinkan PDF saat ini.

### Langkah

1. Buat objek `PdfFileInfo` untuk PDF input.
2. Panggil `getDocumentPrivilege()` untuk mengambil set hak istimewa.
3. Baca flag boolean yang relevan dari hasil yang dikembalikan objek `DocumentPrivilege`.
4. Tutup instans `PdfFileInfo` saat selesai.

### Contoh Java

```java
public static void getDocumentPrivileges(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    DocumentPrivilege privileges = pdfInfo.getDocumentPrivilege();

    System.out.println("Document Privileges:");
    System.out.println("  Can Print: " + privileges.isAllowPrint());
    System.out.println("  Can Degraded Print: " + privileges.isAllowDegradedPrinting());
    System.out.println("  Can Copy: " + privileges.isAllowCopy());
    System.out.println("  Can Modify Contents: " + privileges.isAllowModifyContents());
    System.out.println("  Can Modify Annotations: " + privileges.isAllowModifyAnnotations());
    System.out.println("  Can Fill In: " + privileges.isAllowFillIn());
    System.out.println("  Can Screen Readers: " + privileges.isAllowScreenReaders());
    System.out.println("  Can Assembly: " + privileges.isAllowAssembly());
    pdfInfo.close();
}
```
