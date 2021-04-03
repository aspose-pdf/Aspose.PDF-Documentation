---
title: Replace Image in Existing PDF File
linktitle: Replace Image
type: docs
weight: 70
url: /net/replace-image-in-existing-pdf-file/
description: This section describes about replace image in existing PDF file using C# library.
lastmod: "2021-01-27"
---

The Images collection’s [Replace](https://apireference.aspose.com/pdf/net/aspose.pdf/ximagecollection/methods/replace/index) method allows you to replace an image in an existing PDF file.

The Images collection can be found in a page’s Resources collection. To replace an image:

1. Open the PDF file using the Document object.
2. Replace a particular image, save the updated PDF file using Save method of the Document object.

The following code snippet shows you how to replace an image in a PDF file.

```csharp
// Open document
Document pdfDocument = new Document("input.pdf");
// Replace a particular image
pdfDocument.Pages[1].Resources.Images.Replace(1, new FileStream("lovely.jpg", FileMode.Open));
// Save updated PDF file
pdfDocument.Save("output.pdf");
```
