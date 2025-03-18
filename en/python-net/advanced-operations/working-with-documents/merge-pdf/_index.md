---
title: How to Merge PDF using Python
linktitle: Merge PDF files
type: docs
weight: 50
url: /python-net/merge-pdf-documents/
description: This page explain how to merge PDF documents into a single PDF file with Python.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Combining multiple PDF files 
Abstract: The article "How to Merge PDF using Python" provides a guide for beginners on combining multiple PDF files into a single document using Python via the .NET framework, specifically utilizing the Aspose.PDF library. Merging PDF files can be beneficial for organization, efficient storage, and ease of sharing. The article details the process of merging PDFs by creating Document objects for each input file and utilizing the PageCollection's `add()` method to concatenate pages. The final output is saved using the `save()` method. A code snippet illustrates this procedure, demonstrating how to open PDF files, concatenate them, and save the merged document. Additionally, the article mentions an online application, Aspose.PDF Merger, allowing users to explore merging functionalities directly on the web.
---

## Merge or combine multiple PDF into single PDF in Python

Combining PDF files is a very popular query among users This can be useful when you have several PDF files that you want to share or store together as one document.

Merging PDF files can help you organize your documents, make room for storage on your PC, and share several PDF files with others by combining them into one document.

Merging PDF in Python via .NET is not straightforward task without using 3rd party library.
This article shows how to merge multiple PDF files into a single PDF document using Aspose.PDF for Python via .NET. 

## Merge PDF Files using Python and DOM

To concatenate two PDF files:

1. Create a New Document.
1. Merge the PDF Files
1. Save the Merged Document

Combining multiple PDF documents into a single file:

```python

    import aspose.pdf as apdf
    import aspose.pydrawing as asdrw
    from io import FileIO
    from os import path

    path_infile1 = path.join(self.dataDir, infile1)
    path_infile2 = path.join(self.dataDir, infile2)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document()
    document.merge(files=[path_infile1, path_infile2])
    document.save(path_outfile)
```

## Live Example

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) is an online free web application that allows you to investigate how presentation merging functionality works.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

