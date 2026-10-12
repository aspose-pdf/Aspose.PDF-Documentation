---
title: Add PDF headers and footers in C++
linktitle: Add Headers and Footers
type: docs
weight: 20
url: /cpp/add-headers-and-footers-of-pdf-file/
description: Add text, images, HTML, LaTeX, tables, and page-number placeholders to PDF headers and footers using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Add text, images, HTML, LaTeX, tables, and page-number placeholders to PDF headers and footers using Aspose.PDF for C++.

## Add text headers and footers

1. Create separate [HeaderFooter](https://reference.aspose.com/pdf/cpp/aspose.pdf/headerfooter/) objects for the header and footer.
1. Add a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) to each object.
1. Set margins with [MarginInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/margininfo/).
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Assign the header and footer to every [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `add-header-and-footer-as-text.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Generator/HeaderFooter.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

// Port of AddHeaderFooterExamples.addHeaderAndFooterAsText.
void AddHeaderAndFooterAsText(System::String inputFile, System::String outputFile)
{
    auto header = MakeObject<HeaderFooter>();
    header->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Demo header"));

    auto footer = MakeObject<HeaderFooter>();
    footer->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Demo footer"));

    auto margin = MakeObject<MarginInfo>();
    margin->set_Left(50);
    margin->set_Top(20);
    header->set_Margin(margin);
    footer->set_Margin(margin);

    auto document = MakeObject<Document>(inputFile);

    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        document->get_Pages()->idx_get(i)->set_Header(header);
        document->get_Pages()->idx_get(i)->set_Footer(footer);
    }
    document->Save(outputFile);
}
```

## Add image headers and footers

1. Create separate [Image](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/) objects using imageFile.
1. Add each image to a [HeaderFooter](https://reference.aspose.com/pdf/cpp/aspose.pdf/headerfooter/).
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Set the margins and assign the header and footer to every [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `add-header-and-footer-as-image.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/HeaderFooter.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of AddHeaderFooterExamples.addHeaderAndFooterAsImage.
void AddHeaderAndFooterAsImage(System::String inputFile, System::String imageFile, System::String outputFile)
{
    auto headerImage = MakeObject<Image>();
    headerImage->set_File(imageFile);
    auto header = MakeObject<HeaderFooter>();
    header->get_Paragraphs()->Add(headerImage);

    auto footerImage = MakeObject<Image>();
    footerImage->set_File(imageFile);
    auto footer = MakeObject<HeaderFooter>();
    footer->get_Paragraphs()->Add(footerImage);

    auto document = MakeObject<Document>(inputFile);

    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        auto margin = MakeObject<MarginInfo>();
        margin->set_Left(50);
        header->set_Margin(margin);
        footer->set_Margin(margin);
        document->get_Pages()->idx_get(i)->set_Header(header);
        document->get_Pages()->idx_get(i)->set_Footer(footer);
    }
    document->Save(outputFile);
}
```

## Add HTML headers and footers

The supplied README reports that this example compiled but threw from HtmlFragment::ConvertToPages during saving with SDK 26.7.0. The API usage is preserved; verify it with the SDK version you use.

1. Create two [HeaderFooter](https://reference.aspose.com/pdf/cpp/aspose.pdf/headerfooter/) objects.
1. Add [HtmlFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf/htmlfragment/) content to each and set margins.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Assign the header and footer to every [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `add-header-and-footer-as-html.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/HeaderFooter.h>
#include <Aspose.PDF.Cpp/Generator/HtmlFragment.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of AddHeaderFooterExamples.addHeaderAndFooterAsHtml.
// SDK 26.7.0 throws from HtmlFragment::ConvertToPages when saving this example.
void AddHeaderAndFooterAsHtml(System::String inputFile, System::String outputFile)
{
    auto header = MakeObject<HeaderFooter>();
    header->get_Paragraphs()->Add(MakeObject<HtmlFragment>(u"This is an HTML <strong>Header</strong>"));

    auto footer = MakeObject<HeaderFooter>();
    footer->get_Paragraphs()->Add(MakeObject<HtmlFragment>(u"Powered by <i>Aspose.PDF</i>"));

    auto margin = MakeObject<MarginInfo>();
    margin->set_Left(50);
    margin->set_Top(20);
    header->set_Margin(margin);
    footer->set_Margin(margin);

    auto document = MakeObject<Document>(inputFile);

    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        document->get_Pages()->idx_get(i)->set_Header(header);
        document->get_Pages()->idx_get(i)->set_Footer(footer);
    }
    document->Save(outputFile);
}
```

## Add LaTeX headers and footers

The footer includes the supplied literal year 2025 and interpolates the total page count. Preserve or adapt this sample content for your document.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Read the page count.
1. Create [HeaderFooter](https://reference.aspose.com/pdf/cpp/aspose.pdf/headerfooter/) objects containing [TeXFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf/texfragment/) content for each page.
1. Assign the header and footer to the [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `add-header-and-footer-as-latex.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/HeaderFooter.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/TeXFragment.h>

using namespace System;
using namespace Aspose::Pdf;

// Port of AddHeaderFooterExamples.addHeaderAndFooterAsLatex.
void AddHeaderAndFooterAsLatex(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);

    int pageCount = document->get_Pages()->get_Count();
    for (int i = 1; i <= pageCount; i++) {
        auto header = MakeObject<HeaderFooter>();
        header->get_Paragraphs()->Add(MakeObject<TeXFragment>(u"This is a LaTeX Header. \\today\\", true));

        auto footer = MakeObject<HeaderFooter>();
        footer->get_Paragraphs()->Add(MakeObject<TeXFragment>(String::Format(u"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {0}", pageCount), true));

        document->get_Pages()->idx_get(i)->set_Header(header);
        document->get_Pages()->idx_get(i)->set_Footer(footer);
    }
    document->Save(outputFile);
}
```

## Add table headers and footers

Column widths use the sample's fixed value 594 and the header or footer margins. Adjust them for different page sizes.

1. Configure header and footer [TextState](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/) objects using Arial from [FontRepository](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/).
1. Create [HeaderFooter](https://reference.aspose.com/pdf/cpp/aspose.pdf/headerfooter/) objects and add a [Table](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) to each.
1. Populate the tables with header and footer text and set margins.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Assign the header and footer to every [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `add-header-and-footer-as-table.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Generator/HeaderFooter.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

// Port of AddHeaderFooterExamples.addHeaderAndFooterAsTable.
void AddHeaderAndFooterAsTable(System::String inputFile, System::String outputFile)
{
    auto textStateHeader = MakeObject<TextState>();
    textStateHeader->set_Font(FontRepository::FindFont(u"Arial"));
    textStateHeader->set_FontSize(12);
    textStateHeader->set_HorizontalAlignment(HorizontalAlignment::Center);

    auto textStateFooter = MakeObject<TextState>();
    textStateFooter->set_Font(FontRepository::FindFont(u"Arial"));
    textStateFooter->set_FontSize(12);
    textStateFooter->set_HorizontalAlignment(HorizontalAlignment::Left);

    auto header = MakeObject<HeaderFooter>();
    auto footer = MakeObject<HeaderFooter>();

    auto tableHeader = MakeObject<Table>();
    tableHeader->set_ColumnWidths(String::Format(u"{0}", 594 - header->get_Margin()->get_Left() - header->get_Margin()->get_Right()));
    tableHeader->get_Rows()->Add()->get_Cells()->Add(u"This is a Table Header", textStateHeader);

    auto table = MakeObject<Table>();
    table->set_ColumnWidths(String::Format(u"{0}", 594 - footer->get_Margin()->get_Left() - footer->get_Margin()->get_Right()));
    table->get_Rows()->Add()->get_Cells()->Add(u"Powered by Aspose.PDF", textStateFooter);

    header->get_Paragraphs()->Add(tableHeader);
    footer->get_Paragraphs()->Add(table);
    footer->get_Margin()->set_Left(150);

    auto document = MakeObject<Document>(inputFile);

    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        document->get_Pages()->idx_get(i)->set_Header(header);
        document->get_Pages()->idx_get(i)->set_Footer(footer);
    }
    document->Save(outputFile);
}
```

## Use page-number placeholders

1. Create [HeaderFooter](https://reference.aspose.com/pdf/cpp/aspose.pdf/headerfooter/) objects.
1. Add [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) content using $p for the page number and $P for the total page count.
1. Set the margins.
1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Assign the header and footer to every [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `using-header-and-footer-for-page-numbering.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Generator/HeaderFooter.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

// Port of AddHeaderFooterExamples.usingHeaderAndFooterForPageNumbering.
void UsingHeaderAndFooterForPageNumbering(System::String inputFile, System::String outputFile)
{
    auto header = MakeObject<HeaderFooter>();
    header->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Page $p from $P"));

    auto footer = MakeObject<HeaderFooter>();
    footer->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Page $p / $P"));

    auto margin = MakeObject<MarginInfo>();
    margin->set_Left(50);
    margin->set_Top(20);
    header->set_Margin(margin);
    footer->set_Margin(margin);

    auto document = MakeObject<Document>(inputFile);

    for (int i = 1; i <= document->get_Pages()->get_Count(); i++) {
        document->get_Pages()->idx_get(i)->set_Header(header);
        document->get_Pages()->idx_get(i)->set_Footer(footer);
    }
    document->Save(outputFile);
}
```
