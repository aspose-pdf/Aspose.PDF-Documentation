---
title: Получить метаданные PDF
linktitle: Получить метаданные PDF
type: docs
weight: 20
url: /ru/java/get-pdf-metadata/
description: Узнайте, как читать метаданные PDF в Java с фасадом PdfFileInfo.
lastmod: "2026-08-19"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получение метаданных PDF с помощью Aspose.PDF for Java.
Abstract: Узнайте, как получать метаданные PDF с помощью Aspose.PDF for Java. Пример на Java читает стандартные поля, такие как тема, заголовок, ключевые слова, создатель, дата создания и дата изменения, а также флаги статуса файла и пользовательскую запись метаданных `Reviewer`.
---
## Получите метаданные PDF

Этот пример читает стандартную информацию о документе, флаги статуса файла и пользовательский ключ метаданных.

### Шаги

1. Создайте `PdfFileInfo` объект для исходного PDF.
2. Прочитайте стандартные поля метаданных, такие как тема, название, ключевые слова и создатель.
3. Проверьте флаги состояния файла, например, является ли файл действительным, зашифрованным, защищённым паролем или является ли он портфолио.
4. Прочитать значение пользовательского метаданных с помощью `getMetaInfo`.
5. Закройте `PdfFileInfo` экземпляр.

### Пример на Java

```java
public static void getPdfMetadata(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    System.out.println("Subject: " + pdfInfo.getSubject());
    System.out.println("Title: " + pdfInfo.getTitle());
    System.out.println("Keywords: " + pdfInfo.getKeywords());
    System.out.println("Creator: " + pdfInfo.getCreator());
    System.out.println("Creation Date: " + pdfInfo.getCreationDate());
    System.out.println("Modification Date: " + pdfInfo.getModDate());
    System.out.println("Is Valid PDF: " + pdfInfo.isPdfFile());
    System.out.println("Is Encrypted: " + pdfInfo.isEncrypted());
    System.out.println("Has Open Password: " + pdfInfo.hasOpenPassword());
    System.out.println("Has Edit Password: " + pdfInfo.hasEditPassword());
    System.out.println("Is Portfolio: " + pdfInfo.hasCollection());
    String reviewer = pdfInfo.getMetaInfo("Reviewer");
    System.out.println("Reviewer: " + (reviewer == null || reviewer.isBlank() ? "No Reviewer metadata found." : reviewer));
    pdfInfo.close();
}
```


