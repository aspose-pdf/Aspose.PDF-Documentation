---
title: Verifikasi Tanda Tangan di File PDF
type: docs
weight: 30
url: /id/java/verify-signature-in-pdf/
description: Bagian ini menjelaskan cara bekerja dengan Tanda Tangan di File PDF menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Verifikasi Apakah File PDF Ditandatangani Menggunakan Tanda Tangan

Untuk memverifikasi apakah file PDF ditandatangani menggunakan metode VerifySigned dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). Metode ini memerlukan nama tanda tangan dan mengembalikan nilai benar jika PDF ditandatangani menggunakan nama tanda tangan tersebut. Juga dimungkinkan untuk memverifikasi bahwa sebuah [PDF ditandatangani](/pdf/id/java/working-with-signature-in-a-pdf-file/), tanpa memverifikasi dengan tanda tangan mana ia ditandatangani.

### Memverifikasi bahwa PDF Ditandatangani dengan Tanda Tangan Tertentu

Cuplikan kode berikut menunjukkan kepada Anda cara memverifikasi apakah PDF ditandatangani menggunakan tanda tangan tertentu.

```java
    public static void IsPdfSigned() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.containsSignature())
            System.out.println("Dokumen Ditandatangani");

        pdfSign.close();
    }
```


### Memverifikasi bahwa PDF Sudah Ditandatangani

Untuk menentukan apakah sebuah file sudah ditandatangani, tanpa memberikan nama tanda tangan, gunakan kode berikut.

```java
    public static void IsPdfSignedWithGivenSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySigned("Signature1")) {
            System.out.println("PDF Signed");
        }
    }
```

## Memverifikasi apakah Tanda Tangan Valid

Metode [VerifySignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#verifySignature-java.lang.String-) dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) memungkinkan Anda untuk memvalidasi tanda tangan tertentu. Metode ini memerlukan nama tanda tangan sebagai input dan mengembalikan true jika tanda tangan tersebut valid. Potongan kode berikut menunjukkan cara memvalidasi tanda tangan.

```java
    public static void IsPdfSignatureValid() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySignature("Signature1")) {
            System.out.println("Signature Verified");
        }
    }
```