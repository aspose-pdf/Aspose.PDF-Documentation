---
title: Add background to PDF in Node.js via C++
linktitle: Add backgrounds
type: docs
weight: 10
url: /nodejs-cpp/add-backgrounds/
description: Add background image to the your PDF file with Node.js via C++. 
lastmod: "2023-10-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The following code snippets shows how to add a background image to PDF pages using the [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfaddbackgroundimage/) function in Node.js.

Please check the following code snippet in order to add a background image in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  const background_file = 'Aspose.jpg';
  AsposePdf().then(AsposePdfModule => {
      /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
      const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
      console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  const background_file = 'Aspose.jpg';
  /*Add background image to a PDF-file and save the "ResultBackgroundImage.pdf"*/
  const json = AsposePdfModule.AsposePdfAddBackgroundImage(pdf_file, background_file, "ResultAddBackgroundImage.pdf");
  console.log("AsposePdfAddBackgroundImage => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```