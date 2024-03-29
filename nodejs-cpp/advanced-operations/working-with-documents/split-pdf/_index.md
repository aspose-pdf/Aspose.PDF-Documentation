---
title: Split PDF in Node.js
linktitle: Split PDF files
type: docs
weight: 30
url: /nodejs-cpp/split-pdf/
description: This topic shows how to split PDF pages into individual PDF file with Aspose.PDF for Node.js via C++ .
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Split PDF into two files using Node.js

In case you want to split a single PDF into parts, you can use [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) function. 
Please check the following code snippet in order to split two PDFs in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF files which will be split.
1. Call `AsposePdf` as Promise and perform the operation for splitting file. Receive the object if successful.
1. Call the function [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Split two PDF files. It sets the variable pageToSplit to 1, indicating that the PDF file will be split at page 1. 
1. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultSplit1.pdf", and "ResultSplit2.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the `asposepdfnodejs` module.
1. Specify the name of the PDF files which will be split.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/).
1. Split two PDF files. It sets the variable pageToSplit to 1, indicating that the PDF file will be split at page 1. 
1. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultSplit1.pdf", and "ResultSplit2.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set number a page to split*/
  const pageToSplit = 1;
  /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```