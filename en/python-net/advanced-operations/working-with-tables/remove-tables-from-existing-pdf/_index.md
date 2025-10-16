---
title: Remove Tables from existing PDF
linktitle: Remove Tables
type: docs
weight: 50
url: /python-net/removing-tables/
lastmod: "2025-09-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to delete tables from PDF using Python
Abstract: This article discusses the functionality of Aspose.PDF for Python via .NET, specifically focusing on the manipulation of tables within PDF documents. The library allows users to insert or create tables in both new and existing PDF files, as well as manipulate or remove tables from existing PDFs. The article introduces the `TableAbsorber` class, which is crucial for identifying and interacting with tables in a PDF. A new method, `remove()`, has been added to enable the removal of tables. The document provides two code snippets - one demonstrating how to remove a single table from a PDF, and another illustrating the removal of multiple tables. These examples highlight the practical application of the `TableAbsorber` class to achieve table removal from PDF documents.
---

## Remove Table from PDF document

Aspose.PDF for Python allows you to remove a table from a PDF. It opens an existing PDF, detects the first table on the first page with TableAbsorber, deletes that table using the [remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods). After save the updated PDF to a new file.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(path_outfile)
```

## Remove all Tables from PDF document

With our library, you can remove all tables from a specific page in a PDF. The code opens an existing PDF, detects all tables on the second page with TableAbsorber, iterates through the detected tables, removes each one, and then saves the modified PDF to a new file. It is useful when you need to bulk-remove tables from a page while leaving the rest of the PDF content intact.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(path_outfile)
```

