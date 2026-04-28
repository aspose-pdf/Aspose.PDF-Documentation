---
title: Add PDF Pages in Python
linktitle: Adding Pages
type: docs
weight: 10
url: /python-net/add-pages/
description: Learn how to add or insert pages into PDF documents in Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add or insert PDF pages with Python
Abstract: This article explains how to add pages to PDF files using Aspose.PDF for Python via .NET. Learn how to insert blank pages at specific positions, append pages at the end of a document, and import a page from another PDF using Document and PageCollection APIs.
---

Aspose.PDF for Python via .NET provides flexible page-level operations for PDF documents. You can manage pages through [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) and add pages to a [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) at specific positions or at the end of the file.

Use this page when you need to insert new blank pages into an existing PDF or append pages to the end of a document during generation workflows.

## Add or Insert Pages in a PDF File

Aspose.PDF for Python via .NET supports both page insertion at a specific index and appending pages at the end of a PDF.

### Insert an Empty Page in a PDF File

To insert an empty page in a PDF file:

1. Open an existing [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) using appropriate methods.
1. Insert a new empty page at a specific index using the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `insert()` method.
1. Save the modified [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to the desired output path.

Insert an empty page into an existing PDF file at a specified position:

```python
import aspose.pdf as ap

def insert_empty_page(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.insert(2)
    document.save(output_file_name)
```

### Add an Empty Page at the End of a PDF File

Sometimes, you want to ensure that a document ends on an empty page. This topic explains how to insert an empty page at the end of the PDF document.

To insert an empty page at the end of a PDF file:

1. Open an existing [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) using appropriate methods.
1. Add a new empty page to the end of the document using the [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) `add()` method.
1. Save the updated [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

The following code snippet shows you how to insert an empty page at the end of a PDF file.

```python
import aspose.pdf as ap

def add_empty_page_to_end(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document(input_file_name)
    document.pages.add()
    document.save(output_file_name)
```

### Add a Page from Another PDF Document

With Aspose.PDF for Python via .NET, you can create a new [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/), add an initial page, and then import a page from another PDF into it.

1. Create a new [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Add a new blank [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) and write some text on it using [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/).
1. Open another existing [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Copy a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) from that document.
1. Paste the copied page into your main document using [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. Save the combined file.

```python
import aspose.pdf as ap

def add_page_from_another_document(input_file_name: str, output_file_name: str) -> None:
    document = ap.Document()
    page = document.pages.add()
    text_fragment = ap.text.TextFragment("This is first page!")
    page.paragraphs.add(text_fragment)

    another_document = ap.Document(input_file_name)
    document.pages.add(another_document.pages[1])

    document.save(output_file_name)
```

## Related Page Topics

- [Work with PDF pages in Python](/pdf/python-net/working-with-pages/)
- [Move PDF pages in Python](/pdf/python-net/move-pages/)
- [Delete PDF pages in Python](/pdf/python-net/delete-pages/)
- [Extract PDF pages in Python](/pdf/python-net/extract-pages/)
