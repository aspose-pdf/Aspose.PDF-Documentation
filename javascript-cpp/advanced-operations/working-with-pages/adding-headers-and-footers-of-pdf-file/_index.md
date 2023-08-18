---
title: Add Header and Footer to PDF via JavaScript via C++ 
linktitle: Add Header and Footer to PDF
type: docs
weight: 70
url: /javascript-cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for JavaScript via C++  allows you to add headers and footers to your PDF file using AsposePdfAddTextHeaderFooter.
lastmod: "2023-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for JavaScript via C++** allows you to add header and footer in your existing PDF file. 

1. Create a 'FileReader'.
1. The [AsposePdfAddTextHeaderFooter](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddtextheaderfooter/) function is executed.
1. The name of the resulting file is set, in this example "ResultAddHeader.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

The following code snippet shows you how to add text in the header of a PDF file with JavaScript.

```js

  var ffileAddTextHeaderFooter = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*add page header a PDF-file and save the "ResultAddHeader.pdf"*/
      const json = AsposePdfAddTextHeaderFooter(event.target.result, e.target.files[0].name, "Aspose.PDF for JavaScript via C++", "", "ResultAddHeader.pdf");
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
        (evt.data.json.errorCode == 0) ? `Result:\n${DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Event handler*/
    const ffileAddTextHeaderFooter = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const header = 'Aspose.PDF for JavaScript via C++';
        const footer = 'ASPOSE';
        /*add page header a PDF-file and save the "ResultAddHeaderFooter.pdf" - Ask Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAddTextHeaderFooter', "params": [event.target.result, e.target.files[0].name, header, footer, "ResultAddHeaderFooter.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };
  /// [Code snippet]

    /*make a link to download the result file*/
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