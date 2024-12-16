---
title: 在 Node.js 中优化 PDF 资源
linktitle: 优化 PDF 资源
type: docs
weight: 15
url: /zh/nodejs-cpp/optimize-pdf-resources/
description: 使用 Node.js 工具优化 PDF 文件的资源以实现快速网页浏览。
lastmod: "2023-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 优化 PDF 资源

优化文档中的资源：

1. 删除未在文档页面上使用的资源
1. 将相同的资源合并为一个对象
1. 删除未使用的对象

如果您想优化 PDF 资源，可以使用 [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/) 函数。
请检查以下代码片段，以便在 Node.js 环境中优化 PDF 资源。

**CommonJS:**

1. 调用 `require` 并将 `asposepdfnodejs` 模块导入为 `AsposePdf` 变量。
1. 指定要优化资源的 PDF 文件的名称。

1. 调用 `AsposePdf` 作为 Promise 并执行优化文件的操作。如果成功，则接收对象。
1. 调用函数 [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/)。
1. 优化 PDF 资源。因此，如果 'json.errorCode' 是 0，操作结果保存在 "ResultPdfOptimizeResource.pdf" 中。如果 json.errorCode 参数不是 0 并且相应地，文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*优化 PDF 文件的资源并保存为 "ResultPdfOptimizeResource.pdf"*/
      const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
      console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要优化资源的 PDF 文件名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfOptimizeResource](https://reference.aspose.com/pdf/nodejs-cpp/organize/asposepdfoptimizeresource/)。
1. 优化 PDF 资源。因此，如果 'json.errorCode' 为 0，操作结果将保存到 "ResultPdfOptimizeResource.pdf"。如果 json.errorCode 参数不是 0，并且文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*优化 PDF 文件的资源并保存为 "ResultPdfOptimizeResource.pdf"*/
  const json = AsposePdfModule.AsposePdfOptimizeResource(pdf_file, "ResultPdfOptimizeResource.pdf");
  console.log("AsposePdfOptimizeResource => %O", json.errorCode == 0 ? json.fileNameResult : json.errorText);
```