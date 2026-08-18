---
title: Импорт и экспорт аннотаций с помощью Java
linktitle: Импорт и экспорт аннотаций
type: docs
weight: 80
url: /java/pdfannotationeditor-class/import-export-annotations/
description: Узнайте, как копировать аннотации из одного PDF-документа в другой PDF-документ с помощью Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Перенос аннотаций PDF между документами в Java
Abstract: В этой статье объясняется, как скопировать аннотации из исходного PDF-файла и экспортировать их в новый PDF-документ с помощью Java. Рабочий процесс загружает исходный файл, создает целевой документ, добавляет страницу, копирует аннотации с первой исходной страницы и сохраняет результат.
---
## Копирование аннотаций из одного PDF-файла в другой

1. Откройте исходный PDF-файл и создайте новый целевой документ с целевой страницей.
2. Перечислите аннотации на первой исходной странице и добавьте каждую из них на целевую страницу.
3. Сохраните целевой документ, чтобы сохранить скопированные аннотации.

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
