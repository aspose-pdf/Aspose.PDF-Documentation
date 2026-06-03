---
title: Extract AcroForm - Extract Form Data from PDF in Java
linktitle: Extract AcroForm
type: docs
weight: 30
url: /java/extract-form/
description: Extract values from AcroForm fields in PDF documents using Aspose.PDF for Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract form field values from PDF files with Java
Abstract: This article shows how to extract data from AcroForm fields using Aspose.PDF for Java. The example iterates through field names with the Form facade, reads each current value, and stores the result in a map for downstream processing.
---
Use the `Form` facade when you need a simple field-name to field-value extraction flow.

## Extract values from all AcroForm fields

1. Open the PDF form document with the `Form` facade.
2. Iterate through the field names and read each current field value into a map.
3. Review or export the collected values for downstream processing.

```java
public static Map<String, String> getValuesFromAllFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        Map<String, String> formValues = new LinkedHashMap<>();
        for (String fieldName : form.getFieldNames()) {
            formValues.put(fieldName, form.getField(fieldName));
        }

        System.out.println(formValues);
        return formValues;
    } finally {
        form.close();
    }
}
```

