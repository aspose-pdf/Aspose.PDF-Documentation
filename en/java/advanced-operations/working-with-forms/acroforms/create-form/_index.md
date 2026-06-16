---
title: Create AcroForm - Create Fillable PDF in Java
linktitle: Create AcroForm
type: docs
weight: 10
url: /java/create-form/
description: Create AcroForm fields from scratch in PDF documents using Aspose.PDF for Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create interactive AcroForm fields in PDF files with Java
Abstract: This article explains how to create AcroForm fields using Aspose.PDF for Java. It covers text boxes, multi-widget text fields, radio buttons, combo boxes, checkboxes, list boxes, signature fields, and barcode fields for interactive PDF forms.
---
Aspose.PDF for Java lets you create a wide range of AcroForm field types from scratch.

## Create a text box field

Use this example when you need to add a single-line text input field to a new PDF form.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a page.
1. Create a [TextBoxField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textboxfield/) with a target rectangle and configure its appearance.
1. Add the field to the form and save the document.

```java
public static void addTextBoxField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rectangle = new Rectangle(10, 600, 110, 620, true);
        TextBoxField textBoxField = new TextBoxField(page, rectangle);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");
        textBoxField.setDefaultAppearance(new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()));

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField, 1);
        document.save(outputFile.toString());
    }
}
```

## Create a text box field with multiple widgets

Use this example when the same text field value should appear in several positions on the page.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a page.
1. Define multiple rectangles and appearances for the field widgets.
1. Create the [TextBoxField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textboxfield/), configure each widget, and save the document.

```java
public static void addTextBoxFieldNt(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle[] rects = {
                new Rectangle(10, 600, 110, 620, true),
                new Rectangle(10, 630, 110, 650, true),
                new Rectangle(10, 660, 110, 680, true)
        };

        DefaultAppearance[] defaultAppearances = {
                new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()),
                new DefaultAppearance("Helvetica", 12, Color.getDarkGreen().toRgb()),
                new DefaultAppearance(FontRepository.findFont("Calibri"), 14, Color.getDarkMagenta().toRgb())
        };

        TextBoxField textBoxField = new TextBoxField(page, rects);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Some text");

        int index = 0;
        for (WidgetAnnotation widget : textBoxField) {
            widget.setDefaultAppearance(defaultAppearances[index]);
            index++;
        }

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField);
        document.save(outputFile.toString());
    }
}
```

## Create a radio button field

Use this example when the form should let the user choose one option from a predefined set.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a page.
1. Create a [RadioButtonField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/radiobuttonfield/) and add the required options.
1. Add the field to the form and save the PDF.

```java
public static void addRadioButton(Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();

        RadioButtonField radio = new RadioButtonField(document.getPages().get_Item(1));
        radio.addOption("Option 1", new Rectangle(100, 640, 120, 680, true));
        radio.addOption("Option 2", new Rectangle(140, 640, 160, 680, true));

        document.getForm().add(radio);
        document.save(outputFile.toString());
    }
}
```

## Create a combo box field

Use this example when the user should pick one value from a drop-down list.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a page.
1. Create a [ComboBoxField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/comboboxfield/) and add its selectable options.
1. Set the default selection and save the document.

```java
public static void addComboBox(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ComboBoxField combo = new ComboBoxField(page, new Rectangle(100, 640, 150, 656, true));
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        combo.setSelected(3);

        document.getForm().add(combo);
        document.save(outputFile.toString());
    }
}
```

## Create a checkbox field

Use this example when the form needs a true-or-false option such as consent or feature selection.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a page.
1. Create a [CheckboxField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/checkboxfield/) and configure its appearance.
1. Add the checkbox to the form and save the output file.

```java
public static void addCheckboxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 620, 100, 650, true));
        checkbox.getCharacteristics().setBackground(Color.getAqua().toRgb());
        checkbox.setStyle(BoxStyle.Circle);

        document.getForm().add(checkbox);
        document.save(outputFile.toString());
    }
}
```

## Create a list box field

Use this example when the form should display multiple available choices in a visible list.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a page.
1. Create a [ListBoxField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/listboxfield/) and add the available options.
1. Add the field to the form and save the document.

```java
public static void addListBoxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ListBoxField listBox = new ListBoxField(page, new Rectangle(50, 650, 100, 700, true));
        listBox.setPartialName("list");
        listBox.addOption("Red");
        listBox.addOption("Green");
        listBox.addOption("Blue");

        document.getForm().add(listBox);
        document.save(outputFile.toString());
    }
}
```

## Create a signature field

Use this example when the document must reserve a visible area for a digital signature.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a page.
1. Create a [SignatureField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/signaturefield/) in the required rectangle.
1. Add the field to the form and save the output PDF.

```java
public static void addSignatureField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        SignatureField signatureField = new SignatureField(page, new Rectangle(100, 700, 200, 800, true));
        signatureField.setPartialName("Signature1");
        document.getForm().add(signatureField);
        document.save(outputFile.toString());
    }
}
```

## Create a barcode field

Use this example when the form should display machine-readable data inside a barcode field.

1. Create a new PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a page.
1. Create a [BarcodeField](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/barcodefield/) and add the barcode value.
1. Add the field to the form and save the document.

```java
public static void addBarcodeField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        BarcodeField barcode = new BarcodeField(page, new Rectangle(100, 700, 200, 740, true));
        barcode.setPartialName("Barcode1");
        barcode.addBarcode("1234567890");
        document.getForm().add(barcode);
        document.save(outputFile.toString());
    }
}
```
