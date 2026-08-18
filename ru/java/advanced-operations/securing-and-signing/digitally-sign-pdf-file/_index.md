---
title: Добавьте цифровую подпись или цифровую подпись PDF-файла в Java
linktitle: Цифровая подпись PDF-файла
type: docs
weight: 10
url: /java/digitally-sign-pdf-file/
description: Узнайте, как ставить цифровую подпись и сертифицировать PDF-документы на Java с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Цифровая подпись PDF-файлов с помощью Java
Abstract: В этом руководстве объясняется, как подписывать PDF-документы цифровой подписью с помощью Aspose.PDF для Java. Он охватывает подписание с помощью объекта сертификата, подписание с основными параметрами сертификата и сертификацию документа с помощью подписи DocMDP для контроля разрешенных изменений после подписания.
---
Aspose.PDF для Java поддерживает несколько потоков подписи через `PdfFileSignature`.

## Подпишите PDF-файл с помощью объекта сертификата

1. Создайте фасад [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) и привяжите исходный PDF-документ.
1. Создайте объект подписи [PKCS7](https://reference.aspose.com/pdf/java/com.aspose.pdf/pkcs7/) и настройте параметры подписи.
1. Примените подпись к PDF-документу с помощью [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Сохраните обновленный PDF-документ.

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

Этот подход сначала создает объект подписи `PKCS7`, а затем применяет его к странице 1.

## Подпишите PDF-файл с основными параметрами сертификата

1. Создайте фасад [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) и привяжите исходный PDF-документ.
1. Настройте параметры сертификата, необходимые для примера подписи.
1. Примените подпись к PDF-документу с помощью [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Сохраните обновленный PDF-документ.

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

## Сертификация PDF с помощью DocMDP

Используйте подпись обнаружения и предотвращения изменения документа, если вам нужны ограничения на уровне сертификации:

1. Создайте фасад [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) и привяжите исходный PDF-документ.
1. Создайте объект [DocMDPSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpsignature/) и настройте параметры подписи [DocMDPAccessPermissions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docmdpaccesspermissions/).
1. Примените сертификационную подпись и сохраните обновленный документ PDF.

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
