---
title: Ekstraksi Tanda Tangan
linktitle: Ekstraksi Tanda Tangan
type: docs
weight: 50
url: /id/java/signature-extraction/
description: Pelajari cara mengekstrak sertifikat penandatangan dari PDF yang ditandatangani dalam Java dengan PdfFileSignature.
lastmod: "2026-09-29"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak sertifikat tanda tangan dari PDF dalam Java
Abstract: Pelajari cara mengekstrak sertifikat yang terkait dengan tanda tangan PDF menggunakan Aspose.PDF for Java. Set contoh Java saat ini mencakup ekstraksi sertifikat ke aliran output, tetapi tidak menyertakan contoh ekstraksi gambar tanda tangan terpisah.
---
## Ekstrak sertifikat tanda tangan

Gunakan alur kerja ini ketika Anda perlu menyimpan sertifikat yang terkait dengan tanda tangan yang ada.

### Langkah

1. Buat sebuah `PdfFileSignature` instans dan mengikat PDF yang ditandatangani.
2. Pilih nama tanda tangan untuk diperiksa.
3. Panggil `extractCertificate` untuk membuka aliran sertifikat.
4. Salin byte sertifikat ke file output.
5. Tutup sumber daya aliran dan objek facade.

### Contoh Java

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

Saat ini `PdfFileSignatureExamples.java` kelas tidak menyertakan contoh Java khusus untuk mengekstrak gambar tanda tangan yang dirender.
