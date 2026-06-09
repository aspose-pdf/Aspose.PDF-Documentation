---
title: Set Field Script
type: docs
weight: 20
url: /java/set-field-script/
description: Learn how to assign or update a JavaScript action on a PDF form field in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Set a JavaScript action on a PDF form field in Java
Abstract: This article shows how to bind an existing PDF, add an initial script, replace it with an updated script, and save the modified document using the FormEditor facade in Aspose.PDF for Java.
---
## Set a field script

1. Bind the source PDF to the `FormEditor` facade.
2. Add an initial JavaScript action to the field.
3. Replace it with the updated script text.
4. Save the updated document.

```java
public static void setFieldScript(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addFieldScript("Script_Demo_Button", "app.alert('Script 1 has been executed');");
        editor.setFieldScript("Script_Demo_Button", "app.alert('Script 2 has been executed');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
