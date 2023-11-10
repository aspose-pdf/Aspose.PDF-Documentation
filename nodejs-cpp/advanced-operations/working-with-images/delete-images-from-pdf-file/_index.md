---
title: Delete Images from PDF File in Node.js
linktitle: Delete Images
type: docs
weight: 20
url: /nodejs-cpp/delete-images-from-pdf-file/
description: This section explain how to delete Images from PDF File using Aspose.PDF for Node.js.
lastmod: "2023-10-17"
---


You can delete images from a PDF file using Aspose.PDF for Node.js via C++. You can get the result directly in your browser.

In case you want to delete images from PDF, you can use [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) function. 
Please check the following code snippet in order to delete images in Node.js environment.

**CommonJS:**

```cjs

    const AsposePdf = require('.//AsposePDFforNode.cjs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

```mjs

    import AsposePdf from './/AsposePDFforNode.mjs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```