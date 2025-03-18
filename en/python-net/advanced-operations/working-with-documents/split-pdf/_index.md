---
title: Split PDF programmatically in Python
linktitle: Split PDF files
type: docs
weight: 60
url: /python-net/split-pdf-document/
description: This topic shows how to split PDF pages into individual PDF files in your Python applications.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to Split PDF files via Python
Abstract: The article, authored and published by the Aspose.PDF Doc Team, provides a guide for splitting PDF documents into individual pages using Python. It targets beginners and outlines a straightforward method to accomplish this task programmatically by leveraging the Aspose.PDF library. The process involves iterating through the pages of a PDF document, creating a new document for each page, and saving these as separate PDF files. A sample Python code snippet is provided to demonstrate the implementation. Additionally, the article highlights the availability of the Aspose.PDF Splitter, a free online tool for splitting PDFs, and includes links to Aspose's resources and contact information.
---

Splitting PDF pages can be a useful feature for those who want to split a large file into separate pages or groups of pages.

## Live Example

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) is an online free web application that allows you to investigate how presentation splitting functionality works.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

This topic shows how to split PDF pages into individual PDF files in your Python applications. To split PDF pages into single page PDF files using Python, the following steps can be followed:

1. Loop through the pages of PDF document through the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection
1. For each iteration, create a new Document object and add the individual [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) object into the empty document
1. Save the new PDF using [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method

## Split PDF into multiple files or separate pdfs in Python

The following Python code snippet shows you how to split PDF pages into individual PDF files.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```

