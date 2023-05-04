---
title: Rotate PDF Pages with JavaScript via C++ 
linktitle: Rotate PDF Pages
type: docs
weight: 50
url: /javascript-cpp/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically via JavaScript via C++ 
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

This section describes how to change the page orientation from landscape to portrait and vice versa in an existing PDF file using JavaScript via C++.

1. Create a 'FileReader'.
1. The [AsposePdfRotateAllPages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfrotateallpages/) function is executed.
1. The name of the resulting file is set, in this example "ResultRotation.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileRotateAllPages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*rotate all pages PDF-file and save the "ResultRotation.pdf"*/
      const json = AsposePdfRotateAllPages(event.target.result, e.target.files[0].name, Module.Rotation.on270, "ResultRotation.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```