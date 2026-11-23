---
title: Extract Tables from PDF in C++
linktitle: Extracting Tables
type: docs
weight: 20
url: /cpp/extracting-table/
description: Read table rows, cells, and text segments from an existing PDF in C++.
lastmod: "2026-11-23"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read PDF Table Content with TableAbsorber in C++
Abstract: Scan each PDF page for tables with TableAbsorber. Read each detected cell's text segments and print the rows to the console.
---

## Extract tables from every page

Scanning every page of an existing PDF yields the text of detected tables, which the code prints to the console one row per line.

1. Open the input PDF as a [`Document`](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and iterate over its pages.
2. Create a fresh [`TableAbsorber`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/) for each page and call [`TableAbsorber::Visit()`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/visit/).
3. Traverse the [`AbsorbedTable`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/absorbedtable/) rows and [`AbsorbedCell`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/absorbedcell/) objects. Print each cell's text segments and end each row with a newline.

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
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/TextSegmentCollection.h>
#include <system/collections/list.h>
#include <iostream>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void Extract(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto page : document->get_Pages())
    {
        auto absorber = MakeObject<TableAbsorber>();
        absorber->Visit(page);
        for (auto table : absorber->get_TableList())
        {
            std::cout << "Table ----" << std::endl;
            for (auto row : table->get_RowList())
            {
                for (auto cell : row->get_CellList())
                {
                    std::cout << " | ";
                    for (auto fragment : cell->get_TextFragments())
                        for (auto segment : fragment->get_Segments())
                            std::cout << segment->get_Text();
                }
                std::cout << std::endl;
            }
        }
    }
}
```

## Related table topics

- [Working with Tables](/pdf/cpp/working-with-tables/)
- [Adding Tables](/pdf/cpp/adding-tables/)
- [Integrating Tables with Data Sources](/pdf/cpp/integrate-table/)
- [Manipulating Tables](/pdf/cpp/manipulating-tables/)
- [Removing Tables](/pdf/cpp/removing-tables/)
