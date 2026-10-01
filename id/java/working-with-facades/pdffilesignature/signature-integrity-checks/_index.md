---
title: "Pemeriksaan integritas tanda tangan"
linktitle: "Pemeriksaan integritas tanda tangan"
type: docs
weight: 70
url: /id/java/signature-integrity-checks/
description: "Pelajari cara memvalidasi cakupan tanda tangan dan integritasnya di Java dengan fasad PdfFileSignature."
lastmod: "2026-09-30"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Memvalidasi cakupan tanda tangan PDF dan integritasnya di Java"
Abstract: Pelajari cara memeriksa integritas tanda tangan dengan Aspose.PDF for Java. Set contoh Java saat ini menggunakan `verifySignature` untuk memvalidasi tanda tangan yang dipilih dan `coversWholeDocument` untuk menentukan apakah tanda tangan melindungi seluruh PDF.
---
## Memeriksa integritas tanda tangan

Artikel ini memetakan ke alur kerja verifikasi yang sama yang diungkapkan oleh `PdfFileSignatureExamples.java`.

### Langkah

1. Gabungkan PDF yang ditandatangani dengan `PdfFileSignature`.
2. Pilih nama tanda tangan dari dokumen.
3. Panggil `verifySignature` untuk memvalidasi isi tanda tangan.
4. Panggil `coversWholeDocument` untuk mengonfirmasi cakupan seluruh dokumen.
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
