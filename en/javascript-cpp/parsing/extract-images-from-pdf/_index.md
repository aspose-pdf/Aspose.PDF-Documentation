---
title: Extract Images from PDF JavaScript
linktitle: Extract Images from PDF
type: docs
weight: 20
url: /javascript-cpp/extract-images-from-the-pdf-file/
description: How to extract a part of the image from PDF using Aspose.PDF for JavaScript toolkit.
lastmod: "2023-09-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Web toolkit from Aspose.PDF allows you to easily extract images from PDF files.

In case you want to extract images from PDF document, you can use [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/) function. 
Please check following code snippet in order to extract images from PDF file using JavaScript via C++.

1. Create a 'FileReader'.
1. The [AsposePdfExtractImage](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextractimage/) function is executed.
1. The name of the resulting file is set, in this example "ResultPdfExtractImage{0:D2}.jpg".
1. Next, if the 'json.errorCode' is 0, then you can get links to result files. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

    var ffileExtractImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
    /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
    const json = AsposePdfExtractImage(event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150);
    if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Files(images) count: " + json.filesCount.toString();
        /*Make links to result files*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
    }
    else document.getElementById('output').textContent = json.errorText;
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
    }
```

## Using Web Workers

```js

  /*Create Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error from Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? 
          `Files(images) count: ${evt.data.json.filesCount.toString()}\n${evt.data.params.forEach(
            (element, index) => DownloadFile(evt.data.json.filesNameResult[index], "image/jpeg", element) ) ?? ""}` : 
          `Error: ${evt.data.json.errorText}`;

    /*Event handler*/
    const ffileExtractImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Extract image from a PDF-file with template "ResultPdfExtractImage{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractImage', "params": [event.target.result, e.target.files[0].name, "ResultPdfExtractImage{0:D2}.jpg", 150] }, [event.target.result]);
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