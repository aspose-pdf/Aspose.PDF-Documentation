---
title: Create AcroForm - Create Fillable PDF in Java
linktitle: Create AcroForm
type: docs
weight: 10
url: /java/create-form/
description: Create AcroForm fields from scratch in PDF documents using Aspose.PDF for Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create interactive AcroForm fields in PDF files with Java
Abstract: This article explains how to create AcroForm fields using Aspose.PDF for Java. It covers text boxes, multi-widget text fields, radio buttons, combo boxes, checkboxes, list boxes, signature fields, and barcode fields for interactive PDF forms.
---
Aspose.PDF for Java lets you create a wide range of AcroForm field types from scratch.

## Add a text box field

1. Open or create the PDF document used in this example.
2. Configure the Aspose.PDF objects needed to add a text box field.
3. Save the result to apply the change.

```java
public static void addTextBoxField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rectangle = new Rectangle(10, 600, 110, 620, true);
        TextBoxField textBoxField = new TextBoxField(page, rectangle);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");
        textBoxField.setDefaultAppearance(new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()));

        document.getForm().add(textBoxField, 1);
        document.save(outputFile.toString());
    }
}
```

