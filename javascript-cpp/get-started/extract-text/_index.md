---
title: Extract Text from PDF using JavaScript
linktitle: Extract Text from PDF
type: docs
weight: 10
url: /javascript-cpp/extract-text/
description: This section describes how to extract text from PDF document using JavaScript toolkit.
lastmod: "2022-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Text From all the Pages of PDF Document

Extracting text from PDF isn’t easy. Not many PDF readers can extract text from PDF images or scanned PDFs. But **Aspose.PDF for JavaScript via C++** tool allows you to easily extract text from all PDF file. 

Check the code snippet  and follow the steps to extract text from your PDF:

1. Select a PDF file to extract text.
1. Create a 'FileReader' is to read the text.
1. The [AsposePdfExtractText](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfextracttext/) function is executed.
1. Next, if the 'json.errorCode' is 0, then the 'json.extractText' will contain the extracted content. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, your file will have an error, then information about such an error will be contained in the 'json.errorText'. 
1. As a result, you will receive a string with the extracted text from your PDF.

```js

  var ffileExtract = function (e) {
  const file_reader = new FileReader();
    file_reader.onload = (event) => {
      //Extarct text from a PDF-file
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
        (evt.data.json.errorCode == 0) ? evt.data.json.extractText : `Error: ${evt.data.json.errorText}`; 

    /*Event handler*/
    const ffileExtract = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Extract text from a PDF-file - Ask Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfExtractText', "params": [event.target.result, e.target.files[0].name] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
```