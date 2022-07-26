---
title: Create AcroForms using using C++
linktitle: Create AcroForms
type: docs
weight: 10
url: /cpp/create-form/
description: This section explains how to create AcroForms from scratch in your PDF documents with Aspose.PDF for C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Form Field in PDF Document

The [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) class provides a collection named Form which helps manage form fields in a PDF document.

To add a form field:

1. Create the form field which you want to add.
2. Call the [Form](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.forms) collection’s add method.

This example shows how to add a [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field). You can add any form field using the same approach:

1. First, create a field object and set its properties.
2. Then, add the field to the Form collection.

### Adding TextBoxField

A text field is a form element which allows a recipient to enter text into your form. This would be used any time you want to allow the user the freedom to type what they want.

The following code snippets shows how to add a TextBoxField to a PDF document.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
void AddingTextBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Open document
    auto document = MakeObject<Document>(_dataDir + u"TextField.pdf");

    // Create a field
    auto textBoxField = MakeObject<TextBoxField>(document->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(100, 200, 300, 300));
    textBoxField->set_PartialName (u"textbox1");
    textBoxField->set_Value (u"Text Box");

    // TextBoxField.Border = new Border(
    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textBoxField);
    border->set_Width(5);
    border->set_Dash (MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textBoxField->set_Border(border);

    textBoxField->set_Color(Aspose::Pdf::Color::get_Green());

    // Add field to the document
    document->get_Form()->Add(textBoxField, 1);

    // Save modified PDF
    document->Save(_dataDir + u"TextBox_out.pdf");
}
```

## Adding RadioButtonField

A RadioButton is most commonly used for multiple choice questions, in the scenario where only one answer can be selected.

The following code snippets show how to add [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) in a PDF document.

```cpp
void AddingRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    // Open document
    auto document = MakeObject<Document>();

    // Add a page to PDF file
    document->get_Pages()->Add();

    // Instatiate RadioButtonField object with page number as argument

    auto radio = MakeObject<RadioButtonField>(document->get_Pages()->idx_get(1));

    // Add first radio button option and also specify its origin using Rectangle object
    radio->AddOption(u"Option 1", MakeObject<Rectangle>(0, 0, 20, 20));
    // Add second radio button option
    radio->AddOption(u"Option 2", MakeObject<Rectangle>(20, 20, 40, 40));
    // Add radio button to form object of Document object
    document->get_Form()->Add(radio,1);

    // Save the PDF file
    document->Save(_dataDir + u"RadioButton_out.pdf");
}
```

The following code snippet shows the steps to add [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) with three options and place them inside Table cells.

```cpp
void AddRadioButtonFieldInsideTableCells()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto table = MakeObject<Aspose::Pdf::Table>();

    table->set_ColumnWidths(u"120 120 120");

    page->get_Paragraphs()->Add(table);

    auto r1 = table->get_Rows()->Add();
    auto c1 = r1->get_Cells()->Add();
    auto c2 = r1->get_Cells()->Add();
    auto c3 = r1->get_Cells()->Add();

    auto rf = MakeObject<RadioButtonField>(page);
    rf->set_PartialName(u"radio");
    document->get_Form()->Add(rf, 1);

    auto opt1 = MakeObject<RadioButtonOptionField>();
    auto opt2 = MakeObject<RadioButtonOptionField>();
    auto opt3 = MakeObject<RadioButtonOptionField>();

    opt1->set_OptionName(u"Item1");
    opt2->set_OptionName(u"Item2");
    opt3->set_OptionName(u"Item3");

    opt1->set_Width (15);
    opt1->set_Height(15);
    opt2->set_Width (15);
    opt2->set_Height(15);
    opt3->set_Width (15);
    opt3->set_Height(15);

    rf->Add(opt1);
    rf->Add(opt2);
    rf->Add(opt3);

    opt1->set_Border(MakeObject<Border>(opt1));
    opt1->get_Border()->set_Width(1);
    opt1->get_Border()->set_Style(BorderStyle::Solid);
    opt1->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt1->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt1->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item1"));
    opt2->set_Border(MakeObject<Border>(opt2));
    opt2->get_Border()->set_Width(1);
    opt2->get_Border()->set_Style(BorderStyle::Solid);
    opt2->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt2->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt2->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item2"));
    opt3->set_Border(MakeObject<Border>(opt3));
    opt3->get_Border()->set_Width(1);
    opt3->get_Border()->set_Style(BorderStyle::Solid);
    opt3->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt3->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt3->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item3"));
    c1->get_Paragraphs()->Add(opt1);
    c2->get_Paragraphs()->Add(opt2);
    c3->get_Paragraphs()->Add(opt3);

    // Save the PDF file
    document->Save(_dataDir + u"RadioButtonWithOptions_out.pdf");
}
```

## Adding Caption to RadioButtonField

Following code snippet shows how to add caption which will be associated with [RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field):

```cpp
void AddingCaptionToRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>();

    // Load source PDF form
    auto form1 =
        MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"RadioButtonField.pdf");

    auto PDF_Template_PDF_HTML = MakeObject<Document>(_dataDir + u"RadioButtonField.pdf");

    for(auto item : form1->get_FieldNames())
    {
        System::Console::WriteLine(item);
        auto radioOptions = form1->GetButtonOptionValues(item);
        if (item.Contains(u"radio1"))
        {
            auto field0 = System::DynamicCast<RadioButtonField>(PDF_Template_PDF_HTML->get_Form()->idx_get(item));
            auto fieldoption = MakeObject<RadioButtonOptionField>();
            fieldoption->set_OptionName (u"Yes");
            fieldoption->set_PartialName (u"Yesname");

            auto updatedFragment = MakeObject<Aspose::Pdf::Text::TextFragment>(u"test123");
            updatedFragment->get_TextState()->set_Font (Aspose::Pdf::Text::FontRepository::FindFont(u"Arial"));
            updatedFragment->get_TextState()->set_FontSize(10);
            updatedFragment->get_TextState()->set_LineSpacing(6.32f);

            // Create TextParagraph object
            auto par = MakeObject<Aspose::Pdf::Text::TextParagraph>();

            // Set paragraph position
            par->set_Position(MakeObject<Aspose::Pdf::Text::Position>(field0->get_Rect()->get_LLX(), field0->get_Rect()->get_LLY() + updatedFragment->get_TextState()->get_FontSize()));
            // Specify word wraping mode
        par->get_FormattingOptions()->set_WrapMode(Aspose::Pdf::Text::TextFormattingOptions::WordWrapMode::ByWords);

            // Add new TextFragment to paragraph
            par->AppendLine(updatedFragment);

            // Add the TextParagraph using TextBuilder
            auto textBuilder = MakeObject<Aspose::Pdf::Text::TextBuilder>(PDF_Template_PDF_HTML->get_Pages()->idx_get(1));
            textBuilder->AppendParagraph(par);

            field0->DeleteOption(u"item1");
        }
    }
    PDF_Template_PDF_HTML->Save(_dataDir + u"RadioButtonField_out.pdf");
}
```

## Adding ComboBox field

A Combo Box is a form field which will add a dropdown menu to your document.

The following code snippets show how to add [ComboBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.combo_box_field) field in a PDF document.

```cpp
void AddingComboBoxField()
{
    String _dataDir("C:\\Samples\\");
    // Create Document object
    auto document = MakeObject<Document>();
    // Add page to document object
    document->get_Pages()->Add();
    // Instantiate ComboBox Field object
    auto combo = MakeObject<ComboBoxField>(document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 600, 150, 616));

    // Add option to ComboBox
    combo->AddOption(u"Red");
    combo->AddOption(u"Yellow");
    combo->AddOption(u"Green");
    combo->AddOption(u"Blue");

    // Add combo box object to form fields collection of document object
    document->get_Form()->Add(combo);

    // Save the PDF document
    document->Save(_dataDir + u"ComboBox_out.pdf");
}
```

## Add Tooltip to Form

The Document class provides a collection named Form which manages form fields in a PDF document. To add a tooltip to a form field, use the Field class AlternateName. Adobe Acrobat uses the ‘alternate name’ as a field tooltip.

The code snippets that follow show how to add a tooltip to a form field with C++.

```cpp
void AddTooltipToFormField()
{
    String _dataDir("C:\\Samples\\");
    // Load source PDF form
    auto document = new Document(_dataDir + u"AddTooltipToField.pdf");

    // Set the tooltip for textfield
    //(doc.Form["textbox1"] as Field).AlternateName = "Text box tool tip";

    // Save the updated document
    document->Save(_dataDir + u"AddTooltipToField_out.pdf");
}
```
