---
title: Extract Tables from PDF in Node.js
linktitle: Extract Tables from PDF
type: docs
weight: 10
url: /nodejs-cpp/extract-tables-from-the-pdf-file/
description: How to convert PDF to CSV using Aspose.PDF for Node.js via C++ toolkit.
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract tables while converting PDF to CSV files

### Convert PDF to CSV

If there are tables in PDF then they are saved in separate CSV files. In case you want to convert PDF document, you can use [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/) function. 
Please check following code snippet in order to convert PDF file in Node.js environment.

**CommonJS:**

1. Call `require` and import `asposepdfnodejs` module as `AsposePdf` variable.
1. Specify the name of the PDF file that will be converted.
1. Call `AsposePdf` as Promise and perform the operation for converting file. Receive the object if successful.
1. Call the function [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Convert PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPDFtoXlsX.xlsx". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
      const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
      console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. Import the `asposepdfnodejs` module.
1. Specify the name of the PDF file that will be converted.
1. Initialize the AsposePdf module. Receive the object if successful.
1. Call the function [AsposePdfTablesToCSV](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftablestocsv/).
1. Convert PDF file. Thus, if 'json.errorCode' is 0, the result of the operation is saved in "ResultPDFtoXlsX.xlsx". If the json.errorCode parameter is not 0 and, accordingly, an error appears in your file, the error information will be contained in 'json.errorText'.

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to CSV (extract tables) with template "ResultPdfTablesToCSV{0:D2}.csv" ({0}, {0:D2}, {0:D3}, ... format page number), TAB as delimiter and save*/
  const json = AsposePdfModule.AsposePdfTablesToCSV(pdf_file, "ResultPdfTablesToCSV{0:D2}.csv", "\t");
  console.log("AsposePdfTablesToCSV => %O", json.errorCode == 0 ? json.filesNameResult : json.errorText);
```