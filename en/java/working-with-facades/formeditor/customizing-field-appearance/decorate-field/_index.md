---
title: Decorate Field
type: docs
weight: 10
url: /java/decorate-field/
description: Learn how to decorate a PDF form field with colors and alignment in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Decorate a PDF form field in Java
Abstract: This article shows how to bind an existing PDF, configure a FormFieldFacade with colors and alignment, decorate a field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Decorate a field

1. Bind the source PDF to the `FormEditor` facade.
2. Configure a `FormFieldFacade` with the required colors and alignment.
3. Pass the facade to the editor and call `decorateField(...)`.
4. Save the updated document.

```java
public static void decorateField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        FormFieldFacade facade = new FormFieldFacade();
        facade.setBackgroundColor(Color.RED);
        facade.setTextColor(Color.BLUE);
        facade.setBorderColor(Color.GREEN);
        facade.setAlignment(FormFieldFacade.ALIGN_CENTER);
        editor.setFacade(facade);
        editor.decorateField("First Name");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
