---
title: Работа с метаданными PDF-файла в Java
linktitle: Метаданные PDF-файла
type: docs
weight: 200
url: /ru/java/pdf-file-metadata/
description: Узнайте, как извлекать, обновлять и управлять метаданными PDF-файла, информацией о документе и свойствами XMP в Java с помощью Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Получайте и задавайте информацию о PDF-документе и метаданные XMP в Java
Abstract: В этой статье объясняется, как работать с метаданными PDF с помощью Aspose.PDF for Java. Узнайте, как читать информацию о документе, такую как автор, заголовок и ключевые слова, обновлять свойства файла, проверять версию PDF и привилегии, задавать поля метаданных XMP и сохранять метаданные как через DOM, так и через API фасада.
---
Aspose.PDF for Java предоставляет два основных способа работы с метаданными:

- Через API DOM `Document`, `DocumentInfo`, и `document.getMetadata()`.
- Фасадный API через `PdfFileInfo`.

## Получите информацию о PDF-файле

Используйте этот пример, когда нужно прочитать стандартные поля информации о документе, такие как автор, заголовок, тема или ключевые слова.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) объект.
1. Прочитайте требуемые поля метаданных и выведите их значения.

```java
public static void getPdfFileInformation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();

        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
}
```

## Установите метаданные с префиксом пространства имён

Используйте этот пример, когда вам необходимо добавить или обновить свойство XMP, используя зарегистрированный префикс пространства имён.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Зарегистрируйте требуемое пространство имен XMP и добавьте элемент метаданных.
1. Сохраните обновлённый документ.

```java
public static void setPrefixMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().registerNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");
        document.getMetadata().addItem("xmp:ModifyDate", OffsetDateTime.now().toString());
        document.save(outputFile.toString());
    }
    System.out.println("Prefix metadata saved to " + outputFile);
}
```

## Обновите поля информации документа

Используйте этот пример, когда хотите записать стандартные свойства PDF‑файла, такие как автор, название, производитель или дата создания.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Доступ [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) и назначьте новые значения метаданных.
1. Сохраните документ с обновлённой информацией о файле.

```java
public static void setFileInformation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();
        Date now = new Date();

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(now);
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(now);
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");
        docInfo.setProducer("Custom producer");
        docInfo.setCreator("Custom creator");

        document.save(outputFile.toString());
    }
    System.out.println("File information saved to " + outputFile);
}
```

## Установите свойства XMP метаданных

Используйте этот пример, когда необходимо сохранить дополнительные записи XMP, включая пользовательские значения метаданных.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте требуемые элементы метаданных XMP через `document.getMetadata()`.
1. Сохраните выходной файл.

```java
public static void setXmpMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().addItem("xmp:CreateDate", OffsetDateTime.now().toString());
        document.getMetadata().addItem("xmp:Nickname", "Nickname");
        document.getMetadata().addItem("xmp:CustomProperty", "Custom Value");
        document.save(outputFile.toString());
    }
    System.out.println("XMP metadata saved to " + outputFile);
}
```


