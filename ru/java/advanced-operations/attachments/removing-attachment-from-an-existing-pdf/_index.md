---
title: Удалить вложения из PDF на Java
linktitle: Удаление вложения из существующего PDF
type: docs
weight: 30
url: /ru/java/removing-attachment-from-an-existing-pdf/
description: Узнайте, как удалить одно или все встроенные вложения из PDF‑документов на Java с использованием Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Программно удалять вложения PDF с помощью Java
Abstract: В этой статье показано, как удалить вложения из PDF‑файлов с помощью Aspose.PDF for Java. Примеры демонстрируют удаление одного встроенного файла по ключу и очистку всей коллекции EmbeddedFiles перед сохранением обновлённого документа.
---
Вложения, хранящиеся в документе PDF, можно удалить как по отдельности, так и сразу все через `EmbeddedFiles` коллекция.

## Удалите одно вложение

Используйте этот пример, когда один именованный встроенный файл должен быть удалён из PDF.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите вложение по его ключу из коллекции встроенных файлов.
1. Сохраните обновлённый результирующий документ.

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## Удалите все вложения

Используйте этот подход, когда необходимо очистить всю коллекцию вложенных файлов.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите все элементы из коллекции вложенных файлов.
1. Сохраните очищенный выходной документ.

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```

