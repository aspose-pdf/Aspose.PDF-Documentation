---
title: Removing attachment from PDF 
linktitle: Removing attachment from an existing PDF
type: docs
weight: 30
url: /cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF for C++ can remove attachments from your PDF documents. Use C++ PDF API to remove attachments in PDF files using Aspose.PDF library.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF can remove attachments from PDF files. A PDF document’s attachments are held in the Document object’s EmbeddedFiles collection.

To delete all attachments associated with a PDF file:

1. Call the [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) collection’s [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection#afff8b235b554a66c203464b61204b843) method.
1. Save the updated file using the [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object’s Save method.

The following code snippet shows how to remove attachments from a PDF document.

```cpp
void WorkingWithAttachments::RemovingAttachment() {

 String _dataDir("C:\\Samples\\");

 // Open document
 auto pdfDocument = new Document(_dataDir + u"DeleteAllAttachments.pdf");

 // Delete all attachments
 pdfDocument->get_EmbeddedFiles()->Delete();

 // Save updated file
 pdfDocument->Save(_dataDir + u"DeleteAllAttachments_out.pdf");
}
```
