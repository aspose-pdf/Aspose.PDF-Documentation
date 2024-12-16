---
title: Проверка Подписи в PDF Файле
type: docs
weight: 30
url: /ru/java/verify-signature-in-pdf/
description: Этот раздел объясняет, как работать с подписью в PDF файле с использованием класса PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Проверка, Подписан ли PDF Файл с использованием Подписи

Чтобы проверить, подписан ли PDF файл, используйте метод VerifySigned класса [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). Этот метод требует имя подписи и возвращает true, если PDF подписан с использованием этого имени подписи. Также возможно проверить, что [PDF подписан](/pdf/ru/java/working-with-signature-in-a-pdf-file/), без проверки, какой именно подписью он подписан.

### Проверка, что PDF Подписан Данной Подписью

Следующий фрагмент кода показывает, как проверить, подписан ли PDF с использованием данной подписи.

```java
    public static void IsPdfSigned() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.containsSignature())
            System.out.println("Документ Подписан");

        pdfSign.close();
    }
```


### Проверка, подписан ли PDF

Чтобы определить, подписан ли файл, без указания имени подписи, используйте следующий код.

```java
    public static void IsPdfSignedWithGivenSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySigned("Signature1")) {
            System.out.println("PDF подписан");
        }
    }
```

## Проверка действительности подписи

Метод [VerifySignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#verifySignature-java.lang.String-) класса [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) позволяет проверить действительность конкретной подписи. Этот метод требует имя подписи в качестве входных данных и возвращает true, если подпись действительна. Следующий фрагмент кода показывает, как проверить подпись.

```java
    public static void IsPdfSignatureValid() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySignature("Signature1")) {
            System.out.println("Подпись подтверждена");
        }
    }
```