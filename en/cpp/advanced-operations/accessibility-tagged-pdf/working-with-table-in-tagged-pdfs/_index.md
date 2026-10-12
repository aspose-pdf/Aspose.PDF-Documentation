---
title: Work with tables in tagged PDFs in C++
linktitle: Working with Table in Tagged PDFs
type: docs
weight: 40
url: /cpp/working-with-table-in-tagged-pdfs/
description: Create and style tagged PDF tables in C++, including headers, body rows, footers, merged cells, summaries, and positioning.
lastmod: "2026-10-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Create tagged tables with explicit header, body, and footer elements using Aspose.PDF for C++. The examples show how to describe a table, merge cells, style tables and rows, and adjust their position.

## Create a tagged table

Build a table with a header, body, footer, merged cells, and summary metadata.

The example creates 50 body rows and uses Arial for cell text. Make sure the font is available.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a table with [CreateTableElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append it to the root.
1. Configure the border and create the table header, body, and footer.
1. Create a header row with TH cells.
1. Create body rows with TD cells and configure text, borders, padding, and alignment.
1. Set row and column spans for the merged cell and skip the positions it covers.
1. Create the footer row.
1. Set the table summary with a [StructureAttribute](https://reference.aspose.com/pdf/cpp/aspose.pdf.logicalstructure/structureattribute/).
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/AttributeName.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSTableElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureAttribute.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureAttributeCollection.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureAttributes.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureTextState.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;
using namespace Aspose::Pdf::Text;

void CreateTable(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Example table");
    taggedContent->SetLanguage(u"en-US");

    auto tableElement = taggedContent->CreateTableElement();
    taggedContent->get_RootElement()->AppendChild(tableElement, true);
    tableElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.2f, Color::get_DarkBlue()));


    auto tableTHeadElement = tableElement->CreateTHead();
    auto tableTBodyElement = tableElement->CreateTBody();
    auto tableTFootElement = tableElement->CreateTFoot();

    auto headTrElement = tableTHeadElement->CreateTR();
    headTrElement->set_AlternativeText(u"Head Row");
    headTrElement->set_BackgroundColor(Color::get_LightGray());

    for (int columnIndex = 0; columnIndex < 4; columnIndex++) {
        auto thElement = headTrElement->CreateTH();
        thElement->SetText(String::Format(u"Head {0}", columnIndex));
        thElement->set_BackgroundColor(Color::get_GreenYellow());
        thElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 4.0f, Color::get_Gray()));
        thElement->set_IsNoBorder(true);
        thElement->set_Margin(MakeObject<MarginInfo>(16.0, 2.0, 8.0, 2.0));
        thElement->set_Alignment(HorizontalAlignment::Right);
    }

    for (int rowIndex = 0; rowIndex < 50; rowIndex++) {
        auto trElement = tableTBodyElement->CreateTR();
        trElement->set_AlternativeText(u"Row " + rowIndex);

        for (int columnIndex = 0; columnIndex < 4; columnIndex++) {
            int colSpan = 1;
            int rowSpan = 1;

            if (true && columnIndex == 1 && rowIndex == 1) {
                colSpan = 2;
                rowSpan = 2;
            } else if (true && ((rowIndex == 1 && columnIndex == 2)
            || (rowIndex == 2 && (columnIndex == 1 || columnIndex == 2)))) {
                continue;
            }

            auto tdElement = trElement->CreateTD();
            tdElement->SetText(String::Format(u"Cell [{0}, {1}]", rowIndex, columnIndex));
            tdElement->set_BackgroundColor(Color::get_Yellow());
            tdElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 4.0f, Color::get_Gray()));
            tdElement->set_IsNoBorder(false);
            tdElement->set_Margin(MakeObject<MarginInfo>(8.0, 2.0, 8.0, 2.0));
            tdElement->set_Alignment(HorizontalAlignment::Center);

            auto cellTextState = MakeObject<TextState>();
            cellTextState->set_ForegroundColor(Color::get_DarkBlue());
            cellTextState->set_FontSize(7.5f);
            cellTextState->set_FontStyle(FontStyles::Bold);
            cellTextState->set_Font(FontRepository::FindFont(u"Arial"));
            tdElement->set_DefaultCellTextState(cellTextState);

            tdElement->set_IsWordWrapped(true);
            tdElement->set_VerticalAlignment(VerticalAlignment::Center);
            tdElement->set_ColSpan(colSpan);
            tdElement->set_RowSpan(rowSpan);
        }
    }

    auto footTrElement = tableTFootElement->CreateTR();
    footTrElement->set_AlternativeText(u"Foot Row");
    footTrElement->set_BackgroundColor(Color::get_LightSeaGreen());

    for (int columnIndex = 0; columnIndex < 4; columnIndex++) {
        auto tdElement = footTrElement->CreateTD();
        tdElement->SetText(String::Format(u"Foot {0}", columnIndex));
        tdElement->set_Alignment(HorizontalAlignment::Center);
        tdElement->get_StructureTextState()->set_FontSize(7.0f);
        tdElement->get_StructureTextState()->set_FontStyle(FontStyles::Bold);
    }


    auto tableAttributes = tableElement->get_Attributes()->GetAttributes(AttributeOwnerStandard::Table());
    auto summaryAttribute = MakeObject<StructureAttribute>(AttributeKey::Summary);
    summaryAttribute->SetStringValue(u"The summary text for table");
    tableAttributes->SetAttribute(summaryAttribute);

    document->Save(outputFile);
}
```

## Style a tagged table

Configure table layout, borders, cell defaults, and repeating rows and columns.

The merged-cell branch is disabled in this example. For active row and column spans, see the cell styling example.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a table with [CreateTableElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append it to the root.
1. Set the background, border, alignment, column widths, and column adjustment.
1. Configure default cell borders, padding, and text formatting.
1. Set the table position and repeating row and column settings.
1. Create header, body, and footer rows.
1. Apply per-cell styles and fill the cells with text.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Table/VerticalBroken.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/ColumnAdjustment.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSTableElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureTextState.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;
using namespace Aspose::Pdf::Text;

void StyleTable(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Example table style");
    taggedContent->SetLanguage(u"en-US");

    auto tableElement = taggedContent->CreateTableElement();
    taggedContent->get_RootElement()->AppendChild(tableElement, true);

    tableElement->set_BackgroundColor(Color::get_Beige());
    tableElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 0.80f, Color::get_Gray()));
    tableElement->set_Alignment(HorizontalAlignment::Center);
    tableElement->set_Broken(TableBroken::Vertical);
    tableElement->set_ColumnAdjustment(ColumnAdjustment::AutoFitToWindow);
    tableElement->set_ColumnWidths(u"80 80 80 80 80");
    tableElement->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.50f, Color::get_DarkBlue()));
    tableElement->set_DefaultCellPadding(MakeObject<MarginInfo>(16.0, 2.0, 8.0, 2.0));
    tableElement->get_DefaultCellTextState()->set_ForegroundColor(Color::get_DarkCyan());
    tableElement->get_DefaultCellTextState()->set_FontSize(8.0f);
    tableElement->set_DefaultColumnWidth(u"70");
    tableElement->set_IsBordersIncluded(true);
    tableElement->set_Left(0.0f);
    tableElement->set_Top(40.0f);
    tableElement->set_RepeatingColumnsCount(2);
    tableElement->set_RepeatingRowsCount(3);

    auto rowStyle = MakeObject<TextState>();
    rowStyle->set_BackgroundColor(Color::get_LightCoral());
    tableElement->set_RepeatingRowsStyle(rowStyle);


    auto tableTHeadElement = tableElement->CreateTHead();
    auto tableTBodyElement = tableElement->CreateTBody();
    auto tableTFootElement = tableElement->CreateTFoot();

    auto headTrElement = tableTHeadElement->CreateTR();
    headTrElement->set_AlternativeText(u"Head Row");
    headTrElement->set_BackgroundColor(Color::get_LightGray());

    for (int columnIndex = 0; columnIndex < 5; columnIndex++) {
        auto thElement = headTrElement->CreateTH();
        thElement->SetText(String::Format(u"Head {0}", columnIndex));
        thElement->set_BackgroundColor(Color::get_GreenYellow());
        thElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 4.0f, Color::get_Gray()));
        thElement->set_IsNoBorder(true);
        thElement->set_Margin(MakeObject<MarginInfo>(16.0, 2.0, 8.0, 2.0));
        thElement->set_Alignment(HorizontalAlignment::Right);
    }

    for (int rowIndex = 0; rowIndex < 10; rowIndex++) {
        auto trElement = tableTBodyElement->CreateTR();
        trElement->set_AlternativeText(u"Row " + rowIndex);

        for (int columnIndex = 0; columnIndex < 5; columnIndex++) {
            int colSpan = 1;
            int rowSpan = 1;

            if (false && columnIndex == 1 && rowIndex == 1) {
                colSpan = 2;
                rowSpan = 2;
            } else if (false && ((rowIndex == 1 && columnIndex == 2)
            || (rowIndex == 2 && (columnIndex == 1 || columnIndex == 2)))) {
                continue;
            }

            auto tdElement = trElement->CreateTD();
            tdElement->SetText(String::Format(u"Cell [{0}, {1}]", rowIndex, columnIndex));
            tdElement->set_BackgroundColor(Color::get_Yellow());
            tdElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 4.0f, Color::get_Gray()));
            tdElement->set_IsNoBorder(false);
            tdElement->set_Margin(MakeObject<MarginInfo>(8.0, 2.0, 8.0, 2.0));
            tdElement->set_Alignment(HorizontalAlignment::Center);

            auto cellTextState = MakeObject<TextState>();
            cellTextState->set_ForegroundColor(Color::get_DarkBlue());
            cellTextState->set_FontSize(7.5f);
            cellTextState->set_FontStyle(FontStyles::Bold);
            cellTextState->set_Font(FontRepository::FindFont(u"Arial"));
            tdElement->set_DefaultCellTextState(cellTextState);

            tdElement->set_IsWordWrapped(true);
            tdElement->set_VerticalAlignment(VerticalAlignment::Center);
            tdElement->set_ColSpan(colSpan);
            tdElement->set_RowSpan(rowSpan);
        }
    }

    auto footTrElement = tableTFootElement->CreateTR();
    footTrElement->set_AlternativeText(u"Foot Row");
    footTrElement->set_BackgroundColor(Color::get_LightSeaGreen());

    for (int columnIndex = 0; columnIndex < 5; columnIndex++) {
        auto tdElement = footTrElement->CreateTD();
        tdElement->SetText(String::Format(u"Foot {0}", columnIndex));
        tdElement->set_Alignment(HorizontalAlignment::Center);
        tdElement->get_StructureTextState()->set_FontSize(7.0f);
        tdElement->get_StructureTextState()->set_FontStyle(FontStyles::Bold);
    }

    document->Save(outputFile);
}
```

## Style table rows

Apply row height, pagination, borders, padding, and default cell text settings.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a table with [CreateTableElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append it to the root.
1. Create the table header, body, and footer.
1. Populate the header row.
1. Create seven body rows and set their background, borders, minimum height, and fixed height.
1. Configure row page breaks, row splitting, default cell formatting, padding, and vertical alignment.
1. Populate the body and footer cells.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSTableElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;
using namespace Aspose::Pdf::Text;

void StyleTableRow(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Example table style");
    taggedContent->SetLanguage(u"en-US");

    auto tableElement = taggedContent->CreateTableElement();
    taggedContent->get_RootElement()->AppendChild(tableElement, true);
    auto tableTHeadElement = tableElement->CreateTHead();
    auto tableTBodyElement = tableElement->CreateTBody();
    auto tableTFootElement = tableElement->CreateTFoot();

    auto headTrElement = tableTHeadElement->CreateTR();
    headTrElement->set_AlternativeText(u"Head Row");
    for (int colIndex = 0; colIndex < 3; colIndex++) {
        headTrElement->CreateTH()->SetText(String::Format(u"Head {0}", colIndex));
    }

    for (int rowIndex = 0; rowIndex < 7; rowIndex++) {
        auto trElement = tableTBodyElement->CreateTR();
        trElement->set_AlternativeText(u"Row " + rowIndex);
        trElement->set_BackgroundColor(Color::get_LightGoldenrodYellow());
        trElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 0.75f, Color::get_DarkGray()));
        trElement->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 0.50f, Color::get_Blue()));
        trElement->set_MinRowHeight(100.0);
        trElement->set_FixedRowHeight(120.0);
        trElement->set_IsInNewPage(rowIndex % 3 == 1);
        trElement->set_IsRowBroken(true);

        auto cellTextState = MakeObject<TextState>();
        cellTextState->set_ForegroundColor(Color::get_Red());
        trElement->set_DefaultCellTextState(cellTextState);
        trElement->set_DefaultCellPadding(MakeObject<MarginInfo>(16.0, 2.0, 8.0, 2.0));
        trElement->set_VerticalAlignment(VerticalAlignment::Bottom);

        for (int colIndex = 0; colIndex < 3; colIndex++) {
            trElement->CreateTD()->SetText(String::Format(u"Cell [{0}, {1}]", rowIndex, colIndex));
        }
    }

    auto footTrElement = tableTFootElement->CreateTR();
    footTrElement->set_AlternativeText(u"Foot Row");
    for (int colIndex = 0; colIndex < 3; colIndex++) {
        footTrElement->CreateTD()->SetText(String::Format(u"Foot {0}", colIndex));
    }

    document->Save(outputFile);
}
```

## Style table cells and spans

Set cell appearance and merge a cell across two rows and two columns.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a table with [CreateTableElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append it to the root.
1. Create the table header, body, and footer.
1. Create header cells and set their formatting.
1. Create body cells and set text, background, border, margins, alignment, and text state.
1. Configure word wrapping and vertical alignment.
1. Set ColSpan and RowSpan for the merged cell, skipping the covered cell positions.
1. Populate and style the footer.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSTableElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureTextState.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;
using namespace Aspose::Pdf::Text;

void StyleTableCell(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Example table cell style");
    taggedContent->SetLanguage(u"en-US");

    auto tableElement = taggedContent->CreateTableElement();
    taggedContent->get_RootElement()->AppendChild(tableElement, true);

    auto tableTHeadElement = tableElement->CreateTHead();
    auto tableTBodyElement = tableElement->CreateTBody();
    auto tableTFootElement = tableElement->CreateTFoot();

    auto headTrElement = tableTHeadElement->CreateTR();
    headTrElement->set_AlternativeText(u"Head Row");
    headTrElement->set_BackgroundColor(Color::get_LightGray());

    for (int columnIndex = 0; columnIndex < 4; columnIndex++) {
        auto thElement = headTrElement->CreateTH();
        thElement->SetText(String::Format(u"Head {0}", columnIndex));
        thElement->set_BackgroundColor(Color::get_GreenYellow());
        thElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 4.0f, Color::get_Gray()));
        thElement->set_IsNoBorder(true);
        thElement->set_Margin(MakeObject<MarginInfo>(16.0, 2.0, 8.0, 2.0));
        thElement->set_Alignment(HorizontalAlignment::Right);
    }

    for (int rowIndex = 0; rowIndex < 4; rowIndex++) {
        auto trElement = tableTBodyElement->CreateTR();
        trElement->set_AlternativeText(u"Row " + rowIndex);

        for (int columnIndex = 0; columnIndex < 4; columnIndex++) {
            int colSpan = 1;
            int rowSpan = 1;

            if (true && columnIndex == 1 && rowIndex == 1) {
                colSpan = 2;
                rowSpan = 2;
            } else if (true && ((rowIndex == 1 && columnIndex == 2)
            || (rowIndex == 2 && (columnIndex == 1 || columnIndex == 2)))) {
                continue;
            }

            auto tdElement = trElement->CreateTD();
            tdElement->SetText(String::Format(u"Cell [{0}, {1}]", rowIndex, columnIndex));
            tdElement->set_BackgroundColor(Color::get_Yellow());
            tdElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 4.0f, Color::get_Gray()));
            tdElement->set_IsNoBorder(false);
            tdElement->set_Margin(MakeObject<MarginInfo>(8.0, 2.0, 8.0, 2.0));
            tdElement->set_Alignment(HorizontalAlignment::Center);

            auto cellTextState = MakeObject<TextState>();
            cellTextState->set_ForegroundColor(Color::get_DarkBlue());
            cellTextState->set_FontSize(7.5f);
            cellTextState->set_FontStyle(FontStyles::Bold);
            cellTextState->set_Font(FontRepository::FindFont(u"Arial"));
            tdElement->set_DefaultCellTextState(cellTextState);

            tdElement->set_IsWordWrapped(true);
            tdElement->set_VerticalAlignment(VerticalAlignment::Center);
            tdElement->set_ColSpan(colSpan);
            tdElement->set_RowSpan(rowSpan);
        }
    }

    auto footTrElement = tableTFootElement->CreateTR();
    footTrElement->set_AlternativeText(u"Foot Row");
    footTrElement->set_BackgroundColor(Color::get_LightSeaGreen());

    for (int columnIndex = 0; columnIndex < 4; columnIndex++) {
        auto tdElement = footTrElement->CreateTD();
        tdElement->SetText(String::Format(u"Foot {0}", columnIndex));
        tdElement->set_Alignment(HorizontalAlignment::Center);
        tdElement->get_StructureTextState()->set_FontSize(7.0f);
        tdElement->get_StructureTextState()->set_FontStyle(FontStyles::Bold);
    }


    document->Save(outputFile);
}
```

## Adjust table position

Apply PositionSettings to a tagged table before adding its rows and cells.

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and get its [ITaggedContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) with [get_TaggedContent()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/get_taggedcontent/).
1. Set the document title and language with [SetTitle()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and [SetLanguage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/).
1. Create a table with [CreateTableElement()](https://reference.aspose.com/pdf/cpp/aspose.pdf.tagged/itaggedcontent/) and append it to the root.
1. Create PositionSettings with a left margin and explicit alignment and pagination flags.
1. Apply the settings to the table with AdjustPosition().
1. Create header, body, and footer rows.
1. Populate and style the cells, including the merged cell.
1. Save the document with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Tagged/ITaggedContent.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/BLSTableElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureElement.h>
#include <Aspose.PDF.Cpp/Tagged/LogicalStructure/StructureTextState.h>
#include <Aspose.PDF.Cpp/Tagged/PositionSettings.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>
#include <Aspose.PDF.Cpp/Text/FontStyles.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Tagged;
using namespace Aspose::Pdf::LogicalStructure;
using namespace Aspose::Pdf::Text;

void AdjustTablePosition(System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto taggedContent = document->get_TaggedContent();
    taggedContent->SetTitle(u"Example table position");
    taggedContent->SetLanguage(u"en-US");

    auto tableElement = taggedContent->CreateTableElement();
    taggedContent->get_RootElement()->AppendChild(tableElement, true);

    auto positionSettings = MakeObject<PositionSettings>();
    positionSettings->set_HorizontalAlignment(HorizontalAlignment::None);
    positionSettings->set_Margin(MakeObject<MarginInfo>(20, 0, 0, 0));
    positionSettings->set_VerticalAlignment(VerticalAlignment::None);
    positionSettings->set_IsFirstParagraphInColumn(false);
    positionSettings->set_IsKeptWithNext(false);
    positionSettings->set_IsInNewPage(false);
    positionSettings->set_IsInLineParagraph(false);
    tableElement->AdjustPosition(positionSettings);


    auto tableTHeadElement = tableElement->CreateTHead();
    auto tableTBodyElement = tableElement->CreateTBody();
    auto tableTFootElement = tableElement->CreateTFoot();

    auto headTrElement = tableTHeadElement->CreateTR();
    headTrElement->set_AlternativeText(u"Head Row");
    headTrElement->set_BackgroundColor(Color::get_LightGray());

    for (int columnIndex = 0; columnIndex < 4; columnIndex++) {
        auto thElement = headTrElement->CreateTH();
        thElement->SetText(String::Format(u"Head {0}", columnIndex));
        thElement->set_BackgroundColor(Color::get_GreenYellow());
        thElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 4.0f, Color::get_Gray()));
        thElement->set_IsNoBorder(true);
        thElement->set_Margin(MakeObject<MarginInfo>(16.0, 2.0, 8.0, 2.0));
        thElement->set_Alignment(HorizontalAlignment::Right);
    }

    for (int rowIndex = 0; rowIndex < 4; rowIndex++) {
        auto trElement = tableTBodyElement->CreateTR();
        trElement->set_AlternativeText(u"Row " + rowIndex);

        for (int columnIndex = 0; columnIndex < 4; columnIndex++) {
            int colSpan = 1;
            int rowSpan = 1;

            if (true && columnIndex == 1 && rowIndex == 1) {
                colSpan = 2;
                rowSpan = 2;
            } else if (true && ((rowIndex == 1 && columnIndex == 2)
            || (rowIndex == 2 && (columnIndex == 1 || columnIndex == 2)))) {
                continue;
            }

            auto tdElement = trElement->CreateTD();
            tdElement->SetText(String::Format(u"Cell [{0}, {1}]", rowIndex, columnIndex));
            tdElement->set_BackgroundColor(Color::get_Yellow());
            tdElement->set_Border(MakeObject<BorderInfo>(BorderSide::All, 4.0f, Color::get_Gray()));
            tdElement->set_IsNoBorder(false);
            tdElement->set_Margin(MakeObject<MarginInfo>(8.0, 2.0, 8.0, 2.0));
            tdElement->set_Alignment(HorizontalAlignment::Center);

            auto cellTextState = MakeObject<TextState>();
            cellTextState->set_ForegroundColor(Color::get_DarkBlue());
            cellTextState->set_FontSize(7.5f);
            cellTextState->set_FontStyle(FontStyles::Bold);
            cellTextState->set_Font(FontRepository::FindFont(u"Arial"));
            tdElement->set_DefaultCellTextState(cellTextState);

            tdElement->set_IsWordWrapped(true);
            tdElement->set_VerticalAlignment(VerticalAlignment::Center);
            tdElement->set_ColSpan(colSpan);
            tdElement->set_RowSpan(rowSpan);
        }
    }

    auto footTrElement = tableTFootElement->CreateTR();
    footTrElement->set_AlternativeText(u"Foot Row");
    footTrElement->set_BackgroundColor(Color::get_LightSeaGreen());

    for (int columnIndex = 0; columnIndex < 4; columnIndex++) {
        auto tdElement = footTrElement->CreateTD();
        tdElement->SetText(String::Format(u"Foot {0}", columnIndex));
        tdElement->set_Alignment(HorizontalAlignment::Center);
        tdElement->get_StructureTextState()->set_FontSize(7.0f);
        tdElement->get_StructureTextState()->set_FontStyle(FontStyles::Bold);
    }

    document->Save(outputFile);
}
```
