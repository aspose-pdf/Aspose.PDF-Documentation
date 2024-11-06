---
title: Проверка подписи в PDF-файле
type: docs
weight: 30
url: ru/net/verify-signature-in-pdf/
description: Этот раздел объясняет, как проверить подпись в PDF-файле с помощью класса PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Проверка, подписан ли PDF-файл с использованием подписи

Чтобы проверить, подписан ли PDF-файл с использованием [определенной подписи](/pdf/net/working-with-signature-in-a-pdf-file/), используйте метод VerifySigned класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Этот метод требует имени подписи и возвращает true, если PDF подписан с использованием этого имени подписи. Также возможно проверить, что [PDF подписан](/pdf/net/working-with-signature-in-a-pdf-file/), без проверки, какой именно подписью он подписан.

### Проверка, что PDF подписан с заданной подписью

Следующий пример кода показывает, как проверить, подписан ли PDF с использованием заданной подписи.

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

### Проверка, что PDF подписан

Чтобы определить, подписан ли файл, без предоставления имени подписи, используйте следующий код.

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

## Проверка действительности подписи

Метод [VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) позволяет вам проверить конкретную подпись. Этот метод требует имя подписи в качестве входных данных и возвращает true, если подпись действительна. Следующий фрагмент кода показывает, как проверить подпись.

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