---
title: Repair PDF in Node.js 
linktitle: Repair PDF
type: docs
weight: 10
url: /nodejs-cpp/repair-pdf/
description: This topic describes how to Repair PDF in the Node.js environment.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js allows high-quality PDF repair. The PDF file may not open for any reason, regardless of the program or browser. In some cases the document can be restored, try the following code and see for yourself.
In case you want to repair PDF document, you can use [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) function. 
Please check following code snippet in order to repair PDF file in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file that will be repaired.
1. Call `AsposePdf` as Promise and perform the operation for repairing file. Receive the object if successful.
1. Call the function [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Repair the PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPdfRepair.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.js module.
1. Specify the name of the PDF file that will be repaired.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/).
1. Repair the PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPdfRepair.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```