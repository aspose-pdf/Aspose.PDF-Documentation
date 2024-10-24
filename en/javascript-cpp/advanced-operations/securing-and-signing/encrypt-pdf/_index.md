---
title:  Encrypt PDF using JavaScript
linktitle: Encrypt PDF File
type: docs
weight: 50
url: /javascript-cpp/encrypt-pdf/
description: Encrypt PDF File with Aspose.PDF for JavaScript via C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Encrypt PDF File using using User or Owner Password

If you are sending an email to someone with a PDF attachment that contains confidential  information, you might wish to add some security to it first to hold it falling into the incorrect hands. The best way to limit unauthorized access to a PDF document is to defend it with a password. To easily and securely encrypt documents, you can use Aspose.PDF for JavaScript via C++.

>Please specify different user and owner passwords while encrypting the PDF file.

- The **User password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
- The **Owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

The following code snippet shows you how to encrypt PDF files.

1. Select a PDF file for encrypting.
1. Create a 'FileReader'.
1. The [AsposePdfEncrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfencrypt/) function is executed.
1. The name of the resulting file is set, in this example "ResultEncrypt.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileEncrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*encrypt a PDF-file with passwords "user" and "owner", and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfEncrypt(event.target.result, e.target.files[0].name, "user", "owner", Module.Permissions.PrintDocument, Module.CryptoAlgorithm.RC4x40, "ResultEncrypt.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

## Using Web Workers

```js

    /*Create Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error from Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ?
          `Result:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Event handler*/
    const ffileEncrypt = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const password_user = 'user';
        const password_owner = 'owner';
        const permissions = 'Module.Permissions.PrintDocument';
        const algorithm = 'Module.CryptoAlgorithm.RC4x40';
        /*Encrypt a PDF-file with passwords "user" and "owner", and save the "ResultEncrypt.pdf" - Ask Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfEncrypt',
            "params": [event.target.result, e.target.files[0].name, password_user, password_owner,
                      permissions, algorithm, "ResultEncrypt.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    /*Make a link to download the result file*/
    const DownloadFile = (filename, mime, content) => {
        mime = mime || "application/octet-stream";
        var link = document.createElement("a"); 
        link.href = URL.createObjectURL(new Blob([content], {type: mime}));
        link.download = filename;
        link.innerHTML = "Click here to download the file " + filename;
        document.body.appendChild(link); 
        document.body.appendChild(document.createElement("br"));
        return filename;
      }
```