---
title: Импорт и экспорт аннотаций с помощью Java
linktitle: Импорт и экспорт аннотаций
type: docs
weight: 80
url: /java/import-export-annotations/
description: Узнайте, как скопировать аннотации из одного PDF-документа в другой PDF-документ с помощью Aspose.PDF для Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Перенос аннотаций PDF между документами на Java.
Abstract: В этой статье объясняется, как скопировать аннотации из исходного PDF-файла и экспортировать их в новый PDF-документ с помощью Aspose.PDF для Java. Рабочий процесс загружает исходный файл, создает целевой документ, добавляет страницу, копирует аннотации с первой исходной страницы и сохраняет результат.
---
## Копирование аннотаций из одного PDF-файла в другой

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в целевой [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте каждую [Аннотацию](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) на целевую [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Прочтите или просмотрите элементы [Аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) на целевой странице.
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перечислите элементы [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) на первой исходной странице и добавьте каждый из них на целевую страницу.

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
