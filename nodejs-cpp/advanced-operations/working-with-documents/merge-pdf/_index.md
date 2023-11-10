---
title: How to Merge PDF in Node.js
linktitle: Merge PDF files
type: docs
weight: 20
url: /nodejs-cpp/merge-pdf/
description: This page explain how to merge PDF documents into a single PDF file with Aspose.PDF for Node.js via C++ 
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Merge or combine two PDF into single PDF in Node.js

Combining and merging files is a very popular task during work with a large number of documents. Sometimes, when working with documents and images, when they are scanned, processed, and organized, several files are created.
But what if you need to store everything in one file? Or do you not want to print several documents? Concatenate two PDF files with Aspose.PDF for Node.js via C++.

In case you want to merge two PDFs, you can use [AsposePdfMerge2Files](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfmerge2files/) function. 
Please check the following code snippet in order to merge two PDFs files in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Merge two PDF-files and save the "ResultMerge.pdf"*/
      const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
      console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Merge two PDF-files and save the "ResultMerge.pdf"*/
  const json = AsposePdfModule.AsposePdfMerge2Files(pdf_file, pdf_file, "ResultMerge.pdf");
  console.log("AsposePdfMerge2Files => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```