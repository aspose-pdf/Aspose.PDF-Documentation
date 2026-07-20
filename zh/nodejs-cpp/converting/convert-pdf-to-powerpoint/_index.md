---
title: 在 Node.js 中将 PDF 转换为 PPTX
linktitle: 将 PDF 转换为 PowerPoint
type: docs
weight: 30
url: /zh/nodejs-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-18"
description: Aspose.PDF 允许您在 Node.js 环境中直接使用 Node.js 将 PDF 转换为 PPTX 格式。
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PowerPoint**

Aspose.PDF for Node.js 为您提供在线免费应用程序 ["PDF 转 PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)，在这里您可以尝试了解其功能和工作质量。

[![Aspose.PDF 免费应用将 PDF 转换为 PPTX](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## 将 PDF 转换为 PPTX

如果您想转换 PDF 文档，可以使用 [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/) 函数。 
请查看以下代码片段，以在 Node.js 环境中进行转换。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要转换的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件转换操作。如果成功，则接收该对象。
1. 调用函数 [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果将保存在 "ResultPDFtoPptX.pptx"。如果 json.errorCode 参数不为 0，因而在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
      const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
      console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要转换的 PDF 文件的名称
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfToPptX](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdftopptx/).
1. 转换 PDF 文件。因此，如果 'json.errorCode' 为 0，则操作结果将保存在 "ResultPDFtoPptX.pptx"。如果 json.errorCode 参数不为 0，因而在您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Convert a PDF-file to PptX and save the "ResultPDFtoPptX.pptx"*/
  const json = AsposePdfModule.AsposePdfToPptX(pdf_file, "ResultPDFtoPptX.pptx");
  console.log("AsposePdfToPptX => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```