---
title: "Menambahkan tanda tangan digital atau menandatangani PDF secara digital di Java"
linktitle: "Menandatangani PDF secara digital"
type: docs
weight: 10
url: /id/java/digitally-sign-pdf-file/
description: Pelajari cara menandatangani secara digital dan mensertifikasi dokumen PDF di Java menggunakan Aspose.PDF.
lastmod: "2026-09-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Menandatangani file PDF secara digital dengan Java"
Abstract: Panduan ini menjelaskan cara menandatangani dokumen PDF secara digital menggunakan Aspose.PDF for Java. Panduan ini mencakup penandatanganan dengan objek sertifikat, penandatanganan dengan parameter sertifikat dasar, dan mengesahkan dokumen dengan tanda tangan DocMDP untuk mengontrol perubahan yang diizinkan setelah penandatanganan.
---
Aspose.PDF for Java mendukung beberapa alur penandatanganan melalui `PdfFileSignature`.

## Menandatangani PDF dengan objek sertifikat

1. Buat fasad [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) dan mengikat dokumen PDF sumber.
1. Buat objek [`PKCS7`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) tanda tangan dan mengonfigurasi opsi penandatanganan.
1. Terapkan tanda tangan ke dokumen PDF melalui [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Simpan dokumen PDF yang diperbarui.

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
```

Pendekatan ini membangun sebuah objek `PKCS7` tanda tangan terlebih dahulu dan kemudian menerapkannya ke halaman 1.

## Menandatangani PDF dengan parameter sertifikat dasar

1. Buat fasad [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) dan mengikat dokumen PDF sumber.
1. Konfigurasikan parameter sertifikat yang diperlukan oleh contoh penandatanganan.
1. Terapkan tanda tangan ke dokumen PDF melalui [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Simpan dokumen PDF yang diperbarui.

```java
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

## Sertifikasi PDF dengan DocMDP

Gunakan tanda deteksi dan pencegahan modifikasi dokumen ketika Anda memerlukan pembatasan tingkat sertifikasi:

1. Buat fasad [`PdfFileSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) dan mengikat dokumen PDF sumber.
1. Buat objek [`DocMDPSignature`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) dan konfigurasikan [`DocMDPAccessPermissions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/) opsi penandatanganan.
1. Terapkan tanda tangan sertifikasi dan simpan dokumen PDF yang diperbarui.

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com",
                "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
