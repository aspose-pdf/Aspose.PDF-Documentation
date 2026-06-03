---
title: Create Submit Button
type: docs
weight: 60
url: /java/create-submit-button/
description: Learn how to add a submit button to a PDF document in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-03"
TechArticle: true
AlternativeHeadline: Create a PDF submit button in Java
Abstract: This article shows how to bind an existing PDF, add a submit button field with a target URL, and save the modified document using the FormEditor facade in Aspose.PDF for Java.
---
Use `FormEditorExamples.createSubmitButton(...)` to create a button that submits form data.

## Create a submit button

1. Bind the source PDF to the `FormEditor` facade.
2. Call `addSubmitBtn(...)` with the button name, page, label, target URL, and rectangle.
3. Save the updated document.

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
