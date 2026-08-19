---
title: Создайте PDF документ программно
linktitle: Создайте PDF
type: docs
weight: 10
url: /ru/java/create-document/
description: Узнайте, как создать PDF документ с нуля на Java с помощью Aspose.PDF.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создание PDF файлов с помощью Aspose.PDF for Java
Abstract: В этой статье показано, как создать PDF файл на Java с помощью Aspose.PDF. В примере создаётся новый объект Document, добавляется страница, вставляется TextFragment с образцом текста, и результат сохраняется как PDF файл.
---
Создание PDF файлов в коде является обычной потребностью для отчетов, счетов‑фактур и генерируемых бизнес‑документов. Aspose.PDF for Java предоставляет прямой способ построить документ с нуля.

## Как создать PDF файл в Java

Чтобы создать PDF документ программно:

1. Создайте [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объект.
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) в параграфы страницы.
1. Сохраните [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в выходной файл.

## Создайте простой PDF-документ

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

