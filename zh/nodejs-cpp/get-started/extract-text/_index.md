---
title: 在 Node.js 中从 PDF 提取文本
linktitle: 从 PDF 提取文本
type: docs
weight: 10
url: /zh/nodejs-cpp/extract-text/
description: 本节介绍如何使用 Aspose.PDF for Node.js via C++ 工具包从 PDF 文档中提取文本。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档的所有页面提取文本

从 PDF 中提取文本并不容易。只有少数 PDF 阅读器能够从 PDF 图像或扫描的 PDF 中提取文本。但 **Aspose.PDF for Node.js via C++** 工具能够让您在 Node.js 环境中轻松地从所有 PDF 文件中提取文本。 

此代码演示了如何使用 AsposePDFforNode.js 模块从指定的 PDF 文件中提取文本，并记录提取的文本或出现的错误。

检查代码片段并按照步骤从 PDF 中提取文本：

**CommonJS:**

1. 调用 `require` 并导入 `asposepdfnodejs` 模块 作为 `AsposePdf` 变量。
1. 指定要提取文本的 PDF 文件的名称。
1. 调用 `AsposePdf` 作为 Promise 并执行提取文本的操作。如果成功，接收对象。
1. 调用函数 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. 提取的文本存储在 JSON 对象中。因此，如果 `json.errorCode` 为 0，则使用 console.log 显示提取的文本。如果 `json.errorCode` 参数不为 0，则文件中会出现错误，错误信息将包含在 `json.errorText` 中。

```js

  const AsposePdf = require('asposepdfnodejs');
  const pdf_file = 'Aspose.pdf';
  AsposePdf().then(AsposePdfModule => {
      /*Extract text from a PDF-file*/
      const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
      console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
  });
```

**ECMAScript/ES6:**

1. 导入 `asposepdfnodejs` 模块。
1. 指定要提取文本的 PDF 文件的名称。
1. 初始化 AsposePdf 模块。如果成功，则接收对象。
1. 调用函数 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/).
1. 提取的文本存储在 JSON 对象中。因此，如果 `json.errorCode` 为 0，则使用 console.log 显示提取的文本。如果 `json.errorCode` 参数不为 0，则文件中会出现错误，错误信息将包含在 `json.errorText` 中。

```js

  import AsposePdf from 'asposepdfnodejs';
  const AsposePdfModule = await AsposePdf();
  const pdf_file = 'Aspose.pdf';
  /*Extract text from a PDF-file*/
  const json = AsposePdfModule.AsposePdfExtractText(pdf_file);
  console.log("AsposePdfExtractText => %O", json.errorCode == 0 ? json.extractText : json.errorText);
```
