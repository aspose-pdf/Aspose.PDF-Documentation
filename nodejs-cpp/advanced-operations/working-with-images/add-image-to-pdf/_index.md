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

It is commonly believed that adding images to PDF files requires a complex special tool. However, with Aspose.PDF for Node.js you can quickly and easily add the images you need to PDF using Node.js directly in your browser.

In case you want to split two PDFs into one, you can use [AsposePdfSplit2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfsplit2files/) function. 
Please check the following code snippet in order to split two PDFs in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Set number a page to split*/
  const pageToSplit = 1;
  /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
  const json = AsposePdfModule.AsposePdfSplit2Files(pdf_file, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
  console.log("AsposePdfSplit2Files => %O", json.errorCode == 0 ? [json.fileNameResult1, json.fileNameResult2] : json.errorText);
```