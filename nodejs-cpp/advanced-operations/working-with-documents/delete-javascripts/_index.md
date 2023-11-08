---
title: Clear Node.js code from a PDF file
linktitle: Delete Node.jss
type: docs
weight: 50
url: /nodejs-cpp/delete-javascripts/
description: Clear Node.js macros from a PDF file directly in the Web with Aspose.PDF.
lastmod: "2023-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Removing Node.js in a PDF file may be necessary for security and privacy reasons. Node.js in PDF files can sometimes be used maliciously or for unwanted functions. You can get the result directly in your browser.

1. Create a 'FileReader'.
1. The [AsposePdfDeleteNode.jss](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletejavascripts/) function is executed.
1. The name of the resulting file is set, in this example "ResultPdfDeleteNode.jss.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/nodejs-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

    var ffilePdfDeleteNode.jss = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Delete Node.jss from a PDF-file and save the "ResultPdfDeleteNode.jss.pdf"*/
        const json = AsposePdfDeleteNode.jss(event.target.result, e.target.files[0].name, "ResultPdfDeleteNode.jss.pdf");
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
    const ffilePdfDeleteNode.jss = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Delete Node.jss from a PDF-file and save the "ResultPdfDeleteNode.jss.pdf" - Ask Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteNode.jss', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteNode.jss.pdf"] }, [event.target.result]);
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

