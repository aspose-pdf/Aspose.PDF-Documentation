---
title: Подписание PDF-документов со смарт-карты в Java
linktitle: Подписание PDF-файлов с помощью смарт-карты
type: docs
weight: 30
url: /java/sign-pdf-document-from-smart-card/
description: Ознакомьтесь с текущим примером Java для подписи PDF-файлов на основе сертификатов в Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Охват подписи PDF на основе сертификатов в текущем наборе примеров Java
Abstract: На этой странице описан текущий объем примеров подписи, доступных в дереве исходного кода документации Java. Репозиторий включает примеры подписи PDF-файлов на основе сертификатов с учетными данными PFX или PKCS7, но в настоящее время он не включает специальный пример хранилища сертификатов смарт-карт для Java.
---
Текущий репозиторий Java не включает специальный пример подписи смарт-карты с поддержкой исходного кода в разделе `facades/pdffilesignature`, но следующий рабочий процесс показывает типичный шаблон API для подписания PDF-файла с помощью сертификата, выбранного из локального хранилища сертификатов.

## Подпишите PDF-документ с помощью смарт-карты

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте фасад [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) и привяжите исходный PDF-документ.
1. Получите локальный сертификат и создайте необходимую [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/).
1. Настройте внешний вид визуальной подписи и цель [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Примените подпись к PDF-документу с помощью [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Сохраните обновленный PDF-документ.
1. Привяжите загруженный документ к фасаду [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) с помощью `bindPdf(...)`.
1. Получите локальный сертификат, представляющий учетные данные смарт-карты, позвонив `getLocalCertificate()`.
1. Проверьте, найден ли сертификат. Если нет, сохраните неизмененный выходной файл и остановите рабочий процесс.
1. Создайте [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) из выбранного сертификата.
1. Установите изображение внешнего вида визуальной подписи с помощью `setSignatureAppearance(...)`.
1. Вызовите `sign(...)`, указав целевую страницу, причину, контакт, местоположение, флаг видимости, подпись [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) и внешний объект подписи.
1. Сохраните подписанный PDF-файл в выходной путь.

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
