---
title: Set the background color for PDF in Node.js
linktitle: Set background color 
type: docs
weight: 80
url: /nodejs-cpp/set-background-color/
description: Set background color for the your PDF file with Node.js via C++. 
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

In case you want to set background color of PDF, you can use [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/) function. 

Please check the following code snippet in order to set background color of PDF in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file whose background color you want to set.
1. Call `AsposePdf` as Promise and perform the operation for setting background color. Receive the object if successful.
1. Call the function [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Set the background color for the PDF file. You need to pass 3 arguments to this function: an input file name, a desired color in hexadecimal form, and an output file name. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultRotation.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
      const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
      console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the `asposepdfnodejs` module.
1. Specify the name of the PDF file whose background color you want to set.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfSetBackgroundColor](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsetbackgroundcolor/). 
1. Set the background color for the PDF file. The background color is set to "#426bf4," which is a hexadecimal color code representing a shade of blue. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultRotation.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Set the background color for the PDF-file and save the "ResultPdfSetBackgroundColor.pdf"*/
  const json = AsposePdfModule.AsposePdfSetBackgroundColor(pdf_file, "#426bf4", "ResultPdfSetBackgroundColor.pdf");
  console.log("AsposePdfSetBackgroundColor => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```