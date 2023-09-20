---
title: Bookmarks in PDF with JavaScript
linktitle: Bookmarks in PDF
type: docs
weight: 10
url: /javascript-cpp/bookmark/
description: You can add or delete a bookmarks in PDF document with JavaScript.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Delete a Particular Bookmark from a PDF Document

You can delete bookmarks from a PDF file using Aspose.PDF for JavaScript via C++. You can get the result directly in your browser.

1. Create a 'FileReader'.
1. The [AsposePdfDeleteBookmarks](https://reference.aspose.com/pdf/javascript-cpp/organize/asposepdfdeletebookmarks/) function is executed.
1. The name of the resulting file is set, in this example "ResultPdfDeleteBookmarks.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

    var ffilePdfDeleteBookmarks = function (e) {
        const file_reader = new FileReader();
        file_reader.onload = (event) => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf"*/
        const json = AsposePdfDeleteBookmarks(event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf");
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
    const ffilePdfDeleteBookmarks = e => {
        const file_reader = new FileReader();
        file_reader.onload = event => {
        /*Delete bookmarks from a PDF-file and save the "ResultPdfDeleteBookmarks.pdf" - Ask Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfDeleteBookmarks', "params": [event.target.result, e.target.files[0].name, "ResultPdfDeleteBookmarks.pdf"] }, [event.target.result]);
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

