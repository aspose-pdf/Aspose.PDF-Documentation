---
title: Delete List Item
type: docs
weight: 20
url: /java/del-list-item/
description: Learn how to remove an item from a list field in a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Delete a list item from a PDF form field in Java
Abstract: This article shows how to bind an existing PDF, remove a specific item from a list field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Delete an item from a list field

1. Bind the source PDF to the `FormEditor` facade.
2. Call `delListItem(...)` for the target field and item to remove.
3. Save the updated document.

```java
public static void deleteListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.delListItem("Country", "UK");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
