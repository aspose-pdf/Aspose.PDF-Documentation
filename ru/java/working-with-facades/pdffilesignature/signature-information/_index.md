---
title: Информация о подписи
linktitle: Информация о подписи
type: docs
weight: 60
url: /ru/java/signature-information/
description: Узнайте, как читать имена подписей и сведения о подписанте из подписанных PDF-файлов в Java с помощью PdfFileSignature.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Читать детали подписи из PDF-документов в Java
Abstract: Узнайте, как проверять метаданные подписи с помощью Aspose.PDF for Java. Пример на Java считывает первое доступное имя подписи, а затем получает информацию о подписанте, дате, причине и месте из подписанного PDF.
---
## Получите информацию о подписи

Используйте этот рабочий процесс, когда вам нужно проверить, кто подписал PDF и какие метаданные подписи были сохранены.

### Шаги

1. Создайте `PdfFileSignature` создать экземпляр и привязать подписанный PDF.
2. Прочитайте коллекцию подписей и выберите имя подписи.
3. Вызовите аксессоры информации о подписи для имени подписанта, даты, причины и места.
4. Закройте объект фасада после завершения.

### Пример на Java

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


