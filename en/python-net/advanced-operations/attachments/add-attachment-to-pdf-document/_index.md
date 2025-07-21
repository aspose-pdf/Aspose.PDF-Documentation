---
title: Adding Attachment to a PDF document using Python
linktitle: Adding Attachment to a PDF document
type: docs
weight: 10
url: /python-net/add-attachment-to-pdf-document/
description: This page describes how to add an attachment to a PDF file with Aspose.PDF for Python via .NET library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add Attachments to PDF with Python
Abstract: This article provides a step-by-step guide on how to add attachments to a PDF file using Python and the Aspose.PDF library. It details the process of setting up a new Python project, importing the necessary Aspose.PDF package, and creating a `Document` object. The article explains how to create a `FileSpecification` object with the desired file and description, and how to add this object to the PDF document’s `EmbeddedFileCollection` using the `add` method. The `EmbeddedFileCollection` holds all attachments within the PDF. A code snippet is included to demonstrate the process of opening a document, setting up a file for attachment, appending it to the document’s attachment collection, and saving the updated PDF.
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

