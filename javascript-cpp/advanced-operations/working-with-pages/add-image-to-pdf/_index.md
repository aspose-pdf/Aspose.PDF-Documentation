---
title: Add Image to PDF using JavaScript via C++ 
linktitle: Add Image
type: docs
weight: 50
url: /javascript-cpp/add-image-to-pdf/
description: This section describes how to add image to existing PDF file using Aspose.PDF for JavaScript via C++.
lastmod: "2023-12-15"
---

## Add Image in an Existing PDF File

Do you need to attach an image to a PDF? Want to Improve the readability of your PDF? Add images to your PDF and your presentation or resume will look more presentable.

It is commonly believed that adding images to PDF files requires a complex special tool. However, with Aspose.PDF for JavaScript you can quickly and easily add the images you need to PDF using JavaScript directly in your browser.

To add an image to an existing PDF file:

1. Set the default image filename.
1. Create a 'FileReader'.
1. Set the image filename.
1. Prepare the image file from BLOB.
1. The [AsposePdfAddImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddimage/) function is executed.
1. Add the image file to end a PDF-file and save the "ResultImage.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

The following code snippet shows how to add the image in a PDF document.

```js

  /*set the default image filename*/
  var fileImage = "/Aspose.jpg";

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*set the image filename*/
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*prepare(save) the image file from BLOB*/
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```
In the next example, we select the image to handle:

```js

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*add the image file to end a PDF-file and save the "ResultImage.pdf"*/
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
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
          `Result:\n${(evt.data.operation == 'AsposePdfPrepare') ?
            'image prepared!':
            DownloadFile(evt.data.json.fileNameResult, "application/pdf", evt.data.params[0])}` :
          `Error: ${evt.data.json.errorText}`;

    /*Set the default image filename: 'Aspose.jpg' already loaded, see settings in 'settings.json'*/
    var fileImage = "Aspose.jpg";

    /*Event handler*/
    const ffileAddImage = e => {
      const file_reader = new FileReader();
      file_reader.onload = event => {
        /*Add image to end a PDF-file and save the "ResultImage.pdf" - Ask Web Worker*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfAddImage',
            "params": [event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf"] },
          [event.target.result]
        );
      };
      file_reader.readAsArrayBuffer(e.target.files[0]);
    };

    const ffileImage = e => {
      const file_reader = new FileReader();
      /*Set the image filename*/
      fileImage = e.target.files[0].name;
      file_reader.onload = event => {
        /*Save the BLOB in the Memory FS for processing*/
        AsposePDFWebWorker.postMessage(
          { "operation": 'AsposePdfPrepare', "params": [event.target.result, e.target.files[0].name] },
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