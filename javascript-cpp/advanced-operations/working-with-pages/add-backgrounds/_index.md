---
title: Add background to PDF with JavaScript via C++
linktitle: Add backgrounds
type: docs
weight: 10
url: /javascript-cpp/add-backgrounds/
description: Add background image to the your PDF file with JavaScript via C++. 
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The following code snippets shows how to add a background image to PDF pages using the [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) class with JavaScript.

In the next code snippet, we upload the image for further work in the internal file system:

1. Create a 'FileReader'.
1. Set the image filename.
1. Prepare the image file from BLOB.

```js

  var ffileImage = function (e) {
    const file_reader = new FileReader();
    /*set the image filename*/
    fileBackgroundImage = e.target.files[0].name;
    file_reader.onload = (event) => {
      /*prepare(save) the image file from BLOB*/
      AsposePdfPrepare(event.target.result, fileBackgroundImage);
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

In the next example, we select the PDF file to handle.
1. Create a 'FileReader'.
1. The [AsposePdfAddBackgroundImage](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaddbackgroundimage/) function is executed.
1. Add the image file into PDF and save the "ResultBackgroundImage.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileAddBackgroundImage = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*add a background image file into PDF and save the "ResultBackgroundImage.pdf"*/
      const json = AsposePdfAddBackgroundImage(event.target.result, e.target.files[0].name, fileBackgroundImage, "ResultBackgroundImage.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };
```

