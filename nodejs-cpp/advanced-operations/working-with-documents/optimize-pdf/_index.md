---
title: Optimize PDF using Aspose.PDF for Node.js via C++ 
linktitle: Optimize PDF File
type: docs
weight: 10
url: /nodejs-cpp/optimize-pdf/
description: Optimize and compress PDF files for fast web-view using the Node.js environment.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimize PDF Document

Toolkit by Aspose.PDF for Node.js via C++ allows you to optimize PDF content for the Web. 

Optimization, or linearization for Web, refers to the process of making a PDF file suitable for online browsing using a web browser.

In case you want to optimize PDF, you can use [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) function. 
Please check the following code snippet in order to optimize PDF files in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file which will be optimized.
1. Call `AsposePdf` as Promise and perform the operation for optimizing file. Receive the object if successful.
1. Call the function [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimize a PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultOptimize.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.js module.
1. Specify the name of the PDF file which will be optimized.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. Optimize a PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultOptimize.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```