---
title: Extract Text from PDF using JavaScript
linktitle: Extract text from PDF
type: docs
weight: 30
url: /javascript-cpp/extract-text-from-pdf/
description: This article describes various ways to extract text from PDF documents using Aspose.PDF for JavaScript. 
lastmod: "2023-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Text From PDF Document

Extracting text from the PDF document is a very common and useful task. 
Extracting text from PDFs serves a variety of purposes, from improving search and availability to enabling analysis and automation of data in various fields such as business, research, and information management.

In case you want to extract text from PDF document, you can use [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) function. 
Please check following code snippet in order to extract text from PDF file using JavaScript via C++.

1. Create a 'FileReader'.
1. The [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdfextracttext/) function is executed.
1. Next, if the 'json.errorCode' is 0, then you can get links to result files. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.

```js

    var ffileExtract = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Extract text from a PDF-file*/
        const json = AsposePdfExtractText(event.target.result, e.target.files[0].name);
        if (json.errorCode == 0) document.getElementById('output').textContent = json.extractText;
        else document.getElementById('output').textContent = json.errorText;
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
            evt.data.json.extractText :
            `Error: ${evt.data.json.errorText}`; 

    /*Event handler*/
    const ffileExtract = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Extract text from a PDF-file - Ask Web Worker*/
        AsposePDFWebWorker.postMessage(
            { "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] },
            [event.target.result]
        );
        };
        file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```