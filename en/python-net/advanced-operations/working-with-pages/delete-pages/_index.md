---
title: Deleting PDF Pages programmatically Python
linktitle: Deleting PDF Pages
type: docs
weight: 80
url: /python-net/delete-pages/
description: You can delete pages from your PDF file using Aspose.PDF for Python via .NET library.
lastmod: "2025-11-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to delete pages from PDF using Python
Abstract: This article provides a concise guide on how to delete pages from a PDF file using the Aspose.PDF library for Python via .NET. It focuses on utilizing the `PageCollection` class to remove specific pages. The process involves invoking the `delete()` method with the index of the page to be removed and then saving the updated document with the `save()` method. Additionally, a code snippet is provided to demonstrate the deletion of a page from a PDF file, illustrating the use of the Aspose.PDF library in a practical context.
---

You can delete pages from a PDF file using Aspose.PDF for Python via .NET. To delete a particular page from the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection.

## Delete Page from PDF File

Aspose.PDF for Python via .NET deletes page 2 from the input PDF and saves the updated document to a new file. This feature is helpful for removing unwanted or sensitive pages without altering the rest of the document.

1. Load the input PDF.
1. Delete page.
1. Call the [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method to save the updated PDF file.

The following code snippet shows how to delete a particular page from the PDF file using Python.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_page(input_file_name, output_file_name):
    """
    Delete a single page from a PDF document.

    Demonstrates how to remove a specific page from a PDF document using
    the Aspose.PDF library. This function deletes page 2 from the input
    document and saves the result to a new file.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete a page.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes page 2 (1-based indexing) from the document
        - Page numbering is 1-based (page 2 is the second page)
        - The original document is not modified; a new file is created
        - If the document has fewer than 2 pages, this may raise an error

    Example:
        >>> delete_page("input.pdf", "output.pdf")
        # Removes page 2 from input.pdf and saves result as output.pdf
    """
    document = ap.Document(input_file_name)
    document.pages.delete(2)
    document.save(output_file_name)
```

## Delete Multiple Pages from a PDF Document

Deleting multiple pages allows you to remove a set of specified pages in a single operation, which is more efficient than deleting pages one by one. The resulting PDF is saved to a new file, preserving the original document.

1. Load the input PDF.
1. Delete the pages listed in the pages array.
1. Save the updated document to a new file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def delete_bunch_pages(input_file_name, output_file_name):
    """
    Delete multiple pages from a PDF document in a single operation.

    Demonstrates bulk page deletion by removing multiple specified pages
    from a PDF document. This is more efficient than deleting pages
    one by one when removing multiple pages.

    Args:
        input_file_name (str): Path to the input PDF file from which to delete pages.
        output_file_name (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Deletes pages 2, 3, 4, 6, 7, and 9 in this example
        - Page numbers are 1-based (page 2 is the second page)
        - Pages are deleted in the order specified in the list
        - The original document is not modified; a new file is created
        - Ensure the document has enough pages to avoid errors
        - Page numbers should be adjusted if the source document has fewer pages

    Example:
        >>> delete_bunch_pages("input.pdf", "output.pdf")
        # Removes pages 2, 3, 4, 6, 7, and 9 from input.pdf
    """
    document = ap.Document(input_file_name)
    # Example: Deleting pages 2, 3, 4, 6, 7, and 9; modify this list as needed for your use case.
    pages = [2,3,4,6,7,9]
    document.pages.delete(pages)
    document.save(output_file_name)
```
