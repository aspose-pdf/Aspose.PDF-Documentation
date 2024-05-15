---
title: Convert PDF to PPTX in Node.js
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-16"
description: Aspose.PDF allows you to convert PDF to PPTX format using Node.js directly in the Node.js environment.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**Try to convert PDF to PowerPoint online**

Aspose.PDF for Node.js presents you online free application ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Convert PDF to PPTX

In case you want to convert PDF document, you can use [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/) function. 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file that will be converted.
1. Call `AsposePdf` as Promise and perform the operation for converting file. Receive the object if successful.
1. Call the function [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. Convert PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPDFtoPptX.pptx". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the `asposepdfnodejs` module.
1. Specify the name of the PDF file that will be converted
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. Convert PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPDFtoPptX.pptx". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```