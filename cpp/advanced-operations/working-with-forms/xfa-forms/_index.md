---
title: Working with XFA Forms using C++
linktitle: XFA Forms
type: docs
weight: 20
url: /cpp/xfa-forms/
description: Aspose.PDF for C++ API lets you work with XFA and XFA Acroform fields in a PDF document. The Aspose.PDF.Facades.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFA Forms is  XML Forms Architecture, a family of proprietary XML specifications that were proposed and developed by JetForm to improve the handling of web forms. It can also be used in PDF files starting with the PDF 1.5 specification.

Fill XFA fields with [Form](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form/) class by [Aspose.Pdf.Facades](https://apireference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades).

## Fill XFA fields

The following code snippet shows you how to fill fields in XFA form.

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void FillXFA() {
    String _dataDir("C:\\Samples\\");

    // Load XFA form
    auto document = MakeObject<Document>(_dataDir + u"FillXFAFields.pdf");

    // Get names of XFA form fields
    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Set field values

    document->get_Form()->get_XFA()->idx_set(names->idx_get(0),u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(1),u"Field 1");

    // Save the updated document
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```

## Convert XFA to AcroForm

{{% alert color="primary" %}}

Try online
You can check the quality of Aspose.PDF conversion and view the results online at this link: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Dynamic forms are based on an XML specification known as XFA, the “XML Forms Architecture”. The information about the form (as far as a PDF is concerned) is very vague – it specifies that fields exist, with properties, and JavaScript events, but does not specify any rendering.

Currently, PDF supports two different methods for integrating data and PDF forms:

- AcroForms (also known as Acrobat forms), introduced and included in the PDF 1.2 format specification.
- Adobe XML Forms Architecture (XFA) forms, introduced in the PDF 1.5 format specification as an optional feature (The XFA specification is not included in the PDF specification, it is only referenced.)

We cannot extract or manipulate pages of XFA Forms, because the form content is generated at runtime (during XFA form viewing) within the application trying to display or render the XFA form. Aspose.PDF has a feature that allows developers to convert XFA forms to standard AcroForms.

```cpp
void ConvertXFAtoAcroForms() {

    String _dataDir("C:\\Samples\\");

    // Load XFA form
    auto document = MakeObject<Document>(_dataDir + u"DynamicXFAToAcroForm.pdf");

    // Set the form fields type as standard AcroForm
    document->get_Form()->set_Type(Aspose::Pdf::Forms::FormType::Standard);

    // Save the resultant PDF
    document->Save(_dataDir + u"Standard_AcroForm_out.pdf");
}
```

## Get XFA field properties

To access field properties, first use Document.Form.XFA.Teamplate to access the field template. The following code snippet shows the steps of getting X and Y coordinates of XFA a form field.

```cpp
void GetXFAProprties() {

    String _dataDir("C:\\Samples\\");
    // Load XFA form
    auto document = MakeObject<Document>(_dataDir + u"GetXFAProperties.pdf");

    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Set field values
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 1");

    // Get field position
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"x")->get_Value());

    // Get field position
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"y")->get_Value());

    // Save the updated document
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```
