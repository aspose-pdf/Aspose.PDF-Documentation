---
title: Add background to PDF in Node.js
linktitle: Add background
type: docs
weight: 10
url: /nodejs-cpp/add-background/
description: Add a background image to your PDF file in Node.js 
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The following code snippets shows how to add a background image to PDF pages using the [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) function in Node.js.

Please check the following code snippet in order to add a background image in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file in which the background image will be added.
1. Call `AsposePdf` as Promise and perform the operation for adding background image. Receive the object if successful.
1. Call the function [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. Add background image to a PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultAddBackgroundImage.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the `asposepdfnodejs` module.
1. Specify the name of the PDF file in which the background image will be added.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/).
1. Add background image to a PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultAddBackgroundImage.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  const background_file = 'Aspose.jpg';
  /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```