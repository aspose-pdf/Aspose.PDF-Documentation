---
title: Extract Data Form
linktitle: Extract Data Form
type: docs
weight: 30
url: /androidjava/extract-form/
description: This section explains how to extract forms from your PDF document with Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get Value from an Individual Field of PDF Document

The form field’s [getValue() method](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) allows you to get the value of a particular field.

To get the value, get the form field from the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/classes/Document) object’s Form collection.

This example selects a [TextBoxField](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) and retrieves its value using the [getValue() method](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

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

To get values from all the fields in a PDF document, you need to navigate through all the form fields and then get the value using the [getValue() method](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--). Get each field from the Form collection using the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/classes/Document) object’s [getForm() method](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document#getForm--) and get the list of form fields into an Field array using getFields() and traverse through array to get value of fields.

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
