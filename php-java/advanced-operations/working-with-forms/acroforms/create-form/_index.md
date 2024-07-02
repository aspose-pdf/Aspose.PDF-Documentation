---
title: Create AcroForms - Create Fillable PDF in PHP
linktitle: Create AcroForms
type: docs
weight: 10
url: /php-java/create-forms/
description: This section explains how to create AcroForms from scratch in your PDF documents with Aspose.PDF for PHP via Java.
lastmod: "2024-06-05"
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

```php

    // Open document
    $colors = new Color();
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);

    // Create a field
    $textBoxField = new TextBoxField($page, new Rectangle(110, 300, 310, 320));
    $textBoxField->setPartialName("textbox1");
    $textBoxField->setValue("Some value in Text Box");

    $border = new Border($textBoxField);
    $border->setWidth(5);
    $border->setDash(new Dash(1, 1));
    $textBoxField->setBorder($border);
    $textBoxField->setColor($colors->getGreen());

    // Add field to the document
    $document->getForm()->add($textBoxField, 1);

    // Save modified PDF
    $document->save($outputFile);
    $document->close();
```

## Adding RadioButtonField

A Radio Button is most commonly used for multiple choice questions, in the scenario where only one answer can be selected.

The following code snippets show how to add [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) in a PDF document.

```php

    // Open document            
    $document = new Document($inputFile);

    // add a page to PDF file
    $page = $document->getPages()->get_Item(1);

    // instantiate RadioButtonField object with page number as argument
    $radio = new RadioButtonField($page);

    // add first radio button option and also specify its origin 
    // using Rectangle object

    $radio->addOption("Test1", new Rectangle(20, 720, 40, 740));

    // add second radio button option
    $radio->addOption("Test2", new Rectangle(120, 720, 140, 740));

    // add radio button to form object of Document object
    $document->getForm()->add($radio);

    // save the PDF file
    $document->save($outputFile);
    $document->close();
```

The following code snippet shows the steps to add [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) with three options and place them inside Table cells.

```php

    $colors = new Color();
    $document = new Document();
    $page = $document->getPages()->add();

    $table = new Table();
    $table->setColumnWidths("120 120 120");
    $page->getParagraphs()->add($table);
    $r1 = $table->getRows()->add();
    $c1 = $r1->getCells()->add();
    $c2 = $r1->getCells()->add();
    $c3 = $r1->getCells()->add();

    $rf = new RadioButtonField($page);
    $rf->setPartialName("radio1");
    $document->getForm()->add($rf, 1);

    $opt1 = new RadioButtonOptionField();
    $opt2 = new RadioButtonOptionField();
    $opt3 = new RadioButtonOptionField();

    $opt1->setOptionName("Item1");
    $opt2->setOptionName("Item2");
    $opt3->setOptionName("Item3");

    $opt1->setWidth(15.0);
    $opt1->setHeight(15.0);
    $opt2->setWidth(15.0);
    $opt2->setHeight(15.0);
    $opt3->setWidth(15.0);
    $opt3->setHeight(15.0);

    $rf->add($opt1);
    $rf->add($opt2);
    $rf->add($opt3);

    $border1 = new Border($opt1);
    $opt1->setBorder($border1);
    $opt1->getBorder()->setWidth(1.0);
    $opt1->getBorder()->setStyle(BorderStyle::$Solid);
    $opt1->getCharacteristics()->setBorder($colors->getBlack());
    $opt1->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt1->setCaption(new TextFragment("Item1"));

    $border2 = new Border($opt2);
    $opt3->setBorder($border2);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt2->getCharacteristics()->setBorder($colors->getBlack());
    $opt2->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt2->setCaption(new TextFragment("Item2"));

    $border3 = new Border($opt3);
    $opt3->setBorder($border3);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt3->getCharacteristics()->setBorder($colors->getBlack());
    $opt3->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt3->setCaption(new TextFragment("Item3"));

    $c1->getParagraphs()->add($opt1);
    $c2->getParagraphs()->add($opt2);
    $c3->getParagraphs()->add($opt3);

    $document->save($outputFile);
    $document->close();
```

## Adding ComboBox field

A Combo Box is a form field which will add a dropdown menu to your document. 

The following code snippets show how to add [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) field in a PDF document.

```php

        $document = new Document($inputFile);

        // instantiate ComboBox Field object
        $page = $document->getPages()->get_Item(1);
        $combo = new ComboBoxField($page, new Rectangle(100, 600, 150, 616));

        // add option to ComboBox
        $combo->addOption("Red");
        $combo->addOption("Yellow");
        $combo->addOption("Green");
        $combo->addOption("Blue");

        // add combo box object to form fields collection of document object
        $document->getForm()->add($combo);

        // save the PDF document
        $document->save($outputFile);
        $document->close();
```

## Add Tooltip to Form

The Document class provides a collection named Form which manages form fields in a PDF document. To add a tooltip to a form field, use the Field class AlternateName. Adobe Acrobat uses the ‘alternate name’ as a field tooltip.

The code snippets that follow show how to add a tooltip to a form field with PHP.

```php

    $document = new Document($inputFile);
    $textBoxField = $document->getForm()->get("textbox1");

    // Set the tooltip for textfield
    $textBoxField->setAlternateName("Text box tool tip");

    // save the PDF document
    $document->save($outputFile);
    $document->close();
```



