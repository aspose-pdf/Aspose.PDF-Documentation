---
title: Informasi Tanda Tangan
linktitle: Informasi Tanda Tangan
type: docs
weight: 60
url: /id/java/signature-information/
description: Pelajari cara membaca nama tanda tangan dan detail penandatangan dari PDF yang ditandatangani dalam Java dengan PdfFileSignature.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Baca detail tanda tangan dari dokumen PDF dalam Java
Abstract: Pelajari cara memeriksa metadata tanda tangan dengan Aspose.PDF for Java. Contoh Java membaca nama tanda tangan pertama yang tersedia dan kemudian mengambil penandatangan, tanggal, alasan, dan lokasi dari PDF yang ditandatangani.
---
## Dapatkan informasi tanda tangan

Gunakan Workflow ini ketika Anda perlu memeriksa siapa yang menandatangani PDF dan metadata tanda tangan apa yang disimpan.

### Langkah

1. Buat sebuah `PdfFileSignature` buat instance dan kaitkan PDF yang ditandatangani.
2. Baca koleksi tanda tangan dan pilih nama tanda tangan.
3. Panggil accessor informasi tanda tangan untuk nama penandatangan, tanggal, alasan, dan lokasi.
4. Tutup objek facade saat selesai.

### Contoh Java

```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
