---
title: Remove Tables from existing PDF
linktitle: Remove Tables
type: docs
weight: 50
url: /python-net/remove-tables-from-existing-pdf/
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to delete tables from PDF using Python
Abstract: This article discusses the functionality of Aspose.PDF for Python via .NET, specifically focusing on the manipulation of tables within PDF documents. The library allows users to insert or create tables in both new and existing PDF files, as well as manipulate or remove tables from existing PDFs. The article introduces the `TableAbsorber` class, which is crucial for identifying and interacting with tables in a PDF. A new method, `remove()`, has been added to enable the removal of tables. The document provides two code snippets - one demonstrating how to remove a single table from a PDF, and another illustrating the removal of multiple tables. These examples highlight the practical application of the `TableAbsorber` class to achieve table removal from PDF documents.
---

{{% alert color="primary" %}}

Aspose.PDF for Python via .NET offers the capabilities to insert/create Table inside PDF document while its being generated from scratch or you can also add the table object in any existing PDF document. However you may have a requirement to [Manipulate Tables in existing PDF](https://docs.aspose.com/pdf/python-net/manipulate-tables-in-existing-pdf/) where you can update the contents in existing table cells. However you may come across a requirement to remove table objects from existing PDF document.

{{% /alert %}}

In order to remove the tables, we need to use [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) class to get hold of tables in existing PDF and then call [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods).

## Remove Table from PDF document

We have added new function i.e. [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) to the existing [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) Class in order to remove table from PDF document. Once the absorber successfully finds tables on the page, it becomes capable to remove them. Please check following code snippet showing how to remove a table from PDF document:

```python

    import aspose.pdf as ap

    # Load existing PDF document
    pdf_document = ap.Document(input_file)
    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(pdf_document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    pdf_document.save(output_file)
```

## Remove Multiple Tables from PDF document

Sometimes a PDF document may contain more than one table and you may come up with a requirement to remove multiple tables from it. In order to remove multiple tables from PDF document, please use the following code snippet:

```python

    import aspose.pdf as ap

    # Load existing PDF document
    pdf_document = ap.Document(input_file)
    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(pdf_document.pages[1])
    # Get copy of table collection
    tables = absorber.table_list
    #  Loop through the copy of collection and removing tables
    for table in tables:
        absorber.remove(table)
    # Save document
    pdf_document.save(output_file)
```

