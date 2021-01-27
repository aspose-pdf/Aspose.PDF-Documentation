---
title: Delete Images from PDF File
linktitle: Delete Images
type: docs
weight: 40
url: /net/delete-images-from-pdf-file/
description: This section explain how to delete Images from PDF File using Aspose.PDF for .NET.
lastmod: "2021-01-27"
---

To delete an image from a PDF file:

1. Create a Document object and open the input PDF file.
1. Get the Page that holds the image from the Document object’s Pages collection.
1. Images are held in the Images collection, found in the page’s Resources collection.
1. Delete an image with the Images collection’s Delete method.
1. Saved the output like using the Document object’s Save method.
1. The following code snippet shows how to delete an image from a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Open document
Document pdfDocument = new Document(dataDir+ "DeleteImages.pdf");

// Delete a particular image
pdfDocument.Pages[1].Resources.Images.Delete(1);

dataDir = dataDir + "DeleteImages_out.pdf";
// Save updated PDF file
pdfDocument.Save(dataDir);
```
