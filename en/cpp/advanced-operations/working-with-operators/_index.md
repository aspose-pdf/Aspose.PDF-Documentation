---
title: Work with PDF operators in C++
linktitle: Working with Operators
type: docs
weight: 80
url: /cpp/working-with-operators/
description: Use PDF operators to add images, remove selected graphics instructions, and draw reusable XForms with Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Control PDF Content Streams and Reuse XForms in C++
Abstract: Learn how to manipulate page content streams with Aspose.PDF for C++. The examples place an image with graphics-state and transformation operators, remove selected path-painting operators, and draw an image twice through a reusable XForm.
---

PDF operators are instructions in a content stream that control how text, images, and vector graphics are painted. Aspose.PDF for C++ exposes these instructions through the page Contents collection and classes in the Aspose::Pdf::Operators namespace.

Use operators when you need direct control over drawing instructions and transformations. The following examples modify the first page of an existing PDF. Each function accepts an input PDF path and an output PDF path.

## Add an image with PDF operators

This example loads PDFOperators.jpg from the same directory as the input PDF and adds it to the first page resources. It then appends operators to paint the image.

GSave preserves the current graphics state, ConcatenateMatrix scales and positions the image, Do paints the named image resource, and GRestore restores the previous state. The matrix specifies a 100 by 100 placement translated to (100, 100) in the current coordinate system.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Open PDFOperators.jpg as a file stream.
1. Get the first page and add the image to its [Resources.Images](https://reference.aspose.com/pdf/cpp/aspose.pdf/resources/get_images/) collection.
1. Append [GSave](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/gsave/) to preserve the graphics state.
1. Add [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/concatenatematrix/) to set the image scale and position.
1. Append [Do](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/do/) with the returned image resource name.
1. Add [GRestore](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/grestore/) to restore the graphics state.
1. Save the output PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/) and close the image stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Operator.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>
#include <Aspose.PDF.Cpp/XForm.h>
#include <Aspose.PDF.Cpp/XFormCollection.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/path.h>
#include <system/collections/list.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Operators;

void AddImage(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto image = System::IO::File::OpenRead(
        System::IO::Path::Combine(System::IO::Path::GetDirectoryName(inputFile), u"PDFOperators.jpg"));
    auto page = document->get_Pages()->idx_get(1);
    auto name = page->get_Resources()->get_Images()->Add(image);
    page->get_Contents()->Add(MakeObject<GSave>());
    page->get_Contents()->Add(MakeObject<ConcatenateMatrix>(100, 0, 0, 100, 100, 100));
    page->get_Contents()->Add(MakeObject<Do>(name));
    page->get_Contents()->Add(MakeObject<GRestore>());
    document->Save(outputFile);
    image->Close();
}
```

## Remove selected graphics operators

This example collects Stroke, ClosePathStroke, and Fill operators from the first page content stream and deletes them after enumeration. Collecting the operators first avoids modifying the collection while iterating through it.

The example removes only these operator types from the page content stream. It does not remove image resources, recursively edit XForms, or cover every path-painting operator. Review the result against the source document because other instructions in the stream remain.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first page [Contents](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_contents/) collection.
1. Create a list to hold the [Operator](https://reference.aspose.com/pdf/cpp/aspose.pdf/operator/) objects to remove.
1. Iterate through the content stream and collect [Stroke](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/stroke/), [ClosePathStroke](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/closepathstroke/), and [Fill](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/fill/) operators.
1. Call [Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf/operatorcollection/delete/) to remove the collected operators from [Contents](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_contents/).
1. Save the updated PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Operator.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>
#include <Aspose.PDF.Cpp/XForm.h>
#include <Aspose.PDF.Cpp/XFormCollection.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/path.h>
#include <system/collections/list.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Operators;

void RemoveGraphics(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto contents = document->get_Pages()->idx_get(1)->get_Contents();
    auto removed = MakeObject<System::Collections::Generic::List<SharedPtr<Operator>>>();
    for (auto& item : contents)
    {
        if (item.dynamic_pointer_cast<Stroke>()
            || item.dynamic_pointer_cast<ClosePathStroke>()
            || item.dynamic_pointer_cast<Fill>())
            removed->Add(item);
    }
    contents->Delete(removed);
    document->Save(outputFile);
}
```

## Draw a reusable XForm on a page

An XForm is a form XObject whose content stream can be painted more than once. This example creates an XForm containing sample-cover.jpg and draws it twice on the first page.

The image file must be in the same directory as the input PDF. A matrix inside the form scales the image to 200 by 200 units. The page operators then translate the form to (100, 500) and (100, 300), reusing the same form resource.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and the sample-cover.jpg image stream.
1. Get the first page and its [Contents](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_contents/) collection.
1. Insert [GSave](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/gsave/) before the existing page content and append [GRestore](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/grestore/) after it to isolate its graphics state.
1. Append [GSave](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/gsave/) for the new drawing operations.
1. Create an [XForm](https://reference.aspose.com/pdf/cpp/aspose.pdf/xform/) with [XForm::CreateNewForm](https://reference.aspose.com/pdf/cpp/aspose.pdf/xform/createnewform/) and register it in the page [Resources.Forms](https://reference.aspose.com/pdf/cpp/aspose.pdf/resources/get_forms/) collection.
1. Add the image to the form resources with [XImageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/ximagecollection/add/).
1. Add [GSave](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/gsave/), [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/concatenatematrix/), [Do](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/do/), and [GRestore](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/grestore/) to the form content stream.
1. Draw the form at each position with a separate [GSave](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/gsave/), [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/concatenatematrix/), [Do](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/do/), and [GRestore](https://reference.aspose.com/pdf/cpp/aspose.pdf.operators/grestore/) sequence.
1. Restore the page graphics state.
1. Save the output PDF with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/) and close the image stream.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Operator.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/XImageCollection.h>
#include <Aspose.PDF.Cpp/XForm.h>
#include <Aspose.PDF.Cpp/XFormCollection.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Operators;


void DrawXForm(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto image = System::IO::File::OpenRead(
        System::IO::Path::Combine(System::IO::Path::GetDirectoryName(inputFile), u"sample-cover.jpg"));
    auto page = document->get_Pages()->idx_get(1);
    auto contents = page->get_Contents();
    contents->Insert(1, MakeObject<GSave>());
    contents->Add(MakeObject<GRestore>());
    contents->Add(MakeObject<GSave>());
    auto form = XForm::CreateNewForm(page, document);
    page->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<GSave>());
    form->get_Contents()->Add(MakeObject<ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    auto name = form->get_Resources()->get_Images()->Add(image);
    form->get_Contents()->Add(MakeObject<Do>(name));
    form->get_Contents()->Add(MakeObject<GRestore>());
    for (int y : {500, 300})
    {
        contents->Add(MakeObject<GSave>());
        contents->Add(MakeObject<ConcatenateMatrix>(1, 0, 0, 1, 100, y));
        contents->Add(MakeObject<Do>(form->get_Name()));
        contents->Add(MakeObject<GRestore>());
    }
    contents->Add(MakeObject<GRestore>());
    document->Save(outputFile);
    image->Close();
}
```

