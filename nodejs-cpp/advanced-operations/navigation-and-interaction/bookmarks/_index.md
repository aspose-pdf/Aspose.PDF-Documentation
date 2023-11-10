---
title: Bookmarks in PDF in Node.js
linktitle: Bookmarks in PDF
type: docs
weight: 10
url: /nodejs-cpp/bookmark/
description: You can add or delete a bookmarks in PDF document in the Node.js environment.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Delete a Particular Bookmark from a PDF Document

You can delete bookmarks from a PDF file using Aspose.PDF for Node.js via C++. In case you want to delete bookmarks from a PDF, you can use [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) function. 
Please check the following code snippet in order to delete bookmarks from a PDF file in Node.js environment.

**CommonJS:**

```cjs

    const AsposePdf = require('.//AsposePDFforNode.cjs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

```mjs

    import AsposePdf from './/AsposePDFforNode.mjs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```