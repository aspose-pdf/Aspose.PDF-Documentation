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
