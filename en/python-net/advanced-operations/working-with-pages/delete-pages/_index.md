---
title: Delete PDF Pages programmatically Python
linktitle: Delete PDF Pages
type: docs
weight: 80
url: /python-net/delete-pages/
description: You can delete pages from your PDF file using Aspose.PDF for Python via .NET library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to remove PDF Pages programmatically Python
Abstract: The article titled "Delete PDF Pages programmatically Python" provides a beginner-friendly guide on how to remove pages from a PDF using the Aspose.PDF for Python via .NET library. It offers a step-by-step method to delete a specific page from a PDF file by first calling the `delete()` method on the `PageCollection` to specify the page index, followed by using the `save()` method to update the file. The article includes a practical code snippet to illustrate the process, demonstrating how to open a document, delete a page, and save the modified document. This guide aims to simplify PDF page manipulation for users, highlighting the capabilities of the Aspose.PDF library, which is available across multiple operating systems and offers a variety of features for PDF document generation and manipulation.
---

You can delete pages from a PDF file using Aspose.PDF for Python via .NET. To delete a particular page from the [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection.

## Delete Page from PDF File

1. Call the [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) method and specify the page's index
1. Call the [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method to save the updated PDF file
The following code snippet shows how to delete a particular page from the PDF file using Python.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.pages.delete(2)
    document.save(path_outfile)
```

