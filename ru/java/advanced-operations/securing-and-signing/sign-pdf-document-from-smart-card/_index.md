---
title: Подписание PDF-документов со смарт-карты на Java
linktitle: Подписание PDF с помощью смарт-карты
type: docs
weight: 30
url: /ru/java/sign-pdf-document-from-smart-card/
description: Обзор текущего набора примеров Java для подписания PDF с помощью сертификатов в Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Подписание PDF с помощью сертификатов в текущем наборе примеров Java
Abstract: На этой странице описан текущий набор примеров подписания, доступных в дереве исходного кода документации по Java. Репозиторий содержит примеры подписания PDF-файлов с использованием сертификатов и учетных данных в форматах PFX или PKCS7, однако в нем пока нет отдельного примера работы с хранилищем сертификатов на смарт-карте для Java.
---
В текущем репозитории Java нет отдельного примера подписания с помощью смарт-карты, подкрепленного исходным кодом в разделе `facades/pdffilesignature`. Однако приведенный ниже рабочий процесс демонстрирует типичную схему использования API для подписания PDF с помощью сертификата, выбранного из локального хранилища сертификатов.

## Подписание PDF-документа со смарт-карты

1. Откройте исходный PDF-документ с помощью класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте фасад [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) и привяжите к нему исходный PDF-документ.
1. Получите локальный сертификат и создайте требуемый объект [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/).
1. Настройте внешний вид подписи и целевой объект [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Добавьте подпись в PDF-документ с помощью [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Сохраните обновленный PDF-документ.
1. Привяжите загруженный документ к фасаду [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) с помощью метода `bindPdf(...)`.
1. Получите локальный сертификат, представляющий учетные данные смарт-карты, вызвав метод `getLocalCertificate()`.
1. Проверьте, найден ли сертификат. Если сертификат не найден, сохраните выходной файл без изменений и завершите рабочий процесс.
1. Создайте объект [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) на основе выбранного сертификата.
1. Задайте изображение для визуального представления подписи с помощью метода `setSignatureAppearance(...)`.
1. Вызовите метод `sign(...)`, передав целевую страницу, причину подписания, контактные данные, местоположение, флаг видимости, объект [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) для области подписи и объект внешней подписи.
1. Сохраните подписанный PDF-документ по выходному пути.

```java
public static void signWithSmartCard(Path inputFile, Path outputFile, Path pngFile) {
    try (Document document = new Document(inputFile.toString());
            PdfFileSignature pdfSignature = new PdfFileSignature()) {
        pdfSignature.bindPdf(document);
        X509Certificate2 selectedCertificate = getLocalCertificate();
        if (selectedCertificate == null) {
            System.out.println("Local certificate was not found.");
            document.save(outputFile.toString());
            return;
        }

        ExternalSignature externalSignature = new ExternalSignature(selectedCertificate, null);
        pdfSignature.setSignatureAppearance(pngFile.toString());
        pdfSignature.sign(1, "Reason", "Contact", "Location", true,
                new java.awt.Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature.save(outputFile.toString());
    }
}
```
