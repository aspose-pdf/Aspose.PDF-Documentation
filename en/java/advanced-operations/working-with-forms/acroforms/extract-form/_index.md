---
title: Extract Data AcroForms
linktitle: Extract Data AcroForms
type: docs
weight: 30
url: /java/extract-form/
description: This section explains how to extract forms from your PDF document with Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: 
Abstract: The article provides a detailed guide on extracting values from form fields within PDF documents using Aspose.PDF for Java. It covers three key tasks: retrieving the value of an individual form field, extracting values from all fields, and obtaining form fields from a specific region of a PDF file. The first section explains how to use the `getValue()` method of a `TextBoxField` to fetch the value of a specific field by accessing the form field from the `Document` object's Form collection. The second section describes how to traverse all form fields in a PDF document and retrieve their values using the `getFields()` method. Lastly, the article illustrates how to filter and retrieve fields from a designated rectangular area within a PDF document by using the `getFieldsInRect()` method. Code snippets are included to demonstrate the implementation of each task, highlighting the flexibility and utility of Aspose.PDF for Java in form data extraction and manipulation.
---

## Get Value from an Individual Field of PDF Document

The form field's [getValue() method](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) allows you to get the value of a particular field.

To get the value, get the form field from the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's Form collection.

This example selects a [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) and retrieves its value using the [getValue() method](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.TextBoxField;

public class ExamplesExtractFormData {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void GetValueFromIndividualFieldPDFDocument() {
        // Open a document
        Document pdfDocument = new Document(_dataDir+"GetValueFromField.pdf");

        // Get a field
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Get the field name
        System.out.printf("PartialName :-" + textBoxField.getPartialName());

        // Get the field value
        System.out.printf("Value :-" + textBoxField.getValue());
    }
```

## Get Values from All Fields in a PDF Document

To get values from all the fields in a PDF document, you need to navigate through all the form fields and then get the value using the [getValue() method](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--). Get each field from the Form collection using the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) object's [getForm() method](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) and get the list of form fields into an Field array using getFields() and traverse through array to get value of fields.

The following code snippet shows how to get the values of all the fields in a PDF document.

```java
    public static void GetValuesFromAllFieldsPDFDocument() {
        // Open document
        Document document = new Document(_dataDir + "GetValuesFromAllFields.pdf");

        Field[] fields = document.getForm().getFields();
        for (int i = 0; i < fields.length; i++) {

            System.out.println("Form field: " + fields[i].getFullName());
            System.out.println("Form field: " + fields[i].getValue());
        }

    }
}
```

## Get Form Fields from a Specific Region of PDF File

In some cases, it is required to obtain data not from the entire form, but, for example, only from the upper left quarter of the printed sheet.
With Aspose.PDF for Java, this is not a problem. You can specify a region to filter out fields that are outside the given region of the PDF file. To get form fields from a specific area of a PDF file:

1. Open the PDF file using the Document object.
1. Get the form from the document's Forms collection.
1. Specify the rectangular region and pass it to the Form object's [getFieldsInRect](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form#getFieldsInRect-com.aspose.pdf.Rectangle-) method. A [Fields](https://reference.aspose.com/pdf/java/com.aspose.pdf/Field) collection is returned.
1. Use this to manipulate the fields.

The following code snippet shows how to get form fields in a specific rectangular region of a PDF file.

```java
public static void GetValuesFromSpecificRegion() {
    // Open pdf file
    Document doc = new Document(_dataDir + "GetFieldsFromRegion.pdf");

    // Create rectangle object to get fields in that area
    Rectangle rectangle = new Rectangle(35, 30, 500, 500);

    // Get the PDF form
    com.aspose.pdf.Form form = doc.getForm();

    // Get fields in the rectangular area
    Field[] fields = form.getFieldsInRect(rectangle);

    // Display Field names and values
    for (Field field : fields)
    {
        // Display image placement properties for all placements
        System.out.println("Field Name: " + field.getFullName() + "-" + "Field Value: " + field.getValue());
    }
}
```
