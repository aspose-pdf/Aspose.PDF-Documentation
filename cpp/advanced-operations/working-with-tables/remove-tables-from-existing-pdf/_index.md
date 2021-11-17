---
title: Remove Tables from existing PDF
linktitle: Remove Tables
type: docs
weight: 50
url: /cpp/remove-tables-from-existing-pdf/
description: This section describes how to remove Table from PDF document.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for C++ allows you to insert and create a Table inside PDF document while it's being generated from scratch or you can also add the table object in any existing PDF document. But you may have a requirement to [Manipulate Tables in existing PDF](https://docs.aspose.com/pdf/cpp/manipulate-tables-in-existing-pdf/) where you can update the contents in existing table cells. Also, you may come across a requirement to remove table objects from the existing PDF documents.

In order to remove the tables, we need to use [TableAbsorber](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) class to get hold of tables in existing PDF and then call 'Remove' method.

## Remove Table from PDF document

We have added new function i.e. [Remove](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber#ace39006d8f44c9cb776ee26281a1cbb3) to the existing TableAbsorber Class in order to remove table from PDF document. Once the absorber successfully finds tables on the page, it becomes capable to remove them. Please check following code snippet showing how to remove a table from PDF document:

>Headers:

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void RemoveTable() {

    String _dataDir("C:\\Samples\\");

    // Load source PDF document
    auto document = MakeObject<Document>(_dataDir + u"Table_input.pdf");

    // Create TableAbsorber object to find tables
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visit first page with absorber
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Get first table on the page
    auto table = absorber->get_TableList()->idx_get(0);

    // Remove the table
    absorber->Remove(table);

    // Save PDF
    document->Save(_dataDir + u"Table_out.pdf");
}
```

## Remove Multiple Tables from PDF document

Some tasks will be associated with working with several tables in one pdf document.
And you will need to delete several tables from it. To remove multiple tables from a PDF document, use the following code snippet:

```cpp
void RemoveMultipleTables() {

    String _dataDir("C:\\Samples\\");

    // Load existing PDF document
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Create TableAbsorber object to find tables
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Visit first page with absorber
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Get copy of table collection
    auto tables = absorber->get_TableList();


    // Loop through the copy of collection and removing tables
    for(auto table : tables)
    absorber->Remove(table);

    // Save document
    document->Save(_dataDir + u"Table2_out.pdf");
}
```

{{% alert color="primary" %}}

Please take into account that removing or replacing of a table changes TableList collection. Therefore, in case removing/replacing tables in a loop the copying of TableList collection is essential.

{{% /alert %}}
