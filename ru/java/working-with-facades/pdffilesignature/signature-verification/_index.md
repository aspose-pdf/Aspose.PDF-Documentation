---
title: Проверка подписи
linktitle: Проверка подписи
type: docs
weight: 90
url: /ru/java/signature-verification/
description: Узнайте, как проверять подписи PDF в Java с помощью фасада PdfFileSignature.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверка подписей PDF в Java
Abstract: Узнайте, как проверять подпись PDF с помощью Aspose.PDF for Java. Пример на Java выбирает первую доступную подпись, проверяет её валидность и проверяет, охватывает ли она весь документ.
---
## Проверьте подписи PDF

Используйте этот рабочий процесс, когда вам нужна быстрая проверка валидности уже подписанного PDF.

### Шаги

1. Создайте `PdfFileSignature` экземпляр и привязать подписанный PDF.
2. Выберите имя подписи, которое вы хотите проверить.
3. Вызовите `verifySignature` для проверки подписи.
4. Вызовите `coversWholeDocument` проверить покрытие.
5. Закройте объект фасада.

### Пример Java

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: " + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: " + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```


