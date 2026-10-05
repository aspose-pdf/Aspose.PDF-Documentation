---
title: Объединение двух PDF‑файла
linktitle: Объединение двух PDF‑файла
type: docs
weight: 60
url: /ru/java/concatenate-two-files/
description: Объединить два PDF‑файла в один документ на Java с фасадом PdfFileEditor.
lastmod: "2026-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Объединить два PDF‑файла в один выходной документ с помощью Java
Abstract: Узнайте, как объединять два PDF‑файла с помощью Aspose.PDF for Java. Пример на Java использует PdfFileEditor и перегрузку `concatenate`, основанную на массиве, для объединения двух исходных документов в один выходной PDF.
---
## Объединение двух PDF‑файлов

Эта статья соответствует примеру `mergePdfDocuments` в `PdfFileEditorExamples.java`.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Передайте два пути входных файлов в виде массива строк.
3. Вызовите `concatenate` с массивом и путём к файлу вывода.
4. Сохраните объединённый PDF.

```java
public static void mergePdfDocuments(Path firstInputFile, Path secondInputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.concatenate(new String[] {firstInputFile.toString(), secondInputFile.toString()}, outputFile.toString());
}
```


