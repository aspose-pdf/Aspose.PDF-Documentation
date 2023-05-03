---
title: Split PDF using JavaScript
linktitle: Split PDF files
type: docs
weight: 30
url: /javascript-cpp/split-pdf/
description: This topic shows how to split PDF pages into individual PDF files with Aspose.PDF for JavaScript via C++ .
lastmod: "2022-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Split PDF into multiple files or separate PDFs in JavaScript

This topic shows how to split PDF pages into individual PDF files using JavaScript. 

1. Select a PDF file for splitting.
1. Create a 'FileReader'.
1. Set number a page to split
1. The [AsposePdfOptimize](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsplit2files/) function is executed.
1. The name of the resulting file is set, in this example "ResultSplit2.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a links and allows you to download the resulting first and second files to the user's operating system.


The following JavaScript code snippet shows you how to split PDF pages into individual PDF files.

```js

  var ffileSplit = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*set number a page to split*/
      const pageToSplit = 1;
      /*split a PDF-file and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " split: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the first result file*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*make a link to download the second result file*/
      DownloadFile(json.fileNameResult2, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```