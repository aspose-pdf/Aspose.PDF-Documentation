---
title: Extract Text from PDF using Node.js
linktitle: Extract Text from PDF
type: docs
weight: 10
url: /nodejs-cpp/extract-text/
description: This section describes how to extract text from PDF document using Node.js toolkit.
lastmod: "2023-11-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Text From all the Pages of PDF Document

Extracting text from PDF isn’t easy. Not many PDF readers can extract text from PDF images or scanned PDFs. But **Aspose.PDF for Node.js via C++** tool allows you to easily extract text from all PDF file in the Node.js environment. 

Check the code snippets and follow the steps to extract text from your PDF:

**CommonJS:**

1. Require the AsposePDFforNode.сjs module.
1. The name of the resulting file is set, in this example "ReadMe.pdf".
1. Waiting for module initialization with 'AsposePdf().then'. The object is returned.
1. Call the function [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) from the AsposePDFforNode module.
1. Extracted text is stored in the JSON object. Thus, if 'json.errorCode' is 0, the extracted text is displayed using console.log. If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. The name of the resulting file is set, in this example "ReadMe.pdf".
1. Waiting for module initialization with 'await AsposePdf()' The object is returned.
1. Call the function [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) from the AsposePDFforNode module.
1. Extracted text is stored in the JSON object. Thus, if 'json.errorCode' is 0, the extracted text is displayed using console.log. If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
