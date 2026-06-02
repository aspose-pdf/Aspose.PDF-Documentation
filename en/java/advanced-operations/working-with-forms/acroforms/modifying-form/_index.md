---
title: Modifying AcroForm
linktitle: Modifying AcroForm
type: docs
weight: 45
url: /java/modifying-form/
description: Modify AcroForm fields in PDF documents using Aspose.PDF for Java, including clearing text, setting limits, styling fields, and removing fields.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modify and customize PDF form fields with Java
Abstract: This article explains how to modify AcroForm content using Aspose.PDF for Java. It covers clearing text from Typewriter form resources, setting and reading text field length limits, changing form field font appearance, and deleting specific fields by name.
---
Form maintenance often involves both field-level edits and cleanup of form-related page resources.

## Clear text from a Typewriter form

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to clear text from a Typewriter form.
3. Save the document or inspect the result, depending on the scenario.

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

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to change form field font appearance.
3. Save the document or inspect the result, depending on the scenario.

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

## Delete a form field

`deleteFormField` removes a field by name with `document.getForm().delete("First Name")`.
