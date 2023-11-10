---
title: Rotate PDF Pages in Node.js via C++ 
linktitle: Rotate PDF Pages
type: docs
weight: 50
url: /nodejs-cpp/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically in Node.js environment.
lastmod: "2023-10-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

This section describes how to change the page orientation from landscape to portrait and vice versa in an existing PDF file using Node.js via C++.

In case you want to rotate PDF pages, you can use [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrotateallpages/) function. 

Please check the following code snippet in order to rotate PDF pages in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
      const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
      console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Rotate PDF-pages and save the "ResultRotation.pdf"*/
  const json = AsposePdfModule.AsposePdfRotateAllPages(pdf_file, AsposePdfModule.Rotation.on270, "ResultRotation.pdf");
  console.log("AsposePdfRotateAllPages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```