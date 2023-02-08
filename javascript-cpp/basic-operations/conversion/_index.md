---
title: Convert PDF documents using JavaScript
linktitle: Convert PDF documents
type: docs
weight: 10
url: /javascript-cpp/conversion/
description: This section contains articles relating to convert PDF documents to images formats by Aspose.PDF for JavaScript via C++.
lastmod: "2022-12-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The PDF was developed to provide a standard for presenting documents and other reference materials in a format that is independent of application software, hardware, and operating system. The content of PDF files is not limited to text, it can be hyperlinks, images, clickable buttons and forms, electronic signatures, watermarks, and more. Therefore, it is often necessary to convert PDF files to some other format in order to edit or change their content. 

## Convert PDF using JavaScript

In this article, we will show you the options for converting PDF to image formats.

Previously scanned documents are often saved in the PDF file format. However, do you need to edit it in a graphic editor or send it further in image format? We have a universal tool for you to convert PDF to images using 
The most common task is when you need to save an entire PDF document or some specific pages of a document as a set of images. **Aspose for JavaScript via C++** allows you to convert PDF to JPG and PNG formats to simplify the steps required to get your images from a specific PDF file.

Check the code snippet, follow the steps, and solve your tasks of converting PDF documents.

### Convert PDF to JPEG

1. Select a PDF file for converting.
1. Create a 'FileReader'.
1. The [AsposePdfPagesToJpg](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestojpg/) function is executed.
1. The name of the resulting file is set, in this example "ResultPdfToJpg{0:D2}.jpg".
1. Next, if the 'json.errorCode' is 0, then your result File is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileToJpg = function (e) {
  const file_reader = new FileReader();
  file_reader.onload = (event) => {
    //convert a PDF file to jpg-files with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number) and save
    const json = AsposePdfPagesToJpg(event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg");
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Files(pages) count: " + json.filesCount.toString();
        //make links to result files
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) (json.filesNameResult[fileIndex], "mime/type");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
  file_reader.readAsArrayBuffer(e.target.files[0]);
};

```

### Convert PDF to PNG

1. Select a PDF file for converting.
1. Create a 'FileReader'.
1. The [AsposePdfPagesToPng](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfpagestopng/) function is executed.
1. The name of the resulting file is set, in this example "ResultPdfToPng{0:D2}.png".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileToPng = function (e) {
  const file_reader = new FileReader();
  file_reader.onload = (event) => {
    //convert a PDF file to png-files with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number) and save
    const json = AsposePdfPagesToPng(event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png");
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Files(pages) count: " + json.filesCount.toString();
        //make links to result files
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "mime/type");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
  file_reader.readAsArrayBuffer(e.target.files[0]);
};

```