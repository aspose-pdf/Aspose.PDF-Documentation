---
title: Add and delete PDF bookmarks in C++
linktitle: Add and Delete a Bookmark
type: docs
weight: 10
url: /cpp/add-and-delete-bookmark/
description: Create bookmarks and parent-child outline hierarchies and delete one or all bookmarks using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Build and Remove PDF Bookmark Hierarchies in C++
Abstract: Use OutlineItemCollection and OutlineCollection to add and remove PDF bookmarks. The examples create a page destination, build a parent-child hierarchy, and delete bookmarks by title or remove the complete outline tree.
---

PDF bookmarks are entries in a document's outline tree. These examples add a bookmark targeting page 1, construct a parent-child hierarchy, and remove outline entries.

Configure the Aspose.PDF for C++ SDK and create the output directory before running examples that save a file. The snippets retain the source includes, function parameters, coordinates, and action settings, with the project runner header omitted.

## Add a bookmark

Create a bold, italic Test Outline bookmark targeting page 1.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create an [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlineitemcollection/) in the document outline tree.
1. Set its title, italic flag, and bold flag.
1. Assign a [GoToAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotoaction/) targeting page 1.
1. Add the item with [OutlineCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlinecollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToAction.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineCollection.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineItemCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

// Port of bookmarks/AddExamples.addBookmark.
void AddBookmark(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto pdfOutline = MakeObject<OutlineItemCollection>(document->get_Outlines());
    pdfOutline->set_Title(u"Test Outline");
    pdfOutline->set_Italic(true);
    pdfOutline->set_Bold(true);
    pdfOutline->set_Action(MakeObject<GoToAction>(document->get_Pages()->idx_get(1)));

    document->get_Outlines()->Add(pdfOutline);
    document->Save(outputFile);
}
```

## Add a child bookmark

Create Parent Outline with a nested Child Outline, both bold and italic. This sample builds the hierarchy without assigning a destination or action to either item.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create parent and child [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlineitemcollection/) objects.
1. Set their titles and text styles.
1. Add the child to the parent with [OutlineItemCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlineitemcollection/add/).
1. Add the parent to the document [Outlines](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_outlines/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineCollection.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineItemCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of bookmarks/AddExamples.addChildBookmark.
void AddChildBookmark(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto pdfOutline = MakeObject<OutlineItemCollection>(document->get_Outlines());
    pdfOutline->set_Title(u"Parent Outline");
    pdfOutline->set_Italic(true);
    pdfOutline->set_Bold(true);

    auto pdfChildOutline = MakeObject<OutlineItemCollection>(document->get_Outlines());
    pdfChildOutline->set_Title(u"Child Outline");
    pdfChildOutline->set_Italic(true);
    pdfChildOutline->set_Bold(true);

    pdfOutline->Add(pdfChildOutline);
    document->get_Outlines()->Add(pdfOutline);
    document->Save(outputFile);
}
```

## Delete a bookmark by title

Delete the outline entry named Child Outline using the title-based overload.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the document [Outlines](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_outlines/).
1. Call [OutlineCollection::Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlinecollection/delete/) with Child Outline.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineCollection.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineItemCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of bookmarks/AddExamples.deleteBookmark.
void DeleteBookmark(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->get_Outlines()->Delete(u"Child Outline");
    document->Save(outputFile);
}
```

## Delete all bookmarks

Remove the document outline entries with the no-argument Delete() overload.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [OutlineCollection::Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf/outlinecollection/delete/) on the document outline collection.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineCollection.h>
#include <Aspose.PDF.Cpp/Outlines/OutlineItemCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of bookmarks/AddExamples.deleteBookmarks.
void DeleteBookmarks(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    document->get_Outlines()->Delete();
    document->Save(outputFile);
}
```
