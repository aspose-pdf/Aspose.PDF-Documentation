---
title: Извлечение информации о подписи из PDF в Java
linktitle: Извлечь данные из подписи
type: docs
weight: 20
url: /java/extract-image-and-signature-information/
description: Узнайте, как извлечь данные сертификата и цифровой подписи из файлов PDF на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение данных подписи и данных сертификата из подписанных PDF-файлов на Java.
Abstract: В этой статье объясняется, как проверять цифровые подписи в документах PDF с помощью Aspose.PDF для Java. Узнайте, как читать данные подписывающего лица, проверять подпись, проверять, охватывает ли подпись весь документ, извлекать встроенный сертификат подписи и удалять существующую подпись.
---
Используйте `PdfFileSignature` для проверки и управления подписями, которые уже существуют в PDF-документе.

## Прочитать информацию о подписи

1. Создайте фасад [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) и привяжите исходный PDF-документ.
1. Получите доступ к имени подписи документа и настройте поток проверки подписи, требуемый в примере.
1. Прочтите и проверьте информацию подписи из фасада [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Прочтите возвращенные значения или перейдите к следующему шагу обработки.

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

## Проверка подписи

1. Создайте фасад [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) и привяжите исходный PDF-документ.
1. Получите доступ к имени подписи документа и настройте поток проверки, требуемый в примере.
1. Прочтите и проверьте информацию подписи из фасада [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: "
                + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: "
                + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## Извлеките сертификат подписи

1. Создайте фасад [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) и привяжите исходный PDF-документ.
1. Получите доступ к имени подписи документа, необходимому для извлечения сертификата.
1. Запишите извлеченные выходные данные или проверьте возвращаемые значения из фасада [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).

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
