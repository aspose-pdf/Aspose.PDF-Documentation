---
title: Разделить PDF до конца
linktitle: Разделить PDF до конца
type: docs
weight: 40
url: /ru/java/split-pdf-to-end/
description: Разделить PDF с выбранной страницы до конца на Java с фасадом PdfFileEditor.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечь страницы начиная с определённой позиции до конца PDF с помощью Java
Abstract: Узнайте, как разделить PDF до конца с помощью Aspose.PDF for Java. Пример на Java использует PdfFileEditor для извлечения всех страниц, начиная со страницы 2 и до конца исходного документа.
---
## Разделить PDF до конца

Пример на Java извлекает все страницы, начиная со страницы 2.

### Шаги

1. Создайте `PdfFileEditor` экземпляр.
2. Вызовите `splitToEnd` с исходным файлом, номером начальной страницы и файлом вывода.
3. Сохраните полученный PDF‑документ.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```


