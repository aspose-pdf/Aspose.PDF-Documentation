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

This code demonstrates how to use the AsposePDFforNode.cjs module to extract text from a specified PDF file and log either the extracted text or encountered errors.

Check the code snippets and follow the steps to extract text from your PDF:

**CommonJS:**

1. Require the AsposePDFforNode.сjs module.
1. Specify the name for the PDF file from which the text will be extracted.
1. Initialize the Aspose Pdf() module. Receive the object if successful.
1. Call the function [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Extracted text is stored in the JSON object. Thus, if 'json.errorCode' is 0, the extracted text is displayed using console.log. If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. Specify the name for the PDF file from which the text will be extracted.
1. Initialize the Aspose Pdf() module. Receive the object if successful.
1. Call the function [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. Extracted text is stored in the JSON object. Thus, if 'json.errorCode' is 0, the extracted text is displayed using console.log. If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
