---
title: Add Tooltips to PDF Text in Java
linktitle: PDF Tooltip
type: docs
weight: 20
url: /java/pdf-tooltip/
description: Learn how to add tooltips to text fragments in PDF documents in Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add interactive tooltips to PDF text fragments using Java
Abstract: This article shows how to add interactive help to PDF text using Aspose.PDF for Java. It covers attaching tooltip text to invisible button fields placed over matched text fragments and creating a hidden text field that appears when the pointer enters a trigger area.
---
Aspose.PDF for Java lets you add interactive help by placing form fields over text fragments.

## Add tooltips to matched text

Use this example when existing text in the PDF should show a tooltip on hover.

1. Create the sample PDF and reopen it for editing.
1. Search the target text fragments with `TextFragmentAbsorber`.
1. Place `ButtonField` overlays on the matched text and assign tooltip text.
1. Save the updated document.

```java
public static void addToolTipToSearchedText(Path outputFile) {
        Document document = new Document();
        document.getPages().add().getParagraphs()
                .add(new TextFragment("Move the mouse cursor here to display a tooltip"));
        document.getPages().get_Item(1).getParagraphs()
                .add(new TextFragment("Move the mouse cursor here to display a very long tooltip"));
        document.save(outputFile.toString());
        document.close();

        document = new Document(outputFile.toString());
        TextFragmentAbsorber absorber = new TextFragmentAbsorber(
                "Move the mouse cursor here to display a tooltip");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            field.setAlternateName("Tooltip for text.");
            document.getForm().add(field);
        }

        absorber = new TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
        document.getPages().accept(absorber);

        for (TextFragment fragment : absorber.getTextFragments()) {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            field.setAlternateName("Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                    + " sed do eiusmod tempor incididunt ut labore et dolore magna"
                    + " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                    + " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                    + " Duis aute irure dolor in reprehenderit in voluptate velit"
                    + " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                    + " occaecat cupidatat non proident, sunt in culpa qui officia"
                    + " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        document.save(outputFile.toString());
        document.close();
    }
```

## Show a floating text block on hover

Use this example when hovering over a text area should reveal a hidden text field.

1. Create the sample PDF and reopen it for editing.
1. Find the trigger text fragment with `TextFragmentAbsorber`.
1. Create a hidden `TextBoxField` and a `ButtonField` with enter and exit actions.
1. Save the final PDF.

```java
public static void createHiddenTextBlock(Path outputFile) {
    Document document = new Document();
    document.getPages().add().getParagraphs()
            .add(new TextFragment("Move the mouse cursor here to display floating text"));
    document.save(outputFile.toString());
    document.close();

    document = new Document(outputFile.toString());
    TextFragmentAbsorber absorber = new TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text");
    document.getPages().accept(absorber);
    TextFragment fragment = absorber.getTextFragments().get_Item(1);

    TextBoxField floatingField = new TextBoxField(
            fragment.getPage(), new Rectangle(100.0, 700.0, 220.0, 740.0, false));
    floatingField.setValue("This is the \"floating text field\".");
    floatingField.setReadOnly(true);
    floatingField.setFlags(floatingField.getFlags() | AnnotationFlags.Hidden);
    floatingField.setPartialName("FloatingField_1");
    floatingField.setDefaultAppearance(new DefaultAppearance("Helv", 10, java.awt.Color.BLUE));
    floatingField.getCharacteristics().setBackground(java.awt.Color.CYAN);
    floatingField.getCharacteristics().setBorder(java.awt.Color.BLUE);
    floatingField.setBorder(new Border(floatingField));
    floatingField.getBorder().setWidth(1);
    floatingField.setMultiline(true);

    document.getForm().add(floatingField);

    ButtonField buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
    buttonField.getAnnotationActions().setOnEnter(new HideAction(floatingField, false));
    buttonField.getAnnotationActions().setOnExit(new HideAction(floatingField));

    document.getForm().add(buttonField);
    document.save(outputFile.toString());
    document.close();
}
```
