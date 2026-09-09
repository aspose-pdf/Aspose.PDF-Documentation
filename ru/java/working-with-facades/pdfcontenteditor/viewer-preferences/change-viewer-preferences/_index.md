---
title: Изменить параметры просмотра
linktitle: Изменить параметры просмотра
type: docs
weight: 20
url: /ru/java/change-viewer-preferences/
description: Узнайте, как изменить параметры просмотра PDF‑документа на Java с использованием фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Изменить параметры просмотра PDF на Java
Abstract: В этой статье показано, как привязать PDF, изменить текущее значение параметра просмотра и сохранить обновлённый документ, используя фасад PdfContentEditor в Aspose.PDF for Java.
---
## Измените параметр просмотра

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Прочитайте текущее значение предпочтения просмотрщика.
3. Объедините его с нужным дополнительным флагом и передайте результат в `changeViewerPreference(...)`.
4. Сохраните обновлённый PDF‑документ.

```java
public static void changeViewerPreferences(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.changeViewerPreference(editor.getViewerPreference() | 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```


