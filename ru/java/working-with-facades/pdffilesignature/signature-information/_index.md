---
title: Информация о подписи
linktitle: Информация о подписи
type: docs
weight: 60
url: /java/signature-information/
description: Узнайте, как читать имена подписей и данные подписывающего лица из подписанных PDF-файлов на Java с помощью PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Чтение деталей подписи из PDF-документов на Java
Abstract: Узнайте, как проверять метаданные подписи с помощью Aspose.PDF для Java. Пример Java считывает первое доступное имя подписи, а затем извлекает подписавшего, дату, причину и местоположение из подписанного PDF-файла.
---
## Получите информацию о подписи

Используйте этот рабочий процесс, когда вам нужно проверить, кто подписал PDF-файл и какие метаданные подписи были сохранены.

### Шаги

1. Создайте экземпляр `PdfFileSignature` и привяжите подписанный PDF-файл.
2. Прочтите коллекцию подписей и выберите имя подписи.
3. Вызовите средства доступа к информации о подписи, чтобы узнать имя подписывающего лица, дату, причину и местоположение.
4. По завершении закройте объект фасада.

### Пример Java

```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
