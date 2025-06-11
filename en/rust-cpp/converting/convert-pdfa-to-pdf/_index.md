---
title: Convert PDF/A to PDF format in Node.js
linktitle: Convert PDF/A to PDF format
type: docs
weight: 110
url: /nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-16"
description: This topic show you how to Aspose.PDF allows to convert PDF/A file to PDF document in the Node.js environment.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convert PDF/A to PDF format

In case you want to convert PDF document, you can use [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) function. 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file that will be converted.
1. Call `AsposePdf` as Promise and perform the operation for converting file. Receive the object if successful.
1. Call the function [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Convert PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultConvertToPDF.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the `asposepdfnodejs` module.
1. Specify the name of the PDF/A file that will be converted
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/).
1. Convert PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultConvertToPDF.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```