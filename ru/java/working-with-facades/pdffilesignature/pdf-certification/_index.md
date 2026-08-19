---
title: Сертификация PDF
linktitle: Сертификация PDF
type: docs
weight: 30
url: /ru/java/pdf-certification/
description: Узнайте, как сертифицировать PDF‑документы на Java с помощью PdfFileSignature и DocMDPSignature.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Сертифицируйте PDF‑документы с разрешениями DocMDP на Java
Abstract: Узнайте, как сертифицировать PDF‑документы с помощью Aspose.PDF for Java. Пример на Java использует PdfFileSignature вместе с DocMDPSignature и DocMDPAccessPermissions для сертификации документа, позволяя заполнять формы и подписывать его, одновременно ограничивая другие виды модификации.
---
## Сертифицировать PDF‑документы

Используйте сертификацию, когда документ должен оставаться доверенным, но при этом допускает определённый класс изменений после подписи.

### Шаги

1. Создайте `PdfFileSignature` экземпляр и привязать исходный PDF.
2. Создайте `PKCS7` объект подписи с сертификатом и паролем сертификата.
3. Обверните эту подпись в `DocMDPSignature` с требуемым `DocMDPAccessPermissions` значение.
4. Вызов `certify` с целевой страницей, метаданными подписи, видимым прямоугольником и подписью MDP.
5. Сохраните подписанный PDF и закройте фасадный объект.

### Пример на Java

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

