---
title: Decrypt PDF using JavaScript
linktitle: Decrypt PDF File
type: docs
weight: 40
url: /javascript-cpp/decrypt-pdf/
description: Decrypt PDF File with Aspose.PDF for JavaScript via C++.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Decrypt PDF File using Owner Password

Recently, more and more users exchange encrypted documents in order not to become victims of Internet fraud and protect their documents.
In this regard, it becomes necessary to access the encrypted PDF file, since such access can only be obtained by an authorized user. Also, people are looking for various solutions to decrypt PDF files. 

It is better to solve this problem once by using the Aspose.PDF for JavaScript via C++ directly in your web browser. The following code snippet shows you how to decrypt PDF files.

1. Select a PDF file for decrypting.
1. Create a 'FileReader'.
1. The [AsposePdfDecrypt](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdecrypt/) function is executed.
1. The name of the resulting file is set, in this example "ResultDecrypt.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileDecrypt = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*decrypt a PDF-file with password is "owner" and save the "ResultDecrypt.pdf"*/
      const json = AsposePdfDecrypt(event.target.result, e.target.files[0].name, "owner", "ResultDecrypt.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```
