---
title: Optimize PDF Resources using Node.js via C++ 
linktitle: Optimize PDF Resources
type: docs
weight: 15
url: /nodejs-cpp/optimize-pdf-resources/
description: Optimize Resources of PDF files for fast web-view using Node.js tool.
lastmod: "2023-11-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimize PDF Resources

In case you want to optimize PDF resources, you can use [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) function. 
Please check the following code snippet in order to optimize PDF resources in Node.js environment.

**CommonJS:**

1. Require the AsposePDFforNode.сjs module.
1. Specify the name of the PDF file for which resources will be optimized.
1. Initialize the Aspose Pdf() module. Receive the object if successful.
1. Call the function [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimize a PDF resources. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPdfOptimizeResource.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. Specify the name of the PDF file for which resources will be optimized.
1. Initialize the Aspose Pdf() module. Receive the object if successful.
1. Call the function [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/).
1. Optimize a PDF resources. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPdfOptimizeResource.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize resources of PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```