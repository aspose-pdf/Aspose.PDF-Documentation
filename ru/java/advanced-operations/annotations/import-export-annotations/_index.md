---
title: Импорт и экспорт аннотаций с использованием Java
linktitle: Импорт и экспорт аннотаций
type: docs
weight: 80
url: /ru/java/import-export-annotations/
description: Узнайте, как копировать аннотации из одного PDF‑документа в другой PDF‑документ с помощью Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Переносите аннотации PDF между документами в Java.
Abstract: В этой статье объясняется, как копировать аннотации из исходного PDF и экспортировать их в новый PDF‑документ с помощью Aspose.PDF for Java. Рабочий процесс загружает исходный файл, создаёт документ назначения, добавляет страницу, копирует аннотации с первой исходной страницы и сохраняет результат.
---
## Копировать аннотации из одного PDF в другой

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в пункт назначения [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте каждый [Аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) к целевому [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Читать или перебирать [Аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) элементы на целевой странице.
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перечислить [Аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) элементы на первой исходной странице и добавить каждый из них на целевую страницу.

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


