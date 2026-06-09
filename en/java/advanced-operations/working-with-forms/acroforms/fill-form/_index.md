---
title: Fill AcroForm - Fill PDF Form using Java
linktitle: Fill AcroForm
type: docs
weight: 20
url: /java/fill-form/
description: Fill AcroForm fields in a PDF document using Aspose.PDF for Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Fill AcroForm fields in PDF files with Java
Abstract: This article explains how to fill AcroForm fields using Aspose.PDF for Java. The example loads a PDF through the Form facade, matches field names against a value map, updates the matching fields, and saves the completed document.
---
The `Form` facade can be used to automate field population in an existing AcroForm.

## Fill AcroForm fields with new values

1. Open the PDF form document with the [Form](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/form/) facade.
1. Iterate through the form fields and update the matching entries with the provided values.
1. Save the updated PDF document.

```java
public static void fillForm(Path inputFile, Path outputFile) {
    Map<String, String> newFieldValues = Map.of(
            "First Name", "Alexander_New",
            "Last Name", "Greenfield_New",
            "City", "Yellowtown_New",
            "Country", "Redland_New");

    Form form = new Form(inputFile.toString());
    try {
        for (String fieldName : form.getFieldNames()) {
            if (newFieldValues.containsKey(fieldName)) {
                form.fillField(fieldName, newFieldValues.get(fieldName));
            }
        }
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
