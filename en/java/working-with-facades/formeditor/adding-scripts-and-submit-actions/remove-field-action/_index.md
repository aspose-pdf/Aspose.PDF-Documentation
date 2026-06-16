---
title: Remove Field Action
linktitle: Remove Field Action
type: docs
weight: 50
url: /java/remove-field-action/
description: Learn how to remove a field action from a PDF form field in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Remove a PDF form field action in Java
Abstract: This article shows how to bind an existing PDF, remove the action associated with a specific field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Remove a field action

1. Bind the source PDF to the `FormEditor` facade.
2. Call `removeFieldAction(...)` for the target field.
3. Save the updated document.

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
