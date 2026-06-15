---
title: Import and Export Form Data
linktitle: Import and Export Form Data
type: docs
weight: 80
url: /java/import-export-form-data/
description: Import and export AcroForm field data in XML, FDF, XFDF, and JSON formats using Aspose.PDF for Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Import and export PDF form data with Java
Abstract: This article explains how to exchange AcroForm data with external formats using Aspose.PDF for Java. It covers importing and exporting XML, FDF, and XFDF data through the Form facade and extracting form field values to JSON.
---
Aspose.PDF for Java supports several common data-exchange formats for interactive forms.

## Import form data from XML

Use this example when form values are stored in an XML file and should be applied to a PDF form.

1. Create a [Form](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/form/) facade and bind the source PDF.
1. Open the XML input stream and import the data into the form.
1. Save the updated PDF document.

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

## Export form data to XML

Use this example when you need to store current AcroForm values in XML format.

1. Create a [Form](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/form/) facade and bind the source PDF.
1. Open the output stream for the XML file.
1. Export the form data to XML.

```java
public static void exportDataToXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(stream);
    } finally {
        form.close();
    }
}
```

## Import form data from FDF

Use this example when form values arrive in the FDF interchange format.

1. Create a [Form](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/form/) facade and bind the source PDF.
1. Open the FDF input stream and import the data.
1. Save the filled PDF document.

```java
public static void importDataFromFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Export form data to FDF

Use this example when PDF form values should be shared as an FDF file.

1. Create a [Form](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/form/) facade and bind the source PDF.
1. Open the output stream for the FDF file.
1. Export the form data in FDF format.

```java
public static void exportDataToFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(stream);
    } finally {
        form.close();
    }
}
```

## Import form data from XFDF

Use this example when form data is provided in XFDF format and must be merged into a PDF.

1. Create a [Form](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/form/) facade and bind the source PDF.
1. Open the XFDF input stream and import the values.
1. Save the updated PDF document.

```java
public static void importDataFromXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream stream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(stream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Export form data to XFDF

Use this example when you need an XML-based interchange file for AcroForm values.

1. Create a [Form](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/form/) facade and bind the source PDF.
1. Open the output stream for the XFDF file.
1. Export the current form values to XFDF.

```java
public static void exportDataToXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(stream);
    } finally {
        form.close();
    }
}
```

## Extract form fields to JSON

Use this example when form values should be exported to a lightweight JSON representation.

1. Open the PDF with the [Form](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/form/) facade.
1. Iterate through field names and serialize their values into JSON text.
1. Write the JSON content to the target file.

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

## Reuse the JSON extraction helper

Use this example when you want a dedicated wrapper method that delegates to the main JSON export routine.

1. Call the existing JSON extraction helper with the source PDF and output path.
1. Reuse the same extraction logic without duplicating serialization code.

```java
public static void extractFormFieldsToJsonDoc(Path inputFile, Path outputFile) throws Exception {
    extractFormFieldsToJson(inputFile, outputFile);
}
```
