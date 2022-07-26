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
---

PDF documents are wonderful, and really the preferred file type, for creating Forms.

Aspose.PDF for Java allows you to fill a form field, get the field from the Document object’s Form collection.

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
