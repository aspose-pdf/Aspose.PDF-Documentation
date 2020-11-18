---
title: Removing attachment from an existing PDF 
type: docs
weight: 20
url: /net/removing-attachment-from-an-existing-pdf/
---
# Removing attachment from an existing PDF
Aspose.PDF can remove attachments from PDF files. A PDF document’s attachments are held in the Document object’s EmbeddedFiles collection.

To delete all attachments associated with a PDF file:

1. Call the [EmbeddedFiles](https://apireference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) collection’s [Delete](https://apireference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection/methods/delete) method.
1. Save the updated file using the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object’s [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) method.

The following code snippet shows how to remove attachments from a PDF document.

C#
```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Open document
Document pdfDocument = new Document(dataDir + "DeleteAllAttachments.pdf");

// Delete all attachments
pdfDocument.EmbeddedFiles.Delete();

dataDir = dataDir + "DeleteAllAttachments_out.pdf";

// Save updated file
pdfDocument.Save(dataDir);
```
