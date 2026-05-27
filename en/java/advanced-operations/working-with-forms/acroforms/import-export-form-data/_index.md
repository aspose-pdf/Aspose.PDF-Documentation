---
title: Import and Export Form Data
linktitle: Import and Export Form Data
type: docs
weight: 80
url: /java/import-export-form-data/
description: Import and export AcroForm field data in XML, FDF, XFDF, and JSON formats using Aspose.PDF for Java.
lastmod: "2026-05-27"
TechArticle: true
AlternativeHeadline: Import and export PDF form data with Java
Abstract: This article explains how to exchange AcroForm data with external formats using Aspose.PDF for Java. It covers importing and exporting XML, FDF, and XFDF data through the Form facade and extracting form field values to JSON.
---
Aspose.PDF for Java supports several common data-exchange formats for interactive forms.

## Import or export XML data

```java
public static void importDataFromXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

`exportDataToXml` performs the reverse operation by binding the PDF and calling `form.exportXml(stream)`.

## Import or export FDF and XFDF data

The same example class also includes:

- `importDataFromFdf` and `exportDataToFdf`
- `importDataFromXfdf` and `exportDataToXfdf`

## Extract form fields to JSON

```java
public static void extractFormFieldsToJson(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder json = new StringBuilder();
        json.append("{\n");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            String fieldName = fieldNames[i];
            json.append("    \"").append(escapeJson(fieldName)).append("\": \"")
                    .append(escapeJson(form.getField(fieldName))).append("\"");
            if (i < fieldNames.length - 1) {
                json.append(",");
            }
            json.append("\n");
        }
        json.append("}\n");
        Files.writeString(outputFile, json.toString());
    } finally {
        form.close();
    }
}
```
