---
title: Fill PDF form fields in C++
linktitle: Fill AcroForm
type: docs
weight: 20
url: /cpp/fill-form/
description: Fill selected named fields in an existing PDF form using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Populate Named AcroForm Fields with C++
Abstract: Learn how to match existing field names and assign values with the Form facade in Aspose.PDF for C++. The example fills four selected fields and saves the updated PDF.
---

## Fill selected named fields

Only matching field names are filled. The sample does not inspect the Boolean result of FillField().

1. Create a [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade for the input PDF.
1. Prepare the supplied names and values for First Name, Last Name, City, and Country.
1. Iterate through FieldNames and match the four target names.
1. Call [FillField()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) on [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) for matching fields.
1. Save the facade to outputFile and close it.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;

void FormExamples::FillForm(String inputFile, String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);
    const String names[] = {u"First Name", u"Last Name", u"City", u"Country"};
    const String values[] = {u"Alexander_New", u"Greenfield_New", u"Yellowtown_New", u"Redland_New"};
    for (const auto &fieldName : form->get_FieldNames())
        for (int i = 0; i < 4; ++i)
            if (fieldName == names[i])
                form->FillField(fieldName, values[i]);
    form->Save(outputFile);
    form->Close();
}
```
