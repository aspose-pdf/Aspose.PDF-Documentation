---
title: Inspect tagged PDF content in C++
linktitle: Extract Tagged Content
type: docs
weight: 20
url: /cpp/extract-tagged-content-from-tagged-pdfs/
description: Access tagged PDF content in C++, inspect structure roots and child elements, and update accessibility metadata.
lastmod: "2026-10-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Access the tagged content container and inspect the logical structure of PDF documents with Aspose.PDF for C++. The examples show metadata initialization, structure root access, and inspection and modification of child elements.

## Get the tagged content container

Access tagged content and define the document metadata.

This example creates a new document; it does not extract text from an existing PDF.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void GetTaggedContent(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Simple Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");
    document->Save(outputFile);
}
```

## Access the structure roots

Retrieve the structure-tree root and the document root element.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Get the structure-tree root with [get_StructTreeRootElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Get the document root with [get_RootElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Print the string representations of both roots.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/Element.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/ElementList.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructTreeRootElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void GetRootStructure(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    std::cout << "StructTreeRootElement: " << taggedContent->get_StructTreeRootElement()->ToString() << std::endl;
    std::cout << "RootElement: " << taggedContent->get_RootElement()->ToString() << std::endl;

    document->Save(outputFile);
}
```

## Inspect and update child elements

Read accessibility properties from an existing structure tree and update nested elements.

The sample assumes that the root contains a child at index 1. Inspect the input structure before applying the same indexing to another document.

1. Open the tagged input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Read the structure-tree root children with [get_ChildElements()](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/element/).
1. Cast each applicable child to [StructureElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/structureelement/) and print its title, language, actual text, expansion text, and alternative text.
1. Select the root child at index 1 and iterate through its children.
1. Update the metadata of each applicable child.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/Element.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/ElementList.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructTreeRootElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void AccessChildElements(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto taggedContent = document->get_TaggedContent();

    auto elementList = taggedContent->get_StructTreeRootElement()->get_ChildElements();
    for (const auto& element : elementList) {
        if (auto structureElement = System::DynamicCast_noexcept<StructureElement>(element)) {
            std::cout << "StructureElement properties - "
            << "title: " << structureElement->get_Title()
            << ", language: " << structureElement->get_Language()
            << ", actual_text: " << structureElement->get_ActualText()
            << ", expansion_text: " << structureElement->get_ExpansionText()
            << ", alternative_text: " << structureElement->get_AlternativeText() << std::endl;
        }
    }

    auto firstChild = taggedContent->get_RootElement()->get_ChildElements()->idx_get(1);
    for (const auto& element : firstChild->get_ChildElements()) {
        if (auto structureElement = System::DynamicCast_noexcept<StructureElement>(element)) {
            structureElement->set_Title(u"title");
            structureElement->set_Language(u"fr-FR");
            structureElement->set_ActualText(u"actual text");
            structureElement->set_ExpansionText(u"exp");
            structureElement->set_AlternativeText(u"alt");
        }
    }

    document->Save(outputFile);
}
```
