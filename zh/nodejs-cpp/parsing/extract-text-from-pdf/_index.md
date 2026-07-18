---
title: 在 Node.js 中解析 PDF 文本
linktitle: 解析 PDF 文本
type: docs
weight: 30
url: /zh/nodejs-cpp/extract-text-from-pdf/
description: 本文介绍了使用 Aspose.PDF for Node.js via C++ 解析 PDF 文档文本的多种方法。
lastmod: "2026-07-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档解析文本

从 PDF 文档中解析文本是一项非常常见且有用的任务。 
从 PDF 中提取文本有多种用途，包括提升搜索和可用性，以及在商业、研究和信息管理等各个领域实现数据分析和自动化。

如果您想从 PDF 文档中提取文本，您可以使用 [AsposePdfExtractText](https://reference.aspose.com/pdf/nodejs-cpp/convert/asposepdfextracttext/) 函数。 
请检查以下代码片段，以使用 Node.js via C\u002B\u002B 提取 PDF 文件中的文本。

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