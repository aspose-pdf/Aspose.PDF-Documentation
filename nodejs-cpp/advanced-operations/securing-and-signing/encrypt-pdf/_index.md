---
title:  Encrypt PDF in Node.js
linktitle: Encrypt PDF File
type: docs
weight: 50
url: /nodejs-cpp/encrypt-pdf/
description: Encrypt PDF File with Aspose.PDF for Node.js via C++.
lastmod: "2023-11-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Encrypt PDF File using using User or Owner Password

If you are sending an email to someone with a PDF attachment that contains confidential  information, you might wish to add some security to it first to hold it falling into the incorrect hands. The best way to limit unauthorized access to a PDF document is to defend it with a password. To easily and securely encrypt documents, you can use Aspose.PDF for Node.js via C++.

>Please specify different user and owner passwords while encrypting the PDF file.

- The **User password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it’s not correct, the document will not open.
- The **Owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

In case you want to encrypt PDF file, you can use [AsposePdfEncrypt](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfencrypt/) function. 
If you want to encrypt PDF file try the next code snippet:

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
      const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf"*/
  const json = AsposePdfModule.AsposePdfEncrypt(pdf_file, "user", "owner", AsposePdfModule.Permissions.PrintDocument, AsposePdfModule.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
  console.log("AsposePdfEncrypt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```