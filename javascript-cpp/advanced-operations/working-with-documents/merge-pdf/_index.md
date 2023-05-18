---
title: How to Merge PDF using JavaScript via C++ 
linktitle: Merge PDF files
type: docs
weight: 20
url: /javascript-cpp/merge-pdf/
description: This page explain how to merge PDF documents into a single PDF file with Aspose.PDF for JavaScript via C++ 
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Merge or combine two PDF into single PDF in JavaScript

Combining and merging files is a very popular task during work with a large number of documents. Sometimes, when working with documents and images, when they are scanned, processed, and organized, several files are created.
But what if you need to store everything in one file? Or do you not want to print several documents? Concatenate two PDF files with Aspose.PDF for JavaScript via C++.

This JavaScript tool allows to merge two PDF files into a single PDF document using Aspose.PDF for JavaScript via C++. The example is written in JavaScript. 

1. Select a PDF files for merging.
1. Create a 'FileReader'.
1. The [AsposePdfMerge2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfmerge2files/) function is executed.
1. The name of the resulting file is set, in this example "ResultMerge.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

The following code snippet shows how to concatenate PDF files:

```js

  var ffileMerge = function (e) {
    const file_reader = new FileReader();
    function readFile(index) {
      /*only two files*/
      if (index >= e.target.files.length || index >= 2) {
        /*merge two PDF-files and save the "ResultMerge.pdf"*/
        const json = AsposePdfMerge2Files(undefined, undefined, e.target.files[0].name, e.target.files[1].name, "ResultMerge.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*make a link to download the result file*/
        DownloadFile(json.fileNameResult, "application/pdf");
        return;
      }
      const file = e.target.files[index];
      file_reader.onload = function (event) {
        /*prepare(save) file from BLOB*/
        AsposePdfPrepare(event.target.result, file.name);
        readFile(index + 1)
      }
      file_reader.readAsArrayBuffer(file);
    }
    readFile(0);
  }
```

