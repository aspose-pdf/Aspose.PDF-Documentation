---
title: Add List Item
linktitle: Add List Item
type: docs
weight: 10
url: /java/add-list-item/
description: Learn how to add items to a list field in a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Add a list item to a PDF form field in Java
Abstract: This article shows how to bind an existing PDF, add a new item to a list field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Add an item to a list field

1. Bind the source PDF to the `FormEditor` facade.
2. Call `addListItem(...)` for the target field and new display/value pair.
3. Save the updated document.

```java
public static void addListItem(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addListItem("Country", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
