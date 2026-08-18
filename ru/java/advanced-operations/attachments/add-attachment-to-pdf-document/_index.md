---
title: Добавить вложения в PDF в Java
linktitle: Добавление вложения в PDF-документ
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: Узнайте, как добавлять вложения файлов в PDF-документы на Java с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавляйте встроенные файлы в PDF-документы с помощью Java
Abstract: В этой статье показано, как прикрепить внешний файл к PDF-документу с помощью Aspose.PDF для Java. В примере открывается существующий PDF-файл, создается FileSpecification для вложения, добавляется в коллекцию EmbeddedFiles документа и сохраняется обновленный файл.
---
Чтобы прикрепить файл к PDF-файлу, загрузите исходный документ, создайте `FileSpecification`, добавьте его во встроенную коллекцию файлов и сохраните результат.

## Добавьте вложение в PDF-документ

Используйте этот пример, когда внешний файл необходимо внедрить в существующий PDF-файл.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) для файла, который вы хотите внедрить.
1. Добавьте спецификацию файла в коллекцию `EmbeddedFiles` и сохраните обновленный документ.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
