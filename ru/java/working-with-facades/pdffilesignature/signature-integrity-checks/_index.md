---
title: Проверка целостности подписи
linktitle: Проверка целостности подписи
type: docs
weight: 70
url: /ru/java/signature-integrity-checks/
description: Узнайте, как проверять покрытие подписи и её целостность в Java с помощью фасада PdfFileSignature.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверьте покрытие подписи PDF и её целостность в Java
Abstract: Узнайте, как проверять целостность подписи с помощью Aspose.PDF for Java. Текущий набор примеров Java использует `verifySignature` для проверки выбранной подписи и `coversWholeDocument` для определения, защищает ли подпись весь PDF.
---
## Проверьте целостность подписи

Эта статья сопоставляется с тем же процессом проверки, предоставляемым `PdfFileSignatureExamples.java`.

### Шаги

1. Связать подписанный PDF с `PdfFileSignature`.
2. Выберите имя подписи из документа.
3. Вызовите `verifySignature` для проверки содержимого подписи.
4. Вызовите `coversWholeDocument` для подтверждения охвата всего документа.
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


