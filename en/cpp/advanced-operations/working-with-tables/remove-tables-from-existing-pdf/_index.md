---
title: Remove Tables from Existing PDF Documents in C++
linktitle: Removing Tables
type: docs
weight: 50
url: /cpp/removing-tables/
description: Remove the first detected table or all detected tables from a selected PDF page in C++.
lastmod: "2026-11-23"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete Detected PDF Tables with TableAbsorber in C++
Abstract: Find tables on a selected PDF page and remove one or all of the detected tables. Both examples process the first page.
---

## Remove the first table from a page

1. Open the input PDF as a [`Document`](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and select page 1.
2. Call [`TableAbsorber::Visit()`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/visit/) to find the tables on that page.
3. Call [`TableAbsorber::Remove()`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/remove/) with the first detected table and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <system/collections/list.h>
#include <stdexcept>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void RemoveOneTable(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    auto absorber = MakeObject<TableAbsorber>();
    absorber->Visit(page);
    if (absorber->get_TableList()->get_Count() == 0)
        throw std::runtime_error("No tables found");
    absorber->Remove(absorber->get_TableList()->idx_get(0));
    document->Save(outputFile);
}
```

## Remove all detected tables from a page

1. Open the input PDF as a [`Document`](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and select page 1.
2. Call [`TableAbsorber::Visit()`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/visit/) to find the tables on that page.
3. Copy the detected [`AbsorbedTable`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/absorbedtable/) objects into a vector before removing them.
4. Call [`TableAbsorber::Remove()`](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/remove/) for every copied table and save the PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <system/collections/list.h>
#include <vector>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void RemoveAllTables(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);
    auto absorber = MakeObject<TableAbsorber>();
    absorber->Visit(page);
    std::vector<SharedPtr<AbsorbedTable>> tables;
    for (auto table : absorber->get_TableList())
        tables.push_back(table);
    for (auto table : tables)
        absorber->Remove(table);
    document->Save(outputFile);
}
```

## Related table topics

- [Working with Tables](/pdf/cpp/working-with-tables/)
- [Adding Tables](/pdf/cpp/adding-tables/)
- [Extracting Tables](/pdf/cpp/extracting-table/)
- [Integrating Tables with Data Sources](/pdf/cpp/integrate-table/)
- [Manipulating Tables](/pdf/cpp/manipulating-tables/)
