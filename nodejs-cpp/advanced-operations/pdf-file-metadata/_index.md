---
title: Working with PDF File Metadata using Node.js via C++
linktitle: PDF File Metadata
type: docs
weight: 130
url: /nodejs-cpp/pdf-file-metadata/
description: This section explains how to get PDF file information, how to get metadata from a PDF file, set PDF File Information.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Get PDF File Information

In case you want to get PDF file information, you can use [AsposePdfGetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetinfo/) function. 
Please check the following code snippet in order to get PDF file information in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('../AsposePDFforNode.cjs');
  const pdf_file = '../ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get info (metadata) from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
      /* JSON
        Title           : json.title
        Creator         : json.creator
        Author          : json.author
        Subject         : json.subject
        Keywords        : json.keywords
        Creation Date   : json.creation
        Modify Date     : json.mod
        PDF format      : json.format
        PDF version     : json.version
        PDF is PDF/A    : json.ispdfa
        PDF is PDF/UA   : json.ispdfua
        PDF permission  : json.permission
        PDF page size   : json.size
        Page count      : json.pagecount
        Annotation count: json.annotationcount
        Bookmark count  : json.bookmarkcount
        Attachment count: json.attachmentcount
        Metadata count  : json.metadatacount
        JavaScript count: json.javascriptcount
        Image count     : json.imagecount
      */
      console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from '../AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = '../ReadMe.pdf';
  /*Get info (metadata) from a PDF-file*/
  const json = AsposePdfModule.AsposePdfGetInfo(pdf_file);
  /* JSON
    Title           : json.title
    Creator         : json.creator
    Author          : json.author
    Subject         : json.subject
    Keywords        : json.keywords
    Creation Date   : json.creation
    Modify Date     : json.mod
    PDF format      : json.format
    PDF version     : json.version
    PDF is PDF/A    : json.ispdfa
    PDF is PDF/UA   : json.ispdfua
    PDF permission  : json.permission
    PDF page size   : json.size
    Page count      : json.pagecount
    Annotation count: json.annotationcount
    Bookmark count  : json.bookmarkcount
    Attachment count: json.attachmentcount
    Metadata count  : json.metadatacount
    JavaScript count: json.javascriptcount
    Image count     : json.imagecount
  */
  console.log("AsposePdfGetInfo => %O", json.errorCode == 0 ? 'Title: ' + json.title : json.errorText);
```

## Get All Fonts

Getting fonts from a PDF file can be a useful way to reuse fonts in other documents or applications. 

In case you want to get fonts from a PDF file, you can use [AsposePdfGetAllFonts](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfgetallfonts/) function. 
Please check the following code snippet in order to get fonts from a PDF file in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Get list fonts from a PDF-file*/
      const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
      /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
      console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Get list fonts from a PDF-file*/
  const json = AsposePdfModule.AsposePdfGetAllFonts(pdf_file);
  /*json.fonts - array of fonts: { fontName: <string>, isEmbedded: <boolean>, isAccessible: <boolean> }*/
  console.log("AsposePdfGetAllFonts => fonts: %O", json.errorCode == 0 ? json.fonts : json.errorText);
```

## Set PDF File Information

Aspose.PDF for Node.js via C++ allows you to set file-specific information for a PDF, information like author, creation date, subject, and title. To set this information:

In case you want to set file-specific information, you can use [AsposePdfSetInfo](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfsetinfo/) function. 
Please check the following code snippet in order to set file information in Node.js environment.

Possible to set: 
- title
- creator
- author
- subject
- list keywords
- creation date
- modify date
- result file name

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
      /*If not need to set value, use undefined or "" (empty string)*/
      /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
      const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
      console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Set PDF info: title, creator, author, subject, keywords, creation (date), mod (date modify)*/
  /*If not need to set value, use undefined or "" (empty string)*/
  /*Set info (metadata) in a PDF-file and save the "ResultSetInfo.pdf"*/
  const json = AsposePdfModule.AsposePdfSetInfo(pdf_file, "Setting PDF Document Information", "", "Aspose", undefined, "Aspose.Pdf, DOM, API", undefined, "05/05/2023 11:55 PM", "ResultSetInfo.pdf");
  console.log("AsposePdfSetInfo => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Remove PDF File Information

Aspose.PDF for Node.js via C++ allows you to remove PDF file Metadata:

In case you want to remove metadata from PDF, you can use [AsposePdfRemoveMetadata](https://reference.aspose.com/pdf/nodejs-cpp/metadata/asposepdfremovemetadata/) function. 
Please check the following code snippet in order to remove metadata from PDF in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
      const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
      console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Remove metadata from a PDF-file and save the "ResultPdfRemoveMetadata.pdf"*/
  const json = AsposePdfModule.AsposePdfRemoveMetadata(pdf_file, "ResultPdfRemoveMetadata.pdf");
  console.log("AsposePdfRemoveMetadata => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```