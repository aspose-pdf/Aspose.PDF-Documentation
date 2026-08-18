---
title: Создать PDF-документ программно
linktitle: Создать PDF
type: docs
weight: 10
url: /java/create-document/
description: Узнайте, как создать PDF-документ с нуля на Java с помощью Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создание PDF-файлов с помощью Aspose.PDF для Java
Abstract: В этой статье показано, как создать PDF-файл на Java с помощью Aspose.PDF. В примере создается новый объект Document, добавляется страница, вставляется TextFragment с образцом текста и сохраняется результат в виде PDF-файла.
---
Создание PDF-файлов в коде является общим требованием для отчетов, счетов-фактур и созданных деловых документов. Aspose.PDF для Java предоставляет прямой способ создания документа с нуля.

## Как создать PDF-файл в Java

Чтобы создать PDF-документ программным способом:

1. Создайте объект [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) в абзацы страницы.
1. Сохраните [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в выходной файл.

## Создайте простой PDF-документ

Следующий пример Java основан на `CreatePdfDocumentExamples.java`.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```
