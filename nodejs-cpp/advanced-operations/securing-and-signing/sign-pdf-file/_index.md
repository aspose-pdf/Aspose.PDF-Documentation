---
title: Add digital signature in PDF in Node.js
linktitle: Digitally sign PDF
type: docs
weight: 70
url: /nodejs-cpp/sign-pdf/
description: Digitally sign PDF documents in the Node.js environment.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


A digital signature in a PDF document is a way to verify the document’s authenticity and integrity. This is the process of the electronic signature of a PDF document using a private key and digital certificate. This signature guarantees the holder that the document has not been altered or altered since the signing and that the signatory is the one whom it approves. To sign PDF with Node.js, use the Aspose.PDF tool.

In case you want to sign PDF file, you can use [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) function.

It is possible to use **parameters** related to the signature:

- fileName
- pageNum
- fileSign
- pswSign
- setXIndent
- setYIndent
- setHeight
- setWidth
- reason
- contact
- location
- isVisible
- signatureAppearance
- fileNameResult 

This code snippet utilizes the AsposePDFforNode.cjs module in a Node.js environment to digitally sign a PDF file using the PKCS7 signature.

**CommonJS:**

1. Call `require` and import `AsposePDFforNode` module as `AsposePdf` variable.
1. Specify the name of the PDF file to be signed, the PKCS7 key file, and the signature appearance image file. The certificate and image can be placed anywhere on your file system from where you upload them for PDF signing.
1. Call `AsposePdf` as Promise and perform the operation for signing file. Receive the object if successful.
1. Call the [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) function. 
1. Sign a PDF file with digital signatures. Parameters related to the signature (like the key file, password, coordinates, reason, contact, location, etc). 
1. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultSignPKCS7.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Key PKCS7*/
      const test_pfx_file = 'test.pfx';
      /*Signature appearance*/
      const sign_img_file = 'Aspose.jpg';
      /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
      const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
      console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. Specify the name of the PDF file to be signed, the PKCS7 key file, and the signature appearance image file.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfsignpkcs7/) function. 
1. Sign a PDF file with digital signatures. Parameters related to the signature (like the key file, password, coordinates, reason, contact, location, etc). 
1. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultSignPKCS7.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Key PKCS7*/
  const test_pfx_file = 'test.pfx';
  /*Signature appearance*/
  const sign_img_file = 'Aspose.jpg';
  /*Sign a PDF-file with digital signatures and save the "ResultSignPKCS7.pdf"*/
  const json = AsposePdfModule.AsposePdfSignPKCS7(pdf_file, 1, test_pfx_file, "Pa$$w0rd2023", 100, 100, 200, 100, "Reason", "Contact", "Location", 1, sign_img_file, "ResultSignPKCS7.pdf");
  console.log("AsposePdfSignPKCS7 => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```