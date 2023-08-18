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
      /*Set number a page to split*/
      const pageToSplit = 1;
      /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf"*/
      const json = AsposePdfSplit2Files(event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = e.target.files[0].name + " split: " + json.fileNameResult1 + ", " + json.fileNameResult2;
      else document.getElementById('output').textContent = json.errorText;
      /*Make a link to download the first result file*/
      DownloadFile(json.fileNameResult1, "application/pdf");
      /*Make a link to download the second result file*/
      DownloadFile(json.fileNameResult2, "application/pdf");
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
          `Result:\n${DownloadFile(evt.data.json.fileNameResult1, "application/pdf", evt.data.params[0])}
                  \n${DownloadFile(evt.data.json.fileNameResult2, "application/pdf", evt.data.params[1])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Event handler*/
    const ffileSplit = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Set number a page to split*/
        const pageToSplit = 1;
        /*Split to two PDF-files and save the "ResultSplit1.pdf", "ResultSplit2.pdf" - Ask Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfSplit2Files',
            "params": [event.target.result, e.target.files[0].name, pageToSplit, "ResultSplit1.pdf", "ResultSplit2.pdf"] },
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