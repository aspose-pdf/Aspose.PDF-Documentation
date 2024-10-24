---
title: Manipulate Tables in existing PDF
linktitle: Manipulate Tables
type: docs
weight: 40
url: /cpp/manipulate-tables-in-existing-pdf/
description: This section covers various methods for table modification using Aspose.PDF for C++
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Manipulate tables in existing PDF

Aspose.PDF for C++ allows you to quickly and efficiently work with tables, namely, create them from scratch or add to existing PDF documents.

You also get the ability to integrate the table with the database (DOM) to create dynamic tables based on the contents of the database.

The [Aspose.PDF.Text.TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) class allows you to search and parse simple tables that already exist on a PDF document page. The following code snippet shows the steps to update the content in a specific cell in a table.

>Headers:

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

#include "Table-Manipulate.h"

void ManipulateTables() {

    String _dataDir("C:\\Samples\\");

    // Load existing PDF file
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Create TableAbsorber object to find tables
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visit first page with absorber
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Get access to first table on page, their first cell and text fragments in it
    auto fragment = absorber->get_TableList()->idx_get(0)->get_RowList()->idx_get(0)->get_CellList()->idx_get(0)->get_TextFragments()->idx_get(1);

    // Change text of the first text fragment in the cell
    fragment->set_Text(u"hi world");
    document->Save(_dataDir + u"ManipulateTable_out.pdf");
}
```

## Replace old Table with a new one in PDF document

In case you need to find a particular table and replace it with the desired one, you can use Replace() the method of [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) Class in order to do that.

The following example demonstrate the functionality to replace the table inside the PDF document:

```cpp
void ReplaceOldTable() {
    String _dataDir("C:\\Samples\\");

    // Load existing PDF file
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Create TableAbsorber object to find tables
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visit first page with absorber
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Get first table on the page
    auto table = absorber->get_TableList()->idx_get(0);

    // Create new table
    auto newTable = MakeObject<Table>();
    newTable->set_ColumnWidths(u"100 100 100");
    newTable->set_DefaultCellBorder (MakeObject<BorderInfo>(BorderSide::All, 1.0F));

    auto row = newTable->get_Rows()->Add();
    row->get_Cells()->Add(u"Col 1");
    row->get_Cells()->Add(u"Col 2");
    row->get_Cells()->Add(u"Col 3");

    // Replace the table with new one
    absorber->Replace(document->get_Pages()->idx_get(1), table, newTable);

    // Save document
    document->Save(_dataDir + u"TableReplaced_out.pdf");
}
```
