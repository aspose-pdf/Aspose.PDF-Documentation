---
title: PDF-сертификация
linktitle: PDF-сертификация
type: docs
weight: 30
url: /java/pdf-certification/
description: Узнайте, как сертифицировать PDF-документы на Java с помощью PdfFileSignature и DocMDPSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сертификация PDF-документов с разрешениями DocMDP в Java
Abstract: Узнайте, как сертифицировать PDF-документы с помощью Aspose.PDF для Java. В примере Java используется PdfFileSignature вместе с DocMDPSignature и DocMDPAccessPermissions для сертификации документа для заполнения и подписания форм, ограничивая при этом другие виды изменений.
---
## Сертификация PDF-документов

Используйте сертификацию, когда документ должен оставаться надежным, но при этом разрешать определенный класс изменений после подписания.

### Шаги

1. Создайте экземпляр `PdfFileSignature` и привяжите исходный PDF-файл.
2. Создайте объект подписи `PKCS7` с сертификатом и паролем сертификата.
3. Оберните эту подпись в `DocMDPSignature` с необходимым значением `DocMDPAccessPermissions`.
4. Вызовите `certify`, указав целевую страницу, метаданные подписи, видимый прямоугольник и подпись MDP.
5. Сохраните сертифицированный PDF-файл и закройте объект фасада.

### Пример Java

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com", "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
