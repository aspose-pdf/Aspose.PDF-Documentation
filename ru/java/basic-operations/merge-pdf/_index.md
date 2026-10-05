---
title: Объединение PDF-файлов в Java
linktitle: Объединение PDF-файлов
type: docs
weight: 50
url: /ru/java/merge-pdf/
description: Узнайте, как объединить несколько PDF-файлов в один документ в Java с помощью Aspose.PDF.
lastmod: "2026-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединить страницы PDF с помощью Java
Abstract: В этой статье объясняется, как объединить два PDF-документа в Java с помощью Aspose.PDF. Пример открывает два исходных документа, добавляет страницы второго документа к первому и сохраняет объединённый результат в новый PDF‑файл.
---
Объединение PDF-файлов полезно, когда необходимо собрать связанные документы в один файл для распространения, архивирования или обработки.

## Онлайн-пример

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) — это бесплатное онлайн-приложение для тестирования слияния PDF в браузере.

В этой статье показано, как объединить несколько PDF‑файлов в один документ на Java:

1. Откройте оба исходных документа с помощью конструктора [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте коллекцию страниц [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) из второго документа [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в первый с помощью `document1.getPages().add(document2.getPages())`.
1. Сохраните объединённый [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в выходной файл.

## Объединение двух PDF-документов

Следующий пример на Java основан на `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```


