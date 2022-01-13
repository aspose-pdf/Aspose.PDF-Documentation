---
title: Extract AcroForm Data using C++
linktitle: Extract Data AcroForm
type: docs
weight: 30
url: /cpp/extract-form/
description: This section explains how to extract forms from your PDF document with Aspose.PDF for C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get Values from all the Fields of PDF Document

To get values from all the fields in a PDF document, you need to navigate through all the form fields and then get the value using the Value property. Get each field from the Form collection, in the base field type called Field and access its Value property.

The following code snippets show how to get the values of all the fields from a PDF document.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void ExtractDataFromForm()
{
    String _dataDir("C:\\Samples\\");
    // Open document
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");

    // Get values from all fields
    for(auto wa : document->get_Form())
    {
        auto formField = System::DynamicCast<Aspose::Pdf::Forms::Field>(wa);

        Console::WriteLine(u"Field Name : {0} ", formField->get_PartialName());
        Console::WriteLine(u"Value : {0} ", formField->get_Value());
    }
}
```

## Get Value from an Individual Field of PDF Document

The form field’s Value property allows you to get the value of a particular field. To get the value, get the form field from the Document object’s Form collection. This example selects a [TextBoxField](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field) and retrieves its value using the Value property.

The following code snippet shows how to get the values of individual the fields in a PDF document.

```cpp
void GetValueFromIndividualField(){

    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");

    // Get a field
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Get field value
    Console::WriteLine(u"PartialName : {0} ", textBoxField->get_PartialName());
    Console::WriteLine(u"Value : {0} ", textBoxField->get_Value());
}
```

To get the submit button’s URL, use the following lines of code.

```cpp
void GetSubmitButtonURL()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");
    auto act = System::DynamicCast<Aspose::Pdf::Annotations::SubmitFormAction>(document->get_Form()->idx_get(1)->get_OnActivated());

    if (act != nullptr)
        Console::WriteLine(act->get_Url()->get_Name());
}
```

## Get Form Fields from a Specific Region of PDF File

Sometimes, you might know where in a document a form field is, but not have it’s name. For example, if all you have to go from is a schematic of a printed form. With Aspose.PDF for C++, this is not a problem. You can find out which fields are in a given region of a PDF file. To get form fields from a specific region of a PDF file:

1. Open the PDF file using the Document object.
1. Create rectangle object to get fields in that area
1. Get the form from the document’s Forms collection.
1. Display Field names and values

The following code snippet shows how to get form fields in a specific rectangular region of a PDF file.

```cpp
void GetFormFieldsFromSpecificRegion()
{
    String _dataDir("C:\\Samples\\");

    // Open pdf file
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"GetFieldsFromRegion.pdf");

    // Create rectangle object to get fields in that area
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(35, 30, 500, 500);

    // Get fields in the rectangular area
    auto fields = document->get_Form()->GetFieldsInRect(rectangle);

    // Display Field names and values
    for(auto field : fields)
    {
        // Display image placement properties for all placements
        Console::WriteLine(u"Field Name: {0} - Field Value: {1}", field->get_FullName(), field->get_Value());
    }
}
```