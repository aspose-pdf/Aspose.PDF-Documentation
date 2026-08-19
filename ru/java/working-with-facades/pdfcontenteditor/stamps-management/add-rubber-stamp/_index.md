---
title: Добавить резиновую печать
linktitle: Добавить резиновую печать
type: docs
weight: 10
url: /ru/java/add-rubber-stamp/
description: Узнайте, как добавить аннотацию резиновой печати в PDF‑документ на Java, используя фасад PdfContentEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Добавить резиновую печать в PDF на Java
Abstract: В этой статье показано, как привязать PDF, создать аннотацию резиновой печати с текстом метки и цветом, и сохранить обновлённый документ, используя фасад PdfContentEditor в Aspose.PDF for Java.
---
## Добавьте резиновую печать

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Вызов `createRubberStamp(...)` с номером страницы, прямоугольником, заголовком, содержимым и цветом.
3. Сохраните обновлённый PDF‑документ.

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

