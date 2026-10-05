---
title: Получение параметров просмотра
linktitle: Получение параметров просмотра
type: docs
weight: 10
url: /ru/java/get-viewer-preferences/
description: Узнайте, как читать параметры просмотра PDF‑документа на Java, используя фасад PdfContentEditor в Aspose.PDF.
lastmod: "2026-09-17"
TechArticle: true
AlternativeHeadline: Читать параметры просмотра PDF на Java
Abstract: В этой статье показано, как привязать PDF и вывести текущее значение параметра просмотра, используя фасад PdfContentEditor в Aspose.PDF for Java.
---
## Получение текущего параметра просмотра

1. Привяжите исходный PDF к фасаду `PdfContentEditor`.
2. Вызовите `getViewerPreference()`, чтобы прочитать текущее значение.
3. Проверьте или выведите возвращённый флаг предпочтения.

```java
public static void getViewerPreferences(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        System.out.println("Current viewer preference: " + editor.getViewerPreference());
    } finally {
        editor.close();
    }
}
```


