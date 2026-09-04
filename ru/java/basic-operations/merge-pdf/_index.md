---
title: Объединить PDF-файлы в Java
linktitle: Объединить PDF-файлы
type: docs
weight: 50
url: /ru/java/merge-pdf/
description: Узнайте, как объединить несколько PDF-файлов в один документ в Java с помощью Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединить страницы PDF с помощью Java
Abstract: В этой статье объясняется, как объединить два PDF-документа в Java с помощью Aspose.PDF. Пример открывает два исходных документа, добавляет страницы второго документа к первому и сохраняет объединённый результат в новый PDF‑файл.
---
Объединение PDF-файлов полезно, когда необходимо собрать связанные документы в один файл для распространения, архивирования или обработки.

## Пример в реальном времени

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) это бесплатное онлайн-приложение для тестирования слияния PDF в браузере.

В этой статье показано, как объединить несколько PDF‑файлов в один документ на Java:

1. Откройте оба исходных документа с помощью [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) конструктор.
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) коллекцию со второй [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) к первому с `document1.getPages().add(document2.getPages())`.
1. Сохраните объединённый [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в путь вывода.

## Объедините два PDF-документа

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


