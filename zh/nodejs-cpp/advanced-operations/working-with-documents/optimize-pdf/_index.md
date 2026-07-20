---
title: 使用 Aspose.PDF for Node.js via C++ 优化 PDF
linktitle: 优化 PDF 文件
type: docs
weight: 10
url: /zh/nodejs-cpp/optimize-pdf/
description: 使用 Node.js 环境优化并压缩 PDF 文件，以实现快速网页查看。
lastmod: "2026-07-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 优化 PDF 文档

Aspose.PDF for Node.js via C++ 工具包允许您在 Node.js 环境中优化 PDF 内容。 

优化（或线性化）是指将 PDF 文件制作成适合使用网页浏览器进行在线浏览的过程。

如果您想要优化 PDF，您可以使用 [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) 函数。 
请检查以下代码片段，以在 Node.js 环境中优化 PDF 文件。

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定将要优化的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行文件优化操作。如果成功，接收该对象。
1. 调用函数 [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. 优化 PDF 文件。因此，如果 \u0027json.errorCode\u0027 为 0，则操作结果保存为 \u0022ResultOptimize.pdf\u0022。如果 json.errorCode 参数不为 0，且相应地在您的文件中出现错误，错误信息将包含在 \u0027json.errorText\u0027 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要优化的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/).
1. 优化 PDF 文件。因此，如果 \u0027json.errorCode\u0027 为 0，则操作结果保存为 \u0022ResultOptimize.pdf\u0022。如果 json.errorCode 参数不为 0，且相应地在您的文件中出现错误，错误信息将包含在 \u0027json.errorText\u0027 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Optimize a PDF-file and save the "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```