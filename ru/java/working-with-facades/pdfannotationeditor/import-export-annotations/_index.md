---
title: Импорт и экспорт аннотаций с использованием Java
linktitle: Импорт и экспорт аннотаций
type: docs
weight: 80
url: /ru/java/pdfannotationeditor-class/import-export-annotations/
description: Узнайте, как копировать аннотации из одного PDF‑документа в другой PDF‑документ с помощью Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Перенос PDF‑аннотаций между документами на Java
Abstract: В этой статье объясняется, как копировать аннотации из исходного PDF и экспортировать их в новый PDF‑документ с использованием Java. Рабочий процесс загружает исходный файл, создает целевой документ, добавляет страницу, копирует аннотации с первой исходной страницы и сохраняет результат.
---
## Копируйте аннотации из одного PDF в другой

1. Откройте исходный PDF и создайте новый документ назначения с целевой страницей.
2. Переберите аннотации на первой странице источника и добавьте каждую из них на страницу назначения.
3. Сохраните документ назначения, чтобы зафиксировать скопированные аннотации.

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


