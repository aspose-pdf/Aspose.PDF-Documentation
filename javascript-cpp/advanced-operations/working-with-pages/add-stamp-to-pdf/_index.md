---
title: Add Image stamps in PDF using JavaScript via C++ 
linktitle: Image stamps in PDF File
type: docs
weight: 60
url: /javascript-cpp/stamping/
description: Add the Image Stamp in your PDF document using ImageStamp class with the JavaScript tool.
lastmod: "2023-04-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Image Stamp in PDF File

Stamping a PDF document is similar to stamping a paper document. A stamp in a PDF file provides additional information to the PDF file, such as protecting the PDF file for others to use and confirming the security of the contents of the PDF file.
You can use the [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) function to add an image stamp to a PDF file using JavaScript.

To add an image stamp:

1. Set the default image filename.
1. Create a 'FileReader'.
1. Set the image filename.
1. Prepare the stamp file from BLOB.

The following code snippet shows how to add image stamp in the PDF file.

```js

  /*set the default stamp filename*/
  var fileStamp = "/Aspose.jpg";

  var ffileStamp = function (e) {
    const file_reader = new FileReader();
    /*set the stamp filename*/
    fileStamp = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*prepare(save) the stamp file from BLOB*/
      AsposePdfPrepare(event.target.result, fileStamp);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

1. Create a 'FileReader'.
1. The [AsposePdfAddStamp](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddstamp/) function is executed.
1. Add the image file to end a PDF-file and save the "ResultImage.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js
  var ffileAddStamp = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*insert the stamp file to a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfAddStamp(event.target.result, e.target.files[0].name, fileStamp, 0, 5, 5, 40, 40, Module.Rotation.on270, 0.5, "ResultStamp.pdf");
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
        (evt.data.json.errorCode == 0) ? `Result:\n${(evt.data.operation == 'AsposePdfPrepare') ? 'image prepared!': DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` : `Error: ${evt.data.json.errorText}`;

    /*set the default stamp filename: 'Aspose.jpg' already loaded, see settings in 'settings.json'*/
    var fileStamp = "Aspose.jpg";

    /*Event handler*/
    const ffileAddStamp = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        const setBackground = 0;
        const setXIndent_ = 5;
        const setYIndent_ = 5;
        const setHeight_ = 40;
        const setWidth_ = 40;
        const rotation_ = 'Module.Rotation.on270';
        const setOpacity = 0.5;
        /*insert the stamp file to a PDF-file and save the "ResultStamp.pdf" - Ask Web Worker*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfAddStamp', "params": [event.target.result, e.target.files[0].name, fileStamp, setBackground, setXIndent_, setYIndent_, setHeight_, setWidth_, rotation_, setOpacity, "ResultStamp.pdf"] }, [event.target.result]);
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileStamp = e => {
      const file_reader = new FileReader();
      /*set the stamp filename*/
      fileStamp = e.target.files[0].name;
      file_reader.onload = event => {
        /*prepare(save) the stamp file from BLOB*/
        AsposePDFWebWorker.postMessage({ "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] }, [event.target.result]);
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