---
title: Dapatkan Metadata PDF
linktitle: Dapatkan Metadata PDF
type: docs
weight: 20
url: /id/java/get-pdf-metadata/
description: Pelajari cara membaca metadata PDF dalam Java dengan antarmuka PdfFileInfo.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mengambil Metadata PDF Menggunakan Aspose.PDF untuk Java.
Abstract: Pelajari cara mengambil metadata PDF dengan Aspose.PDF untuk Java. Contoh Java ini membaca bidang standar seperti subjek, judul, kata kunci, pembuat, tanggal pembuatan, dan tanggal modifikasi, bersama dengan flag status file dan entri metadata khusus `Reviewer`.
---
## Dapatkan metadata PDF

Contoh ini membaca informasi dokumen standar, flag status file, dan kunci metadata khusus.

### Langkah

1. Buat `PdfFileInfo` objek untuk PDF sumber.
2. Baca bidang metadata standar seperti subjek, judul, kata kunci, dan pembuat.
3. Periksa flag status file seperti apakah file valid, terenkripsi, dilindungi kata sandi, atau portfolio.
4. Baca nilai metadata khusus dengan `getMetaInfo`.
5. Tutup `PdfFileInfo` instansi.

### Contoh Java

```java
public static void getPdfMetadata(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Subject: " + pdfInfo.getSubject());
    System.out.println("Title: " + pdfInfo.getTitle());
    System.out.println("Keywords: " + pdfInfo.getKeywords());
    System.out.println("Creator: " + pdfInfo.getCreator());
    System.out.println("Creation Date: " + pdfInfo.getCreationDate());
    System.out.println("Modification Date: " + pdfInfo.getModDate());
    System.out.println("Is Valid PDF: " + pdfInfo.isPdfFile());
    System.out.println("Is Encrypted: " + pdfInfo.isEncrypted());
    System.out.println("Has Open Password: " + pdfInfo.hasOpenPassword());
    System.out.println("Has Edit Password: " + pdfInfo.hasEditPassword());
    System.out.println("Is Portfolio: " + pdfInfo.hasCollection());
    String reviewer = pdfInfo.getMetaInfo("Reviewer");
    System.out.println("Reviewer: " + (reviewer == null || reviewer.isBlank() ? "No Reviewer metadata found." : reviewer));
    pdfInfo.close();
}
```
