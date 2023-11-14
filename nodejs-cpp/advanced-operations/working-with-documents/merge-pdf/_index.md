---
title: How to Merge PDF in Node.js
linktitle: Merge PDF files
type: docs
weight: 20
url: /nodejs-cpp/merge-pdf/
description: This page explain how to merge PDF documents into a single PDF file with Aspose.PDF for Node.js via C++.
lastmod: "2023-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Merge or combine two PDF into single PDF in Node.js

Combining and merging files is a very popular task during work with a large number of documents. Sometimes, when working with documents and images, when they are scanned, processed, and organized, several files are created.
But what if you need to store everything in one file? Or do you not want to print several documents? Concatenate two PDF files with Aspose.PDF for Node.js via C++.

In case you want to merge two PDFs, you can use [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) function. 
Please check the following code snippet in order to merge two PDFs files in Node.js environment.

**CommonJS:**

1. Require the AsposePDFforNode.cjs module.
1. Specify the name of the PDF files which will be merged.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Merge two PDF files. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultMerge.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. Specify the name of the PDF files which will be merged.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/).
1. Merge two PDF files. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultMerge.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```