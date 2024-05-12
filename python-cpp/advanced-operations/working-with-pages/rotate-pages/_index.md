---
title: Rotate PDF Pages Using Python via C++
linktitle: Rotate PDF Pages
type: docs
weight: 20
url: /python-cpp/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically with Python via C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Sometimes, PDF pages may have incorrect orientation due to scanning or creation issues. Rotating the pages ensures that they are displayed in the correct orientation for easier reading and viewing.
Rotating PDF pages helps maintain a consistent viewing experience across different devices and platforms. 

Rotating PDF pages can facilitate editing tasks such as adding annotations, comments, or signatures. By rotating pages to the desired orientation, you can make editing and reviewing processes more efficient.

Also, when printing PDF documents, it's important to ensure that pages are oriented correctly to avoid misalignment or cropping issues. Rotating pages as needed before printing helps optimize the printing output and ensures that the content is displayed as intended.
Rotating PDF pages is a useful feature that helps improve the readability, consistency, and presentation of documents across various contexts and purposes.

This topic describes how to update or change the page orientation of pages in an existing PDF file programmatically with Python.

## Change Page Orientation

Aspose.PDF for Python via C++ support great features like changing the page orientation 

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Creating a path to the directory containing the sample files
    dataDir = os.path.join(os.getcwd(), "samples")

    # Creating paths to the input and output files
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "rotated_document.pdf")

    # Creating a document object by loading the input file
    doc = apCore.document_create_from_file(inputFile)

    # Getting the collection of pages in the document
    pages = apCore.document_get_pages(doc)

    # Getting the first page from the collection
    page = apCore.page_collection_get_page(pages, 1)

    # Rotating the page by 90 degrees clockwise
    apCore.page_set_rotate(page, apCore.Rotation(apCore.on90))

    # Saving the modified document to the output file
    apCore.document_save(doc, output_file)

    # Closing the document handle to release resources
    apCore.close_handle(doc)
```

