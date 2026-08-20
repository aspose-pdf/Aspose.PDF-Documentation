---
title: Подписать PDF-документы
linktitle: Подписать PDF-документы
type: docs
weight: 10
url: /ru/java/pdf-signing/
description: Узнайте, как подписывать PDF-документы в Java с помощью фасада PdfFileSignature.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подписать PDF-документы цифровыми подписями в Java
Abstract: Узнайте, как подписывать PDF-документы с помощью Aspose.PDF for Java. Набор примеров Java охватывает подпись с указанным путем к сертификату и паролем, а также подпись с явным объектом подписи PKCS7, который включает метаданные подписи, такие как причина, контактная информация, местоположение и полномочия.
---
## Подписать PDF-документы

Использовать `PdfFileSignature` когда вам нужно применить видимую цифровую подпись к PDF.

### Шаги

1. Создайте `PdfFileSignature` экземпляр и привязать исходный PDF.
2. Загрузите сертификат либо через `setCertificate` или создавая `PKCS7` объект.
3. Вызовите `sign` с целевой страницей, настройками видимости, прямоугольником подписи и данными подписи.
4. Сохраните подписанный PDF и закройте объект фасада.

### Примеры на Java

```java
public static void signPdfWithCertificateObject(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.sign(1, false, signatureRectangle(), createPkcs7(certificateFile, "Document approval"));
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}

public static void signPdfWithBasicParameters(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.setCertificate(certificateFile.toString(), CERTIFICATE_PASSWORD);
        pdfSignature.sign(1, "Document approval", "qa@example.com", "New York, USA", false, signatureRectangle());
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```


