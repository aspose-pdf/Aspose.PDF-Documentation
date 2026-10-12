---
title: Set tagged PDF structure element properties in C++
linktitle: Setting Structure Elements Properties
type: docs
weight: 30
url: /cpp/setting-structure-elements-properties/
description: Set tagged PDF structure properties in C++, including text, language, alternative descriptions, links, notes, and custom tag names.
lastmod: "2026-10-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Configure the content and accessibility metadata of tagged PDF structure elements with Aspose.PDF for C++. This page covers headings, paragraphs, inline spans, links, notes, and custom tags.

## Set common structure element properties

Add accessibility metadata to a heading nested inside a section.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a section with [CreateSectElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append it to the root.
1. Create a level-one heading and append it to the section.
1. Set the heading text.
1. Set the title, language, alternative text, expansion text, and actual text on the [StructureElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/structureelement/).
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/GroupingElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void SetProperties(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    auto rootElement = taggedContent->get_RootElement();
    auto sectionElement = taggedContent->CreateSectElement();
    rootElement->AppendChild(sectionElement, true);

    auto headerElement = taggedContent->CreateHeaderElement(1);
    sectionElement->AppendChild(headerElement, true);
    headerElement->SetText(u"The Header");

    headerElement->set_Title(u"Title");
    headerElement->set_Language(u"en-US");
    headerElement->set_AlternativeText(u"Alternative Text");
    headerElement->set_ExpansionText(u"Expansion Text");
    headerElement->set_ActualText(u"Actual Text");

    document->Save(outputFile);
}
```

## Create a text paragraph

Add a tagged paragraph with text to the document root.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a paragraph with [CreateParagraphElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Set the paragraph text and append it to the root.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void SetTextElements(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    auto paragraphElement = taggedContent->CreateParagraphElement();
    paragraphElement->SetText(u"Paragraph.");
    taggedContent->get_RootElement()->AppendChild(paragraphElement, true);

    document->Save(outputFile);
}
```

## Create headings and block text

Build headings at levels one through six followed by a paragraph.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create headings for levels 1 through 6 with [CreateHeaderElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Set each heading text and append it to the root.
1. Create a paragraph, set its text, and append it to the root.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void SetTextBlockElements(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    for (int level = 1; level <= 6; level++) {
        auto header = taggedContent->CreateHeaderElement(level);
        header->SetText(String::Format(u"H{0}. Header of Level {1}", level, level));
        taggedContent->get_RootElement()->AppendChild(header, true);
    }

    auto p = taggedContent->CreateParagraphElement();
    p->SetText(u"P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet.");
    taggedContent->get_RootElement()->AppendChild(p, true);

    document->Save(outputFile);
}
```

## Create inline spans

Compose headings and paragraphs from inline span elements.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create headings at levels 1 through 6.
1. Create two spans for each heading with [CreateSpanElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append them to the heading.
1. Create a paragraph and append it to the root.
1. Create ten spans, set their text, and append them to the paragraph.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/ILSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void SetInlineElements(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    for (int level = 1; level <= 6; level++) {
        auto header = taggedContent->CreateHeaderElement(level);
        taggedContent->get_RootElement()->AppendChild(header, true);

        auto span1 = taggedContent->CreateSpanElement();
        span1->SetText(String::Format(u"H{0}. ", level));
        header->AppendChild(span1, true);

        auto span2 = taggedContent->CreateSpanElement();
        span2->SetText(String::Format(u"Level {0} Header", level));
        header->AppendChild(span2, true);
    }

    auto paragraphElement = taggedContent->CreateParagraphElement();
    paragraphElement->SetText(u"P. ");
    taggedContent->get_RootElement()->AppendChild(paragraphElement, true);

    for (int index = 1; index <= 10; index++) {
        auto span = taggedContent->CreateSpanElement();
        span->SetText(String::Format(u"Span {0}. ", index));
        paragraphElement->AppendChild(span, true);
    }

    document->Save(outputFile);
}
```

## Create text and image links

Add links with alternate descriptions and an image link with a layout attribute.

Supply an existing image file. The example includes a multiline text link.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create paragraphs and add [LinkElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/linkelement/) objects with [CreateLinkElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Assign each link a WebHyperlink, link text, and alternate description.
1. Create another link and load an image into a [FigureElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/figureelement/).
1. Set the figure alternative text.
1. Create a [StructureAttribute](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/structureattribute/) for block placement and assign it to the link layout attributes.
1. Append the figure to the link and set the link alternate description.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/WebHyperlink.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/AttributeName.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/ILSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/IllustrationElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureAttribute.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureAttributeCollection.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureAttributes.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void SetElements(System::String imageFile, System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Link Elements Example");
    taggedContent->SetLanguage(u"en-US");

    for (int index = 1; index <= 4; index++) {
        auto paragraph = taggedContent->CreateParagraphElement();
        taggedContent->get_RootElement()->AppendChild(paragraph, true);

        auto link = taggedContent->CreateLinkElement();
        paragraph->AppendChild(link, true);
        link->set_Hyperlink(MakeObject<WebHyperlink>(u"http://google.com"));
        link->SetText(index == 4 ? u"The multiline link: Google Google Google Google" : u"Google");
        link->set_AlternateDescriptions(u"Link to Google");
    }

    auto paragraph = taggedContent->CreateParagraphElement();
    taggedContent->get_RootElement()->AppendChild(paragraph, true);

    auto link = taggedContent->CreateLinkElement();
    paragraph->AppendChild(link, true);
    link->set_Hyperlink(MakeObject<WebHyperlink>(u"http://google.com"));

    auto figure = taggedContent->CreateFigureElement();
    figure->SetImage(imageFile, 1200);
    figure->set_AlternativeText(u"Google icon");

    auto linkLayoutAttributes = link->get_Attributes()->GetAttributes(AttributeOwnerStandard::Layout());
    auto placementAttribute = MakeObject<StructureAttribute>(AttributeKey::Placement);
    placementAttribute->SetNameValue(AttributeName::Placement_Block);
    linkLayoutAttributes->SetAttribute(placementAttribute);

    link->AppendChild(figure, true);
    link->set_AlternateDescriptions(u"Link to Google");

    document->Save(outputFile);
}
```

## Compose paragraphs from spans

Append inline spans to paragraphs to build their text content.

Despite its function name AddLinkElement, this example creates spans. It does not create hyperlinks; see the preceding link example.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create four paragraphs with [CreateParagraphElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create two spans for each paragraph with [CreateSpanElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Set the paragraph prefix and the span text.
1. Append both spans to the paragraph.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/ILSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void AddLinkElement(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Text Elements Example");
    taggedContent->SetLanguage(u"en-US");

    for (int paragraphIndex = 1; paragraphIndex <= 4; paragraphIndex++) {
        auto paragraph = taggedContent->CreateParagraphElement();
        taggedContent->get_RootElement()->AppendChild(paragraph, true);

        auto span1 = taggedContent->CreateSpanElement();
        span1->SetText(String::Format(u"Span_{0}1", paragraphIndex));
        auto span2 = taggedContent->CreateSpanElement();
        span2->SetText(String::Format(u" and Span_{0}2.", paragraphIndex));

        paragraph->SetText(u"Paragraph with ");
        paragraph->AppendChild(span1, true);
        paragraph->AppendChild(span2, true);
    }

    document->Save(outputFile);
}
```

## Add notes with identifiers

Create note elements with automatically generated and explicit IDs.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a paragraph and append it to the root.
1. Create three notes with [CreateNoteElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append them to the paragraph.
1. Set the note text.
1. Keep the generated ID for the first note and assign explicit IDs to the other notes with [SetId()](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/structureelement/).
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Note.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/ILSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void SetNoteElement(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Sample of Note Elements");
    taggedContent->SetLanguage(u"en-US");

    auto paragraph = taggedContent->CreateParagraphElement();
    taggedContent->get_RootElement()->AppendChild(paragraph, true);

    auto note1 = taggedContent->CreateNoteElement();
    paragraph->AppendChild(note1, true);
    note1->SetText(u"Note with auto generate ID. ");

    auto note2 = taggedContent->CreateNoteElement();
    paragraph->AppendChild(note2, true);
    note2->SetText(u"Note with ID = 'note_002'. ");
    note2->SetId(u"note_002");

    auto note3 = taggedContent->CreateNoteElement();
    paragraph->AppendChild(note3, true);
    note3->SetText(u"Note with ID = 'note_003'. ");
    note3->SetId(u"note_003");

    document->Save(outputFile);
}
```

## Set custom tag names

Assign custom tags to paragraphs and spans within a section.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a section with [CreateSectElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append it to the root.
1. Create paragraph and span elements and set their text.
1. Assign the sample custom names with [SetTag()](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/structureelement/).
1. Append each span to its paragraph and each paragraph to the section.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/GroupingElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/ILSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void SetTagName(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    auto sectionElement = taggedContent->CreateSectElement();
    taggedContent->get_RootElement()->AppendChild(sectionElement, true);

    const String paragraphTags[] = {u"P1", u"Para", u"Para", u"Paragraph"};
    const String spanTags[] = {u"SPAN", u"Sp", u"Sp", u"TheSpan"};

    for (int index = 0; index < 4; index++) {
        auto paragraph = taggedContent->CreateParagraphElement();
        paragraph->SetText(String::Format(u"P{0}. ", index + 1));
        paragraph->SetTag(paragraphTags[index]);

        auto span = taggedContent->CreateSpanElement();
        span->SetText(String::Format(u"Span {0}.", index + 1));
        span->SetTag(spanTags[index]);

        paragraph->AppendChild(span, true);
        sectionElement->AppendChild(paragraph, true);
    }

    document->Save(outputFile);
}
```
