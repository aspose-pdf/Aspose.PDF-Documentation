---
title: Set Field Comb Number
linktitle: Set Field Comb Number
type: docs
weight: 60
url: /java/set-field-comb-number/
description: Learn how to set a comb number for a PDF form field in Java using the FormEditor facade in Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Set a comb number for a PDF form field in Java
Abstract: This article shows how to bind an existing PDF, set a comb number for a field, and save the updated document using the FormEditor facade in Aspose.PDF for Java.
---
## Set a field comb number

1. Vincule el PDF de origen a la fachada `FormEditor`.
2. Llame a `setFieldCombNumber(...)` para obtener el campo objetivo y el valor del peine.
3. Guarde el documento actualizado.

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
