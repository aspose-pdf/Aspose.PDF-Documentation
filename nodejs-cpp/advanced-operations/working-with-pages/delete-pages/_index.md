---
title: Delete Page in PDF in Node.js
linktitle: Delete PDF Pages
type: docs
weight: 30
url: /nodejs-cpp/delete-pages/
description: You can delete pages from your PDF file using Aspose.PDF for Node.js via C++.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

In case you want to delete PDF pages, you can use [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/) function. 

A feature of this function is that it can accept several types as a numPages parameter:

- string: in this case, we can mention a set of pages using particular pages or intervals. For example, string "7, 20, 30-32, 34" means we want to remove pages 7, 20, from 30 to 32 and 34.
- array: in this case, we can mention pages only. Array [3,7] means we want to remove pages 3 and 7.
- int: a single page number.

Please check the following code snippet in order to delete PDF pages in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file from which pages will be deleted.
1. Call `AsposePdf` as Promise and perform the operation for removing pages. Receive the object if successful.
1. Call the function [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). 
1. Removes the particular pages from the PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultDeletePages.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
      /*const numPages = "1-3";*/
      /*array, array of number pages*/
      /*const numPages = [1,3];*/
      /*number, number page*/
      const numPages = 1;
      /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
      const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
      console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the AsposePDFforNode.js module.
1. Specify the name of the PDF file from which pages will be deleted.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfDeletePages](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfdeletepages/). This function helps to remove the specified pages from the PDF file. The operation is determined by the numPages variable, which can be a string with page intervals (e.g., "7, 20, 22, 30-32, 33, 36-40, 46"), an array of page numbers, or a single page number.
1. Removes the particular pages from the PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultDeletePages.pdf". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*string, include number pages with interval: "7, 20, 22, 30-32, 33, 36-40, 46"*/
  /*const numPages = "1-3";*/
  /*array, array of number pages*/
  /*const numPages = [1,3];*/
  /*number, number page*/
  const numPages = 1;
  /*Delete pages from a PDF-file and save the "ResultDeletePages.pdf"*/
  const json = AsposePdfModule.AsposePdfDeletePages(pdf_file, "ResultDeletePages.pdf", numPages);
  console.log("AsposePdfDeletePages => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```