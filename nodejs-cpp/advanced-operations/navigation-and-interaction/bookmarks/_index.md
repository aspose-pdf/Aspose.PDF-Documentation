---
title: Bookmarks in PDF in Node.js
linktitle: Bookmarks in PDF
type: docs
weight: 10
url: /nodejs-cpp/bookmark/
description: You can add or delete a bookmarks in PDF document in the Node.js environment.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Delete a Particular Bookmark from a PDF Document

You can delete bookmarks from a PDF file using Aspose.PDF for Node.js via C++. In case you want to delete bookmarks from a PDF, you can use [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/) function. 
Please check the following code snippet in order to delete bookmarks from a PDF file in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file from which the bookmarks will be removed.
1. Call `AsposePdf` as Promise and perform the operation for removing bookmark. Receive the object if successful.
1. Call the function [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Delete bookmarks. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPdfDeleteBookmarks.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

    const AsposePdf = require('asposepdfnodejs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
        console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Import the `asposepdfnodejs` module.
1. Specify the name of the PDF file from which the bookmarks will be removed.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletebookmarks/).
1. Delete bookmarks. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPdfDeleteBookmarks.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

    import AsposePdf from 'asposepdfnodejs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteBookmarks(pdf_file, "ResultPdfDeleteBookmarks.pdf");
    console.log("AsposePdfDeleteBookmarks => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```