---
title: Convert PDF/A to PDF format in Node.js
linktitle: Convert PDF/A to PDF format
type: docs
weight: 110
url: /nodejs-cpp/convert-pdfa-to-pdf/
lastmod: "2023-11-01"
description: This topic show you how to Aspose.PDF allows to convert PDF/A file to PDF document in the Node.js environment.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convert PDF/A to PDF format

In case you want to convert PDF document, you can use [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfaconverttopdf/) function. 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
      const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
      console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_PDFA_file = 'ResultConvertToPDFA.pdf';
  /*Convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
  const json = AsposePdfModule.AsposePdfAConvertToPDF(pdf_PDFA_file, "ResultConvertToPDF.pdf");
  console.log("AsposePdfAConvertToPDF => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```