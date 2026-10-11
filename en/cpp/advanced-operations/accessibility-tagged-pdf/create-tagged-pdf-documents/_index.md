---
title: Create tagged PDF documents in C++
linktitle: Create Tagged PDF
type: docs
weight: 10
url: /cpp/create-tagged-pdf/
description: Create tagged PDFs in C++ with headings, figures, forms, tables of contents, automatic tagging, and PDF/UA validation.
lastmod: "2026-10-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Use Aspose.PDF for C++ to build a logical structure tree for PDF content, set language and title metadata, and associate visible content with structure elements. This page covers tagged document creation, text styling, images, form fields, tables of contents, automatic tagging, and validation.

## Create a simple tagged PDF

Build a document with a heading and paragraph in the logical structure tree.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a heading and paragraph with [CreateHeaderElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [CreateParagraphElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Set their text and attach them to [get_RootElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [AppendChild()](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/element/).
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

void CreateTaggedPdfDocumentSimple(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    auto rootElement = taggedContent->get_RootElement();

    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    auto mainHeader = taggedContent->CreateHeaderElement();
    mainHeader->SetText(u"Main Header");

    auto paragraphElement = taggedContent->CreateParagraphElement();
    paragraphElement->SetText(u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo.");

    rootElement->AppendChild(mainHeader, true);
    rootElement->AppendChild(paragraphElement, true);
    document->Save(outputFile);
}
```

## Create a tagged PDF with inline quotes

Combine spans and an emphasized quotation inside a paragraph.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a level-one heading and a paragraph.
1. Set the paragraph font and margins.
1. Create inline spans and a quotation with [CreateSpanElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [CreateQuoteElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Apply bold and italic formatting to the quote through [StructureTextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/structuretextstate/).
1. Append the inline elements to the paragraph, then append the heading and paragraph to the root.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/ILSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureTextState.h>
#include <Aspose.PDF.Cpp/Tagged/PositionSettings.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;
using namespace Aspose::Pdf::Text;

void CreateTaggedPdfDocumentAdv(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    auto rootElement = taggedContent->get_RootElement();

    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    auto header1 = taggedContent->CreateHeaderElement(1);
    header1->SetText(u"Header Level 1");

    auto paragraphWithQuotes = taggedContent->CreateParagraphElement();
    paragraphWithQuotes->get_StructureTextState()->set_Font(FontRepository::FindFont(u"Arial"));

    auto positionSettings = MakeObject<PositionSettings>();
    positionSettings->set_Margin(MakeObject<MarginInfo>(10, 5, 10, 5));
    paragraphWithQuotes->AdjustPosition(positionSettings);

    auto spanElement1 = taggedContent->CreateSpanElement();
    spanElement1->SetText(u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. ");

    auto quoteElement = taggedContent->CreateQuoteElement();
    quoteElement->SetText(u"Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus.");
    quoteElement->get_StructureTextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);

    auto spanElement2 = taggedContent->CreateSpanElement();
    spanElement2->SetText(u" Sed non consectetur elit.");

    paragraphWithQuotes->AppendChild(spanElement1, true);
    paragraphWithQuotes->AppendChild(quoteElement, true);
    paragraphWithQuotes->AppendChild(spanElement2, true);

    rootElement->AppendChild(header1, true);
    rootElement->AppendChild(paragraphWithQuotes, true);
    document->Save(outputFile);
}
```

## Set document and element languages

Define document metadata and identify the language of each multilingual paragraph.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a level-one heading.
1. Create paragraphs containing English, German, French, and Spanish text.
1. Set the language on each [StructureElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/structureelement/) and append it to the root.
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

void SetLanguageAndTitle(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Example Tagged Document");
    taggedContent->SetLanguage(u"en-US");

    auto header = taggedContent->CreateHeaderElement(1);
    header->SetText(u"Phrase on different languages");
    taggedContent->get_RootElement()->AppendChild(header, true);

    {
        auto paragraph = taggedContent->CreateParagraphElement();
        paragraph->SetText(u"Hello, World!");
        paragraph->set_Language(u"en-US");
        taggedContent->get_RootElement()->AppendChild(paragraph, true);
    }
    {
        auto paragraph = taggedContent->CreateParagraphElement();
        paragraph->SetText(u"Hallo Welt!");
        paragraph->set_Language(u"de-DE");
        taggedContent->get_RootElement()->AppendChild(paragraph, true);
    }
    {
        auto paragraph = taggedContent->CreateParagraphElement();
        paragraph->SetText(u"Bonjour le monde!");
        paragraph->set_Language(u"fr-FR");
        taggedContent->get_RootElement()->AppendChild(paragraph, true);
    }
    {
        auto paragraph = taggedContent->CreateParagraphElement();
        paragraph->SetText(u"Hola Mundo!");
        paragraph->set_Language(u"es-ES");
        taggedContent->get_RootElement()->AppendChild(paragraph, true);
    }

    document->Save(outputFile);
}
```

## Style tagged text

Apply font size, color, and font style to a tagged paragraph.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a paragraph and append it to the root.
1. Set its [StructureTextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/structuretextstate/) to 18-point red italic text.
1. Set the paragraph text.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureTextState.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>

using namespace Aspose::Pdf::Text;
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void AddStyle(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();

    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    auto paragraphElement = taggedContent->CreateParagraphElement();
    taggedContent->get_RootElement()->AppendChild(paragraphElement, true);

    paragraphElement->get_StructureTextState()->set_FontSize(18.0f);
    paragraphElement->get_StructureTextState()->set_ForegroundColor(Color::get_Red());
    paragraphElement->get_StructureTextState()->set_FontStyle(FontStyles::Italic);
    paragraphElement->SetText(u"Red italic text.");

    document->Save(outputFile);
}
```

## Position a tagged paragraph

Adjust paragraph margins and layout flags through PositionSettings.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a paragraph, set its text, and append it to the root.
1. Create PositionSettings and configure margins, alignment, and pagination flags.
1. Apply the position settings with AdjustPosition().
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/PositionSettings.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void AdjustPosition(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();

    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    auto paragraph = taggedContent->CreateParagraphElement();
    taggedContent->get_RootElement()->AppendChild(paragraph, true);
    paragraph->SetText(u"Text.");

    auto positionSettings = MakeObject<PositionSettings>();
    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Left(300);
    marginInfo->set_Top(20);
    marginInfo->set_Right(0);
    marginInfo->set_Bottom(0);
    positionSettings->set_Margin(marginInfo);
    positionSettings->set_HorizontalAlignment(HorizontalAlignment::None);
    positionSettings->set_VerticalAlignment(VerticalAlignment::None);
    positionSettings->set_IsFirstParagraphInColumn(false);
    positionSettings->set_IsKeptWithNext(false);
    positionSettings->set_IsInNewPage(false);
    positionSettings->set_IsInLineParagraph(false);
    paragraph->AdjustPosition(positionSettings);

    document->Save(outputFile);
}
```

## Add a tagged figure

Insert an image with an alternative description, title, and custom tag.

Supply an existing image file. The sample descriptions are placeholders; replace them with descriptions of your image.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a [FigureElement](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/figureelement/) with [CreateFigureElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append it to the root.
1. Set the alternative text, title, and custom tag.
1. Load the image from imageFile with SetImage().
1. Configure the image margins and apply AdjustPosition().
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/IllustrationElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/PositionSettings.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void IllustrateStructureElements(System::String imageFile, System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();

    taggedContent->SetTitle(u"Tagged Pdf Document");
    taggedContent->SetLanguage(u"en-US");

    auto figure1 = taggedContent->CreateFigureElement();
    taggedContent->get_RootElement()->AppendChild(figure1, true);
    figure1->set_AlternativeText(u"Figure One");
    figure1->set_Title(u"Image 1");
    figure1->SetTag(u"Fig1");
    figure1->SetImage(imageFile, 300);

    auto positionSettings = MakeObject<PositionSettings>();
    auto marginInfo = MakeObject<MarginInfo>();
    marginInfo->set_Left(50);
    marginInfo->set_Top(20);
    positionSettings->set_Margin(marginInfo);
    figure1->AdjustPosition(positionSettings);

    document->Save(outputFile);
}
```

## Tag a signature form field

Associate a signature field with a form element in the structure tree.

This example creates a signature field; it does not sign the document.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Add a page and create a [SignatureField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/signaturefield/) within a rectangle.
1. Set its partial name and alternate name.
1. Add the field to the document form.
1. Create a form structure element with [CreateFormElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and set its alternative text.
1. Associate the field with the element using Tag() and append the element to the root.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/SignatureField.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/IllustrationElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;
using namespace Aspose::Pdf::Forms;

void CreatePdfWithTaggedFormField(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto taggedContent = document->get_TaggedContent();
    auto rootElement = taggedContent->get_RootElement();

    auto signatureField = MakeObject<SignatureField>(page, MakeObject<Rectangle>(50, 50, 100, 100, true));
    signatureField->set_PartialName(u"Signature1");
    signatureField->set_AlternateName(u"signature 1");

    auto formFields = document->get_Form();
    formFields->Add(System::StaticCast<Field>(signatureField));

    auto form = taggedContent->CreateFormElement();
    form->set_AlternativeText(u"form 1");
    form->Tag(signatureField);
    rootElement->AppendChild(form, true);

    document->Save(outputFile);
}
```

## Create a tagged table of contents

Connect a table-of-contents entry to a heading in the document structure.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document language with [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Add a TOC page and assign TocInfo.
1. Create a TOC structure element with [CreateTOCElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append it to the root.
1. Add a content page and a level-one heading.
1. Create a TOC item with [CreateTOCIElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/), add the heading entry to the TOC page, and reference the heading with AddRef().
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/TOCInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/GroupingElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void CreatePdfWithTocPage(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto content = document->get_TaggedContent();
    auto rootElement = content->get_RootElement();
    content->SetLanguage(u"en-US");

    auto tocPage = document->get_Pages()->Add();
    tocPage->set_TocInfo(MakeObject<TocInfo>());

    auto tocElement = content->CreateTOCElement();
    rootElement->AppendChild(tocElement, true);

    document->get_Pages()->Add();

    auto header = content->CreateHeaderElement(1);
    header->SetText(u"1. Header");
    rootElement->AppendChild(header, true);

    auto toci = content->CreateTOCIElement();
    tocElement->AppendChild(toci, true);
    header->AddEntryToTocPage(tocPage, toci);
    toci->AddRef(header);

    document->Save(outputFile);
}
```

## Create a table of contents with nested entries

Link a TOC title to a heading and include subheadings as nested list entries.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document language and create a TOC page with a visible title.
1. Create a TOC element and associate the page title with a header using LinkTocPageTitleToHeaderElement().
1. Add the first heading and its TOC item.
1. Create a list of subheading entries with [CreateListElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [CreateListLIElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Add each subheading to the TOC page and link its entry with AddRef().
1. Append the list to the first TOC item and add a second heading and TOC item.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/TOCInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/GroupingElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureTextState.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;
using namespace Aspose::Pdf::Text;

void CreatePdfWithTocPageAdvanced(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto content = document->get_TaggedContent();
    auto rootElement = content->get_RootElement();
    content->SetLanguage(u"en-US");

    auto tocPage = document->get_Pages()->Add();
    tocPage->set_TocInfo(MakeObject<TocInfo>());
    tocPage->get_TocInfo()->set_Title(MakeObject<TextFragment>(u"Table of Contents"));

    auto tocElement = content->CreateTOCElement();
    auto headerForTocPageTitle = content->CreateHeaderElement(1);
    tocElement->LinkTocPageTitleToHeaderElement(tocPage, headerForTocPageTitle);

    rootElement->AppendChild(headerForTocPageTitle, true);
    rootElement->AppendChild(tocElement, true);

    document->get_Pages()->Add();

    auto header = content->CreateHeaderElement(1);
    header->SetText(u"1. Header");
    rootElement->AppendChild(header, true);

    auto toci = content->CreateTOCIElement();
    tocElement->AppendChild(toci, true);
    header->AddEntryToTocPage(tocPage, toci);
    toci->AddRef(header);

    auto listElement = content->CreateListElement();
    for (int i = 1; i < 4; i++) {
        auto li = content->CreateListLIElement();
        listElement->AppendChild(li, true);

        auto subHeader = content->CreateHeaderElement(2);
        subHeader->get_StructureTextState()->set_FontSize(14.0f);
        subHeader->set_Language(u"en-US");
        subHeader->SetText(String::Format(u"1.{0} subheader ", i));
        subHeader->AddEntryToTocPage(tocPage, li);
        li->AddRef(subHeader);

        auto p = content->CreateParagraphElement();
        p->SetText(u"Lorem ipsum dolor sit amet, consectetur adipiscing elit.");
        p->set_Language(u"en-US");

        rootElement->AppendChild(subHeader, true);
        rootElement->AppendChild(p, true);
    }
    toci->AppendChild(listElement, true);

    auto header2 = content->CreateHeaderElement(1);
    header2->SetText(u"2. Header");
    rootElement->AppendChild(header2, true);

    auto toci2 = content->CreateTOCIElement();
    tocElement->AppendChild(toci2, true);
    header2->AddEntryToTocPage(tocPage, toci2);
    toci2->AddRef(header2);

    document->Save(outputFile);
}
```

## Convert to PDF/UA with automatic tagging

Enable automatic tagging when converting an existing PDF to PDF/UA-1.

The example uses ConvertErrorAction::Delete, which can remove objects that cannot be converted. Review the conversion log and validate the output; completion of the function does not establish PDF/UA conformance.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pdfformatconversionoptions/) with logFile, PDF_UA_1, and ConvertErrorAction::Delete.
1. Create [AutoTaggingSettings](https://reference.aspose.com/pdf/cpp/aspose.pdf/autotaggingsettings/), enable automatic tagging, and select automatic heading recognition.
1. Assign the tagging settings to the conversion options.
1. Call [Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/) and save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/AutoTaggingSettings.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/ConvertErrorAction.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <Aspose.PDF.Cpp/PdfFormatConversionOptions.h>
#include <Aspose.PDF.Cpp/PdfToMarkdown/MarkdownOptions/HeadingRecognitionStrategy.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void ConvertToPdfUaWithAutomaticTagging(System::String inputFile, System::String outputFile, System::String logFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto options = MakeObject<PdfFormatConversionOptions>(
    logFile, PdfFormat::PDF_UA_1, ConvertErrorAction::Delete);

    auto autoTaggingSettings = MakeObject<AutoTaggingSettings>();
    autoTaggingSettings->set_EnableAutoTagging(true);
    autoTaggingSettings->set_HeadingRecognitionStrategy(HeadingRecognitionStrategy::Auto);
    options->set_AutoTaggingSettings(autoTaggingSettings);

    document->Convert(options);
    document->Save(outputFile);
}
```

## Validate a tagged PDF against PDF/UA-1

Check an input document and write the validation report to a log file.

A false result indicates that the document did not pass validation. Writing a report or completing the function does not mean the input is compliant.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [Validate()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) with logFile and PdfFormat::PDF_UA_1.
1. Print the returned Boolean result.
1. Review the validation report for any reported failures.

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;

void ValidateTaggedPdf(System::String inputFile, System::String logFile)
{
    auto document = MakeObject<Document>(inputFile);
    bool isValid = document->Validate(logFile, PdfFormat::PDF_UA_1);
    std::cout << "Is Valid: " << isValid << std::endl;
}
```
