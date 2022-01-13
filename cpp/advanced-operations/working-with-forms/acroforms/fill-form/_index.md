---
title: Fill AcroForm
linktitle: Fill AcroForm
type: docs
weight: 20
url: /cpp/fill-form/
description: This section explains how to fill form field in a PDF document with Aspose.PDF for C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF documents are the best, and really the preferred file type, for creating Forms.

This topic explains how to fill PDF forms using Aspose.PDF for C++.

Aspose.PDF for C++ allows you to fill a form field, get the field from the Document object’s Form collection.

Let's look at the following example how to resolve this task:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void FillAcroform()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"FillFormField.pdf");

    // Get a field
    auto textBoxField = System::DynamicCast<Aspose::Pdf::Forms::TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Modify field value
    textBoxField->set_Value(u"Value to be filled in the field");

    // Save updated document
    document->Save(_dataDir + u"FillFormField_out.pdf");

}
```
