---
title: "Mengekstrak informasi tanda tangan dari PDF dalam Java"
linktitle: "Mengekstrak detail dari tanda tangan"
type: docs
weight: 20
url: /id/java/extract-image-and-signature-information/
description: Pelajari cara mengekstrak detail sertifikat dan tanda tangan digital dari file PDF dalam Java.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Mengekstrak detail tanda tangan dan data sertifikat dari PDF yang ditandatangani dalam Java"
Abstract: Artikel ini menjelaskan cara memeriksa tanda tangan digital dalam dokumen PDF menggunakan Aspose.PDF for Java. Pelajari cara membaca detail penanda tangan, memverifikasi tanda tangan, memeriksa apakah tanda tangan mencakup seluruh dokumen, mengekstrak sertifikat penandatangan yang tersemat, dan menghapus tanda tangan yang ada.
---
Gunakan `PdfFileSignature` untuk memeriksa dan mengelola tanda tangan yang sudah ada dalam dokumen PDF.

## Membaca informasi tanda tangan

1. Buat fasad [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) dan mengikat dokumen PDF sumber.
1. Akses nama tanda tangan dokumen dan konfigurasikan alur inspeksi tanda tangan yang diperlukan oleh contoh.
1. Baca dan verifikasi informasi tanda tangan dari fasad [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Baca nilai yang dikembalikan atau lanjutkan dengan langkah pemrosesan berikutnya.

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

## Memverifikasi tanda tangan

1. Buat fasad [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) dan mengikat dokumen PDF sumber.
1. Akses nama tanda tangan dokumen dan konfigurasikan alur verifikasi yang diperlukan oleh contoh.
1. Baca dan verifikasi informasi tanda tangan dari fasad [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: "
                + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: "
                + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## Mengekstrak sertifikat penandatangan

1. Buat fasad [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) dan mengikat dokumen PDF sumber.
1. Akses nama tanda tangan dokumen yang diperlukan untuk ekstraksi sertifikat.
1. Tuliskan output yang diekstrak atau periksa nilai yang dikembalikan dari fasad [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```
