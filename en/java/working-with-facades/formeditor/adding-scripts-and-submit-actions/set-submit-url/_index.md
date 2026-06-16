---
title: Set Submit URL
linktitle: Set Submit URL
type: docs
weight: 30
url: /java/set-submit-url/
description: Learn how to set a submit URL for a PDF form button in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Configure a PDF form submit URL in Java
Abstract: This article shows how to bind an existing PDF, set a submit URL and submit flag for a button field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Set a submit URL

1. Bind the source PDF to the `FormEditor` facade.
2. Call `setSubmitUrl(...)` for the button field.
3. Apply the submit flag for the submission format.
4. Save the updated document.

```java
public static void setSubmitUrl(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
        editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
