---
title: Разделить PDF-файлы на Java
linktitle: Разделить PDF-файлы
type: docs
weight: 60
url: /ru/java/split-pdf/
description: Узнайте, как разделить PDF на одностраничные PDF-файлы на Java с использованием Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Разделение страниц PDF с помощью Java
Abstract: В этой статье показано, как разделить PDF-документ на отдельные одностраничные PDF-файлы на Java с использованием Aspose.PDF. Пример открывает исходный документ, перебирает его страницы, создает новый документ для каждой страницы и сохраняет каждую страницу как отдельный PDF-файл.
---
Разделение PDF на отдельные файлы полезно, когда необходимо экспортировать каждую страницу для просмотра, хранения или последующей обработки.

## Живой пример

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) это бесплатное онлайн‑приложение для тестирования разрезания PDF в браузере.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Этот пример использует [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) класс для открытия PDF‑файла и перебора его страниц. Для каждой [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), он создает новый документ, добавляет страницу в него и сохраняет результат как отдельный PDF‑файл.

Чтобы разделить PDF на отдельные файлы страниц в Java:

1. Откройте исходный PDF с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктора.
1. Итерируйте через [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) объекты, возвращаемые `document.getPages()`.
1. Создайте новый пустой [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) для каждой страницы.
1. Добавьте текущий [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) к новому [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Сохраните новый [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) с уникальным именем файла.
1. Закройте оба [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объекты после завершения обработки.

## Разделите PDF на файлы с одной страницей

Следующий пример Java основан на `SplitDocumentExamples.java` и сохраняет страницы как `Page_1.pdf`, `Page_2.pdf`, и так далее.

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


