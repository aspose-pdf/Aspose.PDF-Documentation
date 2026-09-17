---
title: Разделение PDF-файлов на Java
linktitle: Разделение PDF-файлов
type: docs
weight: 60
url: /ru/java/split-pdf/
description: Узнайте, как разделить PDF на одностраничные PDF-файлы на Java с использованием Aspose.PDF.
lastmod: "2026-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделение страниц PDF с помощью Java
Abstract: В этой статье показано, как разделить PDF-документ на отдельные одностраничные PDF-файлы на Java с использованием Aspose.PDF. Пример открывает исходный документ, перебирает его страницы, создает новый документ для каждой страницы и сохраняет каждую страницу как отдельный PDF-файл.
---
Разделение PDF на отдельные файлы полезно, когда необходимо экспортировать каждую страницу для просмотра, хранения или последующей обработки.

## Онлайн-пример

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) — это бесплатное онлайн‑приложение для тестирования разделения PDF в браузере.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Этот пример использует класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для открытия PDF‑файла и перебора его страниц. Для каждой страницы [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) он создаёт новый документ, добавляет страницу в него и сохраняет результат как отдельный PDF‑файл.

Чтобы разделить PDF на отдельные файлы страниц в Java:

1. Откройте исходный PDF с помощью конструктора [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите объекты [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), возвращаемые `document.getPages()`.
1. Создайте новый пустой [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для каждой страницы.
1. Добавьте текущую страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в новый документ [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните новый [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с уникальным именем файла.
1. Закройте оба объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) после завершения обработки.

## Разделение PDF на файлы с одной страницей

Следующий пример на Java основан на `SplitDocumentExamples.java` и сохраняет страницы как `Page_1.pdf`, `Page_2.pdf` и так далее.

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


