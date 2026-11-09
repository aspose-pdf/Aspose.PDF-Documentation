---
title: Work with vector graphics in C++
linktitle: Working with Vector Graphics
type: docs
weight: 110
url: /cpp/working-with-vector-graphics/
description: Inspect, move, remove, and copy vector graphics between PDF pages using GraphicsAbsorber with Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Inspect and Modify PDF Vector Elements with GraphicsAbsorber in C++
Abstract: Use GraphicsAbsorber in Aspose.PDF for C++ to inspect vector elements and their operators on a PDF page. The examples move elements, remove them using a position filter, and copy graphics to a new page with individual or collection-based methods.
---

Aspose.PDF for C++ provides the [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/) class for inspecting and modifying vector graphics in an existing PDF. Visit a page to obtain its graphic elements, then inspect their properties, change their positions, remove them, or copy them to another page.

The examples below operate on the first page, so the input PDF must contain at least one page. Each function accepts an input PDF path; examples that modify the document also accept an output PDF path. Configure the Aspose.PDF for C++ SDK before using the snippets.

## Inspect vector graphics

GraphicsAbsorber reads graphic elements from the selected page. This example prints each element's source page number, position, and operator count. It does not save a modified PDF or export graphics to a separate file.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/) and call [Visit()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/visit/) on the first page.
1. Iterate through [GraphicsAbsorber::get_Elements()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/get_elements/).
1. Read the [GraphicElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/) source page, position, and operators and print the values.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Vector/GraphicsAbsorber.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElement.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElementCollection.h>
#include <system/collections/list.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

void UsingGraphicsAbsorber(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto graphicsAbsorber = MakeObject<GraphicsAbsorber>();
    auto page = document->get_Pages()->idx_get(1);
    graphicsAbsorber->Visit(page);
    for (auto element : graphicsAbsorber->get_Elements())
    {
        std::cout << "Page Number: " << element->get_SourcePage()->get_Number() << std::endl;
        std::cout << "Position: (" << element->get_Position()->get_X() << ", "
                  << element->get_Position()->get_Y() << ")" << std::endl;
        std::cout << "Number of Operators: " << element->get_Operators()->get_Count() << std::endl;
    }
}
```

## Move vector graphics

Move every extracted graphic element on the first page by adding 150 to its X position and subtracting 10 from its Y position. The example batches changes through the absorber before saving.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/) and call [Visit()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/visit/) on the first page.
1. Call [GraphicsAbsorber::SuppressUpdate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/suppressupdate/) before changing the elements.
1. Read each [GraphicElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/) position.
1. Set its new position with [set_Position()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/set_position/) and a [Point](https://reference.aspose.com/pdf/cpp/aspose.pdf/point/) containing the shifted coordinates.
1. Call [GraphicsAbsorber::ResumeUpdate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/resumeupdate/) to apply the pending updates.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Vector/GraphicsAbsorber.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElement.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElementCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

void MoveGraphics(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto graphicsAbsorber = MakeObject<GraphicsAbsorber>();
    auto page = document->get_Pages()->idx_get(1);
    graphicsAbsorber->Visit(page);
    graphicsAbsorber->SuppressUpdate();
    for (auto element : graphicsAbsorber->get_Elements())
    {
        auto position = element->get_Position();
        element->set_Position(MakeObject<Point>(position->get_X() + 150, position->get_Y() - 10));
    }
    graphicsAbsorber->ResumeUpdate();
    document->Save(outputFile);
}
```

## Remove vector graphics

### Remove individual elements

Define the rectangle (70, 248, 170, 252) and remove elements whose Position passes Rectangle::Contains(position, false). This is a position-based filter; it does not test whether the complete graphic lies inside or intersects the rectangle.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/) and call [Visit()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/visit/) on the first page.
1. Create the target [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/).
1. Call [GraphicsAbsorber::SuppressUpdate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/suppressupdate/) before changing the elements.
1. Check each element position with [Rectangle::Contains()](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/contains/).
1. Call [GraphicElement::Remove()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/remove/) on matching elements.
1. Call [GraphicsAbsorber::ResumeUpdate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/resumeupdate/) to apply the pending updates.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Vector/GraphicsAbsorber.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElement.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElementCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

void RemoveGraphicsMethod1(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto graphicsAbsorber = MakeObject<GraphicsAbsorber>();
    auto page = document->get_Pages()->idx_get(1);
    auto rectangle = MakeObject<Rectangle>(70, 248, 170, 252, true);
    graphicsAbsorber->Visit(page);
    graphicsAbsorber->SuppressUpdate();
    for (auto element : graphicsAbsorber->get_Elements())
    {
        if (rectangle->Contains(element->get_Position(), false))
        {
            element->Remove();
        }
    }
    graphicsAbsorber->ResumeUpdate();
    document->Save(outputFile);
}
```

### Delete a collection of elements

Use the same position filter to collect matching elements first, then pass that collection to Page::DeleteGraphics(). This version batches updates through the page Contents collection.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/) and call [Visit()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/visit/) on the first page.
1. Create a [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/) and an empty [GraphicElementCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelementcollection/).
1. Use [Rectangle::Contains()](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/contains/) to test each element position and add matching elements to the collection.
1. Call [OperatorCollection::SuppressUpdate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/operatorcollection/suppressupdate/) on the page Contents collection.
1. Remove the collected elements with [Page::DeleteGraphics()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/deletegraphics/).
1. Call [OperatorCollection::ResumeUpdate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/operatorcollection/resumeupdate/) on the page Contents collection.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Vector/GraphicsAbsorber.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElement.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElementCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

void RemoveGraphicsMethod2(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto graphicsAbsorber = MakeObject<GraphicsAbsorber>();
    auto page = document->get_Pages()->idx_get(1);
    auto rectangle = MakeObject<Rectangle>(70, 248, 170, 252, true);
    graphicsAbsorber->Visit(page);
    auto removedElements = MakeObject<GraphicElementCollection>();
    for (auto element : graphicsAbsorber->get_Elements())
    {
        if (rectangle->Contains(element->get_Position(), false))
        {
            removedElements->Add(element);
        }
    }
    page->get_Contents()->SuppressUpdate();
    page->DeleteGraphics(removedElements);
    page->get_Contents()->ResumeUpdate();
    document->Save(outputFile);
}
```

## Copy vector graphics to another page

### Add elements individually

Append a new page to the same document and copy each graphic element from the first page with AddOnPage(). The new page is not necessarily page 2 when the input already contains multiple pages. The example copies the extracted graphics rather than the entire source page.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first page and append a destination page with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/) and call [Visit()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/visit/) on the first page.
1. Call [OperatorCollection::SuppressUpdate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/operatorcollection/suppressupdate/) on the destination page Contents collection.
1. Iterate through the extracted elements and call [GraphicElement::AddOnPage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/addonpage/) for the destination page.
1. Call [OperatorCollection::ResumeUpdate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/operatorcollection/resumeupdate/) on the destination page Contents collection.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Vector/GraphicsAbsorber.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElement.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElementCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

void AddToAnotherPageMethod1(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto graphicsAbsorber = MakeObject<GraphicsAbsorber>();
    auto page1 = document->get_Pages()->idx_get(1);
    auto page2 = document->get_Pages()->Add();
    graphicsAbsorber->Visit(page1);
    page2->get_Contents()->SuppressUpdate();
    for (auto element : graphicsAbsorber->get_Elements())
    {
        element->AddOnPage(page2);
    }
    page2->get_Contents()->ResumeUpdate();
    document->Save(outputFile);
}
```

### Add the element collection

Append a new page and pass the extracted graphic element collection to AddGraphics(). This provides a collection-based alternative to calling AddOnPage() for each element.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Append a destination page with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/) and call [Visit()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/visit/) on the first page.
1. Call [OperatorCollection::SuppressUpdate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/operatorcollection/suppressupdate/) on the destination page Contents collection.
1. Copy the extracted collection with [Page::AddGraphics()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addgraphics/).
1. Call [OperatorCollection::ResumeUpdate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/operatorcollection/resumeupdate/) on the destination page Contents collection.
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/OperatorCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Vector/GraphicsAbsorber.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElementCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

void AddToAnotherPageMethod2(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto graphicsAbsorber = MakeObject<GraphicsAbsorber>();
    auto page1 = document->get_Pages()->idx_get(1);
    auto page2 = document->get_Pages()->Add();
    graphicsAbsorber->Visit(page1);
    page2->get_Contents()->SuppressUpdate();
    page2->AddGraphics(graphicsAbsorber->get_Elements());
    page2->get_Contents()->ResumeUpdate();
    document->Save(outputFile);
}
```
