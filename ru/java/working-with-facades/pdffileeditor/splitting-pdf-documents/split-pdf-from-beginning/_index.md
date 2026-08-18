---
title: Разделить PDF с начала
linktitle: Разделить PDF с начала
type: docs
weight: 10
url: /java/split-pdf-from-beginning/
description: Разделите PDF-файл с самого начала в Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлеките первые страницы PDF-файла в новый документ с помощью Java.
Abstract: Узнайте, как разделить PDF-файл с самого начала с помощью Aspose.PDF для Java. В примере Java используется PdfFileEditor, чтобы взять первые три страницы документа и сохранить их как отдельный PDF-файл.
---
## Разделить PDF с начала

Образец Java извлекает первые три страницы из исходного документа.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Вызовите `splitFromFirst`, указав исходный файл, количество сохраняемых страниц и выходной файл.
3. Сохраните новый PDF-документ.

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
