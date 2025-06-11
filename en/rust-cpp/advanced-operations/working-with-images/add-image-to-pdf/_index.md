---
title: Add Image to PDF in Node.js 
linktitle: Add Image
type: docs
weight: 10
url: /nodejs-cpp/add-image-to-pdf/
description: This section describes how to add image to existing PDF file using Aspose.PDF for Node.js via C++.
lastmod: "2023-11-16"
---

## Add an image to an existing PDF file

It is commonly believed that adding images to PDF files requires a complex special tool. However, with Aspose.PDF for Node.js you can quickly and easily add the images you need to PDF in Node.js environment.

We can add images to the end of the file only, therefore right example is we have some scanned document pages and convert them into a single PDF.

In case you want to add images, you can use [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) function. 
Please check the following code snippet in order to add images in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file in which the image will be added.
1. Call `AsposePdf` as Promise and perform the operation for adding image. Receive the object if successful.
1. Call the function [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Add image to end a PDF. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultAddImage.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the `asposepdfnodejs` module.
1. Specify the name of the PDF file in which the image will be added.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/).
1. Add image to end a PDF. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultAddImage.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```