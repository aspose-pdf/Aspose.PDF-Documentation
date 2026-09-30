---
title: "Memverifikasi tanda tangan"
linktitle: "Memverifikasi tanda tangan"
type: docs
weight: 90
url: /id/java/signature-verification/
description: "Pelajari cara memverifikasi tanda tangan PDF di Java dengan fasad PdfFileSignature."
lastmod: "2026-09-30"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Memverifikasi tanda tangan PDF di Java"
Abstract: Pelajari cara memverifikasi tanda tangan PDF dengan Aspose.PDF for Java. Contoh Java memilih tanda tangan pertama yang tersedia, memvalidasi tanda tangan, dan memeriksa apakah tanda tangan tersebut mencakup seluruh dokumen.
---
## Memverifikasi tanda tangan PDF

Gunakan alur kerja ini ketika Anda membutuhkan validasi cepat terhadap PDF yang sudah ditandatangani.

### Langkah

1. Buat `PdfFileSignature` instansiasi dan mengikat PDF yang telah ditandatangani.
2. Pilih nama tanda tangan yang ingin Anda periksa.
3. Panggil `verifySignature` untuk memvalidasi tanda tangan.
4. Panggil `coversWholeDocument` untuk memeriksa cakupan.
5. Tutup objek fasad.

### Contoh Java

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: " + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: " + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
