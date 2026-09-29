---
title: Sertifikasi PDF
linktitle: Sertifikasi PDF
type: docs
weight: 30
url: /id/java/pdf-certification/
description: Pelajari cara menyertifikasi dokumen PDF dalam Java dengan PdfFileSignature dan DocMDPSignature.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sertifikasi dokumen PDF dengan izin DocMDP dalam Java
Abstract: Pelajari cara menyertifikasi dokumen PDF dengan Aspose.PDF for Java. Contoh Java tersebut menggunakan PdfFileSignature bersama dengan DocMDPSignature dan DocMDPAccessPermissions untuk menyertifikasi dokumen untuk pengisian formulir dan penandatanganan sambil membatasi jenis modifikasi lainnya.
---
## Menyertifikasi dokumen PDF

Gunakan sertifikasi ketika dokumen harus tetap tepercaya tetapi masih memperbolehkan kelas perubahan tertentu setelah penandatanganan.

### Langkah

1. Buat sebuah `PdfFileSignature` instance dan mengikat PDF sumber.
2. Bangun sebuah `PKCS7` objek tanda tangan dengan sertifikat dan kata sandi sertifikat.
3. Bungkus tanda tangan itu dalam sebuah `DocMDPSignature` dengan yang diperlukan `DocMDPAccessPermissions` nilai.
4. Telepon `certify` dengan halaman target, metadata tanda tangan, persegi panjang terlihat, dan tanda tangan MDP.
5. Simpan PDF yang disertifikasi dan tutup objek facade.

### Contoh Java

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com", "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
