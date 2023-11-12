---
title: Set the background color for PDF in Node.js via C++
linktitle: Set background color 
type: docs
weight: 80
url: /nodejs-cpp/set-background-color/
description: Set background color for the your PDF file with Node.js via C++. 
lastmod: "2023-10-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

In case you want to set background color of PDF, you can use [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) function. 

Please check the following code snippet in order to set background color of PDF in Node.js environment.

**CommonJS:**

1. Require the AsposePDFforNode.сjs module.
1. Specify the name of the PDF file whose background color you want to set.
1. Initialize the Aspose Pdf() module. Receive the object if successful.
1. Call the function [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Set the background color for the PDF file. The background color is set to "#426bf4," which is a hexadecimal color code representing a shade of blue. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultRotation.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. Specify the name of the PDF file whose background color you want to set.
1. Initialize the Aspose Pdf() module. Receive the object if successful.
1. Call the function [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Set the background color for the PDF file. The background color is set to "#426bf4," which is a hexadecimal color code representing a shade of blue. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultRotation.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```