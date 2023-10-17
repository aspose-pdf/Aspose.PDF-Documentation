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

## Split PDF into two files using JavaScript

This topic shows how to split PDF pages into individual PDF files using JavaScript. How does this feature work? In 'pageToSplit' we specify the number of pages, inclusive, to leave in the first file, the remaining pages of the document will be placed in the second. Such operations are very time consuming, so we recommend using Web Worker. Let's try!

The provided code snippet is an example of using a Web Worker in JavaScript to split a PDF file into two separate PDF files and offer the user the option to download the resulting files. Here's a steps of the code:

1. Creating a Web Worker. A web worker is initialized using the "AsposePDFforJS.js" script file. This web worker will handle PDF file splitting tasks in the background. Any errors that occur in the worker are captured and logged to the console.
1. Message Handling. The web worker is set up to listen for messages using the onmessage event handler. When it receives a message from the web page, it processes the request and sends a response back to the main thread.
1. File Splitting Event Handler. There is an event handler ffileSplit that triggers when a user selects a PDF file for splitting. It reads the selected PDF file using a FileReader and sends the file content and relevant parameters (such as the number of pages to split and output file names) to the web worker via a postMessage call.
1. Download File Function. The [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function is responsible for generating a link that allows the user to download a file. It accepts the filename, MIME type, and file content. The function creates a download link, associates the file content with it, sets the filename, and adds it to the document. This allows the user to download the resulting PDF files.
1. Message Handling in the Web Worker. Next, if the 'json.errorCode' is 0, then json.fileNameResult will contain the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' property.
1. Result Display. The main page includes an element with the ID 'output'. When the web worker sends a message with the result, it updates the 'output' element. If the operation is successful, it displays download links for the two split PDF files. If there's an error, it displays an error message.

This code demonstrates a way to offload resource-intensive PDF file splitting tasks to a web worker to prevent blocking the main UI thread. It also offers a user-friendly way to download the split PDF files.

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

The following JavaScript code snippet shows you how to split PDF pages into individual PDF files:

1. Select a PDF file for splitting.
1. Create a 'FileReader' object in handler.
1. Set number a page to split.
1. Call [AsposePdfSplit2Files](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfsplit2files/) in the last handler.
1. Analyse the result. The name of the resulting file is set, in this example "ResultSplit2.pdf".
1. Next, if the 'json.errorCode' is 0, then json.fileNameResult will contain the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' property.
1. You can use helper function [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/).

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





