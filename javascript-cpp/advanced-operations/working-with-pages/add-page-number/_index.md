---
title: Add Page Number to PDF with JavaScript via C++ 
linktitle: Add Page Number
type: docs
weight: 100
url: /javascript-cpp/add-page-number/
description: Aspose.PDF for JavaScript via C++  allows you to add Page Number Stamp to your PDF file using AsposePdfAddPageNum.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

All the documents must have page numbers in it. The page number makes it easier for the reader to locate different parts of the document.

**Aspose.PDF for JavaScript via C++** allows you to add page numbers with [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/).

1. Create a 'FileReader'.
1. The [AsposePdfAddPageNum](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddpagenum/) function is executed.
1. The name of the resulting file is set, in this example "ResultAddPageNum.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js
  var ffileAddPageNum = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*add page num a PDF-file and save the "ResultAddPageNum.pdf"*/
      const json = AsposePdfAddPageNum(event.target.result, e.target.files[0].name, "ResultAddPageNum.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```
