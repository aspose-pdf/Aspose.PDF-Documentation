---
title: Extract Images from PDF in Node.js
linktitle: Extract Images from PDF
type: docs
weight: 20
url: /nodejs-cpp/extract-images-from-the-pdf-file/
description: How to extract a part of the image from PDF using Aspose.PDF for Node.js toolkit.
lastmod: "2023-11-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract images from PDF files in the Node.js environment

In case you want to extract images from PDF document, you can use [AsposePdfExtractImage](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextractimage/) function. 
Please check following code snippet in order to extract images from PDF file using Node.js via C++.

**CommonJS:**



```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfModule.AsposePdfExtractImage(pdf_file, "ResultPdfExtractImage{0:D2}.jpg", 150);
      console.log("AsposePdfExtractImage => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**



```mjs

    import AsposePdf from './/AsposePDFforNode.mjs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'ReadMe.pdf';
    /*Extract text from a PDF-file*/
    const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
    console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
