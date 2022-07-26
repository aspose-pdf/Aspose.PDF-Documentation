---
title: Modifing AcroForm
linktitle: Modifing AcroForm
type: docs
weight: 40
url: /cpp/modifing-form/
description: Modifing form in your PDF file with Aspose.PDF for C++ library. You can Add or remove fields in existing form, getand set fieldlimit and etc.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get or Set Field Limit

The FormEditor class SetFieldLimit(field, limit) method allows you to set a field limit, the maximum number of characters that can be entered into a field.

```cpp
void SetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Open document
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    textBoxField->set_MaxLen(15);
    document->Save(_dataDir + u"GetValuesFromAllFields.pdf");
}
```

Similarly, Aspose.PDF has a method that gets the field limit using the DOM approach. The following code snippet shows the steps.

```cpp
void GetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Open document
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    Console::WriteLine(u"Limit: {0}", textBoxField->get_MaxLen());        
}
```

You can also set and get the same value using the *Aspose.PDF.Facades* namespace using the following code snippet.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void SetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Adding Field with limit
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>(_dataDir + u"input.pdf", _dataDir + u"SetFieldLimit_out.pdf");
    form->SetFieldLimit(u"textbox1", 15);
    form->Save();
}
```

```cpp
void GetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Adding Field with limit
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"input.pdf");
    Console::WriteLine(u"Limit: {0}", form->GetFieldLimit(u"textbox1"));
}
```

## Set Custom Font for the Form Field

Form fields in Adobe PDF files can be configured to use specific default fonts. In the early versions of Aspose.PDF, only the 14 default fonts were supported. Later releases allowed developers to apply any font. To set and update the default font used for form fields, use the DefaultAppearance (Font font, double size, Color color) class. This class can be found under the Aspose.PDF.InteractiveFeatures namespace. To use this object, use the Field class DefaultAppearance property.

The following code snippet shows how to set the default font for PDF form fields.

```cpp
void SetCustomFontForField() {

    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = new Document(_dataDir + u"FormFieldFont14.pdf");

    // Get particular form field from document
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Create font object
    auto font = Aspose::Pdf::Text::FontRepository::FindFont(u"ComicSansMS");

    // Set the font information for form field

    textBoxField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(font, 10, System::Drawing::Color::get_Black()));

    // Save updated document
    document->Save(_dataDir + u"FormFieldFont14.pdf");
}
```

## Delete fields from existing form

All the form fields are contained in the Document object’s Form collection. This collection provides different methods that manage form fields, including the Delete method. If you want to delete a particular field, pass the field name as a parameter to the Delete method and then save the updated PDF document. The following code snippet shows how to delete a particular field from a PDF document.

```cpp
void DeleteFormField() {    
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = new Document(_dataDir + u"DeleteFormField.pdf");

    // Delete a particular field by name
    document->get_Form()->Delete(u"textbox1");
    
    // Save modified document
    document->Save(_dataDir + u"DeleteFormField_out.pdf");
}
```
