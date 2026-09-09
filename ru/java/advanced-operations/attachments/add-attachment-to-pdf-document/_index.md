---
title: Добавление вложений в PDF на Java
linktitle: Добавление вложения в документ PDF
type: docs
weight: 10
url: /ru/java/add-attachment-to-pdf-document/
description: Узнайте, как добавить файловые вложения в документы PDF на Java с использованием Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление встроенных файлов в документы PDF с помощью Java
Abstract: В этой статье показано, как прикрепить внешний файл к документу PDF с использованием Aspose.PDF for Java. Пример открывает существующий PDF, создает объект FileSpecification для вложения, добавляет его в коллекцию EmbeddedFiles документа и сохраняет обновленный файл.
---
Чтобы прикрепить файл к PDF, загрузите исходный документ, создайте a `FileSpecification`, добавьте его в коллекцию встроенных файлов и сохраните результат.

## Добавьте вложение в документ PDF

Используйте этот пример, когда внешний файл должен быть внедрён в существующий PDF.

1. Откройте исходный PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) для файла, который вы хотите встроить.
1. Добавьте спецификацию файла к `EmbeddedFiles` соберите и сохраните обновлённый документ.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```


