---
title: Список марок
linktitle: Список марок
type: docs
weight: 20
url: /java/list-stamps/
description: Узнайте, как разместить штампы на странице в Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Список штампов PDF в Java
Abstract: В этой статье показано, как связать PDF-файл, получить штампы на странице и проверить полученную коллекцию с помощью фасада PdfContentEditor в Aspose.PDF для Java.
---
## Список марок на странице

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Позвоните `getStamps(pageNumber)`, чтобы получить штампы на целевой странице.
3. Осмотрите полученную коллекцию `StampInfo[]`.

```java
public static void listStamps(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        StampInfo[] stamps = editor.getStamps(1);
        System.out.println("Stamps on page 1: " + stamps.length);
    } finally {
        editor.close();
    }
}
```
