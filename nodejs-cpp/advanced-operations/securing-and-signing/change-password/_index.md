---
title: Change Password of a PDF File in Node.js
linktitle: Change Password
type: docs
weight: 50
url: /nodejs-cpp/change-password-pdf/
description: Change Password of a PDF File with Aspose.PDF for Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Change Password of a PDF File

In case you want to change password of PDF, you can use [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/) function. It changes the user password and owner password by owner password, keeping the original security settings.
If you want to change the password of a PDF file from "owner" to "newowner" or "newuser" try the next code snippet:

**CommonJS:**

1. Call `require` and import `AsposePDFforNode` module as `AsposePdf` variable.
1. Specify the name of the PDF file that will change the password.
1. Call `AsposePdf` as Promise and perform the operation for changing password. Receive the object if successful.
1. Call the function [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Change Password. The existing owner password is set to "owner," and it is changed to "newowner" with the new user password "newuser".
1. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPdfChangePassword.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
      const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
      console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

Please note that if the password is an empty string:

1. If the user password is empty - the PDF opens without asking for a password (but it is still encrypted).
1. If the owner's password is empty, the PDF opens with a user password request.
1. If both are empty  - the PDF opens without asking for a password (but it is still encrypted).


**ECMAScript/ES6:**

1. Import the AsposePDFforNode.mjs module.
1. Specify the name of the PDF file that will change the password.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfChangePassword](https://reference.aspose.com/pdf/nodejs-cpp/security/asposepdfchangepassword/).
1. Change Password. The existing owner password is set to "owner," and it is changed to "newowner" with the new user password "newuser".
1. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPdfChangePassword.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_encrypt_file = 'ResultEncrypt.pdf';
  /*Change passwords of the PDF-file from "owner" to "newowner" and save the "ResultPdfChangePassword.pdf"*/
  const json = AsposePdfModule.AsposePdfChangePassword(pdf_encrypt_file, "owner", "newuser", "newowner", "ResultPdfChangePassword.pdf");
  console.log("AsposePdfChangePassword => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```