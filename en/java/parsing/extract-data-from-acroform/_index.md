---
title: Extract Data from AcroForm using Java
linktitle: Extract Data from AcroForm
type: docs
weight: 50
url: /java/extract-data-from-acroform/
description: Aspose.PDF makes it easy to extract form field data from PDF files. Learn how to extract data from AcroForms and save it into JSON, XML, or FDF format.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Data from AcroForm via Java
Abstract: This article explains how to extract and export AcroForm data from PDF files with Aspose.PDF for Java. It covers reading all form fields, retrieving a field value by name, exporting field data to JSON, and writing form data to XML, FDF, and XFDF formats.
---

## Extract form fields from PDF document

Use `com.aspose.pdf.facades.Form` to read field names and values without working through the full document object model.

1. Open the source PDF form with the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade so AcroForm fields can be read without traversing the full document object model.
1. Call `getFieldNames()` to collect all field identifiers present in the form.
1. Iterate through those field names and call `getField(fieldName)` to read each field value.
1. Build the output string from the extracted key-value pairs and print the aggregated form data.
1. Close the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade in the `finally` block.

```java
public static void extractFormFields(Path inputFile) {
    Form form = new Form(inputFile.toString());
    try {
        StringBuilder formValues = new StringBuilder("{");
        String[] fieldNames = form.getFieldNames();
        for (int i = 0; i < fieldNames.length; i++) {
            if (i > 0) {
                formValues.append(", ");
            }
            formValues.append(fieldNames[i]).append("=").append(form.getField(fieldNames[i]));
        }
        formValues.append("}");
        System.out.println(formValues);
    } finally {
        form.close();
    }
}
```

## Retrieve form field value by title

When you know the exact field name defined in the PDF form, you can retrieve its value directly with `getField(fieldName)`
without iterating through the entire field collection.

1. Open the source PDF form with the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade.
1. Call `getField(fieldName)` with the requested field name to read its current value from the AcroForm data.
1. Print the extracted field value.
1. Close the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade in the `finally` block.

```java
public static void extractFormFieldByTitle(Path inputFile, String fieldName) {
    Form form = new Form(inputFile.toString());
    try {
        String formValue = form.getField(fieldName);
        System.out.println(formValue);
    } finally {
        form.close();
    }
}
```

## Extract form fields from PDF document to JSON

Form field values can also be extracted and stored as JSON. This is useful when PDF form data needs to be consumed by
web applications, APIs, or other systems that work with JSON.

1. Open the source PDF form with the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade.
1. Call `getFieldNames()` to collect all available field identifiers from the AcroForm.
1. Iterate through those fields, escape the names and values, and build a JSON object string.
1. Write the JSON result to the output file.
1. Close the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade in the `finally` block.

```java
public static void extractFormFieldsJson(Path inputFile, Path outputFile) throws Exception {
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

## Extract Data to XML from a PDF File

XML export is useful when PDF form data needs to be consumed by systems that work with structured XML data.

1. Create the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade without binding a document yet.
1. Open an output stream for the XML file and bind the source PDF to the facade with `bindPdf(...)`.
1. Call `exportXml(stream)` so the current form field data is serialized as XML.
1. Close the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade after the export completes.

```java
public static void extractDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## Export Data to FDF from a PDF File

FDF (Forms Data Format) is commonly used to exchange AcroForm field data independently of the PDF document.

1. Create the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade without binding a document yet.
1. Open an output stream for the FDF file and bind the source PDF to the facade with `bindPdf(...)`.
1. Call `exportFdf(stream)` so the form field data is serialized in FDF format.
1. Close the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade after the export completes.

```java
public static void extractDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## Export Data to XFDF from a PDF File

XFDF is the XML-based representation of Forms Data Format and is convenient for exchanging form data with systems that work with XML.

1. Create the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade without binding a document yet.
1. Open an output stream for the XFDF file and bind the source PDF to the facade with `bindPdf(...)`.
1. Call `exportXfdf(stream)` so the form field data is serialized in XFDF format.
1. Close the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/form/) facade after the export completes.

```java
public static void extractDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```
