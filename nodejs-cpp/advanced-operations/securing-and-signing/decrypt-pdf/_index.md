---
title: Decrypt PDF in Node.js
linktitle: Decrypt PDF File
type: docs
weight: 40
url: /nodejs-cpp/decrypt-pdf/
description: Decrypt PDF File with Aspose.PDF for Node.js via C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Decrypt PDF File using Owner Password

Recently, more and more users exchange encrypted documents in order not to become victims of Internet fraud and protect their documents.
In this regard, it becomes necessary to access the encrypted PDF file, since such access can only be obtained by an authorized user. Also, people are looking for various solutions to decrypt PDF files. 

In case you want to decrypt PDF file, you can use [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) function. 
If you want to decrypt PDF file try the next code snippet:

**CommonJS:**

1. Require the AsposePDFforNode.cjs module.
1. Specify the name of the PDF file that will change the decrypted.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) function.
1. Decrypt PDF file with password is "owner".
1. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultDecrypt.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
      console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. Specify the name of the PDF file that will change the decrypted.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the [AsposePdfDecrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfdecrypt/) function.
1. Decrypt PDF file with password is "owner".
1. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultDecrypt.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfDecrypt(pdf_encrypt_file, "owner", "ResultDecrypt.pdf");
  console.log("AsposePdfDecrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```