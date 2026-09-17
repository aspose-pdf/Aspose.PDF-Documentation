---
title: Создание PDF документа программно
linktitle: Создание PDF
type: docs
weight: 10
url: /ru/java/create-document/
description: Узнайте, как создать PDF документ с нуля на Java с помощью Aspose.PDF.
lastmod: "2026-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создание PDF файлов с помощью Aspose.PDF for Java
Abstract: В этой статье показано, как создать PDF файл на Java с помощью Aspose.PDF. В примере создаётся новый объект Document, добавляется страница, вставляется TextFragment с образцом текста, и результат сохраняется как PDF файл.
---
Программное создание PDF-файлов часто требуется для подготовки отчётов, счетов‑фактур и других деловых документов. Aspose.PDF for Java предоставляет прямой способ построить документ с нуля.

## Создание PDF-файла в Java

Чтобы создать PDF-документ программно:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Добавьте фрагмент [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) в коллекцию абзацев страницы.
1. Сохраните [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в выходной файл.

## Создание простого PDF-документа

Следующий пример на Java основан на `CreatePdfDocumentExamples.java`.

```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```


