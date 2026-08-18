---
title: Объединение двух PDF-файлов
linktitle: Объединение двух PDF-файлов
type: docs
weight: 60
url: /java/concatenate-two-files/
description: Объедините два PDF-файла в один документ на Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объедините два PDF-файла в один выходной документ с помощью Java.
Abstract: Узнайте, как объединить два файла PDF с помощью Aspose.PDF для Java. В примере Java используется PdfFileEditor и перегрузка `concatenate` на основе массива для объединения двух исходных документов в один выходной PDF-файл.
---
## Объединение двух PDF-файлов

Эта статья напрямую соответствует примеру `mergePdfDocuments` в `PdfFileEditorExamples.java`.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Передайте два пути к входным файлам как массив строк.
3. Вызовите `concatenate`, указав массив и путь к выходному файлу.
4. Сохраните объединенный PDF-файл.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```
