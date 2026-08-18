---
title: Разделить PDF-файлы в Java
linktitle: Разделить PDF-файлы
type: docs
weight: 60
url: /java/split-pdf/
description: Узнайте, как разделить PDF-файл на одностраничные PDF-файлы на Java с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделение страниц PDF с помощью Java
Abstract: В этой статье показано, как разделить PDF-документ на отдельные одностраничные PDF-файлы в Java с помощью Aspose.PDF. В примере открывается исходный документ, перебирает его страницы, создает новый документ для каждой страницы и сохраняет каждую страницу как отдельный файл PDF.
---
Разделение PDF-файла на отдельные файлы полезно, когда вам нужно экспортировать каждую страницу для просмотра, хранения или последующей обработки.

## Живой пример

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) — бесплатное онлайн-приложение для тестирования разделения PDF-файлов в браузере.

[![Как разделить PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

В этом примере используется класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для открытия PDF-файла и перебора его страниц. Для каждой [Страницы](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) создается новый документ, добавляется к нему страница и сохраняется результат в виде отдельного PDF-файла.

Чтобы разделить PDF-файл на отдельные файлы страниц в Java:

1. Откройте исходный PDF-файл с помощью конструктора [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебрать объекты [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), возвращенные `document.getPages()`.
1. Создайте новый пустой [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для каждой страницы.
1. Добавьте текущую [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в новый [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните новый [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с уникальным именем файла.
1. Закройте оба объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) после завершения обработки.

## Разделить PDF на одностраничные файлы

Следующий пример Java основан на `SplitDocumentExamples.java` и сохраняет страницы как `Page_1.pdf`, `Page_2.pdf` и т. д.

```java
public static void splitDocument(Path inputFile, Path outputDir) {
    Document document = new Document(inputFile.toString());
    try {
        int pageCount = 1;
        for (Page page : document.getPages()) {
            Document newDocument = new Document();
            try {
                newDocument.getPages().add(page);
                newDocument.save(outputDir.resolve("Page_" + pageCount + ".pdf").toString());
            } finally {
                newDocument.close();
            }
            pageCount++;
        }
    } finally {
        document.close();
    }
}
```
