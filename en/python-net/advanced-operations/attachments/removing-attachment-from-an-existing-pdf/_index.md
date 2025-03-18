---
title: Removing attachment from PDF using Python
linktitle: Removing attachment from an existing PDF
type: docs
weight: 30
url: /python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF can remove attachments from your PDF documents. Use Python PDF API to remove attachments in PDF files using Aspose.PDF for Python via .NET library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on how to remove attachments from PDF using the Aspose.PDF for Python
Abstract: The article titled "Removing attachment from PDF" provides a beginner-level guide on how to remove attachments from PDF files using the Aspose.PDF library for Python. The document's attachments are stored in the `EmbeddedFiles` collection of the `Document` object. To delete all attachments, one must call the `delete()` method on the `EmbeddedFiles` collection and then save the updated file using the `save()` method of the `Document` object. The article includes a code snippet demonstrating this process. Aspose.PDF for Python is a versatile library that facilitates PDF manipulation, and its applications are available for download across various operating systems. The library is published by Aspose.PDF, which offers customer support and resources through various online platforms.
---

Aspose.PDF for Python can remove attachments from PDF files. A PDF document's attachments are held in the Document object's [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) collection.

To delete all attachments associated with a PDF file:

1. Call the [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) collection's [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) method.
1. Save the updated file using the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method.

The following code snippet shows how to remove attachments from a PDF document.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all attachments
    document.embedded_files.delete()

    # Save updated file
    document.save(output_pdf)
```

