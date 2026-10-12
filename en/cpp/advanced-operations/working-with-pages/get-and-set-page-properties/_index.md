---
title: Inspect PDF page properties in C++
linktitle: Get and Set Page Properties
type: docs
weight: 70
url: /cpp/get-and-set-page-properties/
description: Inspect page counts, page boxes, rotation, and color types, and calculate a generated document's page count before saving with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Inspect page counts, page boxes, rotation, and color types, and calculate a generated document's page count before saving with Aspose.PDF for C++.

## Inspect page boxes and rotation

The example uses C++17 structured bindings. For changes to page properties, see the page-size, cropping, and rotation guides in this section.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select the first [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Read ArtBox, BleedBox, CropBox, MediaBox, TrimBox, and Rect.
1. Print each [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/) size and coordinates.
1. Print the page number and rotation.

```cpp

#include <iostream>
#include <utility>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of GetAndSetPagePropertiesExamples.getPageProperties.
void GetPageProperties(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    const std::pair<const char*, SharedPtr<Rectangle>> boxes[] = {
        {"ArtBox", page->get_ArtBox()},
        {"BleedBox", page->get_BleedBox()},
        {"CropBox", page->get_CropBox()},
        {"MediaBox", page->get_MediaBox()},
        {"TrimBox", page->get_TrimBox()},
        {"Rect", page->get_Rect()},
    };
    for (const auto& [name, box] : boxes) {
        std::cout << name << " : Height=" << box->get_Height()
        << ",Width=" << box->get_Width()
        << ",LLX=" << box->get_LLX() << ",LLY=" << box->get_LLY()
        << ",URX=" << box->get_URX() << ",URY=" << box->get_URY() << std::endl;
    }
    std::cout << "Page Number : " << page->get_Number() << std::endl;
    std::cout << "Rotate : " << static_cast<int>(page->get_Rotate()) << std::endl;
}
```

## Read the page count

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Read Count from [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/).
1. Print the page count.

```cpp

#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of GetAndSetPagePropertiesExamples.getPageCount.
void GetPageCount(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);

    std::cout << "Page Count: " << document->get_Pages()->get_Count() << std::endl;
}
```

## Calculate page count before saving

This creates a document in memory and does not require an input PDF or save an output file.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Add 300 [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) paragraphs.
1. Call [ProcessParagraphs()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/processparagraphs/) to lay out the generated content.
1. Read and print the [PageCollection](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/) count.

```cpp

#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

// Port of GetAndSetPagePropertiesExamples.getPageCountWithoutSaving.
void GetPageCountWithoutSaving()
{
    auto document = MakeObject<Document>();

    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 300; i++) {
        page->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Pages count test"));
    }
    document->ProcessParagraphs();
    std::cout << "Number of pages in document = " << document->get_Pages()->get_Count() << std::endl;
}
```

## Inspect page color types

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through every [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Read ColorType and compare it with the [ColorType](https://reference.aspose.com/pdf/cpp/aspose.pdf/colortype/) enumeration.
1. Print the classification for each page.

```cpp

#include <iostream>
#include <Aspose.PDF.Cpp/ColorType.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of GetAndSetPagePropertiesExamples.getPageColorType.
void GetPageColorType(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (int pageNumber = 1; pageNumber <= document->get_Pages()->get_Count(); ++pageNumber) {
        auto colorType = document->get_Pages()->idx_get(pageNumber)->get_ColorType();
        const char* description = "undefined";
        switch (colorType) {
            case ColorType::BlackAndWhite: description = "Black and white"; break;
            case ColorType::Grayscale: description = "Gray Scale"; break;
            case ColorType::Rgb: description = "RGB"; break;
            case ColorType::Undefined: break;
        }
        std::cout << "Page # " << pageNumber << " is " << description << "." << std::endl;
    }
}
```
