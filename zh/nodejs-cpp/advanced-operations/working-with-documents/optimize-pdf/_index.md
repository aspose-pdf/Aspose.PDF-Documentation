---
title: 使用 Aspose.PDF for Node.js via C++ 优化 PDF
linktitle: 优化 PDF 文件
type: docs
weight: 10
url: zh/nodejs-cpp/optimize-pdf/
description: 使用 Node.js 环境优化和压缩 PDF 文件以实现快速网页浏览。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 优化 PDF 文档

Aspose.PDF for Node.js via C++ 工具包允许您为 Node.js 环境优化 PDF 内容。

优化或线性化是指使 PDF 文件适合使用网络浏览器在线浏览的过程。

如果您想优化 PDF，可以使用 [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/) 函数。 请查看以下代码片段以在 Node.js 环境中优化 PDF 文件。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
2. 指定将被优化的 PDF 文件的名称。

1. 调用 `AsposePdf` 作为 Promise 并执行优化文件的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/)。
1. 优化 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultOptimize.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*优化 PDF 文件并保存为 "ResultOptimize.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
      console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定将要优化的 PDF 文件的名称。

1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfOptimize](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimize/)。
1. 优化 PDF 文件。因此，如果 'json.errorCode' 为 0，操作结果将保存在 "ResultOptimize.pdf" 中。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js
  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*优化 PDF 文件并保存为 "ResultOptimize.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimize(pdf_file, "ResultOptimize.pdf");
  console.log("AsposePdfOptimize => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```