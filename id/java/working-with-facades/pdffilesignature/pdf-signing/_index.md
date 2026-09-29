---
title: Menandatangani Dokumen PDF
linktitle: Menandatangani Dokumen PDF
type: docs
weight: 10
url: /id/java/pdf-signing/
description: Pelajari cara menandatangani dokumen PDF dalam Java dengan antarmuka PdfFileSignature.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menandatangani dokumen PDF dengan tanda tangan digital dalam Java
Abstract: Pelajari cara menandatangani dokumen PDF dengan Aspose.PDF for Java. Set contoh Java mencakup penandatanganan dengan jalur sertifikat dan kata sandi yang dikonfigurasi, serta penandatanganan dengan objek tanda tangan PKCS7 eksplisit yang mencakup metadata tanda tangan seperti alasan, informasi kontak, lokasi, dan otoritas.
---
## Menandatangani dokumen PDF

Gunakan `PdfFileSignature` ketika Anda perlu menerapkan tanda tangan digital yang terlihat pada PDF.

### Langkah

1. Buat sebuah `PdfFileSignature` buat instance dan kaitkan PDF sumber.
2. Muat sertifikat baik melalui `setCertificate` atau dengan membuat sebuah `PKCS7` objek.
3. Panggil `sign` dengan halaman target, pengaturan visibilitas, persegi tanda tangan, dan data tanda tangan.
4. Simpan PDF yang sudah ditandatangani dan tutup objek facade.

### Contoh Java

```java
public static void signPdfWithCertificateObject(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.sign(1, false, signatureRectangle(), createPkcs7(certificateFile, "Document approval"));
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}

public static void signPdfWithBasicParameters(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.setCertificate(certificateFile.toString(), CERTIFICATE_PASSWORD);
        pdfSignature.sign(1, "Document approval", "qa@example.com", "New York, USA", false, signatureRectangle());
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
