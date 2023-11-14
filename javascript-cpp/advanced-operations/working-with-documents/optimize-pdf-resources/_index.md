---
title: Optimize PDF Resources using JavaScript via C++ 
linktitle: Optimize PDF Resources
type: docs
weight: 15
url: /javascript-cpp/optimize-pdf-resources/
description: Optimize Resources of PDF files for fast web-view using JavaScript tool.
lastmod: "2022-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimize PDF Resources

Optimize resources in the document:

  1. Resources that are not used on the document pages are removed
  1. Equal resources are joined into a single object
  1. Unused objects are deleted
 
1. Select a PDF file for optimizing.
1. Create a 'FileReader'.
1. The [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfoptimizeresource/) function is executed.
1. The name of the resulting file is set, in this example "ResultPdfOptimizeResource.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

The following code snippet shows how to optimize a PDF document.

```js

    var ffilePdfOptimizeResource = function (e) {
      const file_reader = new FileReader();
      file_reader.onload = (event) => {
        /*Optimize resources a PDF-file and save the "ResultPdfOptimizeResource.pdf"*/
        const json = AsposePdfOptimizeResource(event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf");
        if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
        else document.getElementById('output').textContent = json.errorText;
        /*Make a link to download the result file*/
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
        (evt.data.json.errorCode == 0) ? `Result:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Event handler*/
    const ffilePdfOptimizeResource = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Optimize resources a PDF-file and save the "ResultPdfOptimizeResource.pdf" - Ask Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfOptimizeResource', "params": [event.target.result, e.target.files[0].name, "ResultPdfOptimizeResource.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Code snippet]

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