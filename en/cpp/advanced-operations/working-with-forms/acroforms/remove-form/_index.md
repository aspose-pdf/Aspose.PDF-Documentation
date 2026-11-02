---
title: Remove PDF Form XObjects in C++
linktitle: Remove Form XObjects
type: docs
weight: 70
url: /cpp/remove-form/
description: Remove all Form XObjects or selected Typewriter resources from the first PDF page using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete Page Form XObject Resources with C++
Abstract: Learn how to clear or selectively delete page Form XObject resources with Aspose.PDF for C++. These examples operate on the first page resource collection rather than deleting interactive AcroForm fields.
---

## Clear the first page Form XObjects

This removes all Form XObject resources on page 1, including any that do not represent interactive form fields.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Retrieve [XFormCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/xformcollection/) from page 1 resources.
1. Call Clear() on the collection.
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XFormCollection.h>


using namespace System;
using namespace Aspose::Pdf;

void FormExamples::RemoveAllForms(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto forms = document->get_Pages()->idx_get(1)->get_Resources()->get_Forms();
    forms->Clear();
    document->Save(outputFile);
}
```

## Remove matching Typewriter XObjects

Collecting names before deletion avoids changing the collection while it is being enumerated. To delete an AcroForm field by name, use the Modify AcroForm guide.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Enumerate [XForm](https://reference.aspose.com/pdf/cpp/aspose.pdf/xform/) resources on page 1.
1. Collect resource names when IT is Typewriter and Subtype is Form.
1. Delete the collected names from [XFormCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/xformcollection/).
1. Save the PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XForm.h>
#include <Aspose.PDF.Cpp/XFormCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void FormExamples::RemoveSpecifiedForm(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto forms = document->get_Pages()->idx_get(1)->get_Resources()->get_Forms();
    std::vector<String> formNames;
    for (auto& form : forms)
    {
        if (String(u"Typewriter") == form->get_IT() && String(u"Form") == form->get_Subtype())
        {
            formNames.push_back(forms->GetFormName(form));
        }
    }
    for (auto& formName : formNames)
    {
        forms->Delete(formName);
    }
    document->Save(outputFile);
}
```
