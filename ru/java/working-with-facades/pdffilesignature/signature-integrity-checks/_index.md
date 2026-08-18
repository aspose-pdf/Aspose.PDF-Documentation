---
title: Проверка целостности подписи
linktitle: Проверка целостности подписи
type: docs
weight: 70
url: /java/signature-integrity-checks/
description: Узнайте, как проверить покрытие и целостность подписи в Java с помощью фасада PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверка покрытия и целостности подписи PDF в Java
Abstract: Узнайте, как проверить целостность подписи с помощью Aspose.PDF для Java. В текущем наборе примеров Java используется `verifySignature` для проверки выбранной подписи и `coversWholeDocument` для определения того, защищает ли подпись весь PDF-файл.
---
## Проверьте целостность подписи

Эта статья соответствует тому же рабочему процессу проверки, представленному `PdfFileSignatureExamples.java`.

### Шаги

1. Свяжите подписанный PDF-файл с помощью `PdfFileSignature`.
2. Выберите имя подписи из документа.
3. Позвоните `verifySignature`, чтобы проверить содержимое подписи.
4. Позвоните `coversWholeDocument`, чтобы подтвердить покрытие всего документа.
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
