---
title: Rotate PDF Pages in Node.js
linktitle: Rotate PDF Pages
type: docs
weight: 50
url: /nodejs-cpp/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically in Node.js environment.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

This section describes how to rotate pages in an existing PDF file using Aspose.PDF for Node.js via C++.

In case you want to rotate PDF pages, you can use [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) function. This function uses a special parameter 'AsposePdfModule.Rotation' for rotation value. With which you can set how many degrees you need to rotate PDF. There are variants: None, 90, 180, or 270 degrees.

Please check the following code snippet in order to rotate PDF pages in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file to rotate.
1. Call `AsposePdf` as Promise and perform the operation for rotating pages. Receive the object if successful.
1. Call the function [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Rotate all PDF files. The rotation is set to 270 degrees (on270). Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultRotation.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.js module.
1. Specify the name of the PDF file to rotate.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/). 
1. Rotate all PDF files. The rotation is set to 270 degrees (on270). Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultRotation.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```