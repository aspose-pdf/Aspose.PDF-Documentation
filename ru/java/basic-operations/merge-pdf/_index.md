---
title: Объединение PDF-файлов в Java
linktitle: Объединить PDF-файлы
type: docs
weight: 50
url: /java/merge-pdf/
description: Узнайте, как объединить несколько файлов PDF в один документ на Java с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединение страниц PDF с помощью Java
Abstract: В этой статье объясняется, как объединить два PDF-документа в Java с помощью Aspose.PDF. В примере открываются два исходных документа, добавляются страницы второго документа к первому и сохраняется объединенный результат как новый файл PDF.
---
Объединение PDF-файлов полезно, когда вам нужно объединить связанные документы в один файл для распространения, архивирования или обработки.

## Живой пример

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) — бесплатное онлайн-приложение для тестирования слияния PDF-файлов в браузере.

В этом разделе показано, как объединить несколько файлов PDF в один документ в Java:

1. Откройте оба исходных документа с помощью конструктора [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте коллекцию [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) из второго [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) к первому с помощью `document1.getPages().add(document2.getPages())`.
1. Сохраните объединенный [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в выходной путь.

## Объединить два PDF-документа

Следующий пример Java основан на `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
