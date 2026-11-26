---
title: Create PDF Tables from CSV in C++
linktitle: Integrating Tables with Data Sources
type: docs
weight: 30
url: /cpp/integrate-table/
description: Read selected CSV columns and write a table to a PDF in C++.
lastmod: "2026-11-23"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Import CSV Data into a PDF Table in C++
Abstract: Read comma-separated records and map their headers to selected table columns. Write the header and up to 20 data rows to a new PDF.
---

## Create a PDF table from CSV data

The CSV import maps four fields (city, country, population, and ISO3) to a PDF table with a shaded header and up to 20 data rows.

1. Read the CSV lines into rows and locate the four required header names.
2. Create a [`Table`](https://reference.aspose.com/pdf/cpp/aspose.pdf/table/) with an outer border and a bottom border for each cell.
3. Copy the header and up to 20 data rows in the selected column order. Use empty strings for missing values and shade the header cells.
4. Add the table to a page in a new [`Document`](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and save the PDF.

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
#include <system/io/file.h>
#include <system/array.h>
#include <vector>
#include <algorithm>
#include <stdexcept>
#include <initializer_list>

using namespace System;
using namespace Aspose::Pdf;

void CreatePdfFromCsv(String inputFile, String outputFile)
{
    std::vector<std::vector<String>> rows;
    for (const auto &line : System::IO::File::ReadAllLines(inputFile))
    {
        std::vector<String> row;
        String value;
        bool quoted = false;
        for (int i = 0; i < line.get_Length(); ++i)
        {
            auto ch = line[i];
            if (ch == u'"')
            {
                if (quoted && i + 1 < line.get_Length() && line[i + 1] == u'"')
                {
                    value += u'"';
                    ++i;
                }
                else
                    quoted = !quoted;
            }
            else if (ch == u',' && !quoted)
            {
                row.push_back(value);
                value = String::Empty;
            }
            else
                value += ch;
        }
        row.push_back(value);
        rows.push_back(row);
    }
    if (rows.empty())
        throw std::runtime_error("CSV file is empty");
    std::vector<size_t> columns;
    for (const auto &name : {u"city", u"country", u"population", u"iso3"})
    {
        auto it = std::find(rows[0].begin(), rows[0].end(), String(name));
        if (it == rows[0].end())
            throw std::runtime_error("Required CSV column is missing");
        columns.push_back(it - rows[0].begin());
    }
    auto document = MakeObject<Document>();
    auto table = MakeObject<Table>();
    table->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.0f, Color::get_LightGray()));
    table->set_DefaultCellBorder(MakeObject<BorderInfo>(BorderSide::Bottom, 1.0f, Color::get_LightGray()));
    for (size_t i = 0; i < std::min<size_t>(21, rows.size()); ++i)
    {
        auto row = table->get_Rows()->Add();
        if (i == 0)
            row->set_IsRowBroken(false);
        for (auto column : columns)
        {
            auto cell = row->get_Cells()->Add(column < rows[i].size() ? rows[i][column] : String::Empty);
            if (i == 0)
                cell->set_BackgroundColor(Color::get_LightGray());
        }
    }
    document->get_Pages()->Add()->get_Paragraphs()->Add(table);
    document->Save(outputFile);
}
```

## Related table topics

- [Working with Tables](/pdf/cpp/working-with-tables/)
- [Adding Tables](/pdf/cpp/adding-tables/)
- [Extracting Tables](/pdf/cpp/extracting-table/)
- [Manipulating Tables](/pdf/cpp/manipulating-tables/)
- [Removing Tables](/pdf/cpp/removing-tables/)
