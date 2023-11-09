---
title: Convert PDF to PPTX in Node.js
linktitle: Convert PDF to PPTX
type: docs
weight: 30
url: /nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2023-11-01"
description: Aspose.PDF allows you to convert PDF to PPTX format using Node.js directly in the Node.js environment.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Node.js** lets you track the progress of PDF to PPTX conversion.

{{% alert color="success" %}}
**Try to convert PDF to PowerPoint online**

Aspose.PDF for Node.js presents you online free application ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Convert PDF to PPTX

In case you want to convert PDF document, you can use [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/) function. 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```