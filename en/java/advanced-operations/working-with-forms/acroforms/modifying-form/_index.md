---
title: Modifying AcroForm
linktitle: Modifying AcroForm
type: docs
weight: 45
url: /java/modifying-form/
description: Modify AcroForm fields in PDF documents using Aspose.PDF for Java, including clearing text, setting limits, styling fields, and removing fields.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modify and customize PDF form fields with Java
Abstract: This article explains how to modify AcroForm content using Aspose.PDF for Java. It covers clearing text from Typewriter form resources, setting and reading text field length limits, changing form field font appearance, and deleting specific fields by name.
---
Form maintenance often involves both field-level edits and cleanup of form-related page resources.

## Clear text from a Typewriter form

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Iterate through the [XForm](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/xform/) resources and create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragmentabsorber/) for the Typewriter form resources.
1. Iterate through the found [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) items and clear their text values.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void clearTextInForm(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (XForm form : document.getPages().get_Item(1).getResources().getForms()) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                absorber.visit(form);

                for (TextFragment fragment : absorber.getTextFragments()) {
                    fragment.setText("");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Set or get a text field limit

`setFieldLimit` uses `FormEditor.setFieldLimit("First Name", 15)`, while `getFieldLimit` reads `TextBoxField.getMaxLen()` from the first form field.

## Change form field font appearance

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Get the target [Field](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/field/) and set its [DefaultAppearance](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/defaultappearance/).
1. Set the properties required by the example.
1. Save the updated PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

```java
public static void setFormFieldFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            textBoxField.setDefaultAppearance(new DefaultAppearance(
                    FontRepository.findFont("Calibri"), 10, com.aspose.pdf.Color.getBlack().toRgb()));
        }

        document.save(outputFile.toString());
    }
}
```
