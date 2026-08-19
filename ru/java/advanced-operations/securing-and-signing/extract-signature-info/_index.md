---
title: Извлечение информации о подписи из PDF в Java
linktitle: Извлечение деталей из подписи
type: docs
weight: 20
url: /ru/java/extract-image-and-signature-information/
description: Узнайте, как извлекать сведения о сертификате и цифровой подписи из PDF‑файлов в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение сведений о подписи и данных сертификата из подписанных PDF‑файлов в Java
Abstract: Эта статья объясняет, как проверять цифровые подписи в PDF‑документах с помощью Aspose.PDF for Java. Узнайте, как читать сведения о подписавшем, проверять подпись, проверять, покрывает ли подпись весь документ, извлекать встроенный сертификат подписи и удалять существующую подпись.
---
Использовать `PdfFileSignature` для проверки и управления подписями, уже существующими в PDF‑документе.

## Читать информацию о подписи

1. Создайте [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) фасад и привязать исходный PDF-документ.
1. Получите имя подписи документа и настройте поток проверки подписи, требуемый в примере.
1. Прочитайте и проверьте информацию о подписи из [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) фасад.
1. Прочитайте возвращенные значения или продолжите следующую операцию обработки.

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

## Проверьте подпись

1. Создайте [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) фасад и привязать исходный PDF-документ.
1. Получите имя подписи документа и настройте поток проверки, требуемый в примере.
1. Прочитайте и проверьте информацию о подписи из [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) фасад.

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

1. Создайте [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) фасад и привязать исходный PDF-документ.
1. Получите имя подписи документа, необходимое для извлечения сертификата.
1. Запишите извлечённый вывод или проверьте возвращённые значения из [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) фасад.

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

