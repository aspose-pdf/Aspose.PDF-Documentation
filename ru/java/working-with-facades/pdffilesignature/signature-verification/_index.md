---
title: Проверка подписи
linktitle: Проверка подписи
type: docs
weight: 90
url: /java/signature-verification/
description: Узнайте, как проверить подписи PDF в Java с помощью фасада PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверка подписей PDF в Java
Abstract: Узнайте, как проверить подпись PDF с помощью Aspose.PDF для Java. В примере Java выбирается первая доступная подпись, проверяется подпись и проверяется, охватывает ли она весь документ.
---
## Проверьте подпись PDF-файла

Используйте этот рабочий процесс, если вам нужно быстро пройти проверку существующего подписанного PDF-файла.

### Шаги

1. Создайте экземпляр `PdfFileSignature` и привяжите подписанный PDF-файл.
2. Выберите имя подписи, которую хотите проверить.
3. Позвоните `verifySignature`, чтобы подтвердить подпись.
4. Позвоните `coversWholeDocument`, чтобы проверить покрытие.
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
