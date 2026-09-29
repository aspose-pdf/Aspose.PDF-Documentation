---
title: Tandatangani Dokumen PDF dari Smart Card di Java
linktitle: Penandatanganan PDF dengan Smart Card
type: docs
weight: 30
url: /id/java/sign-pdf-document-from-smart-card/
description: Tinjau cakupan contoh Java saat ini untuk penandatanganan PDF berbasis sertifikat di Aspose.PDF.
lastmod: "2026-09-29"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cakupan penandatanganan PDF berbasis sertifikat dalam kumpulan contoh Java saat ini
Abstract: Halaman ini menjelaskan ruang lingkup contoh penandatanganan yang tersedia saat ini dalam pohon sumber dokumentasi Java. Repositori mencakup contoh penandatanganan PDF berbasis sertifikat dengan kredensial PFX atau PKCS7, tetapi saat ini tidak menyertakan contoh khusus penyimpanan sertifikat smart-card untuk Java.
---
Repositori Java saat ini tidak menyertakan contoh penandatanganan kartu pintar berbasis sumber yang berdedikasi di bawah `facades/pdffilesignature`, tetapi alur kerja berikut menunjukkan pola API khas untuk menandatangani PDF dengan sertifikat yang dipilih dari penyimpanan sertifikat lokal.

## Tandatangani dokumen PDF dari kartu pintar

1. Buka PDF sumber [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Buat sebuah [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) facade dan ikat dokumen PDF sumber.
1. Ambil sertifikat lokal dan buat yang diperlukan [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/).
1. Konfigurasikan penampilan tanda tangan visual dan targetnya [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Terapkan tanda tangan ke dokumen PDF melalui [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Simpan dokumen PDF yang diperbarui.
1. Hubungkan dokumen yang dimuat ke [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fasad dengan `bindPdf(...)`.
1. Ambil sertifikat lokal yang mewakili kredensial kartu pintar dengan memanggil `getLocalCertificate()`.
1. Periksa apakah sertifikat ditemukan. Jika tidak, simpan file output yang tidak diubah dan hentikan alur kerja.
1. Buat sebuah [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) dari sertifikat yang dipilih.
1. Setel gambar tampilan tanda tangan visual dengan `setSignatureAppearance(...)`.
1. Panggilan `sign(...)` dengan halaman target, alasan, kontak, lokasi, flag visibilitas, tanda tangan [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), dan objek tanda tangan eksternal.
1. Simpan PDF yang sudah ditandatangani ke jalur output.

```java
public static void signWithSmartCard(Path inputFile, Path outputFile, Path pngFile) {
    try (Document document = new Document(inputFile.toString());
            PdfFileSignature pdfSignature = new PdfFileSignature()) {
        pdfSignature.bindPdf(document);
        X509Certificate2 selectedCertificate = getLocalCertificate();
        if (selectedCertificate == null) {
            System.out.println("Local certificate was not found.");
            document.save(outputFile.toString());
            return;
        }

        ExternalSignature externalSignature = new ExternalSignature(selectedCertificate, null);
        pdfSignature.setSignatureAppearance(pngFile.toString());
        pdfSignature.sign(1, "Reason", "Contact", "Location", true,
                new java.awt.Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature.save(outputFile.toString());
    }
}
```
