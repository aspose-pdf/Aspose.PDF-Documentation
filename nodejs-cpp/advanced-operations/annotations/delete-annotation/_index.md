---
title: Delete Annotation using Node.js
linktitle: Delete Annotation
type: docs
weight: 10
url: /nodejs-cpp/delete-annotation/
description: With Aspose.PDF for Node.js you may delete annotation from your PDF file.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

You can delete annotations from a PDF file using Aspose.PDF for Node.js via C++. In case you want to delete annotations from a PDF, you can use [AsposePdfDeleteAnnotations](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteannotations/) function. 
Please check the following code snippet in order to delete annotations from a PDF file in Node.js environment.

**CommonJS:**

```cjs

    const AsposePdf = require('.//AsposePDFforNode.cjs');
    const pdf_file = 'ReadMe.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete annotations from a PDF-file and save the "ResultPdfDeleteAnnotations.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
        console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

```mjs

    import AsposePdf from './/AsposePDFforNode.mjs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'ReadMe.pdf';
    /*Delete annotations from a PDF-file and save the "ResultPdfDeleteAnnotations.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAnnotations(pdf_file, "ResultPdfDeleteAnnotations.pdf");
    console.log("AsposePdfDeleteAnnotations => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```
