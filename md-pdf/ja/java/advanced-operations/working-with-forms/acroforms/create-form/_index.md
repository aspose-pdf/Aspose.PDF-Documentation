---
title: Create AcroForms - Create Fillable PDF in Java
linktitle: Create AcroForms
type: docs
weight: 10
url: /java/create-forms/
description: This section explains how to create AcroForms from scratch in your PDF documents with Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Form Field in a PDF Document

The [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class provides a collection named Form which helps manage form fields in a PDF document.

To add a form field:

1. Create the form field which you want to add.
2. Call the [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form) collection's add method.

This example shows how to add a TextBoxField. You can add any form field using the same approach:

1. First, create a field object and set its properties.
2. Then, add the field to the Form collection.

### Adding TextBoxField

A text field is a form element which allows a recipient to enter text into your form. This would be used any time you want to allow the user the freedom to type what they want.  

The following code snippets shows how to add a TextBoxField to a PDF document.

```java
public class ExamplesCreateForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void AddingTextBoxField() {

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
```

## Adding RadioButtonField

A Radio Button is most commonly used for multiple choice questions, in the scenario where only one answer can be selected.

The following code snippets show how to add [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) in a PDF document.

```java
public static void AddingRadioButton() {
        Document pdfDocument = new Document();
        // add a page to PDF file
        pdfDocument.getPages().add();

        // instantiate RadioButtonField object with page number as argument
        RadioButtonField radio = new RadioButtonField(pdfDocument.getPages().get_Item(1));

        // add first radio button option and also specify its origin using Rectangle
        // object
        radio.addOption("Test", new Rectangle(20, 720, 40, 740));
        // add second radio button option
        radio.addOption("Test1", new Rectangle(120, 720, 140, 740));
        // add radio button to form object of Document object
        pdfDocument.getForm().add(radio);
        // save the PDF file
        pdfDocument.save("RadioButtonSample.pdf");

    }
```

The following code snippet shows the steps to add [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) with three options and place them inside Table cells.

```java
public static void AddingRadioButtonAdvanced() {
        Document doc = new Document();
        Page page = doc.getPages().add();
        Table table = new Table();
        table.setColumnWidths("120 120 120");
        page.getParagraphs().add(table);
        Row r1 = table.getRows().add();
        Cell c1 = r1.getCells().add();
        Cell c2 = r1.getCells().add();
        Cell c3 = r1.getCells().add();

        RadioButtonField rf = new RadioButtonField(page);
        rf.setPartialName("radio");
        doc.getForm().add(rf, 1);

        RadioButtonOptionField opt1 = new RadioButtonOptionField();
        RadioButtonOptionField opt2 = new RadioButtonOptionField();
        RadioButtonOptionField opt3 = new RadioButtonOptionField();

        opt1.setOptionName("Item1");
        opt2.setOptionName("Item2");
        opt3.setOptionName("Item3");

        opt1.setWidth(15);
        opt1.setHeight(15);
        opt2.setWidth(15);
        opt2.setHeight(15);
        opt3.setWidth(15);
        opt3.setHeight(15);

        rf.add(opt1);
        rf.add(opt2);
        rf.add(opt3);

        opt1.setBorder(new Border(opt1));
        opt1.getBorder().setWidth(1);
        opt1.getBorder().setStyle(BorderStyle.Solid);
        opt1.getCharacteristics().setBorder(Color.getBlack());
        opt1.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt1.setCaption(new TextFragment("Item1"));
        opt2.setBorder(new Border(opt2));
        opt2.getBorder().setWidth(1);
        opt2.getBorder().setStyle(BorderStyle.Solid);
        opt2.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt2.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt2.setCaption(new TextFragment("Item2"));
        opt3.setBorder(new Border(opt3));
        opt3.getBorder().setWidth(1);
        opt3.getBorder().setStyle(BorderStyle.Solid);
        opt3.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt3.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt3.setCaption(new TextFragment("Item3"));
        c1.getParagraphs().add(opt1);
        c2.getParagraphs().add(opt2);
        c3.getParagraphs().add(opt3);

        doc.save("RadioButtonField.pdf");
    }
```

## Adding Caption to RadioButtonField

Following code snippet shows how to add caption which will be associated with [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField):

```java
public static void AddingCaptionToRadioButtonField() {
        // Load source PDF form
        com.aspose.pdf.facades.Form form1 = new com.aspose.pdf.facades.Form(_dataDir + "RadioButtonField.pdf");
        Document document = new Document(_dataDir + "RadioButtonField.pdf");
        for (String item : form1.getFieldNames()) {
            System.out.println(item.toString());
            if (item.contains("radio1")) {
                RadioButtonField field0 = (RadioButtonField) document.getForm().get(item);
                RadioButtonOptionField fieldoption = new RadioButtonOptionField();
                fieldoption.setOptionName("Yes");
                fieldoption.setPartialName("Yesname");

                var updatedFragment = new TextFragment("test123");
                updatedFragment.getTextState().setFont(FontRepository.findFont("Arial"));
                updatedFragment.getTextState().setFontSize(10);
                updatedFragment.getTextState().setLineSpacing(6.32f);

                // Create TextParagraph object
                TextParagraph par = new TextParagraph();

                // Set paragraph position
                par.setPosition(new Position(field0.getRect().getLLX(),
                        field0.getRect().getLLY() + updatedFragment.getTextState().getFontSize()));
                // Specify word wraping mode
                par.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

                // Add new TextFragment to paragraph
                par.appendLine(updatedFragment);

                // Add the TextParagraph using TextBuilder
                TextBuilder textBuilder = new TextBuilder(document.getPages().get_Item(1));
                textBuilder.appendParagraph(par);

                field0.deleteOption("item1");
            }
        }
        document.save(_dataDir + "RadioButtonField_out.pdf");

    }
```

## Adding ComboBox field

A Combo Box is a form field which will add a dropdown menu to your document. 

The following code snippets show how to add [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) field in a PDF document.

```java
public static void AddingComboboxField() {
        // create Document object
        Document doc = new Document();
        // add page to document object
        doc.getPages().add();
        // instantiate ComboBox Field object
        ComboBoxField combo = new ComboBoxField(doc.getPages().get_Item(1), new Rectangle(100, 600, 150, 616));
        // add option to ComboBox
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        // add combo box object to form fields collection of document object
        doc.getForm().add(combo);
        // save the PDF document
        doc.save("ComboBox_Added.pdf");
    }
```

## Add Tooltip to Form

The Document class provides a collection named Form which manages form fields in a PDF document. To add a tooltip to a form field, use the Field class AlternateName. Adobe Acrobat uses the ‘alternate name’ as a field tooltip.

The code snippets that follow show how to add a tooltip to a form field with Java.

```java
public static void AddTooltipToFormField() {
        // Load source PDF form
        Document doc = new Document(_dataDir + "AddTooltipToField.pdf");

        // Get a field
        TextBoxField textBoxField = (TextBoxField) doc.getForm().get("textbox1");

        // Set the tooltip for textfield
        textBoxField.setAlternateName("Text box tool tip");

        // Save modified document
        doc.save("output.pdf");
    }
```
