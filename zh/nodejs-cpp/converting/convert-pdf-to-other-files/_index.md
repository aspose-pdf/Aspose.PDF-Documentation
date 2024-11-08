---
title: 将 PDF 转换为 EPUB、TeX、文本、XPS 在 Node.js 中
linktitle: 将 PDF 转换为其他格式
type: docs
weight: 90
url: /zh/nodejs-cpp/convert-pdf-to-other-files/
lastmod: "2023-11-16"
keywords: 转换, PDF, EPUB, TeX, 文本, XPS, Node.js
description: 本主题向您展示如何在 Node.js 环境中将 PDF 文件转换为其他文件格式，如 EPUB、LaTeX、文本、XPS 等。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 EPUB**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)，您可以在其中尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 EPUB 免费应用](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## 将 PDF 转换为 EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** 是国际数字出版论坛 (IDPF) 提供的免费开放电子书标准。
 文件的扩展名为.epub。  
EPUB专为可重排内容而设计，这意味着EPUB阅读器可以针对特定的显示设备优化文本。EPUB也支持固定布局内容。该格式旨在作为出版商和转换公司可以在内部使用以及用于分发和销售的单一格式。它取代了开放电子书标准。

如果您想转换PDF文档，可以使用[AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/)功能。  
请查看以下代码片段，以便在Node.js环境中进行转换。

**CommonJS:**

1. 调用`require`并将`asposepdfnodejs`模块导入为`AsposePdf`变量。
1. 指定将要转换的PDF文件的名称。
1. 将`AsposePdf`调用为Promise并执行文件转换操作。如果成功，接收对象。
1. 调用函数[AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoEPUB.epub" 中。如果 json.errorCode 参数不为 0，并且相应地，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 ePub 并保存为 "ResultPDFtoEPUB.epub"*/
      const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
      console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfToEPUB](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoepub/)。

1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoEPUB.epub" 中。如果 json.errorCode 参数不是 0，并且在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 ePub 并保存为 "ResultPDFtoEPUB.epub"*/
  const json = AsposePdfModule.AsposePdfToEPUB(pdf_file, "ResultPDFtoEPUB.epub");
  console.log("AsposePdfToEPUB => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 LaTeX/TeX**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)，您可以在此尝试研究其功能和工作质量。


[![Aspose.PDF 转换 PDF 为 LaTeX/TeX 免费应用](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## 转换 PDF 为 TeX

**Aspose.PDF for Node.js** 支持将 PDF 转换为 TeX。
如果您想转换 PDF 文档，可以使用 [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/) 函数。
请查看以下代码片段以便在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块为 `AsposePdf` 变量。
1. 指定将被转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，接收对象。
1. 调用函数 [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 是 0，操作结果将保存在 "ResultPDFtoTeX.tex" 中。如果 json.errorCode 参数不为 0，并且，相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 TeX 并保存为 "ResultPDFtoTeX.tex"*/
      const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
      console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```


**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。成功时接收对象。
1. 调用函数 [AsposePdfToTeX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotex/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoTeX.tex" 中。如果 json.errorCode 参数不是 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 TeX 并保存为 "ResultPDFtoTeX.tex"*/
  const json = AsposePdfModule.AsposePdfToTeX(pdf_file, "ResultPDFtoTeX.tex");
  console.log("AsposePdfToTeX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为文本**


Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)，您可以尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 为文本的免费应用](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## 将 PDF 转换为 TXT

如果您想要转换 PDF 文档，可以使用 [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/) 函数。请查看以下代码片段，以便在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块为 `AsposePdf` 变量。
1. 指定要转换的 PDF 文件的名称。
1. 以 Promise 形式调用 `AsposePdf` 并执行转换文件的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/)。

1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoTxt.txt" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 Txt 并保存为 "ResultPDFtoTxt.txt"*/
      const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
      console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将被转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfToTxt](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftotxt/)。

1. 转换 PDF 文件。因此，如果 'json.errorCode' 是 0，操作结果将保存在 "ResultPDFtoTxt.txt" 中。如果 json.errorCode 参数不是 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js
  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 Txt 并保存为 "ResultPDFtoTxt.txt"*/
  const json = AsposePdfModule.AsposePdfToTxt(pdf_file, "ResultPDFtoTxt.txt");
  console.log("AsposePdfToTxt => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 XPS**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)，您可以在其中尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 至 XPS 免费应用](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## 将 PDF 转换为 XPS

XPS 文件类型主要与微软公司的 XML Paper Specification 相关联。XML Paper Specification（XPS），曾用代号为 Metro，并包含下一代打印路径（NGPP）营销概念，是微软将文档创建和查看集成到 Windows 操作系统中的一项计划。

**Aspose.PDF for Node.js** 提供了将 PDF 文件转换为 <abbr title="XML Paper Specification">XPS</abbr> 格式的可能性。让我们尝试使用提供的代码片段将 PDF 文件转换为 XPS 格式与 Node.js。

如果您想转换 PDF 文档，可以使用 [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/) 函数。请检查以下代码片段以便在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块作为 `AsposePdf` 变量。
1. 指定将被转换的 PDF 文件的名称。

1. 将 `AsposePdf` 作为 Promise 调用并执行文件转换操作。如果成功，将接收对象。
1. 调用函数 [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoXps.xps" 中。如果 json.errorCode 参数不为 0，并且相应地，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 Xps 并保存为 "ResultPDFtoXps.xps"*/
      const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
      console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称。

1. 初始化 AsposePdf 模块。成功时接收对象。
1. 调用函数 [AsposePdfToXps](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftoxps/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作的结果将保存在 "ResultPDFtoXps.xps" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 Xps 并保存为 "ResultPDFtoXps.xps"*/
  const json = AsposePdfModule.AsposePdfToXps(pdf_file, "ResultPDFtoXps.xps");
  console.log("AsposePdfToXps => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

## 将 PDF 转换为灰度 PDF

使用 Aspose.PDF for Node.js via C++ 工具包将 PDF 转换为黑白。 为什么我要将 PDF 转换为灰度？
 如果 PDF 文件包含许多彩色图像，并且文件大小比颜色更重要，则转换可以节省空间。如果您以黑白打印 PDF 文件，转换后您可以直观地检查最终结果。

如果您想转换 PDF 文档，可以使用 [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/) 函数。
请查看以下代码片段以便在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定将被转换的 PDF 文件的名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行文件转换操作。如果成功，接收对象。
1. 调用函数 [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultConvertToGrayscale.pdf" 中。如果 json.errorCode 参数不是 0，则文件中会出现错误，相应的错误信息将包含在 'json.errorText' 中。

```js

const AsposePdf = require('asposepdfnodejs');
const pdf_file = 'Aspose.pdf';
AsposePdf().then(AsposePdfModule => {
    /*将 PDF 文件转换为灰度并保存为 "ResultConvertToGrayscale.pdf"*/
    const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
    console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
});
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。

1. 调用函数 [AsposePdfConvertToGrayscale](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfconverttograyscale/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 是 0，操作结果将保存在 "ResultConvertToGrayscale.pdf" 中。如果 json.errorCode 参数不是 0，并且因此在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为灰度并保存为 "ResultConvertToGrayscale.pdf"*/
  const json = AsposePdfModule.AsposePdfConvertToGrayscale(pdf_file, "ResultConvertToGrayscale.pdf");
  console.log("AsposePdfConvertToGrayscale => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```