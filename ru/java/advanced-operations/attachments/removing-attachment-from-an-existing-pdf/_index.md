---
title: Удаление вложений из PDF в Java
linktitle: Удаление вложения из существующего PDF-файла
type: docs
weight: 30
url: /java/removing-attachment-from-an-existing-pdf/
description: Узнайте, как удалить одно или все встроенные вложения из PDF-документов в Java с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалите вложения PDF программно с помощью Java
Abstract: В этой статье показано, как удалить вложения из файлов PDF с помощью Aspose.PDF для Java. В примерах показано удаление одного внедренного файла по ключу и очистка всей коллекции EmbeddedFiles перед сохранением обновленного документа.
---
Вложения, хранящиеся в PDF-документе, можно удалить по отдельности или все сразу с помощью коллекции `EmbeddedFiles`.

## Удалите одно вложение

Используйте этот пример, когда из PDF-файла необходимо удалить внедренный файл с именем.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите вложение по его ключу из коллекции встроенных файлов.
1. Сохраните обновленный выходной документ.

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## Удалите все вложения

Используйте этот подход, когда необходимо очистить всю коллекцию внедренных файлов.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите все элементы из коллекции встроенных файлов.
1. Сохраните очищенный выходной документ.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
