---
title: Replace Text Simple
type: docs
weight: 10
url: /java/replace-text-simple/
description: Learn how to replace text throughout a PDF document in Java using the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Replace text in a PDF in Java
Abstract: This article shows how to bind a PDF, configure the replace-text scope, replace all matching text occurrences, and save the updated document using the PdfContentEditor facade in Aspose.PDF for Java.
---
## Replace text throughout the document

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Set the replace-text scope to `ReplaceAll`.
3. Call `replaceText(...)` with the search text and replacement text.
4. Save the updated PDF document.

```java
public static void replaceTextSimple(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("33", "XXXIII ");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
