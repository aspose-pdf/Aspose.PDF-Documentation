---
title: PDF Tooltip using using C++
linktitle: PDF Tooltip
type: docs
weight: 20
url: /cpp/pdf-tooltip/
description: Aspose.PDF implements a function of hiding actions, with which you can show/hide an annotation when you enter/leave the mouse over an invisible button.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Tooltip to Searched Text by adding Invisible Button

This article demonstrates how to add tooltip to the text on an existing PDF document in C++. Aspose.PDF supports to create tooltips by adding invisible button over the searched text from the PDF file.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void AddTooltipToSearchedText() {

    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("Tooltip_out.pdf");

    // Create sample document with text
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Move the mouse cursor here to display a tooltip"));

    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(MakeObject<TextFragment>("Move the mouse cursor here to display a very long tooltip"));

    document->Save(outputFileName);

    // Open document with text
    auto document = MakeObject<Document>(outputFileName);
    // Create TextAbsorber object to find all the phrases matching the regular expression
    auto absorber = MakeObject<TextFragmentAbsorber>("Move the mouse cursor here to display a tooltip");
    // Accept the absorber for the document pages
    document->get_Pages()->Accept(absorber);

    // Get the extracted text fragments
    auto textFragments = absorber->get_TextFragments();

    // Loop through the fragments
    for(auto fragment : textFragments)
    {
        // Create invisible button on text fragment position
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // AlternateName value will be displayed as tooltip by a viewer application
        field->set_AlternateName (u"Tooltip for text.");
        // Add button field to the document
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Next will be sapmle of very long tooltip
    absorber = MakeObject<TextFragmentAbsorber>("Move the mouse cursor here to display a very long tooltip");
    document->get_Pages()->Accept(absorber);
    textFragments = absorber->get_TextFragments();

    for(auto fragment : textFragments)
    {
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // Set very long text
        field->set_AlternateName(String("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.\
            Duis aute irure dolor in reprehenderit in voluptate velit\
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\
            occaecat cupidatat non proident, sunt in culpa qui officia\
            deserunt mollit anim id est laborum."));
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // Save document
    document->Save(outputFileName);

}
```

## Create a Hidden Text Block and Show it on Mouse Over

Aspose.PDF for C++ implements a hide actions function, with which you can show/hide a text field (or any other type of annotation) when entering/exiting the mouse over some invisible button. To do this, use the Aspose.Pdf.Annotations.HideAction class to assign a hide/show action to the text block. Use the following code snippet to show/hide the text block on mouse input/output.

Also note that PDF actions on documents work fine in their respective readers (such as Adobe Reader), but do not provide any guarantees for other PDF readers (such as web browser plug-ins). We did a short investigation and found:

- All implementations of the hide action in PDF documents work fine in Internet Explorer v.11.0.
- All implementations of the hide action also work in Opera v.12.14, but we spot some response delay at the first opening of the document.
- Only implementation using HideAction constructor accepting field name works if Google Chrome v.61.0 browses the document; Please use corresponding constructors if browsing in the Google Chrome is significant:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```cpp
void CreateHiddenTextBlock() {

    String _dataDir("C:\\Samples\\");

    // String for output file name
    String outputFileName("TextBlock_HideShow_MouseOverOut_out.pdf");

    // Create sample document with text
    auto document = MakeObject<Document>();

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("Move the mouse cursor here to display floating text"));
    document->Save(outputFileName);

    // Open document with text
    auto document = MakeObject<Document>(outputFileName);

    // Create TextAbsorber object to find all the phrases matching the regular expression
    auto absorber = MakeObject<TextFragmentAbsorber>("Move the mouse cursor here to display floating text");
    // Accept the absorber for the document pages
    document->get_Pages()->Accept(absorber);
    // Get the first extracted text fragment
    auto textFragments = absorber->get_TextFragments();
    auto fragment = textFragments->idx_get(1);

    // Create hidden text field for floating text in the specified rectangle of the page
    auto floatingField = MakeObject<Aspose::Pdf::Forms::TextBoxField>(fragment->get_Page(), MakeObject<Rectangle>(100, 700, 220, 740));
    // Set text to be displayed as field value
    floatingField->set_Value(u"This is the \"floating text field\".");
    // We recommend to make field 'readonly' for this scenario
    floatingField->set_ReadOnly(true);
    // Set 'hidden' flag to make field invisible on document opening
    floatingField->set_Flags(floatingField->get_Flags() | Aspose::Pdf::Annotations::AnnotationFlags::Hidden);

    // Setting a unique field name isn't necessary but allowed
    floatingField->set_PartialName (u"FloatingField_1");

    // Setting characteristics of field appearance isn't necessary but makes it better
    floatingField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>("Helv", 10, Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background (System::Drawing::Color::get_LightBlue());
    floatingField->get_Characteristics()->set_Border (System::Drawing::Color::get_DarkBlue());
    floatingField->set_Border(MakeObject<Aspose::Pdf::Annotations::Border>(floatingField));
    floatingField->get_Border()->set_Width (1);
    floatingField->set_Multiline (true);

    // Add text field to the document
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(floatingField));

    // Create invisible button on text fragment position
    auto buttonField = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    // Create new hide action for specified field (annotation) and invisibility flag.
    // (You also may reffer floating field by the name if you specified it above.)
    // Add actions on mouse enter/exit at the invisible button field
    buttonField->get_Actions()->set_OnEnter(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField));

    // Add button field to the document
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(buttonField));

    // Save document
    document->Save(outputFileName);
}
```
