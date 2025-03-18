---
title: Remove Tables from existing PDF
linktitle: Remove Tables
type: docs
weight: 50
url: /python-net/remove-tables-from-existing-pdf/
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to remove Tables from existing PDF
Abstract: The article, authored, provides a beginner-level guide on how to remove tables from existing PDF documents using Aspose.PDF for Python via .NET. It discusses the use of the `TableAbsorber` class, which can identify and manipulate tables within a PDF. The article offers code snippets demonstrating how to utilize the `remove()` method of the `TableAbsorber` class to delete single or multiple tables from PDF documents. This functionality is particularly useful for users who need to manage and edit tables in PDF files dynamically. The article is published by the Aspose.PDF Doc Team and is targeted at users interested in PDF document generation and manipulation.
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

