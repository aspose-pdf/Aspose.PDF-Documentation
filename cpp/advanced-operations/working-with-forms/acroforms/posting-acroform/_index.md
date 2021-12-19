---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /cpp/posting-acroform-data/
description: You can import and export form data to and XML file with Aspose.Pdf.Facades namespace in Aspose.PDF for C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

AcroForm is an important type of the PDF document. You can not only create and edit an AcroForm using [Aspose.Pdf.Facades namepsace](https://apireference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades), but also import and export form data to and XML file. Aspose.Pdf.Facades namespace in Aspose.PDF for C++ allows you to implement another feature of AcroForm, which helps you post an AcroForm data to an external web page. This web page then reads the post variables and uses this data for further processing. This feature is useful in the cases when you don’t just want to keep the data in the PDF file, rather you want to send it to your server and then save it in a database etc.

{{% /alert %}}

## Implementation details

In this article, we have tried to create an AcroForm using [Aspose.Pdf.Facades namepsace](https://apireference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades) and [FormEditor](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form_editor/) class. We have also added a submit button and set its target URL.

The following code snippets show you how to create the form and then receive the posted data on the web page.

```cpp
using namespace System;
using namespace Aspose::Pdf;

void PostingExample() {

    // String _dataDir("C:\\Samples\\");
    // Create an instance of FormEditor class and bind input and output pdf files
    auto editor = MakeObject<Aspose::Pdf::Facades::FormEditor>("input.pdf", "output.pdf");

    // Create AcroForm fields - I have created only two fields for simplicity
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"firstname", 1, 100, 600, 200, 625);
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"lastname", 1, 100, 550, 200, 575);

    // Add a submit button and set target URL
    editor->AddSubmitBtn(u"submitbutton", 1, u"Submit", u"http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

    // Save output pdf file
    editor->Save();
}
```
