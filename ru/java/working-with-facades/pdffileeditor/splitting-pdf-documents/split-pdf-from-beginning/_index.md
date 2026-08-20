---
title: Разделить PDF с начала
linktitle: Разделить PDF с начала
type: docs
weight: 10
url: /ru/java/split-pdf-from-beginning/
description: Разделить PDF с начала в Java с помощью фасада PdfFileEditor.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечь первые страницы PDF в новый документ с помощью Java
Abstract: Узнайте, как разделить PDF с начала с помощью Aspose.PDF for Java. Пример на Java использует PdfFileEditor, чтобы взять первые три страницы документа и сохранить их как отдельный PDF.
---
## Разделить PDF с начала

Пример на Java извлекает первые три страницы из исходного документа.

### Шаги

1. Создайте `PdfFileEditor` экземпляр.
2. Вызовите `splitFromFirst` с исходным файлом, количеством страниц для сохранения и выходным файлом.
3. Сохраните новый PDF-документ.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```


