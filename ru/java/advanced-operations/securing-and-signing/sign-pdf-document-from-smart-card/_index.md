---
title: Подписывайте PDF-документы с помощью смарт-карты в Java
linktitle: Подписание PDF с помощью смарт-карты
type: docs
weight: 30
url: /ru/java/sign-pdf-document-from-smart-card/
description: Просмотрите текущий охват примеров Java для подписи PDF на основе сертификата в Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Охват подписи PDF на основе сертификата в текущем наборе примеров Java
Abstract: Эта страница описывает текущий масштаб примеров подписи, доступных в исходном дереве документации Java. Репозиторий включает примеры подписи PDF на основе сертификата с учётными данными PFX или PKCS7, но в настоящее время не содержит отдельного примера хранилища сертификатов смарт‑карты для Java.
---
Текущий репозиторий Java не включает отдельный пример подписания смарт-картой, основанный на исходных данных, под `facades/pdffilesignature`, но следующий рабочий процесс показывает типичный шаблон API для подписи PDF с сертификатом, выбранным из локального хранилища сертификатов.

## Подписать PDF‑документ со смарт‑карты

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) facade и привязать исходный PDF‑документ.
1. Получите локальный сертификат и создайте требуемый [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/).
1. Настройте внешний вид визуальной подписи и цель [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Примените подпись к PDF‑документу через [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Сохраните обновлённый PDF‑документ.
1. Привяжите загруженный документ к [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) фасад с `bindPdf(...)`.
1. Получите локальный сертификат, представляющий учетные данные смарт‑карты, вызвав `getLocalCertificate()`.
1. Проверьте, найден ли сертификат. Если нет, сохраните неизмененный выходной файл и остановите рабочий процесс.
1. Создайте [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) из выбранного сертификата.
1. Установите изображение внешнего вида визуальной подписи с `setSignatureAppearance(...)`.
1. Вызовите `sign(...)` с целевой страницей, причиной, контактом, местоположением, флагом видимости, подпись [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), и объект внешней подписи.
1. Сохраните подписанный PDF по пути вывода.

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


