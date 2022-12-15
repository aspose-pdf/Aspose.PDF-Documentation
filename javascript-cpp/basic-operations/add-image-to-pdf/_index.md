---
title: Add Image to PDF using JavaScript via C++ 
linktitle: Add Image
type: docs
weight: 50
url: /javascript-cpp/add-image-to-pdf/
description: This section describes how to add image to existing PDF file using Aspose.PDF for JavaScript via C++.
lastmod: "2022-12-15"
---

## Add Image in an Existing PDF File

Do you need to attach an image to a PDF? Want to Improve the readability of your PDF? Add images to your PDF and your presentation or resume will look more presentable.

It is commonly believed that adding images to PDF files requires a complex special tool. However, with Aspose.PDF for JavaScript you can quickly and easily add the images you need to PDF using JavaScript directly in your browser.

To add an image to an existing PDF file:

1. Set the default image filename.
1. Create a 'FileReader'.
1. Set the image filename.
1. Prepare the image file from BLOB.
1. The 'AsposePdfAddImage' function is executed.
1. Add the image file to end a PDF-file and save the "ResultImage.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the 'DownloadFile' function generates a link and allows you to download the resulting file to the user's operating system.

The following code snippet shows how to add the image in a PDF document.

```js

  //set the default image filename
    var fileImage = "/Aspose.jpg";

   var ffileImage = function (e) {
    const file_reader = new FileReader();
    //set the image filename
    fileImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      //prepare(save) the image file from BLOB
      AsposePdfPrepare(event.target.result, fileImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

  var ffileAddImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      //add the image file to end a PDF-file and save the "ResultImage.pdf"
      const json = AsposePdfAddImage(event.target.result, e.target.files[0].name, fileImage, "ResultImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      //make a link to download the result file
      DownloadFile(json.fileNameResult, "mime/type");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```
