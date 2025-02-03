---
title: Fill AcroForms
linktitle: Fill AcroForms
type: docs
weight: 20
url: /java/fill-form/
description: This section explains how to fill form field in a PDF document with Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on managing Fill AcroForms in PDF documents using Aspose.PDF for Java
Abstract: The Fill Form section of the Aspose.PDF for Java documentation provides a step-by-step guide on how to programmatically populate form fields within PDF documents. It explains how to identify and fill various types of form fields, including text fields, checkboxes, radio buttons, and dropdowns. The documentation also covers techniques for updating existing form data and flattening forms to prevent further modifications. With practical Java code examples and detailed explanations, developers can easily automate form-filling processes, enhancing efficiency in document management and data entry workflows.
SoftwareApplication: java    
---

PDF documents are wonderful, and really the preferred file type, for creating Forms.

Aspose.PDF for Java allows you to fill a form field, get the field from the Document object's Form collection.

Let's look at the following example how to resolve this task:

```java
public class ExamplesFillForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillFormFieldPDFDocument() {
        // Open document
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // Create a field
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // Add field to the document
        pdfDocument.getForm().add(textBoxField, 1);

        // Save modified PDF
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }

    
}
```
