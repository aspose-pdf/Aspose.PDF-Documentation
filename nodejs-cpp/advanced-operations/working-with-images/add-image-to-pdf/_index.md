---
title: Add Image to PDF using Node.js via C++ 
linktitle: Add Image
type: docs
weight: 10
url: /nodejs-cpp/add-image-to-pdf/
description: This section describes how to add image to existing PDF file using Aspose.PDF for Node.js via C++.
lastmod: "2023-12-15"
---

## Add Image in an Existing PDF File

Do you need to attach an image to a PDF? Want to Improve the readability of your PDF? Add images to your PDF and your presentation or resume will look more presentable.

It is commonly believed that adding images to PDF files requires a complex special tool. However, with Aspose.PDF for Node.js you can quickly and easily add the images you need to PDF in Node.js environment.

In case you want to add images, you can use [AsposePdfAddImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddimage/) function. 
Please check the following code snippet in order to add images in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  const image_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
      console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  const image_file = 'Aspose.jpg';
  /*Add an image to end a PDF-file and save the "ResultImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddImage(pdf_file, image_file, "ResultAddImage.pdf");
  console.log("AsposePdfAddImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```