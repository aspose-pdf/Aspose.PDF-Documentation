---
title: Create a PDF with images, text, and a table in C++
linktitle: Creating a complex PDF
type: docs
weight: 30
url: /cpp/complex-pdf-example/
description: Build a PDF containing an image, styled heading and paragraph, and a two-column table using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combine Images, Styled Text, and Tables in a C++ PDF
Abstract: Create a PDF with an image, a centered heading, descriptive text, and a formatted timetable using Aspose.PDF for C++. The example configures table borders, cell padding, header colors, and ten rows of sample departure times.
---

The ComplexExample function combines an image, a heading, descriptive text, and a two-column table in a new PDF. Its ferry heading and departure times are sample content.

Configure the Aspose.PDF for C++ SDK and make Arial, Times New Roman, and Helvetica available. Supply an image path as imageFile and a writable PDF path as outputFile.

## Build the document content

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Add imageFile with [Page::AddImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addimage/) using the [Rectangle](https://reference.aspose.com/pdf/cpp/aspose.pdf/rectangle/) (20, 730, 120, 830).
1. Create a heading [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) with Arial at 24 points, centered alignment, and the source position (130, 720).
1. Add the heading to the page [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Create the description [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) with Times New Roman at 14 points and left alignment, then add it to the page.
1. Create a [Table](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) with two columns, each 200 units wide.
1. Configure the table and cell borders with [BorderInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/borderinfo/), padding with [MarginInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/margininfo/), and the default cell font through [FontRepository](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/).
1. Add a header row through [Rows::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/rows/add/) with Departs City and Departs Island cells, gray backgrounds, and WhiteSmoke text.
1. Add ten data rows through [Rows](https://reference.aspose.com/pdf/cpp/aspose.pdf/rows/) and [Cells](https://reference.aspose.com/pdf/cpp/aspose.pdf/cells/), starting at 06:00 and advancing 30 minutes after each cell.
1. Add the table to the page [Paragraphs](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection.
1. Save the PDF with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>
#include <Aspose.PDF.Cpp/Text/Position.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ComplexExample(String imageFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    page->AddImage(imageFile, MakeObject<Rectangle>(20, 730, 120, 830));
    auto header = MakeObject<TextFragment>(u"New ferry routes in Fall 2029");
    header->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    header->get_TextState()->set_FontSize(24);
    header->set_HorizontalAlignment(HorizontalAlignment::Center);
    header->set_Position(MakeObject<Position>(130, 720));
    page->get_Paragraphs()->Add(header);
    auto description = MakeObject<TextFragment>(u"Visitors must buy tickets online and tickets are limited to 5,000 per day. "
        u"Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.");
    description->get_TextState()->set_Font(FontRepository::FindFont(u"Times New Roman"));
    description->get_TextState()->set_FontSize(14);
    description->set_HorizontalAlignment(HorizontalAlignment::Left);
    page->get_Paragraphs()->Add(description);
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200 200");
    table->set_Border(MakeObject<BorderInfo>(BorderSide::Box, 1.0f, Color::get_DarkSlateGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::Box, 0.5f, Color::get_Black()));
    table->set_DefaultCellPadding(MakeObject<MarginInfo>(4.5, 4.5, 4.5, 4.5));
    table->get_Margin()->set_Bottom(10);
    table->get_DefaultCellTextState()->set_Font(FontRepository::FindFont(u"Helvetica"));
    auto row = table->get_Rows()->Add();
    for (const auto& title : {u"Departs City", u"Departs Island"}) {
        auto cell = row->get_Cells()->Add(title);
        cell->set_BackgroundColor(Color::get_Gray());
        cell->get_DefaultCellTextState()->set_ForegroundColor(Color::get_WhiteSmoke());
    }
    int minutes = 6 * 60;
    for (int index = 0; index < 10; ++index) {
        row = table->get_Rows()->Add();
        for (int column = 0; column < 2; ++column, minutes += 30) {
            row->get_Cells()->Add(String::Format(u"{0:D2}:{1:D2}", minutes / 60, minutes % 60));
        }
    }
    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

After running ComplexExample(imageFile, outputFile), inspect the saved PDF to check image placement, text formatting, and the table layout.
