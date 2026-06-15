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

## Clear text in embedded form resources

Use this example when Typewriter form content should be emptied without removing the form objects themselves.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Iterate through page form resources and locate Typewriter forms.
1. Clear the absorbed text fragments and save the document.

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

## Set a text field length limit

Use this example when a text field should accept only a limited number of characters.

1. Create a [FormEditor](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/formeditor/) facade and bind the source PDF.
1. Set the maximum length for the target field.
1. Save the updated document.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor form = new FormEditor();
    form.bindPdf(inputFile.toString());
    try {
        form.setFieldLimit("First Name", 15);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## Get a text field length limit

Use this example when you need to inspect the current maximum length of a text field.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Access the target field from the form collection.
1. Read the limit from the [TextBoxField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textboxfield/) and output it.

```java
public static void getFieldLimit(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            System.out.println("Limit: " + textBoxField.getMaxLen());
        }
    }
}
```

## Change a form field font

Use this example when an existing text field should use a different font or appearance.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Access the target [TextBoxField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textboxfield/) and set a new default appearance.
1. Save the updated PDF.

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

## Delete a form field by name

Use this example when a specific field should be removed from the AcroForm.

1. Open the source PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).
1. Delete the target field from the form by its name.
1. Save the updated document.

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
