---
title: Repair PDF with Node.js via C++ 
linktitle: Repair PDF
type: docs
weight: 10
url: /nodejs-cpp/repair-pdf/
description: This topic describes how to Repair PDF in the Node.js environment.
lastmod: "2023-10-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js allows high-quality PDF repair. The PDF file may not open for any reason, regardless of the program or browser. In some cases the document can be restored, try the following code and see for yourself.
In case you want to repair PDF document, you can use [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) function. 
Please check following code snippet in order to repair PDF file in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Repair a PDF-file and save the "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```