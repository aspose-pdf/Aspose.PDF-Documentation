---
title: Convert PDF to EPUB, TeX, Text, XPS in Node.js
linktitle: Convert PDF to other formats 
type: docs
weight: 90
url: /nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-01"
keywords: convert, PDF, EPUB, TeX, Text, XPS, Node.js
description: This topic shows you how to convert PDF file to other file formats like EPUB, LaTeX, Text, XPS etc in the Node.js environment.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**Try to convert PDF to EPUB online**

Aspose.PDF for Node.js presents you online free application ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Convert PDF to EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub.
EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device. EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.

In case you want to convert PDF document, you can use [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/) function. 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Try to convert PDF to LaTeX/TeX online**

Aspose.PDF for Node.js presents you online free application ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convert PDF to TeX

**Aspose.PDF for Node.js** support converting PDF to TeX.
In case you want to convert PDF document, you can use [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) function. 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Try to convert Convert PDF to Text online**

Aspose.PDF for Node.js presents you online free application ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convert PDF to TXT

In case you want to convert PDF document, you can use [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) function. 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**Try to convert PDF to XPS online**

Aspose.PDF for Node.js presents you online free application ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Convert PDF to XPS

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into the Windows operating system.

**Aspose.PDF for Node.js** gives a possibility to convert PDF files to <abbr title="XML Paper Specification">XPS</abbr> format. Let try to use the presented code snippet for converting PDF files to XPS format with Node.js.

In case you want to convert PDF document, you can use [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) function. 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

```cjs

  const AsposePdf = require('.//AsposePDFforNode.cjs');
  const pdf_file = 'ReadMe.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## Convert PDF to Grayscale PDF

Convert PDF to black and white with Aspose.PDF for Node.js via C++ toolkit. 
Why should I convert PDF to Grayscale? If the PDF file contains many color images and the file size is important instead of color, the conversion saves space. If you print a PDF file in black and white, converting it will allow you to visually check what the end result looks like. 

In case you want to convert PDF document, you can use [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) function. 
Please check the following code snippet in order to convert in Node.js environment.

**CommonJS:**

```cjs

const AsposePdf = require('.//AsposePDFforNode.cjs');
const pdf_file = 'ReadMe.pdf';
AsposePdf().then(AsposePdfModule => {
    /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

```mjs

  import AsposePdf from './/AsposePDFforNode.mjs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'ReadMe.pdf';
  /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```






