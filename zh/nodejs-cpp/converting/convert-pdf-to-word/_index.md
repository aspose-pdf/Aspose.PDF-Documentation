---
title: 将PDF转换为Word文档在Node.js中
linktitle: 将PDF转换为Word
type: docs
weight: 10
url: zh/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2023-11-16"
description: 学习如何在Node.js环境中将PDF转换为DOC（DOCX）。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

要在Microsoft Word或其他支持DOC和DOCX格式的文字处理器中编辑PDF文件的内容。PDF文件是可编辑的，但DOC和DOCX文件更灵活和可定制。

{{% alert color="success" %}}
**尝试在线将PDF转换为DOC**

Aspose.PDF for Node.js为您提供在线免费应用程序["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，您可以尝试研究其功能和工作质量。

[![将PDF转换为DOC](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 将PDF转换为DOC

如果您想转换PDF文档，您可以使用[AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/)函数。
 
请检查以下代码片段，以便在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行转换文件的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPDFtoDoc.doc" 中。如果 json.errorCode 参数不为 0，并且相应地文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 Doc 并保存为 "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要转换的 PDF 文件的名称
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 是 0，则操作结果保存在 "ResultPDFtoDoc.doc" 中。如果 json.errorCode 参数不是 0，且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 Doc 并保存为 "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，您可以在其中尝试研究其功能和工作质量。

[![Aspose.PDF 转换 PDF 为 Word 免费应用程序](/pdf/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 将 PDF 转换为 DOCX

Aspose.PDF for Node.js via C++ 工具包让您可以读取和转换 PDF 文档为 DOCX。DOCX 是一种众所周知的 Microsoft Word 文档格式，其结构从纯二进制变为 XML 和二进制文件的组合。Docx 文件可以用 Word 2007 及更高版本打开，但不能用支持 DOC 文件扩展名的早期版本的 MS Word 打开。

如果您想转换 PDF 文档，可以使用 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) 函数。
请检查以下代码片段以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。

1. 以 Promise 的形式调用 `AsposePdf` 并执行文件转换操作。如果成功，接收对象。
1. 调用函数 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 是 0，操作结果将保存在 "ResultPDFtoDocX.docx" 中。如果 json.errorCode 参数不是 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*将 PDF 文件转换为 DocX 并保存为 "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称。

1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/)。
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPDFtoDocX.docx"。如果 json.errorCode 参数不为 0，相应地，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*将 PDF 文件转换为 DocX 并保存为 "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```