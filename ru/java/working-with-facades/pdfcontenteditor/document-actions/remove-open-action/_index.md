---
title: Удалить действие открытия
linktitle: Удалить действие открытия
type: docs
weight: 20
url: /ru/java/remove-open-action/
description: Узнайте, как удалить действие открытия документа из PDF в Java, используя фасад PdfContentEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Удалить действие открытия PDF-документа в Java
Abstract: В этой статье показано, как привязать PDF, удалить действие открытия документа и сохранить обновлённый документ, используя фасад PdfContentEditor в Aspose.PDF for Java.
---
## Удалите действие открытия документа

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Вызов `removeDocumentOpenAction()`.
3. Сохраните обновлённый PDF документ.

```java
public static void removeOpenAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeDocumentOpenAction();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

