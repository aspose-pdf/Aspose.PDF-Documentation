---
title: Modifying AcroForms
linktitle: Modifying AcroForms
type: docs
weight: 40
url: /java/modifing-form/
description: This section explains how to modifying forms in your PDF document with Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Set Custom Form Field Font

Form fields in Adobe PDF files can be configured to use specific default fonts. Aspose.PDF allows developers to apply any font as a field default font, whether one of the 14 core fonts or a custom font.
To set and update the default font used for form fields, Aspose.PDF has the DefaultAppearance (Font font, double size, Color color) class. This class can be accessed using com.aspose.pdf.DefaultAppearance. To use this object, use the Field class’ setDefaultAppearance(..) method.

The following code snippet shows you how to set the default font for PDF form field.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.DefaultAppearance;
import com.aspose.pdf.Document;
import com.aspose.pdf.Field;
import com.aspose.pdf.Font;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.TextBoxField;

public class ExamplesModifying {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void SetFormFieldFontOtherThan14CorePDFFonts() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "FormFieldFont14.pdf");
        // Get particular form field from document
        Field field = (Field) pdfDocument.getForm().get("textbox1");

        // Create font object
        Font font = FontRepository.findFont("ComicSansMS");

        // Set the font information for form field
        field.setDefaultAppearance (new DefaultAppearance(font, 10, java.awt.Color.BLACK));
        
        // Save updated document
        pdfDocument.save(_dataDir + "FormFieldFont14_out.pdf");
    }
```

## Get/Set FieldLimit

The FormEditor class SetFieldLimit method allows you to set a field limit, the maximum number of characters that can be entered into a field.

```java
    public static void GettingMaximumFieldLimit()
    {
        // Getting maximum field limit using DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        System.out.println("Limit: " +field.getMaxLen());
    }
```

You can also get the same value using the Aspose.PDF.Facades namespace using the following code snippet.

```java
    public static void GettingMaximumFieldLimitFacades()
    {
        // Getting maximum field limit using Facades
        com.aspose.pdf.facades.Form form = new com.aspose.pdf.facades.Form();
        form.bindPdf(_dataDir + "FieldLimit.pdf");
        System.out.println("Limit: " + form.getFieldLimit("textbox1"));
    }
```

Similarly, Aspose.PDF has a method that gets the field limit using the DOM approach. The following code snippet shows the steps.

```java
    public static void SettingMaximumFieldLimit()
    {
        // Getting maximum field limit using DOM
        Document doc = new Document(_dataDir + "FieldLimit.pdf");
        TextBoxField field = (TextBoxField)doc.getForm().get("textbox1");
        field.setMaxLen(10);
        System.out.println("Limit: " +field.getMaxLen());       
    }
```

## Delete a Particular Form Field from a PDF Document

All the form fields are contained in the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object’s Form collection. This collection provides different methods that manage form fields, including the delete method. If you want to delete a particular field, pass the field name as a parameter to the delete method and then save the updated PDF document.

The following code snippet shows how to delete a named field from a PDF document.

```java
    public static void DeleteParticularFormField()
    {    
        // Open a document
        Document pdfDocument = new Document("input.pdf");

        // Delete a named field by name
        pdfDocument.getForm().delete("textbox1");

        // Save the modified PDF
        pdfDocument.save("output.pdf");
    }
```

## Modify Form Field in a PDF Document

The [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object’s Form collection allows you to manage form fields in a PDF document.

To modify a form field, get the field from the Form collection and set its properties. Then save the updated PDF document.

The following code snippet shows how to modify an existing form field in a PDF document.

```java
    public static void ModifyFormField()
    {
        Document pdfDocument = new Document("input.pdf");
        // Get a field
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Modify the field value
        textBoxField.setValue("Updated Value");

        // Set the field as read only
        textBoxField.setReadOnly(true);

        // Save the updated document
        pdfDocument.save("output.pdf");
    }
```

### Move Form Field to a New Location in a PDF File

If you want to move a form field to a new location on a PDF page, first get the field object and then specify a new value for its setRect method. A [Rectangle](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) object with new coordinates is assigned to the setRect(..) method. Then save the updated PDF using the [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Document) object’s save method.

The following code snippet shows you how to move a form field to a new location.

```java
    public static void ModifyMoveFormFieldNewLocation()
    {    
        // Open a document
        Document pdfDocument = new Document(_dataDir+"input.pdf");
        // Get a field
        TextBoxField textBoxField = (TextBoxField) pdfDocument.getForm().get("textbox1");

        // Modify the field location
        textBoxField.setRect(new Rectangle(300, 400, 600, 500));

        // Save the modified document
        pdfDocument.save("output.pdf");
    }
}
```
