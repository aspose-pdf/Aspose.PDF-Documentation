---
title: Delete Images from PDF File in Node.js
linktitle: Delete Images
type: docs
weight: 20
url: /nodejs-cpp/delete-images-from-pdf-file/
description: This section explain how to delete Images from PDF File using Aspose.PDF for Node.js.
lastmod: "2023-10-17"
---


You can delete images from a PDF file using Aspose.PDF for Node.js via C++.

In case you want to delete images from PDF, you can use [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/) function. 
Please check the following code snippet in order to delete images in Node.js environment.

**CommonJS:**

1. Require the AsposePDFforNode.cjs module.
1. Specify the name of the PDF file in which the image will be removed.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Delete images from a PDF. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPdfDeleteImages.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

    const AsposePdf = require('.//AsposePDFforNode.cjs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
        console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. Specify the name of the PDF file in which the image will be removed.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfDeleteImages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteimages/).
1. Delete images from a PDF. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPdfDeleteImages.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

    import AsposePdf from './/AsposePDFforNode.mjs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete images from a PDF-file and save the "ResultPdfDeleteImages.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteImages(pdf_file, "ResultPdfDeleteImages.pdf");
    console.log("AsposePdfDeleteImages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```