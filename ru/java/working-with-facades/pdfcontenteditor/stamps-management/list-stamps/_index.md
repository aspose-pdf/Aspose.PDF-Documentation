---
title: Список штампов
linktitle: Список штампов
type: docs
weight: 20
url: /ru/java/list-stamps/
description: Узнайте, как перечислить резиновые штампы на странице в Java, используя фасад `PdfContentEditor` в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Список резиновых штампов PDF в Java
Abstract: В этой статье показывается, как привязать PDF, извлечь штампы на странице и проверить полученную коллекцию, используя фасад `PdfContentEditor` в Aspose.PDF for Java.
---
## Перечислить штампы на странице

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Вызовите `getStamps(pageNumber)` получить штампы на целевой странице.
3. Проверьте результат `StampInfo[]` коллекция.

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


