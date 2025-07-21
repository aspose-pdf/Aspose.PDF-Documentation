---
title: Split PDF programmatically in Python
linktitle: Split PDF files
type: docs
weight: 60
url: /python-net/split-pdf-document/
description: This topic shows how to split PDF pages into individual PDF files in your Python applications.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Splitting PDF pages using Python
Abstract: The article discusses the process of splitting PDF pages into individual files using Python, highlighting the utility of such a feature for managing large PDF documents. It references the Aspose.PDF Splitter, an online tool designed to demonstrate PDF splitting functionality. The article provides a detailed method for achieving this in Python applications, involving iterating through a PDF document's pages via the `Document` object's `PageCollection`. For each page, a new `Document` object is created, the page is added to it, and the new PDF file is saved using the `save()` method. An accompanying Python code snippet illustrates this process, showcasing the steps necessary to split a PDF document into separate files by iterating through its pages and saving each as an individual PDF.
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

