---
title: Verifikasi Tanda Tangan dalam File PDF
type: docs
weight: 30
url: /id/net/verify-signature-in-pdf/
description: Bagian ini menjelaskan cara memverifikasi tanda tangan dalam File PDF menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Verifikasi Apakah File PDF Ditandatangani Menggunakan Tanda Tangan

Untuk memverifikasi apakah file PDF ditandatangani menggunakan [tanda tangan tertentu](/pdf/id/net/working-with-signature-in-a-pdf-file/), gunakan metode VerifySigned dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Metode ini memerlukan nama tanda tangan dan mengembalikan nilai true jika PDF ditandatangani menggunakan nama tanda tangan tersebut. Juga dimungkinkan untuk memverifikasi bahwa sebuah [PDF ditandatangani](/pdf/id/net/working-with-signature-in-a-pdf-file/), tanpa memverifikasi tanda tangan mana yang digunakan untuk menandatanganinya.

### Memverifikasi bahwa PDF Ditandatangani dengan Tanda Tangan Tertentu

Potongan kode berikut menunjukkan cara memverifikasi apakah PDF ditandatangani menggunakan tanda tangan tertentu.

```csharp
public static void IsPdfSigned()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.ContainsSignature())
                Console.WriteLine("Document Signed");
            pdfSign.Close();
        }
```

### Memverifikasi bahwa PDF Ditandatangani

Untuk menentukan apakah file ditandatangani, tanpa memberikan nama tanda tangan, gunakan kode berikut.

```csharp
 public static void IsPdfSignedWithGivenSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySigned("Signature1"))
            {
                Console.WriteLine("PDF Signed");
            }
            //if (pdfSign.VerifySigned("Signature2"))
            //{
            //    Console.WriteLine("PDF Signed");
            //}
        }
```

## Verifikasi apakah Tanda Tangan Valid

Metode [VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) dari kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) memungkinkan Anda memvalidasi tanda tangan tertentu. Metode ini memerlukan nama tanda tangan sebagai input dan mengembalikan true jika tanda tangan tersebut valid. Cuplikan kode berikut menunjukkan cara memvalidasi tanda tangan.

```csharp
public static void IsPdfSignatureValid()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySignature("Signature1"))
            {
                Console.WriteLine("Signature Verified");
            }
        }
```