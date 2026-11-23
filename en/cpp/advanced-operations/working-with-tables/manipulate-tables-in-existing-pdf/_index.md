---
title: Update Tables in Existing PDF Documents in C++
linktitle: Manipulating Tables
type: docs
weight: 40
url: /cpp/manipulating-tables/
description: Change cell text or replace a detected table on the first page of a PDF in C++.
lastmod: "2026-11-23"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Edit PDF Table Text and Replace Tables in C++
Abstract: Use TableAbsorber to identify tables on a PDF page. Update a cell fragment or replace the detected table with a newly built table.
---

## Replace text in a table cell

To update a single cell, the code changes the second text fragment in the upper-left cell of the first table detected on page 1 and saves the PDF.

1. Open the input PDF as a [`Document`](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and select page 1.
2. Call [`TableAbsorber::Visit()`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/visit/) to find the tables on that page.
3. Select the first table, its first row, and its first [`AbsorbedCell`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/absorbedcell/).
4. Set the text of the second [`TextFragment`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) to `New Value`. The sample requires at least two text fragments in that cell.
5. Save the [`Document`](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) to the output PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <system/collections/list.h>
#include <stdexcept>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceCells(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    auto absorber = MakeObject<TableAbsorber>();
    absorber->Visit(page);
    if (absorber->get_TableList()->get_Count() == 0)
        throw std::runtime_error("No tables found");
    auto rows = absorber->get_TableList()->idx_get(0)->get_RowList();
    if (rows->get_Count() == 0)
        throw std::runtime_error("The target table has no rows");
    auto cells = rows->idx_get(0)->get_CellList();
    if (cells->get_Count() == 0)
        throw std::runtime_error("The target row has no cells");
    auto fragments = cells->idx_get(0)->get_TextFragments();
    if (fragments->get_Count() < 2)
        throw std::runtime_error("The target cell has fewer than two text fragments");
    fragments->idx_get(1)->set_Text(u"New Value");
    document->Save(outputFile);
}
```

## Replace an existing table

A new two-row, three-column table takes the place of the first table detected on page 1.

1. Open the input PDF as a [`Document`](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and select page 1.
2. Call [`TableAbsorber::Visit()`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/visit/) to find the tables on that page.
3. Create a new [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) with two rows, three columns, and default cell borders.
4. Call [`TableAbsorber::Replace()`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/replace/) to replace the first detected table, then save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <system/collections/list.h>
#include <stdexcept>
#include <initializer_list>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ReplaceTable(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    auto absorber = MakeObject<TableAbsorber>();
    absorber->Visit(page);
    if (absorber->get_TableList()->get_Count() == 0)
        throw std::runtime_error("No tables found");
    auto table = MakeObject<Table>();
    table->set_ColumnWidths(u"100 100 100");
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::All, 1.0f));
    auto row = table->get_Rows()->Add();
    for (const auto &text : {u"Col 1", u"Col 2", u"Col 3"})
        row->get_Cells()->Add(text);
    row = table->get_Rows()->Add();
    for (const auto &text : {u"Col 12", u"Col 22", u"Col 32"})
        row->get_Cells()->Add(text);
    absorber->Replace(page, absorber->get_TableList()->idx_get(0), table);
    document->Save(outputFile);
}
```

## Related table topics

- [Working with Tables](/pdf/cpp/working-with-tables/)
- [Adding Tables](/pdf/cpp/adding-tables/)
- [Extracting Tables](/pdf/cpp/extracting-table/)
- [Integrating Tables with Data Sources](/pdf/cpp/integrate-table/)
- [Removing Tables](/pdf/cpp/removing-tables/)
