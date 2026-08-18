---
title: Подписание PDF-документов
linktitle: Подписание PDF-документов
type: docs
weight: 10
url: /java/pdf-signing/
description: Узнайте, как подписывать PDF-документы на Java с помощью фасада PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подписывайте PDF-документы цифровыми подписями на Java
Abstract: Узнайте, как подписывать документы PDF с помощью Aspose.PDF для Java. Набор примеров Java охватывает подписание с использованием настроенного пути сертификата и пароля, а также подписание с использованием явного объекта подписи PKCS7, который включает метаданные подписи, такие как причина, контактная информация, местоположение и полномочия.
---
## Подписывать PDF-документы

Используйте `PdfFileSignature`, если вам нужно применить видимую цифровую подпись к PDF-файлу.

### Шаги

1. Создайте экземпляр `PdfFileSignature` и привяжите исходный PDF-файл.
2. Загрузите сертификат либо через `setCertificate`, либо создав объект `PKCS7`.
3. Вызовите `sign`, указав целевую страницу, настройки видимости, прямоугольник подписи и данные подписи.
4. Сохраните подписанный PDF-файл и закройте объект фасада.

### Примеры Java

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
