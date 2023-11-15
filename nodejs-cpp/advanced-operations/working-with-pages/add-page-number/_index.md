---
title: Add Page Number to PDF in Node.js via C++ 
linktitle: Add Page Number
type: docs
weight: 100
url: /nodejs-cpp/add-page-number/
description: Aspose.PDF for Node.js via C++ allows you to add Page Number Stamp to your PDF file using AsposePdfAddPageNum.
lastmod: "2023-10-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document.

The following code snippets shows how to add a page numbers to PDF pages using the [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/) function in Node.js.

Please check the following code snippet in order to add a page numbers into PDF in Node.js environment.

**CommonJS:**

1. Require the AsposePDFforNode.cjs module.
1. Specify the name of the PDF file in which the page numbers will be added.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Add page number to a PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultAddPageNum.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Add page number to a PDF-file save the "ResultAddPageNum.pdf"*/
      const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
      console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. Specify the name of the PDF file in which the page numbers will be added.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfAddPageNum](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddpagenum/).
1. Add page number to a PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultAddPageNum.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Add page number to a PDF-file and save the "ResultAddPageNum.pdf"*/
  const json = AsposePdfModule.AsposePdfAddPageNum(pdf_file, "ResultAddPageNum.pdf");
  console.log("AsposePdfAddPageNum => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```