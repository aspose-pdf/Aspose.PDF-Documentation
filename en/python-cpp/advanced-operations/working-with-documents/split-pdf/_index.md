---
title: Split PDF programmatically in Python
linktitle: Split PDF files
type: docs
weight: 20
url: /python-cpp/split-pdf-document/
description: This topic shows how to split PDF pages into individual PDF files in your Python via C++ applications.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Splitting PDF pages can be a useful feature for those who want to split a large file into separate pages or groups of pages.

## Live Example

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) is an online free web application that allows you to investigate how presentation splitting functionality works.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

This topic shows how to split PDF pages into individual PDF files in your Python C++ applications. To split PDF pages into single page PDF files using Python, the following steps can be followed:

The code snippet sets up the necessary directories and file paths, opens a PDF document, and then loops through each page of the document. For each page, it creates a new document, copies the current page to the new document, and saves the new document as a separate PDF file with a specific naming convention.

1. Open the input document
1. Initialize the page count
1. Loop through all the pages of the document

## Split PDF into multiple files or separate PDFs in Python

The following Python code snippet shows you how to split PDF pages into individual PDF files.

```python

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    dataDir = os.path.join(os.getcwd(), "samples")
    input_file= os.path.join(dataDir , "sample.pdf")
    outputFolder = os.path.join(dataDir , "results")
    # Open document
    document = apw.Document(inputFile)

    pageCount = 1

    # Loop through all the pages

    while (pageCount <= document.pages.count()):
        page = document.pages[pageCount]    
        newDocument = apw.Document()
        newDocument.pages.copy_page(page)
        newDocument.save(os.path.join(outputFolder,"page_" + str(pageCount) + "_out" + ".pdf"))
        pageCount += 1
```

