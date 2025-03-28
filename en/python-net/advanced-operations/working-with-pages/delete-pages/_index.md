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
AlternativeHeadline: How to delete pages from PDF using Python
Abstract: This article provides a concise guide on how to delete pages from a PDF file using the Aspose.PDF library for Python via .NET. It focuses on utilizing the `PageCollection` class to remove specific pages. The process involves invoking the `delete()` method with the index of the page to be removed and then saving the updated document with the `save()` method. Additionally, a code snippet is provided to demonstrate the deletion of a page from a PDF file, illustrating the use of the Aspose.PDF library in a practical context.
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

