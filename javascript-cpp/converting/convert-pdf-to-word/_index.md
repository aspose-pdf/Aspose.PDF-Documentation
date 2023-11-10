---
title: Convert PDF to Word documents in JavaScript
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /javascript-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: Learn how to write JavaScript code for conversion PDF to DOC(DOCX) directly in the Web.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Converting operation depends on the number of pages in the document and can be very time-consuming. Therefore, we highly recommend using Web Workers. 

This code demonstrates a way to offload resource-intensive PDF file converting tasks to a web worker to prevent blocking the main UI thread. It also offers a user-friendly way to download the converted file.

To edit the content of a PDF file in Microsoft Word or other word processors that support DOC and DOCX formats. PDF files are editable, but DOC and DOCX files are more flexible and customizable.

{{% alert color="success" %}}
**Try to convert PDF to DOC online**

Aspose.PDF for JavaScript presents you online free application ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), where you may try to investigate the functionality and quality it works.

[![Convert PDF to DOC](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convert PDF to DOC

```js

  /*Create Web Worker*/
  const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
  AsposePDFWebWorker.onerror = evt => console.log(`Error from Web Worker: ${evt.message}`);
  AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
    (evt.data == 'ready') ? 'loaded!' :
      (evt.data.json.errorCode == 0) ? `Result:\n${DownloadFile(evt.data.json.fileNameResult, "application/msword", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

  /*Event handler*/
  const ffileToDoc = e => {
    const file_reader = new FileReader();
    file_reader.onload = event => {
      /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc" - Ask Web Worker*/
      AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDoc', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc"] }, [event.target.result]);
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

The following JavaScript code snippet shows simple example of coverting PDF pages into DOC files:

1. Select a PDF file for converting.
1. Create a 'FileReader'.
1. The [AsposePdfToDoc](https://reference.aspose.com/pdf/javascript-cpp/convert/asposepdftodoc/) function is executed.
1. The name of the resulting file is set, in this example "ResultPDFtoDoc.doc".
1. Next, if the 'json.errorCode' is 0, then your result File is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileToDoc = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
      const json = AsposePdfToDoc(event.target.result, e.target.files[0].name, "ResultPDFtoDoc.doc");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*Make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/msword");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```

{{% alert color="warning" %}}
**Try to convert PDF to DOCX online**

Aspose.PDF for JavaScript presents you online free application ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Word Free App](/pdf/javascript-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Convert PDF to DOCX

Aspose.PDF for JavaScript API lets you read and convert PDF documents to DOCX. DOCX is a well-known format for Microsoft Word documents whose structure was changed from plain binary to a combination of XML and binary files. Docx files can be opened with Word 2007 and lateral versions but not with the earlier versions of MS Word which support DOC file extensions.

```js

  /*Create Web Worker*/
    const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
    AsposePDFWebWorker.onerror = evt => console.log(`Error from Web Worker: ${evt.message}`);
    AsposePDFWebWorker.onmessage = evt => document.getElementById('output').textContent = 
      (evt.data == 'ready') ? 'loaded!' :
        (evt.data.json.errorCode == 0) ? `Result:\n${DownloadFile(evt.data.json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*Event handler*/
    const ffileToDocX = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx" - Ask Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfToDocX', "params": [event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx"] }, [event.target.result]);
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

The following JavaScript code snippet shows simple example of coverting PDF pages into DOCX files:

1. Select a PDF file for converting.
1. Create a 'FileReader'.
1. The [AsposePdfToDocX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftodocx/) function is executed.
1. The name of the resulting file is set, in this example "ResultPDFtoDocX.docx".
1. Next, if the 'json.errorCode' is 0, then your result File is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileToDocX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
      const json = AsposePdfToDocX(event.target.result, e.target.files[0].name, "ResultPDFtoDocX.docx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.wordprocessingml.document");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```


