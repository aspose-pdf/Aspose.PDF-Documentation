---
title: Add Image stamps to PDF in Node.js via C++ 
linktitle: Image stamps in PDF File
type: docs
weight: 60
url: /nodejs-cpp/stamping/
description: Add the Image Stamp in your PDF document using AsposePdfAddStamp with the Node.js tool.
lastmod: "2023-10-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Image Stamp in PDF File

Stamping a PDF document is similar to stamping a paper document. A stamp in a PDF file provides additional information to the PDF file, such as protecting the PDF file for others to use and confirming the security of the contents of the PDF file.
You can use the [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/) function to add an image stamp to a PDF file using Node.js.

Please check the following code snippet in order to add an image stamp to a PDF file in Node.js environment.

**CommonJS:**

1. Require the AsposePDFforNode.cjs module.
1. Specify the name of the PDF file in which the image stamp will be added.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Add stamp to a PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultImage.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
      console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. Specify the name of the PDF file in which the image stamp will be added.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfAddStamp](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddstamp/).
1. Add stamp to a PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultImage.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const stamp_file = 'Aspose.jpg';
  /*Add stamp to a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddStamp(pdf_file, stamp_file, 0, 5, 5, 40, 40, AsposePdfModule.Rotation.on270, 0.5, "ResultAddStamp.pdf");
  console.log("AsposePdfAddStamp => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```