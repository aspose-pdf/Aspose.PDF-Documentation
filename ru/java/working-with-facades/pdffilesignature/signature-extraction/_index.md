---
title: Извлечение подписи
linktitle: Извлечение подписи
type: docs
weight: 50
url: /java/signature-extraction/
description: Узнайте, как извлечь сертификат подписи из подписанного PDF-файла на Java с помощью PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение сертификата подписи из PDF в Java
Abstract: Узнайте, как извлечь сертификат, связанный с подписью PDF, с помощью Aspose.PDF для Java. Текущий набор примеров Java включает извлечение сертификата в выходной поток, но не включает отдельный образец извлечения изображения подписи.
---
## Извлеките сертификат подписи

Используйте этот рабочий процесс, если вам нужно сохранить сертификат, связанный с существующей подписью.

### Шаги

1. Создайте экземпляр `PdfFileSignature` и привяжите подписанный PDF-файл.
2. Выберите имя подписи для проверки.
3. Позвоните `extractCertificate`, чтобы открыть поток сертификатов.
4. Скопируйте байты сертификата в выходной файл.
5. Закройте ресурсы потока и объект фасада.

### Пример Java

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

Текущий класс `PdfFileSignatureExamples.java` не включает специальный пример Java для извлечения визуализированного изображения подписи.
