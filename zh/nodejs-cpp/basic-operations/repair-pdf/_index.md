---
title: 在 Node.js 中修复 PDF
linktitle: 修复 PDF
type: docs
weight: 10
url: /zh/nodejs-cpp/repair-pdf/
description: 本主题介绍如何在 Node.js 环境中修复 PDF。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Node.js 允许高质量的 PDF 修复。无论使用何种程序或浏览器，PDF文件可能由于某种原因无法打开。在某些情况下，文档可以恢复，尝试以下代码并自行查看。
如果您想修复 PDF 文档，可以使用 [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/) 函数。
请查看以下代码片段以在 Node.js 环境中修复 PDF 文件。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块为 `AsposePdf` 变量。
1. 指定将被修复的 PDF 文件的名称。
1. 将 `AsposePdf` 作为 Promise 调用并执行修复文件的操作。如果成功，接收对象。

1. 调用函数 [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/)。
1. 修复 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultPdfRepair.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
    /*修复 PDF 文件并保存为 "ResultPdfRepair.pdf"*/
    const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
    console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将被修复的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。

1. 调用函数 [AsposePdfRepair](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfrepair/)。
1. 修复 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存为 "ResultPdfRepair.pdf"。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*修复 PDF 文件并保存为 "ResultPdfRepair.pdf"*/
  const json = AsposePdfModule.AsposePdfRepair(pdf_file, "ResultPdfRepair.pdf");
  console.log("AsposePdfRepair => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```