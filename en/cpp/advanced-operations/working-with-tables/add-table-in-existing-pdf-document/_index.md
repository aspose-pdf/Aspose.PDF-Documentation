---
title: Add Tables to PDF in C++
linktitle: Adding Tables
type: docs
weight: 10
url: /cpp/adding-tables/
description: Create PDF tables with cell spans, images, borders, padding, and repeating headers in C++.
lastmod: "2026-11-23"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create and Format PDF Tables in C++
Abstract: Build tables with formatted cells, images, and LaTeX fragments. Control column sizing, page breaks, and repeating rows or columns.
---

## Creating basic tables

### Create a table

The generated PDF contains a three-column table with ten rows of sample text.

1. Create a [`Document`](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/), add a page, and create a [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/).
2. Use [`BorderInfo`](https://reference.aspose.com/pdf/cpp/aspose.pdf/borderinfo/) to set light gray borders for the table and its cells.
3. Add 10 rows with three text cells each through [`Rows`](https://reference.aspose.com/pdf/cpp/aspose.pdf/rows/) and [`Cells`](https://reference.aspose.com/pdf/cpp/aspose.pdf/cells/).
4. Add the table to the page's [`Paragraphs`](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>

using namespace System;
using namespace Aspose::Pdf;

void CreateTable(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 5, Color::get_LightGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 5, Color::get_LightGray()));
    for (int rowCount = 0; rowCount < 10; rowCount++)
    {
        auto row = table->get_Rows()->Add();
        row->get_Cells()->Add(String(u"Column (") + String::Format(u"{0}", rowCount) + String(u", 1)"));
        row->get_Cells()->Add(String(u"Column (") + String::Format(u"{0}", rowCount) + String(u", 2)"));
        row->get_Cells()->Add(String(u"Column (") + String::Format(u"{0}", rowCount) + String(u", 3)"));
    }
    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

### Add an image to a table cell

A two-column table displays the source file path alongside a 50-by-50-point image preview.

1. Create a two-column [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) and add a row.
2. Put the input image path in the first cell as a [`TextFragment`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).
3. Load the file into an [`Image`](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/), set its width and height to 50 points, and add it to the second cell's paragraphs.
4. Add the table to the page's [`Paragraphs`](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddImage(String inputFile, String outputFile)
{

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200 100");

    auto row = table->get_Rows()->Add();
    row->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>(inputFile));
    auto image = MakeObject<Image>();
    image->set_File(inputFile);
    image->set_FixWidth(50);
    image->set_FixHeight(50);
    row->get_Cells()->Add()->get_Paragraphs()->Add(image);

    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);

}
```

### Add SVG images to a table

Build an SVG catalog in a PDF by giving each file its own row with a path and a preview.

1. Pass the directory containing the three named SVG files as the input path.
2. Create a two-column [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) and add a row for each file.
3. Add the file path to the first cell and an [`Image`](https://reference.aspose.com/pdf/cpp/aspose.pdf/image/) with the `Svg` file type and fixed dimensions to the second cell.
4. Add the table to the page's [`Paragraphs`](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Image.h>
#include <Aspose.PDF.Cpp/Generator/ImageFileType.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <system/io/path.h>
#include <vector>
#include <initializer_list>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddSvgImage(String inputFile, String outputFile)
{
    std::vector<String> imageFiles;
    for (const auto &name : {u"genetic-algorithm-svgrepo-com.svg", u"genetic-research-svgrepo-com.svg",
                             u"gene-structure-svgrepo-com.svg"})
        imageFiles.push_back(System::IO::Path::Combine(inputFile, name));

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"200 100");
    for (const auto &imageFile : imageFiles)
    {
        auto row = table->get_Rows()->Add();
        row->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>(imageFile));
        auto image = MakeObject<Image>();
        image->set_FileType(ImageFileType::Svg);
        image->set_File(imageFile);
        image->set_FixWidth(50);
        image->set_FixHeight(50);
        row->get_Cells()->Add()->get_Paragraphs()->Add(image);
    }
    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

### Span rows and columns

One cell spans two columns, and another spans two rows, demonstrating both ways to merge cells.

1. Create a [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) with five rows and a four-column layout.
2. Use [`Cell::set_ColSpan()`](https://reference.aspose.com/pdf/cpp/aspose.pdf/cell/set_colspan/) to span two columns in the second row.
3. Use [`Cell::set_RowSpan()`](https://reference.aspose.com/pdf/cpp/aspose.pdf/cell/set_rowspan/) to span the fourth and fifth rows and skip the occupied column when filling the fifth row.
4. Add the table to the page's [`Paragraphs`](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>

using namespace System;
using namespace Aspose::Pdf;

void AddRowspanOrColspan(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 0.5f, Color::get_Black()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.5f, Color::get_Black()));

    auto row1 = table->get_Rows()->Add();
    for (int cellCount = 1; cellCount < 5; cellCount++)
    {
        row1->get_Cells()->Add(String(u"Test 1") + String::Format(u"{0}", cellCount));
    }

    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"Test 2 1");
    auto cell = row2->get_Cells()->Add(u"Test 2 2");
    cell->set_ColSpan(2);
    row2->get_Cells()->Add(u"Test 2 4");

    auto row3 = table->get_Rows()->Add();
    row3->get_Cells()->Add(u"Test 3 1");
    row3->get_Cells()->Add(u"Test 3 2");
    row3->get_Cells()->Add(u"Test 3 3");
    row3->get_Cells()->Add(u"Test 3 4");

    auto row4 = table->get_Rows()->Add();
    row4->get_Cells()->Add(u"Test 4 1");
    cell = row4->get_Cells()->Add(u"Test 4 2");
    cell->set_RowSpan(2);
    row4->get_Cells()->Add(u"Test 4 3");
    row4->get_Cells()->Add(u"Test 4 4");

    auto row5 = table->get_Rows()->Add();
    row5->get_Cells()->Add(u"Test 5 1");
    row5->get_Cells()->Add(u"Test 5 3");
    row5->get_Cells()->Add(u"Test 5 4");

    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

### Apply borders to tables and cells

A thicker outer border frames the cell grid, and one cell displays its text with wrapping disabled.

1. Create a three-column [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) and add it to the page.
2. Use [`BorderInfo`](https://reference.aspose.com/pdf/cpp/aspose.pdf/borderinfo/) to set a 1-point outer border and a 0.1-point default cell border.
3. Set default cell padding with [`MarginInfo`](https://reference.aspose.com/pdf/cpp/aspose.pdf/margininfo/), populate two rows, and disable word wrapping in the first row's third [`Cell`](https://reference.aspose.com/pdf/cpp/aspose.pdf/cell/).
4. Save the [`Document`](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) to the output PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddBorders(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    page->get_Paragraphs()->Add(table);
    table->set_ColumnWidths(u"50 50 50");
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1));
    table->set_DefaultCellPadding(MakeObject<MarginInfo>(5, 5, 5, 5));

    auto row1 = table->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(
        MakeObject<TextFragment>(u"col3 with large text string"));
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);

    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    document->Save(outputFile);
}
```

## Table layout and sizing

### Set table margins and cell padding

Table margins control the space around the table, while cell padding sets the space between cell borders and their contents.

1. Create a three-column [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) with outer and cell borders.
2. Use [`MarginInfo`](https://reference.aspose.com/pdf/cpp/aspose.pdf/margininfo/) to set the outer table margin and the default cell padding independently.
3. Populate two rows, disable wrapping in the first row's third cell, and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddMarginsOrPadding(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    page->get_Paragraphs()->Add(table);
    table->set_ColumnWidths(u"50 50 50");
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1));
    table->set_DefaultCellPadding(MakeObject<MarginInfo>(5, 10, 5, 15));
    table->set_Margin(MakeObject<MarginInfo>(3, 3, 3, 3));

    auto row1 = table->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add();
    row1->get_Cells()->idx_get(2)->get_Paragraphs()->Add(
        MakeObject<TextFragment>(u"col3 with large text string"));
    row1->get_Cells()->idx_get(2)->set_IsWordWrapped(false);

    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    document->Save(outputFile);
}
```

### Fit columns to the available width

Automatic column sizing fits the three-column table to the available page width.

1. Add a three-column [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) to a page and specify initial column widths.
2. Set the [`ColumnAdjustment`](https://reference.aspose.com/pdf/cpp/aspose.pdf/columnadjustment/) mode to `AutoFitToWindow`.
3. Set borders and padding, populate two rows, and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>

using namespace System;
using namespace Aspose::Pdf;

void AutoFit(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    page->get_Paragraphs()->Add(table);
    table->set_ColumnWidths(u"50 50 50");
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToWindow);
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.1f));
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1));
    table->set_DefaultCellPadding(MakeObject<MarginInfo>(5, 5, 5, 5));

    auto row1 = table->get_Rows()->Add();
    row1->get_Cells()->Add(u"col1");
    row1->get_Cells()->Add(u"col2");
    row1->get_Cells()->Add(u"col3");
    auto row2 = table->get_Rows()->Add();
    row2->get_Cells()->Add(u"item1");
    row2->get_Cells()->Add(u"item2");
    row2->get_Cells()->Add(u"item3");
    document->Save(outputFile);
}
```

### Combine merged headers with repeating columns

Colored header cells span multiple columns in a wide table whose first two columns repeat when it splits.

1. Add a [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) to the page, configure vertical splitting, and set the first two columns to repeat.
2. Set a default [`BorderInfo`](https://reference.aspose.com/pdf/cpp/aspose.pdf/borderinfo/) for the cells and build a header with colored cells spanning two or three columns.
3. Add three rows with 17 cells each and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/VerticalBroken.h>

using namespace System;
using namespace Aspose::Pdf;

void AddTableHideBorders(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    table->set_Broken(TableBroken::Vertical);
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All));
    table->set_RepeatingColumnsCount(2);
    page->get_Paragraphs()->Add(table);

    auto row = table->get_Rows()->Add();
    auto cell = row->get_Cells()->Add(u"header 1");
    cell->set_ColSpan(2);
    cell->set_BackgroundColor(Color::get_LightGray());
    row->get_Cells()->Add(u"header 3");
    auto cell2 = row->get_Cells()->Add(u"header 4");
    cell2->set_ColSpan(2);
    cell2->set_BackgroundColor(Color::get_LightBlue());
    row->get_Cells()->Add(u"header 6");
    auto cell3 = row->get_Cells()->Add(u"header 7");
    cell3->set_ColSpan(2);
    cell3->set_BackgroundColor(Color::get_LightGreen());
    auto cell4 = row->get_Cells()->Add(u"header 9");
    cell4->set_ColSpan(3);
    cell4->set_BackgroundColor(Color::get_LightCoral());
    for (int i = 12; i < 18; i++)
    {
        row->get_Cells()->Add(String(u"header ") + String::Format(u"{0}", i));
    }

    for (int rowCounter = 0; rowCounter < 3; rowCounter++)
    {
        auto row1 = table->get_Rows()->Add();
        for (int i = 1; i < 18; i++)
        {
            row1->get_Cells()->Add(String(u"col ") + String::Format(u"{0}", rowCounter) + String(u", ") +
                                   String::Format(u"{0}", i));
        }
    }
    document->Save(outputFile);
}
```

### Round the corners of a table

A 15-point radius rounds the outer corners of the PDF table.

1. Create a [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) and configure a [`BorderInfo`](https://reference.aspose.com/pdf/cpp/aspose.pdf/borderinfo/) with a corner radius of 15 points.
2. Set the table's corner style to `Round` and assign the border.
3. Add 10 rows with three cells each, attach the table to the page, and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderCornerStyle.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>

using namespace System;
using namespace Aspose::Pdf;

void CreateTableWithRoundCorner(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All);
    borderInfo->set_RoundedBorderRadius(15);
    table->set_CornerStyle(BorderCornerStyle::Round);
    table->set_Border(borderInfo);
    for (int rowCount = 0; rowCount < 10; rowCount++)
    {
        auto row = table->get_Rows()->Add();
        row->get_Cells()->Add(String(u"Column (") + String::Format(u"{0}", rowCount) + String(u", 1)"));
        row->get_Cells()->Add(String(u"Column (") + String::Format(u"{0}", rowCount) + String(u", 2)"));
        row->get_Cells()->Add(String(u"Column (") + String::Format(u"{0}", rowCount) + String(u", 3)"));
    }
    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

## Add formatted content to cells

### Add LaTeX fragments to cells

LaTeX fragments render inside the cells of the generated PDF table.

1. Create a [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) with light gray outer and cell borders.
2. Add nine rows and insert a [`TeXFragment`](https://reference.aspose.com/pdf/cpp/aspose.pdf/texfragment/) in each of the three cells to render formatted text.
3. Add the table to the page's [`Paragraphs`](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Generator/TeXFragment.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>

using namespace System;
using namespace Aspose::Pdf;

void AddLatexFragments(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 0.5f, Color::get_LightGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.5f, Color::get_LightGray()));
    for (int rowCount = 1; rowCount < 10; rowCount++)
    {
        auto row = table->get_Rows()->Add();
        row->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TeXFragment>(
            String(u"Column $\\mathbf{(") + String::Format(u"{0}", rowCount) + String(u", 1)}$")));
        row->get_Cells()->Add()->get_Paragraphs()->Add(
            MakeObject<TeXFragment>(String(u"Column $\\tiny{(") +String::Format(u"{0}", rowCount) + String(u", 2)}$")));
        row->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TeXFragment>(
            String(u"Column $\\underline{(") + String::Format(u"{0}", rowCount) + String(u", 3)}$")));
    }
    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

## Control table pagination

### Start selected table rows on a new page

Selected rows in the two-column table begin on a new page.

1. Create a two-column [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) with red borders.
2. Populate 201 rows and call [`Row::set_IsInNewPage()`](https://reference.aspose.com/pdf/cpp/aspose.pdf/row/set_isinnewpage/) at row indexes 10, 20, and so on through 200.
3. Add the table to the page's [`Paragraphs`](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void InsertPageBreak(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));
    table->set_ColumnWidths(u"100 100");
    for (int counter = 0; counter < 201; counter++)
    {
        auto row = MakeObject<Row>();
        table->get_Rows()->Add(row);
        row->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>(
            String(u"Cell ") + String::Format(u"{0}", counter) + String(u", 0")));
        row->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>(
            String(u"Cell ") + String::Format(u"{0}", counter) + String(u", 1")));
        if (counter % 10 == 0 && counter != 0)
        {
            row->set_IsInNewPage(true);
        }
    }
    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

### Start a second table on a new page

In the landscape PDF, the second table begins on a new page.

1. Set the [`Document`](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) page defaults to landscape with 37-point margins and add a page.
2. Add a two-column [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) with 120 fixed-height rows, then create a second table with 10 rows.
3. Call [`BaseParagraph::set_IsInNewPage()`](https://reference.aspose.com/pdf/cpp/aspose.pdf/baseparagraph/set_isinnewpage/) on the second table, add it to the same paragraph collection, and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTableOnNewPage(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    document->get_PageInfo()->get_Margin()->set_Left(37);
    document->get_PageInfo()->get_Margin()->set_Right(37);
    document->get_PageInfo()->get_Margin()->set_Top(37);
    document->get_PageInfo()->get_Margin()->set_Bottom(37);
    document->get_PageInfo()->set_IsLandscape(true);

    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"50 100");
    for (int i = 1; i < 121; i++)
    {
        auto row = table->get_Rows()->Add();
        row->set_FixedRowHeight(15);
        row->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Content 1"));
        row->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Content 2"));
    }
    page->get_Paragraphs()->Add(table);

    auto table1 = MakeObject<Table>();
    table1->set_ColumnWidths(u"100 100");
    for (int i = 1; i < 11; i++)
    {
        auto row = table1->get_Rows()->Add();
        row->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Content 3"));
        row->get_Cells()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>(u"Content 4"));
    }
    table1->set_IsInNewPage(true);
    page->get_Paragraphs()->Add(table1);
    document->Save(outputFile);
}
```

### Repeat header rows across pages

The first two rows serve as headers and repeat on each continuation page.

1. Set the [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) break mode to `Vertical` and configure its first two rows to repeat.
2. Use [`TextState`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textstate/) to style the repeating rows with 12-point red Times New Roman. Make sure the font is available in the runtime environment.
3. Add two header rows with different background colors, then add 100 data rows.
4. Add the table to the page's [`Paragraphs`](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/VerticalBroken.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddRepeatingRows(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    table->set_Broken(TableBroken::Vertical);
    table->set_RepeatingRowsCount(2);
    auto textState = MakeObject<TextState>();
    textState->set_FontSize(12);
    textState->set_Font(FontRepository::FindFont(u"Times New Roman"));
    textState->set_ForegroundColor(Color::get_Red());
    table->set_RepeatingRowsStyle(textState);
    table->set_ColumnWidths(u"100 100 100");
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.5f, Color::get_Black()));
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1, Color::get_Black()));

    auto headerRow1 = table->get_Rows()->Add();
    headerRow1->get_Cells()->Add(u"Header 1-1");
    headerRow1->get_Cells()->Add(u"Header 1-2");
    headerRow1->get_Cells()->Add(u"Header 1-3");
    for (auto cell : headerRow1->get_Cells())
    {
        cell->set_BackgroundColor(Color::get_LightGray());
    }
    auto headerRow2 = table->get_Rows()->Add();
    headerRow2->get_Cells()->Add(u"Header 2-1");
    headerRow2->get_Cells()->Add(u"Header 2-2");
    headerRow2->get_Cells()->Add(u"Header 2-3");
    for (auto cell : headerRow2->get_Cells())
    {
        cell->set_BackgroundColor(Color::get_LightBlue());
    }
    for (int i = 1; i < 101; i++)
    {
        auto row = table->get_Rows()->Add();
        row->get_Cells()->Add(String(u"Data ") + String::Format(u"{0}", i) + String(u"-1"));
        row->get_Cells()->Add(String(u"Data ") + String::Format(u"{0}", i) + String(u"-2"));
        row->get_Cells()->Add(String(u"Data ") + String::Format(u"{0}", i) + String(u"-3"));
    }
    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

### Repeat columns when a table splits horizontally

When the wide table splits into sections on a landscape A5 page, the configured columns repeat.

1. Add a landscape A5 page and create a [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) with the `VerticalInSamePage` break mode.
2. Use `AutoFitToContent` and set the first five columns to repeat.
3. Fill 17 columns across a header row and five data rows, shade the repeating columns, and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/PageSize.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/VerticalBroken.h>

using namespace System;
using namespace Aspose::Pdf;

void AddRepeatingColumns(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    page->SetPageSize(PageSize::get_A5()->get_Height(), PageSize::get_A5()->get_Width());
    auto border = MakeObject<BorderInfo>(BorderSide::All, 0.5f, Color::get_LightGray());
    auto table = MakeObject<Table>();
    table->set_Broken(TableBroken::VerticalInSamePage);
    table->set_ColumnAdjustment(ColumnAdjustment::AutoFitToContent);
    table->set_RepeatingColumnsCount(5);
    table->set_Border(border);
    table->set_DefaultCellBorder(border);
    page->get_Paragraphs()->Add(table);

    auto row = table->get_Rows()->Add();
    for (int i = 1; i < 6; i++)
    {
        auto cell = row->get_Cells()->Add(String(u"header ") + String::Format(u"{0}", i));
        cell->set_BackgroundColor(Color::get_LightGray());
    }
    for (int i = 6; i < 18; i++)
    {
        row->get_Cells()->Add(String(u"header ") + String::Format(u"{0}", i));
    }

    for (int rowCounter = 1; rowCounter < 6; rowCounter++)
    {
        row = table->get_Rows()->Add();
        for (int i = 1; i < 6; i++)
        {
            auto cell = row->get_Cells()->Add(String(u"cell ") + String::Format(u"{0}", rowCounter) +
                                              String(u",") + String::Format(u"{0}", i));
            cell->set_BackgroundColor(Color::get_LightGray());
        }
        for (int i = 6; i < 18; i++)
        {
            row->get_Cells()->Add(String(u"cell ") + String::Format(u"{0}", rowCounter) + String(u",") +
                                  String::Format(u"{0}", i));
        }
    }
    document->Save(outputFile);
}
```

### Rotate text inside table cells

Four adjacent cells display centered text at 0, 90, 180, and 270 degrees.

1. Create a bordered [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) and add one [`Row`](https://reference.aspose.com/pdf/cpp/aspose.pdf/row/) with a minimum height of 200 points.
2. Add four cells and center a [`TextFragment`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) in each one.
3. Set the [`TextFragmentState`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentstate/) rotation to 0, 90, 180, and 270 degrees respectively.
4. Add the table to the page's [`Paragraphs`](https://reference.aspose.com/pdf/cpp/aspose.pdf/paragraphs/) collection and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void RotatedTextTable(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto table = MakeObject<Table>();
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 0.5f, Color::get_Black()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.5f, Color::get_Black()));
    auto row = table->get_Rows()->Add();
    row->set_MinRowHeight(200);
    for (int cellCount = 0; cellCount < 4; cellCount++)
    {
        auto cell = row->get_Cells()->Add();
        auto textFragment =
            MakeObject<TextFragment>(String(u"Cell ") + String::Format(u"{0}", (cellCount + 1)));
        textFragment->get_TextState()->set_Rotation(90 * cellCount);
        textFragment->set_HorizontalAlignment(HorizontalAlignment::Center);
        cell->get_Paragraphs()->Add(textFragment);
    }
    page->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

## Related table topics

- [Working with Tables](/pdf/cpp/working-with-tables/)
- [Extracting Tables](/pdf/cpp/extracting-table/)
- [Integrating Tables with Data Sources](/pdf/cpp/integrate-table/)
- [Manipulating Tables](/pdf/cpp/manipulating-tables/)
- [Removing Tables](/pdf/cpp/removing-tables/)
