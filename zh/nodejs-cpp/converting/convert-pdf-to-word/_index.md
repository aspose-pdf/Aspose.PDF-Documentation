---
title: 在 Node.js 中将 PDF 转换为 Word 文档
linktitle: 将 PDF 转换为 Word
type: docs
weight: 10
url: /zh/nodejs-cpp/convert-pdf-to-doc/
lastmod: "2026-07-18"
description: 了解如何在 Node.js 环境中将 PDF 转换为 DOC（DOCX）。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

在 Microsoft Word 或其他支持 DOC 和 DOCX 格式的文字处理器中编辑 PDF 文件的内容。PDF 文件是可编辑的，但 DOC 和 DOCX 文件更灵活且可定制。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 DOC**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF 转 DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)，在这里您可以尝试了解其功能和工作质量。

[![将 PDF 转换为 DOC](/pdf/zh/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## 将 PDF 转换为 DOC

如果您想转换 PDF 文档，可以使用 [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/) 函数。 
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPDFtoDoc.doc"。如果 json.errorCode 参数不为 0，并相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
      const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
      console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfToDoc](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodoc/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果保存在 "ResultPDFtoDoc.doc"。如果 json.errorCode 参数不为 0，并相应地在您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to Doc and save the "ResultPDFtoDoc.doc"*/
  const json = AsposePdfModule.AsposePdfToDoc(pdf_file, "ResultPDFtoDoc.doc");
  console.log("AsposePdfToDoc => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```

{{% alert color="warning" %}}
**尝试在线将 PDF 转换为 DOCX**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF 转 Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)，在这里您可以尝试了解其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 Word 免费应用](/pdf/zh/nodejs-cpp/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## 将 PDF 转换为 DOCX

Aspose.PDF for Node.js via C++ 工具包允许您读取并将 PDF 文档转换为 DOCX。DOCX 是一种广为人知的 Microsoft Word 文档格式，其结构已从纯二进制更改为 XML 与二进制文件的组合。Docx 文件可以使用 Word 2007 及其后续版本打开，但不能在早期支持 DOC 文件扩展名的 MS Word 版本中打开。

如果您想转换 PDF 文档，可以使用 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/) 函数。 
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果将保存在 "ResultPDFtoDocX.docx" 中。如果 json.errorCode 参数不为 0，并因此在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
      const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
      console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfToDocX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftodocx/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果将保存在 "ResultPDFtoDocX.docx" 中。如果 json.errorCode 参数不为 0，并因此在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to DocX and save the "ResultPDFtoDocX.docx"*/
  const json = AsposePdfModule.AsposePdfToDocX(pdf_file, "ResultPDFtoDocX.docx");
  console.log("AsposePdfToDocX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```


