---
title: Replace Text With State
type: docs
weight: 20
url: /java/replace-text-with-state/
description: Learn how to replace text with custom formatting in Java using the PdfContentEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Replace PDF text with custom formatting in Java
Abstract: This article shows how to bind a PDF, configure a custom TextState, replace all matching text occurrences, and save the updated document using the PdfContentEditor facade in Aspose.PDF for Java.
---
## Replace text with a custom text state

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Create and configure a `TextState` with the required color and font size.
3. Set the replace-text scope to `ReplaceAll`.
4. Call `replaceText(...)` with the search text, replacement text, and configured `TextState`.
5. Save the updated PDF document.

```java
public static void replaceTextWithState(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        TextState textState = new TextState();
        textState.setForegroundColor(com.aspose.pdf.Color.getBlue());
        textState.setFontSize(14);
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("software", "SOFTWARE", textState);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
