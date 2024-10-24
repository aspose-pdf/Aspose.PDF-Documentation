---
title: Set Size of PDF using pythob via C++
linktitle: Set Size of PDF
type: docs
weight: 30
url: /python-cpp/get-and-set-page-properties/
description: This section shows how to get or set PDF page properties such as size of document using Python via C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Set Size of PDF file

Aspose.PDF for Python via C++ lets you read and set properties of pages in a PDF file in your Python applications.

The next code snippet opens a PDF file, resizes the first page by adjusting the **Crop box** (the crop box is the "page" size at which your PDF document is displayed in Adobe Acrobat), and saves the modified document to a new file.

1. Create a document object from the input file
1. Get the pages collection from the document using [document_get_pages](https://reference.aspose.com/pdf/python-cpp/core/document_get_pages/)
1. Get the first page from the pages collection with [page_collection_get_page](https://reference.aspose.com/pdf/python-cpp/core/page_collection_get_page/)
1. Get the crop box rectangle from the page using [page_get_rectangle](https://reference.aspose.com/pdf/python-cpp/core/page_get_rectangle/)
1. Calculate the new coordinates for the crop box
1. Update the crop box coordinates with the new values
1. Save the modified document to the output file with 'document.save' method

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Get the current working directory and create the path to the "samples" directory
    dataDir = os.path.join(os.getcwd(), "samples")

    # Create the input and output file paths
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "resized_document.pdf")

    # Create a document object from the input file
    doc = apCore.document_create_from_file(inputFile)

    # Get the pages collection from the document
    pages = apCore.document_get_pages(doc)

    # Get the first page from the pages collection
    page = apCore.page_collection_get_page(pages, 1)

    # Get the crop box rectangle from the page
    crop_box = apCore.page_get_rectangle(page)

    # Calculate the new coordinates for the crop box
    LLX = apCore.rectangle_get_LLX(crop_box) + 10
    LLY = apCore.rectangle_get_LLY(crop_box) + 10
    URX = apCore.rectangle_get_URX(crop_box) - 10
    URY = apCore.rectangle_get_URY(crop_box) - 10

    # Update the crop box coordinates with the new values
    apCore.rectangle_set_LLX(crop_box, LLX)
    apCore.rectangle_set_LLY(crop_box, LLY)
    apCore.rectangle_set_URX(crop_box, URX)
    apCore.rectangle_set_URY(crop_box, URY)

    # Save the modified document to the output file
    apCore.document_save(doc, output_file)

    # Close the document handle
    apCore.close_handle(doc)
```



