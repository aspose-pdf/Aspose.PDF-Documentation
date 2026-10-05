---
title: Импорт и экспорт аннотаций с использованием Java
linktitle: Импорт и экспорт аннотаций
type: docs
weight: 80
url: /ru/java/import-export-annotations/
description: Узнайте, как копировать аннотации из одного PDF‑документа в другой PDF‑документ с помощью Aspose.PDF for Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Переносите PDF‑аннотации между документами в Java.
Abstract: В этой статье объясняется, как копировать аннотации из исходного PDF и экспортировать их в новый PDF‑документ с использованием Aspose.PDF for Java. Рабочий процесс загружает исходный файл, создает целевой документ, добавляет страницу, копирует аннотации с первой исходной страницы и сохраняет результат.
---
## Копирование аннотаций из одного PDF в другой

1. Откройте исходный PDF-документ с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в целевой документ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте каждую аннотацию [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) на целевую страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Прочитайте или переберите элементы [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) на целевой странице.
1. Сохраните обновлённый PDF-документ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите элементы [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) на первой странице исходного документа и добавьте каждый из них на целевую страницу.

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
