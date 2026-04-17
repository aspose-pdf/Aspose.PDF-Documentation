---
title: Remove Attachments from PDF in Python
linktitle: Removing attachment from an existing PDF
type: docs
weight: 30
url: /python-net/removing-attachment-from-an-existing-pdf/
description: Learn how to remove embedded file attachments from PDF documents in Python using Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to delete attachments from PDF with Python
Abstract: This article discusses how to remove attachments from PDF files using Aspose.PDF for Python. Attachments in a PDF document are stored within the `EmbeddedFiles` collection of the `Document` object. To delete all attachments from a PDF, you can invoke the `delete()` method on the `EmbeddedFiles` collection and then save the updated document using the `save()` method of the `Document` object. A code snippet is provided to demonstrate this process, showcasing the steps of opening a document, deleting its attachments, and saving the modified file.
---

Aspose.PDF for Python can remove attachments from PDF files. A PDF document's attachments are held in the Document object's [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) collection.

This workflow is useful when you need to clean up outdated embedded files, reduce package size, or prepare a PDF for redistribution without attached source materials.

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

## Related Attachment Topics

- [Work with PDF attachments in Python](/pdf/python-net/attachments/)
- [Add attachments to PDF in Python](/pdf/python-net/add-attachment-to-pdf-document/)
- [Create and manage PDF portfolios in Python](/pdf/python-net/portfolio/)

