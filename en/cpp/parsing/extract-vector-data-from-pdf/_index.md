---
title: Extract vector graphics from PDF in C++
linktitle: Extract Vector Data from PDF
type: docs
weight: 80
url: /cpp/extract-vector-data-from-pdf/
description: Inspect vector graphics properties and export page or element graphics to SVG with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Inspect vector graphics properties and export page or element graphics to SVG with Aspose.PDF for C++.

## Inspect graphics elements

Write bounds, positions, and operator counts for graphics detected on page 1.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/) and visit page 1.
1. Iterate through its [GraphicElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/) collection.
1. Read Rectangle, Position, and the operator count.
1. Write the report to the output file.

Source example: `vector-01.cpp`.

```cpp
#include <system/io/file.h>
#include <system/io/memory_stream.h>
#include <system/text/string_builder.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Vector/GraphicsAbsorber.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElementCollection.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElement.h>

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

void ExtractGraphicsElements(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<GraphicsAbsorber>();
    absorber->Visit(document->get_Pages()->idx_get(1));

    auto text = MakeObject<System::Text::StringBuilder>();
    int index = 1;
    for (auto& element : absorber->get_Elements()) {
        text->Append(u"Element ")->Append(index)
            ->Append(u": Rectangle = ")
            ->Append(element->get_Rectangle())
            ->Append(u", Position = ")
            ->Append(element->get_Position())
            ->Append(u", Operators = ")
            ->Append(element->get_Operators()->get_Count())
            ->Append(u"\n");
        index++;
    }
    System::IO::File::WriteAllText(outputFile, text->ToString());
}
```

## Save page vector graphics as SVG

Attempt to export the vector graphics from page 1.

The example does not inspect the method return value. Check whether export succeeded before using the output.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Call [TrySaveVectorGraphics()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) with the output path.

Source example: `vector-02.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

void SaveVectorGraphicsToSvg(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    page->TrySaveVectorGraphics(outputFile);
}
```

## Save graphics elements as separate SVG files

Export each absorbed graphics element to a file in a subpaths directory.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Visit page 1 with [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/).
1. Create the subpaths output directory.
1. Iterate through the [GraphicElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/) collection.
1. Call [SaveToSvg()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/) with a unique subpath_N.svg file name.

Source example: `vector-03.cpp`.

```cpp
#include <system/io/directory.h>
#include <system/io/path.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Vector/GraphicsAbsorber.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElementCollection.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElement.h>

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

void ExtractSubpathsToSvgs(System::String inputFile, System::String outputDir)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<GraphicsAbsorber>();
    absorber->Visit(document->get_Pages()->idx_get(1));
    auto subpathsDir = System::IO::Path::Combine(outputDir, u"subpaths");
    System::IO::Directory::CreateDirectory_(subpathsDir);

    int index = 1;
    for (auto& element : absorber->get_Elements()) {
        element->SaveToSvg(System::IO::Path::Combine(subpathsDir, u"subpath_" + System::ObjectExt::ToString(index) + u".svg"));
        index++;
    }
}
```

## Combine graphics elements into one SVG

Build an SVG document from the serialized content of absorbed elements.

The helper checks for missing SVG tags but is a string-based extraction helper. It does not merge wrapper attributes or resolve namespace and ID conflicts.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Visit page 1 with [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/).
1. Create an SVG root element in a StringBuilder.
1. Serialize each [GraphicElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/) with [SaveToSvg()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/).
1. Use extractSvgContent() to strip its outer SVG wrapper.
1. Append the inner content, close the SVG root, and write the output file.

Source example: `vector-04.cpp`.

```cpp
#include <system/io/file.h>
#include <system/text/string_builder.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Vector/GraphicsAbsorber.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElementCollection.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElement.h>

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

String extractSvgContent(String svgData);
void ExtractListOfElementsToSingleImage(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<GraphicsAbsorber>();
    absorber->Visit(document->get_Pages()->idx_get(1));

    auto svg = MakeObject<System::Text::StringBuilder>();

    svg->Append(u"<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
    for (auto& element : absorber->get_Elements()) {
        auto svgData = element->SaveToSvg();
        auto svgContent = extractSvgContent(svgData);
        svg->Append(svgContent)->Append(u"\n");
    }
    svg->Append(u"</svg>\n");
    System::IO::File::WriteAllText(outputFile, svg->ToString());
}

String extractSvgContent(String svgData) {
    if (svgData == String::Empty) {
        throw std::invalid_argument("SVG content must not be empty");
    }

    auto openingTagStart = svgData->IndexOf(u"<svg");
    if (openingTagStart < 0) {
        throw std::invalid_argument("SVG opening tag was not found");
    }

    auto openingTagEnd = svgData->IndexOf('>', openingTagStart);
    if (openingTagEnd < 0) {
        throw std::invalid_argument("SVG opening tag is not closed");
    }

    if (svgData->Substring(openingTagStart, openingTagEnd - openingTagStart).TrimEnd()->EndsWith(u"/")) {
        return String::Empty;
    }

    auto closingTagStart = svgData->LastIndexOf(u"</svg>");
    if (closingTagStart < openingTagEnd) {
        throw std::invalid_argument("SVG closing tag was not found");
    }

    return svgData->Substring(openingTagEnd + 1, closingTagStart - openingTagEnd - 1);
}
```

## Save a selected vector element

Export an element selected by collection index, optionally from an XForm placement.

The function may produce no output when the requested elements are absent. These collection indices are independent of the one-based page indices.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Visit page 1 with [GraphicsAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicsabsorber/).
1. Check that the graphics collection contains more than one element.
1. Select the element at index 1.
1. If it is an [XFormPlacement](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/xformplacement/), export its nested element at index 2 when present.
1. Otherwise, export the selected [GraphicElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/) with [SaveToSvg()](https://reference.aspose.com/pdf/cpp/aspose.pdf.vector/graphicelement/).

Source example: `vector-05.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Vector/GraphicsAbsorber.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElementCollection.h>
#include <Aspose.PDF.Cpp/Vector/Model/GraphicElement.h>
#include <Aspose.PDF.Cpp/Vector/Model/XFormPlacement.h>

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Vector;

void ExtractSingleVectorElement(System::String inputFile, System::String outputFile) {
    auto document = MakeObject<Document>(inputFile);
    auto graphicsAbsorber = MakeObject<GraphicsAbsorber>();
    auto page = document->get_Pages()->idx_get(1);

    graphicsAbsorber->Visit(page);
    if (graphicsAbsorber->get_Elements()->get_Count() > 1) {
        auto xformPlacement = graphicsAbsorber->get_Elements()->idx_get(1);
        if (xformPlacement->Is(XFormPlacement::Type())) {
            auto placement = System::DynamicCast<XFormPlacement>(xformPlacement);
            if (placement->get_Elements()->get_Count() > 2) {
                placement->get_Elements()->idx_get(2)->SaveToSvg(outputFile);
            }
        }
        else {
            xformPlacement->SaveToSvg(outputFile);
        }
    }
}
```
