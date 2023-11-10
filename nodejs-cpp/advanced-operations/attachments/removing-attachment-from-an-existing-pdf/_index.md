---
title: Removing attachments from PDF with Node.js
linktitle: Removing attachment from an existing PDF
type: docs
weight: 10
url: /nodejs-cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF can remove attachments from your PDF documents. Use Node.js environment to remove attachments in PDF files by Aspose.PDF.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

You can delete attachments from a PDF file using Aspose.PDF for Node.js via C++. In case you want to delete attachments from a PDF, you can use [AsposePdfDeleteAttachments](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeleteattachments/) function. 
Please check the following code snippet in order to delete attachments from a PDF file in Node.js environment.

**CommonJS:**

```cjs

    const AsposePdf = require('.//AsposePDFforNode.cjs');
    const pdf_file = 'Aspose.pdf';
    AsposePdf().then(AsposePdfModule => {
        /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
        const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
        console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
    });
```

**ECMAScript/ES6:**

```mjs

    import AsposePdf from './/AsposePDFforNode.mjs';
    const AsposePdfModule = await AsposePdf();
    const pdf_file = 'Aspose.pdf';
    /*Delete attachments from a PDF-file and save the "ResultPdfDeleteAttachments.pdf"*/
    const json = AsposePdfModule.AsposePdfDeleteAttachments(pdf_file, "ResultPdfDeleteAttachments.pdf");
    console.log("AsposePdfDeleteAttachments => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```