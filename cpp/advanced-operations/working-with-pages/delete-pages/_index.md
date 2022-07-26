---
title: Delete PDF Pages programmatically 
linktitle: Delete PDF Pages
type: docs
weight: 30
url: /cpp/delete-pages/
description: You can delete pages from your PDF file using C++ library.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

You can delete pages from a PDF file using Aspose.PDF for C++. To delete a particular page from the [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) collection.

## Delete Page from PDF File

1. Call the [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a02bb7a96e66ef6e10bcf4930b299b3b7) method and specify the page’s index
1. Call the Save method to save the updated PDF file
The following code snippet shows how to delete a particular page from the PDF file using C++.

```cpp
void DeletePDFPages() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("DeleteParticularPage.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Delete a particular page
    document->get_Pages()->Delete(2);

    // Save updated PDF
    document->Save(_dataDir + inputFileName);
}
```
