---
title: 从 PDF 中提取文本在 Node.js
linktitle: 从 PDF 中提取文本
type: docs
weight: 10
url: /zh/nodejs-cpp/extract-text/
description: 本节描述如何使用 Aspose.PDF for Node.js via C++ 工具从 PDF 文档中提取文本。
lastmod: "2023-11-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档的所有页面提取文本

从 PDF 中提取文本并不容易。只有少数 PDF 阅读器可以从 PDF 图像或扫描的 PDF 中提取文本。但是 **Aspose.PDF for Node.js via C++** 工具允许您在 Node.js 环境中轻松从所有 PDF 文件中提取文本。

此代码演示了如何使用 AsposePDFforNode.js 模块从指定的 PDF 文件中提取文本，并记录提取的文本或遇到的错误。

查看代码片段并按照步骤从您的 PDF 中提取文本：

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块为 `AsposePdf` 变量。

1. 指定要从中提取文本的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行提取文本的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/)。
1. 提取的文本存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，提取的文本将使用 console.log 显示。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，错误信息将包含在 'json.errorText' 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*从 PDF 文件中提取文本*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。

1. 指定要从中提取文本的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，接收对象。
1. 调用函数 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/)。
1. 提取的文本存储在 JSON 对象中。因此，如果 'json.errorCode' 为 0，则使用 console.log 显示提取的文本。如果 json.errorCode 参数不为 0，并且相应地，您的文件中出现错误，则错误信息将包含在 'json.errorText' 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*从 PDF 文件中提取文本*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```