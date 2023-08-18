---
title: Delete PDF Pages with JavaScript via C++ 
linktitle: Delete PDF Pages
type: docs
weight: 30
url: /javascript-cpp/delete-pages/
description: You can delete pages from your PDF file using Aspose.PDF for JavaScript via C++  library.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

You can delete pages from a PDF file using Aspose.PDF for JavaScript via C++. You can get the result directly in your browser.

1. Create a 'FileReader'.
1. Specify page numbers to delete.
1. The [AsposePdfDeletePages](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfdeletepages/) function is executed.
1. The name of the resulting file is set, in this example "ResultDeletePages.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileDeletePages = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      const numPages = "1-3";
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      /*const numPages = 1;*/
      /*delete 1-3 pages a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfDeletePages(event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages);
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
    const ffileDeletePages = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
        const numPages = "1-3";
        /*array, array of number pages*/
        /*const numPages = [1,3];*/
        /*number, number page*/
        /*const numPages = 1;*/
        /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf - Ask Web Worker"*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfDeletePages',
            "params": [event.target.result, e.target.files[0].name, "ResultDeletePages.pdf", numPages] },
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
