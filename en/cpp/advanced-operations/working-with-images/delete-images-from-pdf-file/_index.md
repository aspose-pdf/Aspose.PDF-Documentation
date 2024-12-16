---
title: Delete Images from PDF File using C++
linktitle: Delete Images
type: docs
weight: 20
url: /cpp/delete-images-from-pdf-file/
description: This section explain how to delete Images from PDF File using Aspose.PDF for C++.
lastmod: "2021-12-18"
---

To delete an image from a PDF file:

1. Create a [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) object and open the input PDF file.
1. Get the Page that holds the image from the Document object's [Pages collection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. Images are held in the Images collection, found in the page's Resources collection.
1. Delete an image with the Images collection's Delete method.
1. Saved the output like using the Document object's Save method.

The following code snippet shows how to delete an image from a PDF file.

```cpp
void WorkingWithImages::DeleteImagesFromPDFFile()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"DeleteImages.pdf");

    // Delete a particular image
    document->get_Pages()->idx_get(1)->get_Resources()->get_Images()->Delete(1);

    // Save updated PDF file
    document->Save(_dataDir + u"DeleteImages_out.pdf");
}
```
