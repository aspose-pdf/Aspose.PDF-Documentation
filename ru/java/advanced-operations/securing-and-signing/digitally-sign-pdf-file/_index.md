---
title: Добавить цифровую подпись или подписать PDF в Java
linktitle: Подписать PDF цифровой подписью
type: docs
weight: 10
url: /ru/java/digitally-sign-pdf-file/
description: Узнайте, как цифрово подписывать и заверять PDF документы в Java с помощью Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подписать PDF файлы цифровой подписью с помощью Java
Abstract: Это руководство объясняет, как цифровой подписью подписывать PDF‑документы с использованием Aspose.PDF for Java. Оно охватывает подпись с использованием объекта сертификата, подпись с базовыми параметрами сертификата и сертификацию документа подписью DocMDP для контроля разрешённых изменений после подписи.
---
Aspose.PDF for Java поддерживает несколько потоков подписи через `PdfFileSignature`.

## Подписать PDF с объектом сертификата

1. Создайте [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) фасад и привязать исходный PDF документ.
1. Создайте [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) объект подписи и настроить параметры подписи.
1. Применить подпись к PDF‑документу через [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Сохраните обновлённый PDF‑документ.

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
```

Этот подход создает `PKCS7` сначала объект подписи, а затем применяет его к странице 1.

## Подпишите PDF с базовыми параметрами сертификата

1. Создайте [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) фасад и привязать исходный PDF документ.
1. Настройте параметры сертификата, требуемые примером подписи.
1. Применить подпись к PDF‑документу через [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Сохраните обновлённый PDF‑документ.

```java
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

## Сертифицировать PDF с помощью DocMDP

Используйте подпись обнаружения и предотвращения изменения документа, когда требуются ограничения уровня сертификации:

1. Создайте [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) фасад и привязать исходный PDF документ.
1. Создайте [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) объект и настройте [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/) параметры подписи.
1. Примените сертификационную подпись и сохраните обновлённый PDF‑документ.

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com",
                "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

