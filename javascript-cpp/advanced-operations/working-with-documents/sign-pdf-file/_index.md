---
title: Add digital signature or digitally sign PDF in JavaScript via C++
linktitle: Digitally sign PDF
type: docs
weight: 70
url: /javascript-cpp/sign-pdf/
description: Digitally sign PDF documents using JavaScript via C++.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---


A digital signature in a PDF document is a way to verify the document’s authenticity and integrity. This is the process of the electronic signature of a PDF document using a private key and digital certificate. This signature guarantees the holder that the document has not been altered or altered since the signing and that the signatory is the one whom it approves. To sign PDF with JavaScript, use the Aspose.PDF tool.

Aspose.PDF for JavaScript via C++ supports the feature to digitally sign the PDF files using the [AsposePdfSignPKCS7](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsignpkcs7/).

## Sign PDF with digital signatures

```js

/*set the default PKCS7 key filename*/
  var fileSign = "/test.pfx";

  var ffileSign = function (e) {
    const file_reader = new FileReader();
    /*set the PKCS7 key filename*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*prepare(save) the PKCS7 key file from BLOB*/
      AsposePdfPrepare(event.target.result, fileSign);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

```js
  /*set the default image (Signature Appearance) filename*/
  var signatureAppearance = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*set the image filename*/
    signatureAppearance = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*prepare(save) the image file from BLOB*/
      AsposePdfPrepare(event.target.result, signatureAppearance);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

```js
  var ffileSignPKCS7 = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      let pswSign = document.getElementById("passwordSign").value;
      /*sign a PDF-file and save the "ResultSignPKCS7.pdf"*/
      const json = AsposePdfSignPKCS7(event.target.result, e.target.files[0].name, 1, fileSign, pswSign, 200, 200, 200, 100, "TEST", "test@test.com", "EU", 1, signatureAppearance,"ResultSignPKCS7.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```
