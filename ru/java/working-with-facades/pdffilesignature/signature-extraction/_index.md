---
title: Извлечение подписи
linktitle: Извлечение подписи
type: docs
weight: 50
url: /ru/java/signature-extraction/
description: Узнайте, как извлечь сертификат подписи из подписанного PDF на Java с помощью PdfFileSignature.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечь сертификат подписи из PDF на Java
Abstract: Узнайте, как извлечь сертификат, связанный с подписью PDF, используя Aspose.PDF for Java. Текущий набор примеров на Java включает извлечение сертификата в выходной поток, но не включает отдельный пример извлечения изображения подписи.
---
## Извлеките сертификат подписи

Используйте этот процесс, когда вам нужно сохранить сертификат, связанный с существующей подписью.

### Шаги

1. Создайте `PdfFileSignature` создайте экземпляр и привяжите подписанный PDF.
2. Выберите имя подписи для проверки.
3. Вызов `extractCertificate` для открытия потока сертификата.
4. Скопируйте байты сертификата в выходной файл.
5. Закройте ресурсы потока и объект фасада.

### Пример на Java

```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```

Текущий `PdfFileSignatureExamples.java` класс не включает отдельный пример на Java для извлечения изображения отрисованной подписи.

