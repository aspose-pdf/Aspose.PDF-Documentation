---
title: Convert PDF documents using JavaScript
linktitle: Convert PDF documents
type: docs
weight: 50
url: /javascript-cpp/conversion/
description: This section contains articles relating to convert PDF documents to other formats by Aspose.PDF for JavaScript via C++.
lastmod: "2022-12-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

The PDF was developed to provide a standard for presenting documents and other reference materials in a format that is independent of application software, hardware, and operating system. The content of PDF files is not limited to text, it can be hyperlinks, images, clickable buttons and forms, electronic signatures, watermarks, and more. Therefore, it is often necessary to convert PDF files to some other format in order to edit or change their content. 

## Convert PDF to DOCX

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
## Convert PDF to XLSX

1. Select a PDF file for converting.
1. Create a 'FileReader'.
1. The [AsposePdfToXlsX](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdftoxlsx/) function is executed.
1. The name of the resulting file is set, in this example "ResultPDFtoXlsX.xlsx".
1. Next, if the 'json.errorCode' is 0, then your result File is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileToXlsX = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convert a PDF-file to XlsX and save the "ResultPDFtoXlsX.xlsx"*/
      const json = AsposePdfToXlsX(event.target.result, e.target.files[0].name, "ResultPDFtoXlsX.xlsx");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
    }
    file_reader.readAsArrayBuffer(e.target.files[0]);
  }
```

## Convert PDF to image formats using JavaScript

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
      /*convert a PDF file to jpg-files with template "ResultPdfToJpg{0:D2}.jpg" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfPagesToJpg(event.target.result, e.target.files[0].name, "ResultPdfToJpg{0:D2}.jpg", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Files(pages) count: " + json.filesCount.toString();
        /*make links to result files*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/jpeg");
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
      /*convert a PDF file to png-files with template "ResultPdfToPng{0:D2}.png" ({0}, {0:D2}, {0:D3}, ... format page number), resolution 150 DPI and save*/
      const json = AsposePdfPagesToPng(event.target.result, e.target.files[0].name, "ResultPdfToPng{0:D2}.png", 150);
      if (json.errorCode == 0) {
        document.getElementById('output').textContent = "Files(pages) count: " + json.filesCount.toString();
        /*make links to result files*/
        for (let fileIndex = 0; fileIndex < json.filesCount; fileIndex++) DownloadFile(json.filesNameResult[fileIndex], "image/png");
      }
      else document.getElementById('output').textContent = json.errorText;
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```

## Convert PDF to other formats using JavaScript

### Convert PDF to Grayscale

Convert PDF to black and white with Aspose.PDF for JavaScript via C++ library. 
Why should I convert PDF to Grayscale? If the PDF file contains many color images and the file size is important instead of color, the conversion saves space. If you print a PDF file in black and white, converting it will allow you to visually check what the end result looks like. 

1. Select a PDF file for converting.
1. Create a 'FileReader'.
1. The [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttograyscale/) function is executed.
1. The name of the resulting file is set, in this example "ResultConvertToGrayscale.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffileConvertToGrayscale = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
      const json = AsposePdfConvertToGrayscale(event.target.result, e.target.files[0].name, "ResultConvertToGrayscale.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```

### Convert PDF to PDF/A format

1. Select a PDF file for converting.
1. Create a 'FileReader'.
1. The [AsposePdfConvertToPDFA](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfconverttopdfa/) function is executed.
1. The name of the resulting file is set, in this example "ResultConvertToPDFA.pdf". During conversion process, the validation is also performed, "ResultConvertToPDFA.xml".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file, and link to download the Log (xml) file to the user's operating system.

```js

  var ffilePdfConvertToPDFA = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convert a PDF-file to PDF/A(1A) and save the "ResultConvertToPDFA.pdf"*/
      /*during conversion process, the validation is also performed, "ResultConvertToPDFA.xml"*/
      const json = AsposePdfConvertToPDFA(event.target.result, e.target.files[0].name, Module.PdfFormat.PDF_A_1A, "ResultConvertToPDFA.pdf", "ResultConvertToPDFA.xml");
      if (json.errorCode == 0)
      {
        document.getElementById('output').textContent = json.fileNameResult + "\nLog file (xml format): " + json.fileNameLogResult;
        /*make a link to download the result file*/
        DownloadFile(json.fileNameResult, "application/pdf");
      }
      else document.getElementById('output').textContent = json.errorText + "\nLog file (xml format): " + json.fileNameLogResult;
      /*make a link to download the Log (xml)*/
      DownloadFile(json.fileNameLogResult, "application/xml");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```

### Convert PDF/A to PDF format

1. Select a PDF file for converting.
1. Create a 'FileReader'.
1. The [AsposePdfAConvertToPDF](https://reference.aspose.com/pdf/javascript-cpp/core/asposepdfaconverttopdf/) function is executed.
1. The name of the resulting file is set, in this example "ResultConvertToPDFA.pdf".
1. Next, if the 'json.errorCode' is 0, then your DownloadFile is given the name you specified earlier. If the 'json.errorCode' parameter is not equal to 0 and, accordingly, there will be an error in your file, then information about such an error will be contained in the 'json.errorText' file.
1. As a result, the [DownloadFile](https://reference.aspose.com/pdf/javascript-cpp/misc/downloadfile/) function generates a link and allows you to download the resulting file to the user's operating system.

```js

  var ffilePdfAConvertToPDF = function (e) {
    const file_reader = new FileReader();
    file_reader.onload = (event) => {
      /*convert a PDF/A-file to PDF and save the "ResultConvertToPDF.pdf"*/
      const json = AsposePdfAConvertToPDF(event.target.result, e.target.files[0].name, "ResultConvertToPDF.pdf");
      if (json.errorCode == 0) document.getElementById('output').textContent = json.fileNameResult;
      else document.getElementById('output').textContent = json.errorText;
      /*make a link to download the result file*/
      DownloadFile(json.fileNameResult, "application/pdf");
    };
    file_reader.readAsArrayBuffer(e.target.files[0]);
  };

```