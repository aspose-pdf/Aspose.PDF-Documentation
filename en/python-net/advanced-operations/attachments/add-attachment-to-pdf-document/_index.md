---
title: Adding Attachment to a PDF document using Python
linktitle: Adding Attachment to a PDF document
type: docs
weight: 10
url: /python-net/add-attachment-to-pdf-document/
description: This page describes how to add an attachment to a PDF file with Aspose.PDF for Python via .NET library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Tutorial on adding attachments to a PDF document using Python
Abstract: The article published by the Aspose.PDF Doc Team, offers a beginner-level tutorial on adding attachments to a PDF document using Python and the Aspose.PDF for Python via .NET library. It provides a step-by-step guide to creating a new Python project, importing the necessary Aspose.PDF package, and utilizing the `Document` and `FileSpecification` objects to embed files in a PDF. The process involves appending the `FileSpecification` object to the `EmbeddedFileCollection` of the `Document` object. The article includes a code snippet demonstrating how to implement this functionality, highlighting the efficiency and simplicity of the Aspose.PDF library for managing PDF documents programmatically. The tutorial is aimed at users interested in enhancing PDF documents with various file attachments, utilizing the Aspose.PDF library's capabilities.
---

Attachments can contain a wide variety of information and can be of a variety of file types. This article explains how to add an attachment to a PDF file.

1. Create a new Python project.
1. Import the Aspose.PDF package
1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
1. Create a [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) object with the file you are adding, and file description.
1. Add the [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) object to the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) collection, with the collection's [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) method.

The [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) collection contains all the attachments in the PDF file. The following code snippet shows you how to add an attachment in a PDF document.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Setup new file to be added as attachment
    fileSpecification = ap.FileSpecification(attachment_file, "Sample text file")

    # Add attachment to document's attachment collection
    document.embedded_files.append(fileSpecification)

    # Save new output
    document.save(output_pdf)
```

