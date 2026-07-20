---
title: 在 Node.js 中将 PDF 转换为 EPUB、TeX、Text、XPS
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: /zh/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-18"
description: 本主题向您展示如何在 Node.js 环境中将 PDF 文件转换为其他文件格式，如 EPUB、LaTeX、Text、XPS 等。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 EPUB**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF 转 EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，在这里您可以尝试了解其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 EPUB 的免费应用](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## 将 PDF 转换为 EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** 是一种由国际数字出版论坛（IDPF）制定的免费且开放的电子书标准。文件的扩展名为 .epub。
EPUB 旨在用于可重排内容，这意味着 EPUB 阅读器可以针对特定显示设备优化文本。EPUB 还支持固定布局内容。该格式旨在作为一种统一格式，供出版商和转换公司内部使用，也用于分发和销售。它取代了 Open eBook 标准。

如果您想转换 PDF 文档，可以使用 [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/) 函数。 
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoEPUB.epub"。如果 json.errorCode 参数不是 0，并且因此在你的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoEPUB.epub"。如果 json.errorCode 参数不是 0，并且因此在你的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to ePub and save the "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF 转 LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，在这里您可以尝试了解其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 LaTeX/TeX 的免费应用](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## 将 PDF 转换为 TeX

**Aspose.PDF for Node.js** 支持将 PDF 转换为 TeX。
如果您想转换 PDF 文档，可以使用 [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) 函数。 
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存到 "ResultPDFtoTeX.tex"。如果 json.errorCode 参数不是 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存到 "ResultPDFtoTeX.tex"。如果 json.errorCode 参数不是 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to TeX and save the "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**尝试将 PDF 转换为文本在线**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF 转文本"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，在这里您可以尝试了解其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为文本的免费应用](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## 将 PDF 转换为 TXT

如果您想转换 PDF 文档，可以使用 [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) 函数。 
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPDFtoTxt.txt" 中。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPDFtoTxt.txt" 中。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Txt and save the "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF 转 XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，在这里您可以尝试了解其功能和工作质量。

[![Aspose.PDF 将 PDF 转换为 XPS 的免费应用](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## 将 PDF 转换为 XPS

XPS 文件类型主要与微软公司推出的 XML Paper Specification（XML 纸张规范）相关。XML Paper Specification（XPS），曾用代号 Metro，并包含下一代打印路径（NGPP）营销概念，是微软将文档创建和查看集成到 Windows 操作系统中的倡议。

**Aspose.PDF for Node.js** 提供了将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式。让我们尝试使用提供的代码片段将 PDF 文件转换为 XPS 格式（使用 Node.js）。

如果您想转换 PDF 文档，可以使用 [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) 函数。
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPDFtoXps.xps" 中。如果 json.errorCode 参数不为 0，并相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPDFtoXps.xps" 中。如果 json.errorCode 参数不为 0，并相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Xps and save the "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## 将 PDF 转换为灰度 PDF

使用 Aspose.PDF for Node.js via C++ 工具包将 PDF 转换为黑白。 
为什么要将 PDF 转换为灰度？如果 PDF 文件包含大量彩色图像且文件大小比颜色更重要，转换可以节省空间。如果在黑白模式下打印 PDF 文件，转换可以让您直观地查看最终效果。 

如果您想转换 PDF 文档，可以使用 [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) 函数。 
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultConvertToGrayscale.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultConvertToGrayscale.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to grayscale and save the "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```




