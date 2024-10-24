---
title: Optimize PDF using Aspose.PDF for JavaScript via C++ 
linktitle: Optimize PDF File
type: docs
weight: 10
url: /javascript-cpp/optimize-pdf/
description: Optimize and compress PDF files for fast web-view using JavaScript tool.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimize PDF Document

Toolkit by Aspose.PDF for JavaScript via C++ allows you to optimize a PDF content for the Web. 

Optimization, or linearization for Web, refers to the process of making a PDF file suitable for online browsing using a web browser. To optimize a file for web display:
 
1. Select a PDF file for optimizing.
1. Create a 'FileReader'.
1. The [AsposePdfOptimize](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfoptimize/) function is executed.
1. The name of the resulting file is set, in this example "ResultOptimize.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

The following code snippet shows how to optimize a PDF document.

```js

  var ffileOptimize = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*optimize a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfOptimize(event.target.result, e.target.files[0].name, "ResultOptimize.pdf");
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
    const ffileOptimize = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Optimize a PDF-file and save the "ResultOptimize.pdf" - Ask Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfOptimize', "params": [event.target.result, e.target.files[0].name, "ResultOptimize.pdf"] },
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